#!/usr/bin/env python3
"""wealthTensor-57 · red-proof the P11 leg rows.

WHY. "A row is not done when it is green; it is done when it has been seen red." Five of the
seven P11 rows are red on the day they were written, because their legs have not run -- that
is five live demonstrations that the check can fail. The two green ones (P11a, P11c) have not
been seen red, and a green row nobody has watched fail is a decoration.

WHAT. For each GREEN P11 row: copy the RESULT document aside, delete the verdict line the row
greps for, run the row's OWN check verbatim, require a non-zero exit, restore, and compare
byte-for-byte. A row whose mutation leaves it green is reported WEAK -- that is the finding,
not the pass. Same contract as scripts/redproof_apparatus.py, pointed at a different artefact.

    python3 scripts/redproof_p11.py
"""
import hashlib
import pathlib
import re
import subprocess
import sys

REPO = pathlib.Path(__file__).resolve().parent.parent
TSV = REPO / "docs" / "done-criteria.tsv"
VERDICT_LINE = re.compile(r"^- \*\*Verdict: .*$", re.M)


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def rows():
    for line in TSV.read_text(encoding="utf-8").split("\n"):
        parts = line.split("\t")
        if len(parts) >= 4 and re.fullmatch(r"P11[a-z]", parts[0]) and parts[3].startswith("cmd:"):
            cmd = parts[3][len("cmd:"):]
            m = re.search(r"docs/RESULT-END-TO-END-001[^ ']*\.md", cmd)
            yield parts[0], cmd, (REPO / m.group(0) if m else None)


def run(cmd):
    return subprocess.run(["bash", "-c", cmd], capture_output=True).returncode


def main():
    weak, proven, skipped = [], [], []
    for rid, cmd, target in rows():
        if target is None or not target.exists():
            skipped.append((rid, "artefact absent — the row is RED right now, which IS its red-proof"))
            continue
        if run(cmd) != 0:
            skipped.append((rid, "row is already RED — no mutation needed"))
            continue
        before, digest = target.read_text(encoding="utf-8"), sha(target)
        mutated, n = VERDICT_LINE.subn("- **(verdict line removed by redproof_p11)**", before, count=1)
        try:
            if n < 1:
                weak.append((rid, "mutation did not apply: no verdict line found"))
                continue
            target.write_text(mutated, encoding="utf-8")
            rc = run(cmd)
            (proven if rc != 0 else weak).append(
                (rid, "check exits %d with the verdict line removed" % rc))
        finally:
            target.write_text(before, encoding="utf-8")
            if sha(target) != digest:
                sys.exit("FATAL: %s not restored byte-for-byte" % target)

    for rid, why in proven:
        print("  PROVEN  %s — %s" % (rid, why))
    for rid, why in skipped:
        print("  RED     %s — %s" % (rid, why))
    for rid, why in weak:
        print("  WEAK    %s — %s" % (rid, why))
    print("\n%d proven by mutation, %d red on their own, %d WEAK" % (len(proven), len(skipped), len(weak)))
    return 1 if weak else 0


if __name__ == "__main__":
    sys.exit(main())
