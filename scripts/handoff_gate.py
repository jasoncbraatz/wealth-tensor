#!/usr/bin/env python3
"""Staleness guard for docs/HANDOFF.md.

The handoff lives in the repo so it can be version-controlled and turned over rather than
accreted. The cost of that choice is that a stale file looks authoritative in a way a stale
chat message does not. This script is the price of admission -- HANDOFF-GATE.md §G-F is
explicit that the file half must not be adopted without it.

  --check   run at ORIENT. Compares the handoff's recorded gh_sha against HEAD and
            distinguishes code drift (blocker) from docs-only drift (advisory).
  --stamp   rewrite gh_sha to HEAD. Run AFTER the final content commit.
  --emit    run at WRAP. Refuses to bless the handoff on missing fields, TODO
            placeholders, a dirty tree, gh_sha != HEAD, or gate_passed: false.

Correct wrap sequence -- --emit does NOT stamp, and running it on an unstamped file was
a silent-green failure until 2026-08-05 (see below):

    git commit ...                      # the last content commit
    python3 scripts/handoff_gate.py --stamp
    git commit -am "docs: stamp handoff gh_sha to HEAD"
    python3 scripts/handoff_gate.py --emit

EXIT CODES ARE TRI-STATE. 0 = pass. 1 = BLOCKER. 2 = CANNOT VERIFY, which is NOT a pass.

Why 2 exists (bug found and fixed 2026-08-05, S2). `sh()` swallows git's stderr and returns
an empty string on failure, so `git diff --name-only <garbage>..HEAD` looked exactly like
"nothing changed". A handoff carrying `gh_sha: PENDING` therefore made --check print a cheery
advisory and return 0, and made --emit print "sha matches HEAD" and bless the file. The gate
built to catch stale handoffs was blind to the most obvious stale handoff there is. An
unverifiable claim must never be reported as a verified one.
"""
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
HANDOFF = ROOT / "docs" / "HANDOFF.md"
REQUIRED = ["project", "gh_sha", "updated", "session", "gate_passed", "gate_version"]


SHA_RE = re.compile(r"^[0-9a-f]{40}$")


def sh(*args):
    """stdout of a git command, or "" -- use `sh_ok` when a failure must be distinguishable."""
    return subprocess.run(args, cwd=ROOT, capture_output=True, text=True).stdout.strip()


def sh_ok(*args):
    """(stdout, ok). The `ok` flag is the whole point: an empty stdout from a FAILED command
    is not the same fact as an empty stdout from a successful one, and conflating them is
    what made this gate score a placeholder sha as a match."""
    r = subprocess.run(args, cwd=ROOT, capture_output=True, text=True)
    return r.stdout.strip(), r.returncode == 0


def classify_sha(recorded):
    """"placeholder" | "absent" | "present". Three answers, because they need three responses.

    placeholder -- not 40 hex chars at all (PENDING, TODO, an empty string). Unambiguously
                   wrong, and a blocker wherever it is found.
    absent      -- well-formed but not an object in this clone. Could be a shallow clone or a
                   sha from another repo; either way the comparison CANNOT be made. Not a pass.
    present     -- a real commit here; proceed with the normal comparison.
    """
    if not SHA_RE.match(recorded or ""):
        return "placeholder"
    _, ok = sh_ok("git", "cat-file", "-e", f"{recorded}^{{commit}}")
    return "present" if ok else "absent"


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
    kind = classify_sha(recorded)
    if kind == "placeholder":
        print(f"\nBLOCKER: gh_sha {recorded!r} is not a commit sha. The handoff was never\n"
              "         stamped, so nothing about it can be trusted as current. Whoever wrote\n"
              "         it skipped `--stamp`; re-read git log rather than believing the file.")
        return 1
    if kind == "absent":
        print(f"\nCANNOT VERIFY (exit 2): gh_sha {recorded} is well-formed but is not an object\n"
              "         in this clone -- a shallow clone, or a sha from somewhere else. This is\n"
              "         NOT a pass. Run `git fetch --unshallow` and try again.")
        return 2
    changed = files_changed_since(recorded)
    if not changed:
        print("ADVISORY: the recorded commit is an ancestor with no diff to HEAD.")
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
        kind = classify_sha(recorded)
        if kind == "placeholder":
            problems.append(
                f"gh_sha is {recorded!r}, not a commit sha -- run --stamp, commit, then --emit")
        elif kind == "absent":
            problems.append(
                f"gh_sha {recorded} is not an object in this clone; the comparison cannot be "
                "made and an unverifiable handoff must not be blessed")
        else:
            # Stamping necessarily moves HEAD, so gh_sha trails by exactly the stamp commit.
            # Tolerate that and only that: the sole file changed since gh_sha must be this file.
            drifted = [f for f in files_changed_since(recorded) if f != "docs/HANDOFF.md"]
            if drifted:
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
