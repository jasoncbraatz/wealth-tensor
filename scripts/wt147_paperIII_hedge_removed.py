#!/usr/bin/env python3
"""wt147 · wealthTensor-81 · the guard fought wt145 and the guard was right.

test_defensive_count.py went red on paper-III: wt145's new §11 bullet added ONE defensive
sentence -- "The same caveat as §5.3's applies here". The guard's own instruction is not
"raise the baseline"; it is *if a finding seems to demand new hedging, it demands a NARROWER
CLAIM. Rewrite the claim and delete the hedge.* So the hedge is deleted and the claim is
made directly, which is also shorter and truer: this command re-pulls, so it reproduces the
instrument and not the sample. No baseline was raised.
"""
import pathlib, shutil

REPO = pathlib.Path(__file__).resolve().parent.parent
P3 = REPO / "docs/papers/paper-III-dual-tensor/paper-III.md"
TAG = "wt147"

OLD = """  or the off-diagonal. That distinction went unrecorded until wealthTensor-81, and Paper IV §10
  inherited the nearer command as a result. The same caveat as §5.3's applies here — the run
  reproduces the instrument and not the sample, and its own §2 reconciles the rebuild against
  `RESULT-002` before any statistic is computed."""
NEW = """  or the off-diagonal. This command re-pulls `companyfacts` as §5.3's does, so it reproduces the
  instrument and not the sample; its own §2 reconciles the rebuild against `RESULT-002` before it
  computes a statistic."""


def main():
    t = P3.read_text(encoding="utf-8")
    if NEW in t:
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
        ("S1 wt089 is still named in Paper III", "wt089_recognition_and_offdiagonal.py" in t),
        ("S2 the hedge is gone from the new bullet",
         "The same caveat as §5.3's applies here" not in flat),
        ("S3 the substance survives - instrument not sample",
         "reproduces the instrument and not the sample; its own §2 reconciles" in flat),
        ("S4 NEGATIVE - no defensive baseline file was touched",
         not (REPO / ("docs/papers/paper-III-dual-tensor/DEFENSIVE-BASELINE.json.bak-" + TAG)).exists()),
        ("S5 the §5.3 bullet still names wt026",
         "wt026_severe_test.py --universe pilot --onset peak" in flat),
    ]
    for name, ok in checks:
        print("  %s  %s" % ("PASS" if ok else "FAIL", name))
    assert all(ok for _, ok in checks), "post-conditions failed"
    print("wt147: 5/5 green.")


main()
