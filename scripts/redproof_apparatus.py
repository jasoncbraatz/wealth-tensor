#!/usr/bin/env python3
"""wealthTensor-54 · red-proof the manuscript apparatus rows.

WHY. A criterion that has never been seen to FAIL is not a criterion, it is a decoration.
-49 established this for the existence leg ("an absence predicate passes vacuously on a
missing file"); this script generalises it to every writable row in done-criteria.tsv:
for each row, apply the smallest mutation that ought to break it, run the row's OWN check
verbatim, and require a non-zero exit. A row whose mutation leaves it green is reported as
WEAK -- that is the finding, not the pass.

Reversibility comes first, as always: the manuscript is copied aside before the first
mutation and restored in a finally: block, and the copy is compared byte-for-byte at the
end. Run it any time; it leaves the tree exactly as it found it.

    python3 scripts/redproof_apparatus.py            # all papers
    python3 scripts/redproof_apparatus.py P3         # one prefix
"""
import hashlib
import pathlib
import re
import subprocess
import sys

REPO = pathlib.Path(__file__).resolve().parent.parent
TSV = REPO / "docs" / "done-criteria.tsv"

PAPER = {
    "P1": REPO / "docs/papers/paper-III-dual-tensor/paper-III.md",
    "P3": REPO / "docs/papers/paper-II-redistribution/paper-II.md",
    "P5": REPO / "docs/papers/paper-IV-composition/paper-IV.md",
}


def sub(pattern, repl, flags=0, count=1):
    def f(t):
        new, n = re.subn(pattern, repl, t, count=count, flags=flags)
        if n < 1:
            raise RuntimeError("mutation did not apply: %r" % pattern)
        return new
    return f


def within(start_re, end_re, inner):
    """Apply `inner` ONLY inside a named section.

    -54 built this after the first run reported FIVE rows WEAK. Every one was the
    harness's fault: the mutations matched the first occurrence ANYWHERE in the file, and
    in a 200 kB manuscript the first '1. ' is nowhere near the contributions list. A
    mutation that lands outside the section the row measures does not mutate, and a
    mutation that does not mutate reports a sound guard as weak -- which is the more
    dangerous direction, because it invites someone to "strengthen" a check that was
    already right. Scope the mutation to the section, or do not trust the verdict.
    """
    def f(t):
        m = re.search(start_re, t, re.M)
        if not m:
            raise RuntimeError("section not found: %r" % start_re)
        e = re.search(end_re, t[m.end():], re.M)
        stop = m.end() + (e.start() if e else len(t) - m.end())
        return t[:m.end()] + inner(t[m.end():stop]) + t[stop:]
    return f


def append(line):
    return lambda t: t + "\n" + line + "\n"


CONTRIB = (r"^\*\*Contributions\.\*\*", r"^## 2 ")
LIMITS = (r"^## [0-9]+ · Limitations", r"^## ")
DATACODE = (r"^## [0-9]+ · Data and code availability", r"^## ")
ABSTRACT = (r"^## Abstract", r"^\*\*Keywords")
KEYWORDS = (r"^\*\*Keywords:\*\*", r"^\*\*JEL")


