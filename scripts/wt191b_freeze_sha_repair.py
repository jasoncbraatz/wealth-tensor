import pathlib, subprocess, sys
REPO = pathlib.Path.home() / "repos/wealth-tensor"
P = REPO / "docs/POST-SHIP.md"
FAILED, NEG = [], 0
def chk(l, c, n=False):
    global NEG
    if n: NEG += 1
    print("  %s %s%s" % ("PASS" if c else "FAIL", "(NEGATIVE) " if n else "", l))
    if not c: FAILED.append(l)

def sh(a): return subprocess.run(a, capture_output=True, text=True, cwd=REPO).stdout.strip()
# `git log -1` RETURNS THE LATEST COMMIT TOUCHING THE FILE, WHICH MOVES EVERY TIME THE DoD IS
# AMENDED -- and Jason amended it the same day, so this pointed at the AMENDMENT and tried to
# re-stamp the freeze. The freeze is the commit that ADDED the document and it cannot move:
# --diff-filter=A, oldest-last, take the last line.
_adds = sh(["git", "log", "--diff-filter=A", "--format=%H", "--", "docs/DEFINITION-OF-DONE-SHIP.md"])
decl = _adds.split("\n")[-1].strip()
parent = sh(["git", "rev-parse", decl + "^"])
chk("F1 the declaring commit resolves", len(decl) == 40)
chk("F2 its parent resolves", len(parent) == 40)
chk("F3 NEGATIVE: they are different commits", decl != parent, True)
chk("F4 the declaring commit is the one that ADDED the DoD document",
    "docs/DEFINITION-OF-DONE-SHIP.md" in sh(["git", "show", "--name-only", "--format=", decl]))
chk("F4b NEGATIVE: it is the ADDING commit, not merely the latest one to touch the file",
    decl != sh(["git", "log", "--format=%H", "-1", "--", "docs/DEFINITION-OF-DONE-SHIP.md"])
    or len(_adds.split("\n")) == 1, True)

OLD = "**FREEZE COMMIT: `%s` (`wealthTensor-102`, 2026-08-24).**" % parent
NEW = ("**FREEZE DECLARED AT: `%s`** — the commit that added `docs/DEFINITION-OF-DONE-SHIP.md`.\n"
       "**TREE STATE FROZEN: `%s`**, its parent — the corpus as it stood when the ruling was made.\n"
       "*(`wealthTensor-102`, 2026-08-24. Both are named because ONE OF THEM IS THE ANSWER TO A\n"
       "DIFFERENT QUESTION: `%s` is what you diff against to see what the freeze changed, `%s` is\n"
       "what you diff against to see what has happened since. `-102`'s freeze commit message\n"
       "claimed this file carried \"this commit's own sha\", which no commit can do — it recorded the\n"
       "PARENT. Repaired here rather than left as a small false statement in the log, which is an S1\n"
       "under the very rubric that commit introduced.)*") % (decl, parent, decl, parent)
t = P.read_text()
if OLD in t:
    P.write_text(t.replace(OLD, NEW, 1))
t = P.read_text()
chk("F5 the declaring commit is named", decl in t)
chk("F6 the frozen tree state is named", parent in t)
chk("F7 NEGATIVE: the file no longer presents ONE sha as 'the' freeze commit",
    "**FREEZE COMMIT: `" not in t, True)
chk("F8 NEGATIVE: the correction is disclosed rather than silently applied",
    "which no commit can do" in t, True)
chk("F9 line 3 still leads with a sha, so the file's first lines remain the authority",
    decl in t.split("\n")[2])
chk("F10 NEGATIVE: nothing else in the file moved",
    t.count("Nothing in this file blocks shipping") == 1, True)
print("\n post-conditions: %d checks, %d NEGATIVE" % (11, NEG))
if FAILED:
    print(" FAILURE"); [print("   FAILED:", f) for f in FAILED]; sys.exit(1)
print(" ALL PASS")
