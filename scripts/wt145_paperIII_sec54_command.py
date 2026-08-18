#!/usr/bin/env python3
"""wt145 · wealthTensor-81 · the ROOT of Paper IV's IV-1, repaired in Paper III.

Paper IV §10 attributed the diagonality rejection to wt026_severe_test.py. It got that
from Paper III §11, whose "Regenerate §5" bullet names wt026 -- and wt026 is §5.3's
instrument. Paper III's §5.4 results (the recognition rate and the off-diagonal) have had
NO named command in any manuscript since they were written. Paper IV inherited the nearest
one. Naming the real instrument in Paper III is the repair that stops the next inheritance.

DELIBERATELY RESTATES NO FIGURE. tests/test_restatement_reach.py pins how many times each
declared figure appears per section; this bullet names a command and no number.
"""
import pathlib, re, shutil

REPO = pathlib.Path(__file__).resolve().parent.parent
P3 = REPO / "docs/papers/paper-III-dual-tensor/paper-III.md"
TAG = "wt145"

OLD = """- **Test suite:** `python3 -m pytest tests/ -q` runs the whole repository; at the pinned commit"""
NEW = """- **Regenerate §5.4:** `python3 scripts/wt089_recognition_and_offdiagonal.py`. §5.4 asks two
  questions of §5.3's sample that it was not collected for, and neither is answered by the command
  above: `wt026_severe_test.py` is §5.3's instrument and prints nothing about the recognition rate
  or the off-diagonal. That distinction went unrecorded until wealthTensor-81, and Paper IV §10
  inherited the nearer command as a result. The same caveat as §5.3's applies here — the run
  reproduces the instrument and not the sample, and its own §2 reconciles the rebuild against
  `RESULT-002` before any statistic is computed.
- **Test suite:** `python3 -m pytest tests/ -q` runs the whole repository; at the pinned commit"""


def main():
    t = P3.read_text(encoding="utf-8")
    if NEW.split("\n")[0] in t:
        print("ALREADY APPLIED")
    else:
        n = t.count(OLD)
        assert n == 1, "anchor count %d" % n
        shutil.copy2(P3, str(P3) + ".bak-" + TAG)
        P3.write_text(t.replace(OLD, NEW, 1), encoding="utf-8")
        print("applied")
    t = P3.read_text(encoding="utf-8")
    flat = " ".join(t.split())
    checks = [
        ("Q1 wt089 is named in Paper III", "wt089_recognition_and_offdiagonal.py" in t),
        ("Q2 the §5.3 bullet still names wt026", "wt026_severe_test.py --universe pilot --onset peak" in flat),
        ("Q3 NEGATIVE - no figure restated: 4.12 count unchanged in §11",
         "Regenerate §5.4:** `python3 scripts/wt089" in flat and "4.12" not in NEW),
        ("Q4 NEGATIVE - no new SHA", sorted(set(re.findall(r"\b[0-9a-f]{7}\b", NEW))) == []),
        ("Q5 the test-suite bullet survives exactly once", flat.count("runs the whole repository") == 1),
    ]
    for name, ok in checks:
        print("  %s  %s" % ("PASS" if ok else "FAIL", name))
    assert all(ok for _, ok in checks), "post-conditions failed"
    print("wt145: 5/5 green.")


main()
