import pathlib, shutil

REPO = pathlib.Path(".")
PAPER = REPO / "docs/papers/paper-III-dual-tensor/paper-III.md"
WT093 = REPO / "scripts/wt093_edits_scope001.py"
TEST  = REPO / "tests/test_scope001_steelman.py"

OLD_P = ("**Every event in this test is a recognised impairment, which places the sample on the boundary\n"
         "of §10's restriction rather than inside its complement:**")
NEW_P = ("**Every event in this test is a recognised impairment, which places the sample on the boundary\n"
         "of §2's domain restriction rather than inside its complement:**")

changed = []

t = PAPER.read_text(encoding="utf-8")
if OLD_P in t:
    bak = PAPER.with_suffix(PAPER.suffix + ".bak-wt202")
    if not bak.exists(): shutil.copy2(PAPER, bak)
    PAPER.write_text(t.replace(OLD_P, NEW_P, 1), encoding="utf-8"); changed.append("paper 5.1 pointer")
elif NEW_P not in t:
    raise SystemExit("PRECONDITION FAILED: neither the old nor the new 5.1 pointer is present")

s = WT093.read_text(encoding="utf-8")
if "of §10's restriction rather than inside its complement:**\\n\"" in s:
    bak = WT093.with_suffix(WT093.suffix + ".bak-wt202")
    if not bak.exists(): shutil.copy2(WT093, bak)
    s = s.replace("of §10's restriction rather than inside its complement:**\\n\"",
                  "of §2's domain restriction rather than inside its complement:**\\n\"", 1)
    s = s.replace('"§5.1 · the sample is the boundary of §10\'s restriction"',
                  '"§5.1 · the sample is the boundary of §2\'s domain restriction"')
    WT093.write_text(s, encoding="utf-8"); changed.append("wt093 NEW text")

OLD_T = '''def test_section_10s_restriction_is_untouched(paper):
    ten = _section(paper, "\\n## 10 · ", "\\n## 11 · ")
    assert "no observable event to key recognition" in ten
    assert "recognition is faster than the market and §2 predicts nothing" in ten, (
        "§10's restriction is the half of the pair the repair deliberately leaves alone. "
        "Weakening it would convert a steelman into the scope creep SCOPE-001 refused."
    )'''
NEW_T = '''def test_the_restriction_is_stated_with_the_model_and_is_unweakened(paper):
    """The restriction must SURVIVE, unweakened, and sit where the model is stated.

    It lived in §10 until wealthTensor-105, and this guard pinned it there because that is
    where it was. Pass C ruled the location a C-d fold -- §5.1 pointed at it across 740 lines,
    and it is a statement of §2's domain, not a concession to a rival literature -- and moved
    it into §2. THE SUBJECT OF THIS CHECK WAS NEVER THE SECTION NUMBER: it is that the
    restriction exists, is not softened, and is reachable from the sentence that leans on it.
    Pinning it to §10 made a legitimate move look like a deletion.
    """
    two = _section(paper, "\\n## 2 · ", "\\n## 3 · ")
    assert "no observable event to key recognition" in two, (
        "the SCOPE-001 restriction has left §2. It is the half of the pair the steelman leans "
        "on; weakening or deleting it converts a steelman into the scope creep SCOPE-001 refused."
    )
    assert "recognition is faster than the market and this model predicts nothing" in two
    ten = _section(paper, "\\n## 10 · ", "\\n## 11 · ")
    assert "§2's domain restriction" in ten, (
        "§10 must still NAME the restriction it credits to Basu, or the Basu paragraph is "
        "crediting an object the reader cannot find."
    )'''
u = TEST.read_text(encoding="utf-8")
if OLD_T in u:
    bak = TEST.with_suffix(TEST.suffix + ".bak-wt202")
    if not bak.exists(): shutil.copy2(TEST, bak)
    TEST.write_text(u.replace(OLD_T, NEW_T, 1), encoding="utf-8"); changed.append("test subject")

print("  applied:", ", ".join(changed) if changed else "nothing (idempotent no-op)")

# post-conditions
p = PAPER.read_text(encoding="utf-8")
print("  P1 5.1 points at section 2 :", NEW_P in p)
print("  P2 old section-10 pointer gone :", OLD_P not in p)
print("  P3 wt093 in sync with paper  :",
      "of §2's domain restriction rather than inside its complement:**\\n\"" in WT093.read_text(encoding="utf-8"))
print("  P4 test no longer pins section 10 :",
      "def test_section_10s_restriction_is_untouched" not in TEST.read_text(encoding="utf-8"))
