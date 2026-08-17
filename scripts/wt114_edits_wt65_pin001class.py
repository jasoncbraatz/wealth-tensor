#!/usr/bin/env python3
"""wealthTensor-65 · close `PIN-001`'s class hole — part 1, the orphan.

`PIN-001` said it repaired the CLASS and hardcoded one manuscript of four. `-64` measured
the census and found the shape intact in Paper IV: §10 pins `5efe626` in prose and no file
under `scripts/`, `tests/` or `src/` names it. `-65` verified the orphan by RUNNING the
widened instrument against the un-instrumented registry first — it went red naming exactly
`paper-IV.md 5efe626`, which is the card's ordering claim turned into a measurement.

This script does part 1 only: teach `LATEST_TOUCH` the module, so the pin has something
watching it. Part 2 — the glob — lands in the same commit but replaces a whole file, so it
is staged separately.

It also repairs the registry's own docstring, which still says the mapping is *"as of this
edit"* — meaning `PIN-001`'s edit, in 2026-08-11. It has since gained Paper II's module
(`-64`) and Paper IV's (here). A registry that misdescribes its own scope is `WT-092` in
the registry that exists to prevent `WT-092`.

Every anchor is asserted unique before any write; `--dry` writes a `*.wt65-dryrun` sibling.
"""
from __future__ import annotations

import pathlib
import shutil
import sys

DRY = "--dry" in sys.argv
ROOT = pathlib.Path(__file__).resolve().parents[1]

REG = "scripts/wt099_edits_pin001.py"

EDITS = [
    (REG, "LATEST_TOUCH scope docstring",
     "#: The commit that most recently touched each pinned path, as of this edit. THIS is what\n"
     "#: the guard checks, and it is what makes the defect impossible to reintroduce silently:\n"
     "#: the next commit touching a pinned file makes the guard red, so the pin and the paper\n"
     "#: move together or the suite says so.",

     "#: The commit that most recently touched each pinned path — **the corpus's per-file pin\n"
     "#: registry**, and no longer a snapshot of PIN-001's own edit. It began as one paper's\n"
     "#: (`-56`, paper III); `-64` added paper II's module and `-65` added paper IV's as each\n"
     "#: manuscript's pin was instrumented. This comment said \"as of this edit\" for two\n"
     "#: sessions after that stopped being true — WT-092 in the registry that exists to stop\n"
     "#: WT-092, and worth one line to say out loud. THIS is what the guard checks, and it is\n"
     "#: what makes the defect impossible to reintroduce silently: the next commit touching a\n"
     "#: pinned file makes the guard red, so the pin and the paper move together or the suite\n"
     "#: says so.",),

    (REG, "paper IV's instrument pin",
     '    "src/wealth_tensor/redistribution.py": "3b11f23",\n',

     '    "src/wealth_tensor/redistribution.py": "3b11f23",\n'
     "    # wealthTensor-65: paper IV §10 pins the REG-013 instrument per file — \"5efe626 —\n"
     "    # the last commit touching scripts/reg013_citation_whitespace.py, and therefore the\n"
     "    # state of the instrument that produced every number in §6\". It was the LAST orphan\n"
     "    # in the four-manuscript census: the pin was TRUE and completely unwatched, which is\n"
     "    # exactly how d655501 stayed true for five days and false for nine more. This line is\n"
     "    # what makes it go red the day the instrument moves.\n"
     '    "scripts/reg013_citation_whitespace.py": "5efe626",\n',),
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
        print(f"ok  {rel:36s}  {label}")

    for rel, text in src.items():
        p = ROOT / rel
        if DRY:
            out = p.with_suffix(p.suffix + ".wt65-dryrun")
            out.write_text(text, encoding="utf-8")
            print(f"DRY  wrote {out}")
        else:
            shutil.copy2(p, p.with_suffix(p.suffix + ".bak-wt65-pin001class"))
            p.write_text(text, encoding="utf-8")
            print(f"WROTE {rel}  (.bak-wt65-pin001class kept)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
