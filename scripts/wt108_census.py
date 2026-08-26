import pathlib, sys, subprocess, json
P = pathlib.Path("tests/test_defensive_count.py")
s = P.read_text(encoding="utf-8")

old_map = '''MANUSCRIPTS = {
    "paper-I": PAPERS / "paper-I-price-formation" / "paper-I.md",
    "paper-II": PAPERS / "paper-II-redistribution" / "paper-II.md",
    "paper-III": PAPERS / "paper-III-dual-tensor" / "paper-III.md",
    "paper-IV": PAPERS / "paper-IV-composition" / "paper-IV.md",
}'''
new_map = '''MANUSCRIPTS = {
    "paper-I": PAPERS / "paper-I-price-formation" / "paper-I.md",
    "paper-II": PAPERS / "paper-II-redistribution" / "paper-II.md",
    "paper-II-v1": PAPERS / "paper-II-redistribution" / "paper-II-v1.md",
    "paper-III": PAPERS / "paper-III-dual-tensor" / "paper-III.md",
    "paper-III-v1": PAPERS / "paper-III-dual-tensor" / "paper-III-v1.md",
    "paper-IV": PAPERS / "paper-IV-composition" / "paper-IV.md",
}'''

old_base = '''def _baseline(md: Path) -> Path:
    return md.parent / "DEFENSIVE-BASELINE.json"'''
new_base = '''def _baseline(md: Path) -> Path:
    """One baseline per MANUSCRIPT, not per directory.

    `-108`: the v1 rebuild put a second manuscript in `paper-II-redistribution/` and in
    `paper-III-dual-tensor/`, and a directory-keyed baseline silently makes two papers share
    one committed count -- so a hedge added to the rebuild would have been measured against
    the v0.x draft's baseline and passed. The per-stem name is the fix; the legacy
    directory-keyed name is still honoured for the four manuscripts that already carry it,
    because renaming a committed baseline would reset the very history it exists to hold.
    """
    per_stem = md.parent / ("DEFENSIVE-BASELINE-%s.json" % md.stem)
    if per_stem.exists():
        return per_stem
    legacy = md.parent / "DEFENSIVE-BASELINE.json"
    if legacy.exists() and md.stem in ("paper-I", "paper-II", "paper-III", "paper-IV"):
        return legacy
    return per_stem'''

for old, new, label in ((old_map, new_map, "MANUSCRIPTS"), (old_base, new_base, "_baseline")):
    if s.count(old) != 1:
        sys.exit("ABORT %s: anchor count %d" % (label, s.count(old)))
    s = s.replace(old, new, 1)
    print("  ok", label)

s = s.replace(
 '# Every manuscript in the estate. A paper added here without a baseline fails\n'
 '# `test_the_baseline_exists_and_describes_this_manuscript` rather than being skipped.',
 '# Every manuscript in the estate. A paper added here without a baseline fails\n'
 '# `test_the_baseline_exists_and_describes_this_manuscript` rather than being skipped.\n'
 '# The `-v1` entries are the paper-rebuild drafts; each carries its OWN per-stem baseline,\n'
 '# because two manuscripts now share a directory (see _baseline).', 1)

P.write_text(s, encoding="utf-8")
print("patched", P)

for stem, d in (("paper-II-v1", "paper-II-redistribution"),
                ("paper-III-v1", "paper-III-dual-tensor")):
    md = "docs/papers/%s/%s.md" % (d, stem)
    out = "docs/papers/%s/DEFENSIVE-BASELINE-%s.json" % (d, stem)
    r = subprocess.run([sys.executable, "scripts/defensive_count.py", md, "--json", out],
                       capture_output=True, text=True)
    print(" ", stem, "rc=%d" % r.returncode, (r.stdout or r.stderr).strip()[:200])
    if r.returncode == 0:
        b = json.loads(pathlib.Path(out).read_text())
        print("    totals:", b["totals"], "sections:", len(b["sections"]))
