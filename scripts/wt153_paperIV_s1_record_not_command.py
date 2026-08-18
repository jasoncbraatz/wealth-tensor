#!/usr/bin/env python3
"""wt153 · REVIEW-024 · Paper IV §1 promised something §10 refuses to do.

FINDING (REVIEW-024, row 388811fc0a). §1 says "§10 names the command for each". §10 says, in
bold: "Those files, not a command, are the record of §6." §10 was corrected at wealthTensor-82
("this bullet said 'regenerate' until wealthTensor-82"); §1's promise ABOUT §10 was not.

REPAIR. Rewrite §1's clause to name what §10 actually names, in §10's own terms. No hedge is
added: the claim is narrowed, not caveated (CO-AUTHOR-CHARTER §2, the illegal ABSORB move).

Refuses on a moved anchor. Rolls back on any failed post-condition.
"""
import re, subprocess, sys, pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
P4 = ROOT / "docs/papers/paper-IV-composition/paper-IV.md"

OLD = ("Numbers appearing below without a citation to II or III come\n"
       "from two places and §10 names the command for each: §6's are `REG-013`'s, and §5's and §8's are the\n"
       "output of the fourth paper's apparatus, which is still in this repository and still runs.")

NEW = ("Numbers appearing below without a citation to II or III come\n"
       "from two places and §10 names the record for each: §6's are `REG-013`'s, and its record is the\n"
       "committed output of that run rather than a command, because the instrument re-queries a live\n"
       "database; §5's and §8's are the output of the fourth paper's apparatus, which is still in this\n"
       "repository and still runs.")

FORBIDDEN = "§10 names the command for each"
S10_ANCHOR = "**Those files, not a\n  command, are the record of §6.**"

def fail(msg):
    print("wt153: FAIL — " + msg); sys.exit(1)

src = P4.read_text(encoding="utf-8")
before = src

# --- PRE-CONDITIONS (refuse on a moved anchor) --------------------------------
if src.count(OLD) != 1:
    fail("anchor not found exactly once in paper-IV.md (count=%d) — REFUSING, the site moved" % src.count(OLD))
if S10_ANCHOR not in src:
    fail("§10's 'Those files, not a command' sentence is not where this repair reads it — REFUSING")

def defensive_count(t):
    return len(re.findall(r"(?im)^\s*(?:however|nevertheless|that said|to be fair|admittedly|we concede|it must be admitted)\b", t))

d_before = defensive_count(before)
lines_before = before.count("\n")

src = src.replace(OLD, NEW)
P4.write_text(src, encoding="utf-8")

def rollback(msg):
    P4.write_text(before, encoding="utf-8")
    print("wt153: ROLLED BACK — " + msg); sys.exit(1)

after = P4.read_text(encoding="utf-8")
checks = []
def check(name, ok, negative=False):
    checks.append((name, ok, negative))
    if not ok: rollback("post-condition failed: " + name)

# --- POST-CONDITIONS ----------------------------------------------------------
check("P1  the new clause is present exactly once", after.count(NEW) == 1)
check("P2  NEGATIVE: the old clause is gone", after.count(OLD) == 0, True)
check("P3  NEGATIVE: '§10 names the command for each' occurs nowhere in the manuscript",
      after.count(FORBIDDEN) == 0, True)
check("P4  NEGATIVE: no defensive opener was added (ABSORB is illegal, charter §2)",
      defensive_count(after) <= d_before, True)
check("P5  §10's 'Those files, not a command, are the record of §6' is untouched",
      S10_ANCHOR in after)
check("P6  §10's 'Re-run the instrument' bullet is untouched",
      "**Re-run the instrument:** `python3 scripts/reg013_citation_whitespace.py`" in after)
check("P7  the edit added exactly two lines", after.count("\n") - lines_before == 2)
check("P8  §1's sentence and §10's restatement now agree that §6's is a record, not a command",
      "§10 names the record for each" in after and "not a\n  command, are the record of §6" in after)
_dirty = [l for l in subprocess.run(["git","-C",str(ROOT),"diff","--name-only"],
          capture_output=True,text=True).stdout.split("\n") if l.strip()]
check("P9  paper-IV.md is dirty and NO OTHER manuscript is",
      "docs/papers/paper-IV-composition/paper-IV.md" in _dirty
      and not [d for d in _dirty if d.startswith("docs/papers/") and d.endswith(".md")
               and d != "docs/papers/paper-IV-composition/paper-IV.md"])
check("P10 NEGATIVE: no en-dash/em-dash mangling — the manuscript's — count is unchanged",
      after.count("—") == before.count("—"), True)

print("wt153 · Paper IV §1 — 1 repair, %d post-conditions (%d NEGATIVE)"
      % (len(checks), sum(1 for _,_,n in checks if n)))
for name, ok, neg in checks:
    print(("  ✓ " if ok else "  ✗ ") + name)
print("\nNOW RUN: python3 scripts/wt148_promise_sweep.py  — it MUST go RC 1 with 388811fc0a STALE.")
print("That red is the proof the edit landed. scripts/wt153b_tsv.py clears it.")