# row-suffix -> (human name, mutation). Only rows whose break is unambiguous.
MUTATIONS = {
    "a": ("abstract padded past 250 words",
          within(*ABSTRACT, inner=lambda t: t + " " + ("padding " * 80).strip() + "\n\n")),
    "b": ("author block loses the affiliation line",
          sub(r"^\*Independent researcher\*", "*Researcher*", re.M)),
    "c": ("three more keywords are added",
          within(*KEYWORDS, inner=lambda t: " alpha · beta · gamma ·" + t)),
    "d": ("JEL line renamed",
          sub(r"^\*\*JEL classification:\*\*", "**JEL codes:**", re.M)),
    "e": ("every numbered contribution demoted to prose",
          within(*CONTRIB, inner=sub(r"^([0-9]+)\. ", r"- ", re.M, count=0))),
    "f": ("Abandoned approaches demoted to an unnumbered appendix",
          sub(r"^## ([0-9]+) · Abandoned approaches", "## Appendix A · Abandoned approaches", re.M)),
    "g": ("the against-comfort item is no longer FIRST",
          within(*LIMITS, inner=sub(r"^1\. \*\*", "9. **", re.M))),
    "h": ("the test command drops out of data-and-code",
          within(*DATACODE, inner=sub(r"pytest", "pyt3st", 0, count=0))),
    "i": ("a live placeholder is left in the manuscript",
          append("**Commit SHA at submission:** [placeholder]")),
    "j": ("the SMD overclaim-forbidding test is no longer named ANYWHERE",
          sub(r"test_excess_demand_is_monotone_here_so_this_is_not_an_SMD_result",
              "test_excess_demand_is_monotone", 0, count=0)),
    "l": ("the loss is quietly dropped from the abstract",
          within(*ABSTRACT, inner=lambda t: "\n\nA tidy summary with every number intact and no "
                 "mention of what this paper got wrong, which is exactly the abstract this row "
                 "exists to refuse. " + ("filler " * 150).strip() + "\n\n")),
    "m": ("the code pin is replaced by one that resolves to nothing",
          within(*DATACODE, inner=sub(r"\*\*[0-9a-f]{7}\*\*|`[0-9a-f]{7}`", "**0000000**"))),
    "n": ("the asserted test count drifts away from the suite",
          sub(r"18 tests", "19 tests", 0, count=0)),
}


def rows_for(prefix):
    out = {}
    for line in TSV.read_text(encoding="utf-8").split("\n"):
        f = line.split("\t")
        # Match the SHAPE P<digit><letter>. startswith(prefix) collected the CORPUS rows
        # P11/P12/P13 into family "P1" -- harmless only because "1"/"2"/"3" are not
        # mutation keys, which is luck, not design. Same defect as the generator's old
        # CORPUS tuple, and banked as a lesson the same afternoon.
        if len(f) == 4 and f[3].startswith("cmd:") \
                and re.fullmatch(re.escape(prefix) + r"[a-z]", f[0]):
            out[f[0][len(prefix):]] = f[3][4:]
    return out


def run(cmd):
    return subprocess.run(["bash", "-c", cmd], cwd=str(REPO),
                          stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL).returncode


def main():
    want = sys.argv[1:] or list(PAPER)
    weak, tested, skipped = [], 0, []
    for prefix in want:
        paper = PAPER[prefix]
        original = paper.read_bytes()
        digest = hashlib.sha256(original).hexdigest()
        checks = rows_for(prefix)
        print("\n=== %s  (%s)" % (prefix, paper.name))
        try:
            for suffix, (name, mutate) in MUTATIONS.items():
                rid = prefix + suffix
                if suffix not in checks:
                    skipped.append("%s (no cmd: row)" % rid)
                    continue
                if run(checks[suffix]) != 0:
                    print("   %-5s SKIP  row is already red unmutated" % rid)
                    skipped.append("%s (already red)" % rid)
                    continue
                try:
                    paper.write_text(mutate(original.decode("utf-8")), encoding="utf-8")
                except RuntimeError as e:
                    print("   %-5s SKIP  %s" % (rid, e))
                    skipped.append("%s (mutation n/a)" % rid)
                    paper.write_bytes(original)
                    continue
                rc = run(checks[suffix])
                paper.write_bytes(original)
                tested += 1
                if rc == 0:
                    print("   %-5s WEAK  survived: %s" % (rid, name))
                    weak.append((rid, name))
                else:
                    print("   %-5s red   %s" % (rid, name))
        finally:
            paper.write_bytes(original)
            assert hashlib.sha256(paper.read_bytes()).hexdigest() == digest, \
                "RESTORE FAILED for %s -- recover from git" % paper
        print("   restored, sha256 %s" % digest[:12])

    print("\n%d mutations run, %d survived (WEAK), %d skipped" % (tested, len(weak), len(skipped)))
    for rid, name in weak:
        print("   WEAK %s: %s" % (rid, name))
    return 1 if weak else 0


if __name__ == "__main__":
    sys.exit(main())
