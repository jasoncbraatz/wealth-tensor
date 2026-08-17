#!/usr/bin/env python3
"""wealthTensor-65 · WHEN did paper-III's §4.7 actually move?

-64's card asserts the §4.7 freeze went red at `6314302` and names that commit's III-3
repair as the licence. The card is a claim about history, and a claim about history is
checkable. This walks every commit that touched paper-III.md since `REG-012` registered
at `ba59370` and prints §4.7's digest at each, so the moment of the move is measured
rather than inferred from a commit message that happens to sound right.

WT-092: what is the widest object this check's own words claim, and what is the
narrowest thing it actually touches? The card's words claim "red since -63's commit
6314302". The narrowest thing anybody had touched was the failure message at HEAD.
"""
from __future__ import annotations

import hashlib
import re
import subprocess

PAPER_REL = "docs/papers/paper-III-dual-tensor/paper-III.md"
REG_012_COMMIT = "ba59370e49bce580820183484f1e4c58bffdcdf6"

H47 = re.compile(r"^### 4\.7 · .*$", re.M)
H48 = re.compile(r"^### 4\.8 · ", re.M)


def section_47(text: str) -> str:
    start = H47.search(text)
    assert start, "no 4.7 heading"
    rest = text[start.start():]
    end = H48.search(rest)
    assert end, "no 4.8 heading"
    return rest[: end.start()]


def git(*args: str) -> str:
    return subprocess.run(("git", *args), capture_output=True, text=True,
                          check=True).stdout


def digest_at(sha: str) -> str:
    blob = git("show", f"{sha}:{PAPER_REL}")
    return hashlib.sha256(section_47(blob).encode("utf-8")).hexdigest()


revs = git("log", "--reverse", "--format=%H %s",
           f"{REG_012_COMMIT}..HEAD", "--", PAPER_REL).splitlines()

base = digest_at(REG_012_COMMIT)
print(f"{'registration':>12}  {base[:16]}  ba59370  (REG-012 registered)")

prev = base
for line in revs:
    sha, subject = line.split(" ", 1)
    d = digest_at(sha)
    mark = "MOVED  <<<" if d != prev else "same      "
    print(f"{mark:>12}  {d[:16]}  {sha[:7]}  {subject[:64]}")
    prev = d

print()
print("registration-era :", base)
print("HEAD             :", prev)
print("moved            :", base != prev)
