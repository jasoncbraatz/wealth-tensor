import pathlib, shutil
p = pathlib.Path("scripts/wt188_paperII_p7pass13.py")
bak = pathlib.Path("scripts/wt188_paperII_p7pass13.py.bak-wt105")
if not bak.exists():
    shutil.copy2(p, bak)
t = p.read_text(encoding="utf-8")
done = 0

# ---- E1 : the finding is that EVERY rule-1 flag on paper-II is a co-occurrence false
# positive. The literal 11 was the count on the day, and a global count is a loose proxy for
# that finding: any later pass that edits paper-II moves it without touching what was found.
# wealthTensor-105's Pass C C-d repairs moved it 11 -> 12 with every flag still co-occurrence.
old1 = 'chk("paper-II: RULE 1 flags 11", st2[\'num_flag\'] == 11)'
new1 = ('chk("paper-II: RULE 1 flags at least one figure to adjudicate", st2[\'num_flag\'] > 0)\n'
        'print("     RULE 1 flags on paper-II today: %d (11 when this pass measured it at -102)"\n'
        '      % st2[\'num_flag\'])')
if old1 in t:
    t = t.replace(old1, new1, 1); done += 1

old2 = ('chk("paper-II: all 11 flagged numbers live in SOME other section (co-occurrence, not error)",\n'
        '    elsewhere == 11)')
new2 = ('chk("paper-II: EVERY flagged number lives in SOME other section (co-occurrence, not error)",\n'
        '    elsewhere == st2[\'num_flag\'] and st2[\'num_flag\'] > 0)')
if old2 in t:
    t = t.replace(old2, new2, 1); done += 1

# ---- E8 : "across this repair" is a BEFORE/AFTER of THIS run, not a reading of whatever the
# working tree happens to hold. Reading `git status` made a check about wt188's own blast radius
# red whenever any later session legitimately edited a sibling manuscript -- which is what
# wealthTensor-105 did, editing all three under Pass C. The tighter subject is the digest pair
# this run took itself. A FALSE-POSITIVE REDUCTION under DoD 1.1: it looks at nothing new.
old3 = ('    rc, out, _ = sh("git status --porcelain docs/papers/paper-I-price-formation "\n'
        '                    "docs/papers/paper-III-dual-tensor docs/papers/paper-IV-composition")\n'
        '    chk("papers I, III and IV are byte-identical across this repair", out.strip() == "",\n'
        '        negative=True)')
new3 = ('    after = _sibling_digests()\n'
        '    moved = sorted(k for k in after if after[k] != SIBLINGS_BEFORE.get(k))\n'
        '    chk("papers I, III and IV are byte-identical across this repair", not moved,\n'
        '        negative=True)\n'
        '    if moved:\n'
        '        print("     moved by THIS run: %s" % ", ".join(moved))')
if old3 in t:
    t = t.replace(old3, new3, 1); done += 1

# ---- the digest helper + the BEFORE snapshot, taken before anything is written
helper = '''
def _sibling_digests():
    """Content digests of the three manuscripts this repair must not touch.

    Read BEFORE the repair runs and again after, so "across this repair" measures THIS run
    rather than the working tree's whole history. The `git status` form it replaces went red
    at wealthTensor-105 because a later pass had legitimately edited two of these files --
    a check pinned to a subject that moves for reasons unrelated to what it checks.
    """
    import hashlib
    out = {}
    for rel in ("docs/papers/paper-I-price-formation/paper-I.md",
                "docs/papers/paper-III-dual-tensor/paper-III.md",
                "docs/papers/paper-IV-composition/paper-IV.md"):
        f = REPO / rel
        out[rel] = hashlib.sha256(f.read_bytes()).hexdigest() if f.exists() else None
    return out


SIBLINGS_BEFORE = _sibling_digests()

'''
anchor = "def sh(cmd):"
if "_sibling_digests" not in t.split(anchor)[0]:
    assert t.count(anchor) == 1
    t = t.replace(anchor, helper.lstrip("\n") + "\n" + anchor, 1); done += 1

if done:
    p.write_text(t, encoding="utf-8")
print("  wt188: %d edit(s) applied" % done if done else "  wt188: already patched (idempotent no-op)")
