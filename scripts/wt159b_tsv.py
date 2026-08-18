#!/usr/bin/env python3
"""wt159b · one evidence column, widened — and the reason is a blind spot in wt154.

wt159 gave row d0729375b9 the evidence

    `git merge-base --is-ancestor fff7063 5efe626; echo $?`

which is the exactly right instrument for the sentence's claim (REG-013 was committed before the
instrument existed): it is a PREDICATE, and `echo $?` prints its answer.  wt154 flagged it under
D1, "evidence names no content-printing operation", because `merge-base --is-ancestor` writes
nothing to stdout.

**wt154 is wrong here and the row is not.**  An exit code is a read of behaviour — the same class
wt154 already declines to flag when a named test's pass/fail is the verdict.  Rather than widen a
committed instrument's criterion in a pass that is not about that instrument, this script widens
the EVIDENCE: the predicate stays, and the two timestamps that make the order legible without
running anything are added beside it.  The row gets strictly better; wt154's blind spot is
recorded in REVIEW-026 §5 and carded rather than silently patched.

RC 0 repaired · RC 2 refused or rolled back (from .bak-wt159b).
"""

import shutil
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
TSV = REPO / "docs/promises-adjudicated.tsv"
BAK = Path(str(TSV) + ".bak-wt159b")
PID = "d0729375b9"

OLD_EV = "`git merge-base --is-ancestor fff7063 5efe626; echo $?`"
NEW_EV = ("`git merge-base --is-ancestor fff7063 5efe626; echo $?` + `git log -1 "
          "--format='%h %ad' --date=iso fff7063` + `git log -1 --format='%h %ad' "
          "--date=iso 5efe626`")


def rows():
    out, head = [], []
    for line in TSV.read_text().splitlines():
        if line.startswith("#") or not line.strip():
            head.append(line)
        else:
            out.append(line.split("\t"))
    return head, out


def main():
    head, rs = rows()
    hit = [r for r in rs if r[1] == PID]
    if len(hit) != 1:
        print(f"wt159b: REFUSING — {PID} appears {len(hit)} times."); return 2
    if hit[0][4] != OLD_EV:
        print("wt159b: REFUSING — the evidence is not the string this script was written for.")
        return 2

    shutil.copy2(TSV, BAK)
    before_note = hit[0][5]
    try:
        hit[0][4] = NEW_EV
        TSV.write_text("\n".join(head + ["\t".join(r) for r in rs]) + "\n")

        checks = []

        def c(n, pol, cond, d=""):
            checks.append((n, pol, bool(cond), d))

        _, after = rows()
        row = [r for r in after if r[1] == PID][0]
        c("C1 the evidence now names the predicate AND two content-printing commands", "POSITIVE",
          row[4] == NEW_EV)
        c("C2 the note is unchanged", "POSITIVE", row[5] == before_note)
        c("C3 the row count is unchanged at 130", "POSITIVE", len(after) == 130, str(len(after)))

        for name, script, want in (("wt156", "scripts/wt156_reproducibility_sweep.py", 0),
                                   ("wt154", "scripts/wt154_evidence_discrimination_sweep.py", 0),
                                   ("wt148", "scripts/wt148_promise_sweep.py", 0),
                                   ("wt133", "scripts/wt133_crossref_sweep.py", 0)):
            r = subprocess.run([sys.executable, script], cwd=REPO,
                               capture_output=True, text=True)
            c(f"C{len(checks)+1} {name} returns {want}", "POSITIVE", r.returncode == want,
              f"rc={r.returncode}\n{r.stdout[-600:]}")

        c("C8 NEGATIVE every other row is byte-identical", "NEGATIVE",
          all("\t".join(a) == "\t".join(b) for a, b in zip(after, rs) if a[1] != PID))
        c("C9 NEGATIVE no manuscript changed", "NEGATIVE", not _dirty_manuscripts_beyond_iv())

        ok = all(x[2] for x in checks)
        nneg = sum(1 for x in checks if x[1] == "NEGATIVE")
        print(f"wt159b · POST-CONDITIONS ({len(checks)} total, {nneg} NEGATIVE, "
              f"{len(checks) - nneg} POSITIVE)")
        for n, pol, passed, d in checks:
            print(f"    [{'ok  ' if passed else 'FAIL'}] {n}" + (f"\n           {d}" if d and not passed else ""))
        if not ok:
            shutil.copy2(BAK, TSV)
            print("\nwt159b: ROLLED BACK from .bak-wt159b.")
            return 2
        print("\nwt159b: d0729375b9 widened; all four sweeps green.")
        return 0
    except Exception as exc:  # noqa: BLE001
        shutil.copy2(BAK, TSV)
        print(f"wt159b: EXCEPTION {exc!r} — ROLLED BACK.")
        return 2


def _dirty_manuscripts_beyond_iv():
    out = subprocess.run(["git", "status", "--porcelain"], cwd=REPO,
                         capture_output=True, text=True).stdout
    d = [l[3:] for l in out.splitlines()
         if "docs/papers/" in l and l.rstrip().endswith(".md")]
    return [x for x in d if x != "docs/papers/paper-IV-composition/paper-IV.md"]


if __name__ == "__main__":
    sys.exit(main())
