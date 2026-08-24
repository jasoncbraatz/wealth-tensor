import pathlib, shutil
REPO = pathlib.Path(".")
WT093 = REPO / "scripts/wt093_edits_scope001.py"
TEST  = REPO / "tests/test_scope001_steelman.py"
done = []

s = WT093.read_text(encoding="utf-8")
old = "of §10's restriction rather than inside its complement:** a charge is the moment degradation"
new = "of §2's domain restriction rather than inside its complement:** a charge is the moment degradation"
if old in s:
    bak = WT093.with_suffix(WT093.suffix + ".bak-wt202")
    if not bak.exists(): shutil.copy2(WT093, bak)
    s = s.replace(old, new, 1)
    s = s.replace("§5.1 · the sample is the boundary of §10's restriction",
                  "§5.1 · the sample is the boundary of §2's domain restriction")
    WT093.write_text(s, encoding="utf-8"); done.append("wt093 NEW text")

# A LINE WRAP IS NOT A FACT ABOUT THE PAPER -- flatten the post-state assertions.
u = TEST.read_text(encoding="utf-8")
if "_flat(" not in u:
    bak = TEST.with_suffix(TEST.suffix + ".bak-wt202")
    if not bak.exists(): shutil.copy2(TEST, bak)
    helper = '''

def _flat(s: str) -> str:
    """Whitespace-normalised. These assertions read POST-repair prose only, so flattening
    cannot make a before look like an after -- the failure mode wealthTensor-104 hit in
    wt182. Added at -105, where "\\u00a72's domain restriction" fell across a line break and a
    landed repair read as absent."""
    return " ".join(s.split())
'''
    anchor = '\ndef test_the_steelman_is_in_the_manuscript_exactly_once(paper):'
    assert u.count(anchor) == 1
    u = u.replace(anchor, helper + anchor, 1)
    for a, b in [
        ('assert "no observable event to key recognition" in two,',
         'assert "no observable event to key recognition" in _flat(two),'),
        ('assert "recognition is faster than the market and this model predicts nothing" in two',
         'assert "recognition is faster than the market and this model predicts nothing" in _flat(two)'),
        ('assert "§2\'s domain restriction" in ten,',
         'assert "§2\'s domain restriction" in _flat(ten),'),
    ]:
        assert u.count(a) == 1, a
        u = u.replace(a, b, 1)
    TEST.write_text(u, encoding="utf-8"); done.append("test whitespace-insensitive")

print("  applied:", ", ".join(done) if done else "nothing (idempotent no-op)")
