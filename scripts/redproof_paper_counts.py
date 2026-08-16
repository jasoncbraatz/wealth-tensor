#!/usr/bin/env python3
"""wealthTensor-58 · red-proof tests/test_paper_test_counts_are_derived.py.

A ROW IS NOT DONE UNTIL SEEN RED. These six asserts are cheap to write and would be worthless
if any of them passed vacuously, so each is mutated on the real artefact, its OWN test is run,
a NON-ZERO exit is required, and the artefact is restored and checked byte-for-byte by SHA-256.

Same contract as scripts/redproof_p11.py: mutate -> run -> require red -> restore -> verify.
Run:  python3 scripts/redproof_paper_counts.py
"""
import hashlib
import pathlib
import subprocess
import sys

REPO = pathlib.Path(__file__).resolve().parent.parent
MODULE = "tests/test_paper_test_counts_are_derived.py"
P2 = REPO / "docs/papers/paper-II-redistribution/paper-II.md"
P3 = REPO / "docs/papers/paper-III-dual-tensor/paper-III.md"

# (label, file, old, new, the test that must go red)
MUTATIONS = [
    ("Paper III's suite total drifts", P3,
     "held **100** tests", "held **101** tests",
     "test_paper_iii_suite_total_at_the_pin_is_what_paper_iii_says"),
    ("Paper III's paper-scoped count drifts", P3,
     "the **62** in", "the **63** in",
     "test_paper_iii_paper_scoped_count_at_the_pin_is_what_paper_iii_says"),
    ("Paper III stops naming a module it counts", P3,
     "`tests/test_lag.py`", "`tests/test_lagg.py`",
     "test_paper_iii_names_every_module_it_counts"),
    ("Paper II's live module count drifts", P2,
     "the **18** tests in", "the **19** tests in",
     "test_paper_ii_module_count_is_live_and_is_what_paper_ii_says"),
    ("Paper II §1's old over-claim comes back", P2,
     "held in place by the 18 tests in", "held in place by 18 tests including two and by the tests in",
     "test_paper_ii_does_not_claim_both_named_guards_are_in_the_counted_module"),
]


def sha(path: pathlib.Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run(test: str) -> int:
    return subprocess.run(
        [sys.executable, "-m", "pytest", f"{MODULE}::{test}", "-q"],
        cwd=REPO, capture_output=True, text=True,
    ).returncode


survivors, proven = [], 0
for label, path, old, new, test in MUTATIONS:
    before_sha, before = sha(path), path.read_text()
    if before.count(old) != 1:
        survivors.append(f"{label}: anchor appears {before.count(old)}x, cannot mutate cleanly")
        continue
    try:
        path.write_text(before.replace(old, new))
        rc = run(test)
    finally:
        path.write_text(before)
    assert sha(path) == before_sha, f"RESTORE FAILED on {path.name} -- repo is dirty, fix by hand"
    if rc == 0:
        survivors.append(f"{label}: {test} stayed GREEN under mutation")
    else:
        proven += 1
        print(f"  red  ✓  {label}  ->  {test}")

# The precondition guard has no artefact-side mutation; it is exercised by the two pinned rows,
# which cannot resolve their counts at all if the pin stops naming a commit. Stated, not hidden.
print(f"\nproven by mutation: {proven}/{len(MUTATIONS)}"
      f"  ·  not mutated (precondition, exercised transitively): 1"
      f"  ·  survivors: {len(survivors)}")
for s in survivors:
    print(f"  SURVIVOR: {s}")
sys.exit(1 if survivors else 0)
