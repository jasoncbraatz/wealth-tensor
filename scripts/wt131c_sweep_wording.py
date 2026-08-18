#!/usr/bin/env python3
"""wt131c -- reword `wt130`'s output so "N lines" cannot be read as manuscript length.

`wt130` prints "864 quantifier tokens on 668 lines".  668 is the number of lines that CARRY
a quantifier; Paper III is 2,685 lines.  That reading propagated three documents deep --
`-72`'s handoff, `LEDGER` `WT-116` and `docs/HANDOFF.md` all record Paper III as "668 lines,
the largest manuscript in the batch", and the session budget written from it was "~50 min"
for a document four times that size.  The conclusion was right for a different reason.

The tool is where this is fixed, because the tool is what the next session reads.  Three
print sites, and the total line now carries the manuscript's own length beside the count so
the two numbers can never be confused again.

Guard honesty (WT-118): every invariant is asserted against the ORIGINAL as well as the
patch, so a red line names which failure mode fired.
"""
from __future__ import annotations

import pathlib
import shutil
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
SWEEP = ROOT / "scripts" / "wt130_quantifier_sweep.py"

HELPER = '''

def n_lines(path):
    """The manuscript's own length. Kept beside the sweep's count because the two were
    conflated once: `wt130`'s "N lines" is lines that CARRY a quantifier (wealthTensor-73,
    LEDGER WT-119 §1)."""
    return len(path.read_text(encoding="utf-8").splitlines())

'''

EDITS = [
    # the helper, inserted above main()
    ("\n\ndef main(argv):", HELPER + "\ndef main(argv):"),
    # 1 · the four-line orientation output
    ('            print(f"{p.parent.name:28s} {len(rows):4d} lines  {n:4d} quantifier tokens")',
     '            print(f"{p.parent.name:28s} {n:4d} quantifier tokens on "\n'
     '                  f"{len(rows):4d} of its {n_lines(p):5d} lines")'),
    # 2 · the per-manuscript heading
    ('        head = f"{rel} — {n} quantifier tokens on {len(rows)} lines"',
     '        head = (f"{rel} — {n} quantifier tokens on {len(rows)} lines that carry one, "\n'
     '                f"of {n_lines(p)} in the manuscript")'),
    # 3 · the total
    ('        print(f"\\nTOTAL: {n} tokens / {len(rows)} lines")',
     '        print(f"\\nTOTAL: {n} tokens on {len(rows)} lines that carry one; "\n'
     '              f"the manuscript is {n_lines(p)} lines long")'),
]

DOC_OLD = """    python3 scripts/wt130_quantifier_sweep.py                 # all four manuscripts, counts"""
DOC_NEW = """A COUNTING NOTE, because the first reading of this output was wrong and travelled three
documents deep. "N lines" means LINES THAT CARRY A QUANTIFIER, never manuscript length --
Paper III is 864 tokens on 668 such lines and is 2,685 lines long. Every print site below
now says so; do not restate it as a manuscript size (wealthTensor-73, LEDGER WT-119 §1).

    python3 scripts/wt130_quantifier_sweep.py                 # all four manuscripts, counts"""


def main() -> int:
    text = SWEEP.read_text(encoding="utf-8")
    print("CENSUS")
    ok = True
    for old, _new in EDITS:
        n = text.count(old)
        print(f"  {'ok ' if n == 1 else '!! '}{n} (want 1)  {old.strip()[:62]}…")
        ok &= n == 1
    n = text.count(DOC_OLD)
    print(f"  {'ok ' if n == 1 else '!! '}{n} (want 1)  docstring usage block")
    ok &= n == 1
    if not ok:
        print("CENSUS FAILED — nothing written", file=sys.stderr)
        return 3

    patched = text
    for old, new in EDITS:
        patched = patched.replace(old, new)
    patched = patched.replace(DOC_OLD, DOC_NEW)

    fails = []

    def check(name, on_orig, on_new):
        if not on_orig(text):
            fails.append(f"GUARD VACUOUS -- {name}: false of the ORIGINAL too")
        elif not on_new(patched):
            fails.append(f"GUARD RED -- {name}: the edit broke it")

    check("the token regex is untouched",
          lambda t: 'PAT = re.compile' in t, lambda t: 'PAT = re.compile' in t)
    check("the TOKENS tuple is untouched",
          lambda t: t.count('"one of", "sole"') == 1,
          lambda t: t.count('"one of", "sole"') == 1)
    check("sweep() is untouched",
          lambda t: "def sweep(path):" in t, lambda t: "def sweep(path):" in t)
    check("no print site still says a bare 'lines'",
          lambda t: t.count("{len(rows)} lines\"") + t.count("{len(rows):4d} lines ") >= 1,
          lambda t: t.count("{len(rows)} lines\"") + t.count("{len(rows):4d} lines ") == 0)
    if fails:
        for f in fails:
            print("  " + f)
        return 1

    shutil.copy2(SWEEP, SWEEP.with_suffix(SWEEP.suffix + ".bak-wt131c"))
    SWEEP.write_text(patched, encoding="utf-8")

    # The only guard that matters: it still runs, and the counts did not move.
    out = subprocess.run((sys.executable, str(SWEEP)), capture_output=True, text=True,
                         cwd=ROOT)
    print("\n--- wt130, reworded ---")
    print(out.stdout.strip() or out.stderr.strip())
    if out.returncode != 0:
        print("!! wt130 no longer runs — restore from .bak-wt131c")
        return 1
    for expect in ("184", "155", "870", "194", "2694"):
        if expect not in out.stdout:
            print(f"!! expected figure {expect} missing from the reworded output")
            return 1
    print("\ncounts unchanged; wording fixed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
