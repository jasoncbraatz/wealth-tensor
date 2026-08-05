#!/usr/bin/env python3
"""Staleness guard for docs/HANDOFF.md.

The handoff lives in the repo so it can be version-controlled and turned over rather than
accreted. The cost of that choice is that a stale file looks authoritative in a way a stale
chat message does not. This script is the price of admission -- HANDOFF-GATE.md §G-F is
explicit that the file half must not be adopted without it.

  --check   run at ORIENT. Compares the handoff's recorded gh_sha against HEAD and
            distinguishes code drift (blocker) from docs-only drift (advisory).
  --emit    run at WRAP. Refuses to bless the handoff on missing fields, TODO
            placeholders, a dirty tree, gh_sha != HEAD, or gate_passed: false.
"""
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
HANDOFF = ROOT / "docs" / "HANDOFF.md"
REQUIRED = ["project", "gh_sha", "updated", "session", "gate_passed", "gate_version"]


def sh(*args):
    return subprocess.run(args, cwd=ROOT, capture_output=True, text=True).stdout.strip()


def frontmatter():
    if not HANDOFF.exists():
        sys.exit("BLOCKER: docs/HANDOFF.md does not exist")
    text = HANDOFF.read_text()
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        sys.exit("BLOCKER: docs/HANDOFF.md has no YAML frontmatter")
    fm = {}
    for line in m.group(1).splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            fm[k.strip()] = v.strip().strip('"').strip("'")
    return fm, text


def files_changed_since(sha):
    out = sh("git", "diff", "--name-only", f"{sha}..HEAD")
    return [f for f in out.splitlines() if f]


def check():
    fm, _ = frontmatter()
    head = sh("git", "rev-parse", "HEAD")
    recorded = fm.get("gh_sha", "")
    print(f"handoff gh_sha : {recorded}")
    print(f"repo HEAD      : {head}")
    if recorded == head:
        print("IN SYNC: the handoff describes this exact commit.")
        return 0
    changed = files_changed_since(recorded) if recorded else []
    if not changed:
        print("ADVISORY: sha differs but no diff resolved (shallow clone or bad sha?).")
        return 0
    code = [f for f in changed if not f.startswith("docs/")]
    print(f"\n{len(changed)} file(s) changed since the handoff was written:")
    for f in changed:
        print(f"  {'CODE' if not f.startswith('docs/') else 'docs'}  {f}")
    if code:
        print("\nBLOCKER: code advanced past the handoff. Re-read git log before trusting it.")
        return 1
    print("\nADVISORY: docs-only drift. The described state still holds.")
    return 0


def emit():
    fm, text = frontmatter()
    problems = []
    for k in REQUIRED:
        if not fm.get(k):
            problems.append(f"missing frontmatter field: {k}")
    if fm.get("gate_passed", "").lower() != "true":
        problems.append("gate_passed is not true -- walk HANDOFF-GATE.md first")
    head = sh("git", "rev-parse", "HEAD")
    recorded = fm.get("gh_sha", "")
    if recorded != head:
        # Stamping necessarily moves HEAD, so gh_sha trails by exactly the stamp commit.
        # Tolerate that and only that: the sole file changed since gh_sha must be this file.
        drifted = [f for f in files_changed_since(recorded) if f != "docs/HANDOFF.md"]
        if drifted or not recorded:
            problems.append(
                f"gh_sha {recorded} != HEAD {head}; content changed since stamp: {drifted}")
    if sh("git", "status", "--porcelain"):
        problems.append("working tree is dirty -- commit before emitting")
    body = text.split("---", 2)[-1]
    for placeholder in ("TODO", "TBD", "FIXME", "<fill", "XXX"):
        if placeholder in body:
            problems.append(f"placeholder {placeholder!r} left in the handoff body")
    if problems:
        print("HANDOFF REFUSED:")
        for p in problems:
            print(f"  - {p}")
        return 1
    print("HANDOFF OK: frontmatter complete, sha matches HEAD, tree clean, no placeholders.")
    return 0


def stamp():
    """Rewrite gh_sha to current HEAD. Run after the final content commit."""
    fm, text = frontmatter()
    head = sh("git", "rev-parse", "HEAD")
    new = re.sub(r"^gh_sha:.*$", f"gh_sha: {head}", text, count=1, flags=re.M)
    HANDOFF.write_text(new)
    print(f"stamped gh_sha: {head}")
    return 0


if __name__ == "__main__":
    arg = sys.argv[1] if len(sys.argv) > 1 else "--check"
    sys.exit({"--check": check, "--emit": emit, "--stamp": stamp}.get(arg, check)())
