#!/usr/bin/env python3
"""wt215 — close P7 by making it CHECKABLE rather than asserted.

`board.py` treats `manual:` as NEVER auto-closing, so P7 could not be closed by editing its
prose -- it would render PENDING-HUMAN forever. That was right while "done" meant a
convergence criterion nobody could evaluate. It stopped being right at `-102`, when Jason
replaced the criterion with docs/DEFINITION-OF-DONE-SHIP.md -- a punch list, and a punch list
is checkable by construction.

So P7 becomes a `cmd:` criterion over the four things the DoD actually requires, and it
REOPENS if any of them regresses:

  1. SHIP-LIST.md is CLOSED -- no OPEN S1 or S2 remains on it.
  2. HARD C-e is zero across all three in-scope manuscripts -- no session number, REVIEW doc,
     LEDGER.md or WT-0NN ticket id, which is the one C-class type with a mechanical signature.
  3. docs/FIGURE-PLAN.md and docs/SHIP-STATEMENT.md exist and are substantial (DoD 4.2, 4.3).
  4. The v1.0-preprint tag exists and points at a commit in this history.

This is project bookkeeping, not a review instrument: DoD 1.1 freezes the apparatus that
LOOKS AT THE MANUSCRIPTS, and this looks at whether the ship conditions hold. Idempotent.
"""
import pathlib, sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
TSV = ROOT / "docs/done-criteria.tsv"

CHECK = (
 'cmd:cd $HOME/repos/wealth-tensor && '
 '! grep -qE "^\\| *\\*\\*SL-[0-9]+\\*\\* *\\| *(S1|S2) *\\| *OPEN" docs/SHIP-LIST.md && '
 '! grep -rqE "wealthTensor-[0-9]+|REVIEW-[0-9]{3}|LEDGER\\.md|WT-[0-9]{3}" '
 'docs/papers/paper-II-redistribution/paper-II.md '
 'docs/papers/paper-III-dual-tensor/paper-III.md '
 'docs/papers/paper-IV-composition/paper-IV.md && '
 '[ "$(wc -l < docs/FIGURE-PLAN.md)" -gt 100 ] && '
 '[ "$(wc -l < docs/SHIP-STATEMENT.md)" -gt 100 ] && '
 'git rev-parse -q --verify refs/tags/v1.0-preprint >/dev/null'
)

def main():
    lines = TSV.read_text(encoding="utf-8").split("\n")
    for i, l in enumerate(lines):
        f = l.split("\t")
        if f and f[0] == "P7":
            if f[3].startswith("cmd:"):
                print("ALREADY-APPLIED: P7 is already a cmd criterion"); return 0
            if not f[3].startswith("manual:"):
                print("FAIL: P7's check is neither manual: nor cmd:"); return 2
            bak = TSV.with_suffix(".tsv.bak-wt215")
            if not bak.exists(): bak.write_text("\n".join(lines), encoding="utf-8")
            lines[i] = "\t".join([f[0], f[1], f[2], CHECK])
            TSV.write_text("\n".join(lines), encoding="utf-8")
            print("APPLIED: P7 is now a cmd criterion over the four DoD ship conditions")
            return 0
    print("FAIL: no P7 row found"); return 2

if __name__ == "__main__":
    sys.exit(main())
