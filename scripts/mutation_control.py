#!/usr/bin/env python3
"""MUTATION CONTROL — measure what the suite actually catches, before grading a constraint.

WHY THIS IS A COMMITTED SCRIPT AND NOT A SCRATCH FILE
------------------------------------------------------
`CONSTRAINT-INVENTORY-001` §2b: three sessions running, a column or a paragraph of this
estate has turned out to be a COVERAGE CLAIM that nobody ever verified — `-44` the
`machine` column, `-45` the `source` column, `-46` the inventory's own ranking prose,
which was wrong by eleven. The reason the claims survive is that verifying one by hand is
tedious and every cheaper check passes. So the tedious thing is an instrument now.

    python3 scripts/mutation_control.py --list
    python3 scripts/mutation_control.py                    # every probe, ~20 min
    python3 scripts/mutation_control.py --only 13 P6 P7    # a few

For each probe it copies the working tree to a scratch directory, applies ONE forbidden
move, runs the WHOLE suite, and reports every test that went red. A probe with no catchers
is an unguarded constraint — that is the measurement, and it is the only evidence that
earns a `FOR` or a `BINDS` in §1's `machine` column (`-44`'s ruling).

TWO THINGS THIS SCRIPT EXISTS TO STOP YOU DOING
------------------------------------------------
1. **Grading from the column.** The `machine` cell names the tests written FOR a
   constraint. It never names the tests that happen to catch it, and for C42 those were
   most of them. Count catchers, not pointers.
2. **Reading a red as the red you wanted.** `--only` prints every catcher, not the first.
   Eight of C42's fifteen were held solely by an instrument-reruns-to-itself test, which
   catches a hand-edit and is blind to a number a changed instrument re-derives. A
   reproducibility pin is not a freeze, and you only see that in the catcher list.

ADDING A PROBE: append to `PROBES`. A probe is `(slug, description, fn)` where `fn` takes
the scratch root and makes exactly one forbidden move. Keep them one-move: a probe that
changes two things cannot tell you which one the suite saw.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = "data"
DOCS = "docs/preregistration"
DEFAULT_SCRATCH = Path(os.environ.get("MUTATION_SCRATCH", "/tmp/wt-mutation-control"))


# ----------------------------------------------------------------------------- helpers
def _json_edit(root: Path, rel: str, *path_and_value):
    """Set one key. `_json_edit(root, "data/x.json", "a", "b", 3)` sets x["a"]["b"] = 3."""
    *path, value = path_and_value
    p = root / rel
    obj = json.loads(p.read_text())
    node = obj
    for k in path[:-1]:
        node = node[k]
    if path[-1] not in node:
        raise SystemExit(f"PROBE SITE MISSING: {rel} has no {'.'.join(map(str, path))}")
    node[path[-1]] = value
    p.write_text(json.dumps(obj, indent=2) + "\n")


def _prose_edit(root: Path, rels: list[str], old: str, new: str):
    hits = 0
    for rel in rels:
        p = root / rel
        if not p.exists():
            continue
        text = p.read_text()
        hits += text.count(old)
        p.write_text(text.replace(old, new))
    if hits == 0:
        raise SystemExit(f"PROBE SITE MISSING: {old!r} in {rels}")


R9 = f"{DATA}/reg-009-result.json"
R10 = f"{DATA}/reg-010-half-integer-banding.json"
BC = f"{DATA}/reg-009-band-count.json"
BCF = f"{DATA}/reg-009-band-count-filled.json"
PRIMARY = ("psi", "pooled|R_MID|raw")

BAND_DOCS = [f"{DOCS}/RESULT-REG-009-band-count.md",
             f"{DOCS}/RESULT-REG-009-band-count-filled.md",
             f"{DOCS}/REG-009-p3-lifetime-sourced-delta.md",
             f"{DOCS}/CONSTRUCTION-REG-009-coverage-fill.md"]
RESULT_DOCS = [f"{DOCS}/RESULT-REG-009.md"]


# ------------------------------------------------- REG-010 §4's fifteen, in §4's order
PROBES: list[tuple[str, str, object]] = [
    ("01", "the 683 pairs",
     lambda r: (_json_edit(r, R9, "counts", "pairs_pooled", 684),
                _json_edit(r, R9, *PRIMARY, "n", 684))),
    ("02", "the 428 distinct pairs",
     lambda r: _json_edit(r, R9, *PRIMARY, "distinct_pairs", 429)),
    ("03", "the 665 admissible rows",
     lambda r: _json_edit(r, R9, *PRIMARY, "n_admissible", 666)),
    ("04", "Ψ = 0.6586 and its clustered interval",
     lambda r: (_json_edit(r, R9, *PRIMARY, "psi", 0.6686466165413534),
                _json_edit(r, R9, *PRIMARY, "ci_lo", 0.6310514299447248))),
    ("05", "A", lambda r: _json_edit(r, R9, *PRIMARY, "A", 0.9636456808199122)),
    ("06", "S", lambda r: _json_edit(r, R9, "S", "R_MID", [0.1490922401171303, 95, 683])),
    ("07", "Ψ_rect",
     lambda r: _json_edit(r, R9, "psi_rect", "calibration", "admissible_share", 0.10)),
    ("08", "Ψ_rect(α̂)",
     lambda r: (_json_edit(r, R9, "psi_rect", "measured", "rises_of_admissible", 0.988),
                _json_edit(r, R9, "stopping", "psi_rect_alpha_hat", 0.988))),
    ("09", "α̂", lambda r: _json_edit(r, R9, "alpha_hat", 0.418)),
    ("10", "the verdicts on P1..P4",
     lambda r: _json_edit(r, R9, "predictions", "P3", True)),
    ("11", "REG-009's numbering",
     lambda r: _prose_edit(r, [f"{DOCS}/REG-009-p3-lifetime-sourced-delta.md"],
                           "\n## 12 ", "\n## 13 ")),
    ("12", "the 151 tier-0 events",
     lambda r: (_json_edit(r, BC, "events_total", 152),
                _json_edit(r, BCF, "events_total", 152))),
    ("13", "the 98 firms — PROSE ONLY; it has no artifact field at all",
     lambda r: _prose_edit(r, BAND_DOCS, "98 firms", "99 firms")),
    ("14", "the 110 of the band counts",
     lambda r: _json_edit(r, BC, "events_joinable", 111)),
    ("15", "the 133 of the band counts",
     lambda r: _json_edit(r, BCF, "events_joinable", 134)),
    # The prose axis. Artifacts untouched — this is the half `-46` found unguarded.
    ("P1", "prose: 683", lambda r: _prose_edit(r, RESULT_DOCS, "683", "684")),
    ("P2", "prose: 428", lambda r: _prose_edit(r, RESULT_DOCS, "428", "429")),
    ("P3", "prose: 665", lambda r: _prose_edit(r, RESULT_DOCS, "665", "666")),
    ("P4", "prose: 0.6586", lambda r: _prose_edit(r, RESULT_DOCS, "0.6586", "0.6686")),
    ("P5", "prose: 151", lambda r: _prose_edit(r, BAND_DOCS, "151 events", "152 events")),
    ("P6", "prose: 110", lambda r: _prose_edit(r, BAND_DOCS, "110 of", "111 of")),
    ("P7", "prose: 133", lambda r: _prose_edit(r, BAND_DOCS, "133 of", "134 of")),
]


def run_probe(probe, scratch: Path, jobs_note: str = "") -> dict:
    slug, desc, fn = probe
    root = scratch / slug
    shutil.rmtree(root, ignore_errors=True)
    shutil.copytree(ROOT, root, ignore=shutil.ignore_patterns(
        "__pycache__", ".pytest_cache", ".git", "*.tgz"))
    try:
        fn(root)
    except SystemExit as exc:
        shutil.rmtree(root, ignore_errors=True)
        return {"probe": slug, "what": desc, "error": str(exc), "catchers": []}
    env = dict(os.environ, PYTHONPATH=str(root / "src"), PYTHONDONTWRITEBYTECODE="1")
    proc = subprocess.run(
        [sys.executable, "-m", "pytest", "-q", "-p", "no:cacheprovider",
         "--no-header", "--tb=no", "-rf"],
        cwd=str(root), capture_output=True, text=True, env=env, timeout=7200)
    catchers = sorted(set(re.findall(r"^FAILED (tests/\S+)", proc.stdout, re.M)))
    shutil.rmtree(root, ignore_errors=True)
    return {"probe": slug, "what": desc, "catchers": catchers}


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--only", nargs="*", metavar="SLUG")
    ap.add_argument("--list", action="store_true")
    ap.add_argument("--jobs", type=int, default=2)
    ap.add_argument("--scratch", type=Path, default=DEFAULT_SCRATCH)
    ap.add_argument("--out", type=Path)
    args = ap.parse_args()

    if args.list:
        for slug, desc, _ in PROBES:
            print(f"{slug:>3}  {desc}")
        return 0

    chosen = [p for p in PROBES if not args.only or p[0] in args.only]
    if not chosen:
        print(f"no probe matches {args.only}; --list to see them", file=sys.stderr)
        return 2
    args.scratch.mkdir(parents=True, exist_ok=True)

    rows = []
    with ThreadPoolExecutor(max_workers=max(1, args.jobs)) as ex:
        for row in ex.map(lambda p: run_probe(p, args.scratch), chosen):
            rows.append(row)
            if row.get("error"):
                print(f"[ERROR] {row['probe']:>3}  {row['error']}", flush=True)
                continue
            mark = "RED  " if row["catchers"] else "GREEN"
            print(f"[{mark}] {row['probe']:>3}  {row['what']}", flush=True)
            for c in row["catchers"]:
                print(f"           {c}", flush=True)

    green = [r for r in rows if not r.get("error") and not r["catchers"]]
    print("\n" + "=" * 84)
    print(f"{len(rows) - len(green)}/{len(rows)} probes caught. "
          f"{len(green)} UNGUARDED: {[r['probe'] for r in green] or 'none'}")
    print("A probe with no catchers is the evidence a guard is needed. A probe whose only")
    print("catcher reruns the instrument is a reproducibility pin, NOT a freeze — read the")
    print("list above before you write a grade into CONSTRAINT-INVENTORY-001 §1.")
    print("=" * 84)
    if args.out:
        args.out.write_text(json.dumps(rows, indent=2) + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
