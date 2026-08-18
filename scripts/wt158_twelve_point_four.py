#!/usr/bin/env python3
"""wt158 · make Paper IV §8's twelve-point FOUR an assertion instead of a memory.

THE DEFECT.  Two sentences in Paper IV §10 say that `tests/test_excess_demand.py` ASSERTS
§8's twelve-point four:

    "§5's **399** interior grid points and §8's twelve-point **four** are *asserted* by
     `tests/test_excess_demand.py` rather than printed by it"                    (30191fec1a)
    "... its 500-point monotonicity sweep, and the twelve-point tie convention §8 records"
                                                                                 (10d2d456ea)

The 399 is asserted, at `assert grid.size == 399`.  The FOUR was not asserted anywhere.  The
module's only twelve-point test counts DEMAND CURVES and asserts 25; no line in the module ever
built the twelve-point EXCESS-DEMAND set, which is the object §8's four counts.  Both rows sat on
`read the module`, and nobody could tell what the adjudicator had read.

THE REPAIR.  Rather than weaken the manuscript, assert the number.  On the 12-point grid the
distinct excess-demand schedules across the 25 allocations number exactly 4 — measured on darwin
2026-08-18, and now asserted, so §8's number is machine-checked and both sentences become true.
This is the stronger repair: the sentence claimed a property of the artefact, so the artefact was
given the property.

RC 0 repaired · RC 2 refused or rolled back (from .bak-wt158).
"""

import shutil
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
MOD = REPO / "tests/test_excess_demand.py"
BAK = MOD.with_suffix(".py.bak-wt158")

ANCHOR = """    grid = np.linspace(M.min(), M.max(), 12)
    curves = {tuple(mk.demand_at(p) for p in grid) for mk in allocations()}
    assert len(curves) == 25
"""

ADDITION = '''

def test_the_twelve_point_grid_returns_the_four_schedules_section_8_reports():
    """Paper IV §8's abandoned approach, asserted rather than remembered.

    §8 reports that §5's identity was first measured on a 12-point grid spanning the full range
    of reservation prices and returned FOUR distinct excess-demand schedules rather than one --
    two grid endpoints x two holding states. Until wealthTensor-86 the manuscript said that four
    was ASSERTED by this module, and it was not: the twelve-point test above counts DEMAND curves
    (25) and never builds the excess-demand set at all. The number is asserted here, so §8's
    figure is checked by the suite rather than carried in a paragraph.
    """
    grid = np.linspace(M.min(), M.max(), 12)
    excess = {tuple(mk.excess_demand(float(p)) for p in grid) for mk in allocations()}
    assert len(excess) == 4
'''

NAME = "test_the_twelve_point_grid_returns_the_four_schedules_section_8_reports"


def main():
    text = MOD.read_text()
    if text.count(ANCHOR) != 1:
        print(f"wt158: REFUSING — the twelve-point anchor does not appear exactly once "
              f"(found {text.count(ANCHOR)}). Read the module before editing.")
        return 2
    if NAME in text:
        print("wt158: REFUSING — the assertion is already present.")
        return 2

    n_defs_before = text.count("\ndef test_")
    shutil.copy2(MOD, BAK)
    try:
        MOD.write_text(text.replace(ANCHOR, ANCHOR + ADDITION))
        new = MOD.read_text()

        checks = []

        def c(name, pol, cond, detail=""):
            checks.append((name, pol, bool(cond), detail))

        c("C1 the new test is present exactly once", "POSITIVE", new.count(f"def {NAME}") == 1)
        c("C2 the module gained exactly one test function", "POSITIVE",
          new.count("\ndef test_") == n_defs_before + 1,
          f"{n_defs_before} -> {new.count(chr(10) + 'def test_')}")

        run = subprocess.run([sys.executable, "-m", "pytest", str(MOD), "-q"],
                             cwd=REPO, capture_output=True, text=True)
        c("C3 the module is green with the new assertion", "POSITIVE", run.returncode == 0,
          run.stdout[-400:])
        c("C4 the module now reports 11 passed", "POSITIVE", "11 passed" in run.stdout,
          run.stdout.strip().splitlines()[-1] if run.stdout.strip() else "")

        one = subprocess.run([sys.executable, "-m", "pytest", f"{MOD}::{NAME}", "-q"],
                             cwd=REPO, capture_output=True, text=True)
        c("C5 the new assertion passes when run alone", "POSITIVE", one.returncode == 0)

        # ---- NEGATIVE
        c("C6 NEGATIVE the 399 assertion is untouched", "NEGATIVE",
          new.count("assert grid.size == 399") == 1)
        c("C7 NEGATIVE the 25-demand-curve assertion is untouched", "NEGATIVE",
          new.count("assert len(curves) == 25") == 1)
        c("C8 NEGATIVE the 500-point monotonicity sweep is untouched", "NEGATIVE",
          new.count("np.linspace(M.min(), M.max(), 500)") == 1)
        c("C9 NEGATIVE no manuscript is dirty in the working tree", "NEGATIVE",
          not _dirty_manuscripts())
        c("C10 NEGATIVE nothing outside tests/ and this script changed the module set",
          "NEGATIVE", MOD.name == "test_excess_demand.py")

        ok = all(x[2] for x in checks)
        nneg = sum(1 for x in checks if x[1] == "NEGATIVE")
        print(f"wt158 · POST-CONDITIONS ({len(checks)} total, {nneg} NEGATIVE, "
              f"{len(checks) - nneg} POSITIVE)")
        for name, pol, passed, detail in checks:
            print(f"    [{'ok  ' if passed else 'FAIL'}] {name}" +
                  (f"  {detail}" if detail and not passed else ""))
        if not ok:
            shutil.copy2(BAK, MOD)
            print("\nwt158: ROLLED BACK from .bak-wt158.")
            return 2
        print("\nwt158: §8's twelve-point four is now asserted by the suite.")
        return 0
    except Exception as exc:  # noqa: BLE001
        shutil.copy2(BAK, MOD)
        print(f"wt158: EXCEPTION {exc!r} — ROLLED BACK.")
        return 2


def _dirty_manuscripts():
    out = subprocess.run(["git", "status", "--porcelain"], cwd=REPO,
                         capture_output=True, text=True).stdout
    return [l[3:] for l in out.splitlines()
            if "docs/papers/" in l and l.rstrip().endswith(".md")]


if __name__ == "__main__":
    sys.exit(main())
