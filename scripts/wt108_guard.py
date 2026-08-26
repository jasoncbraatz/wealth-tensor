"""wealthTensor-108 — wt179 can now say "on disk, deliberately not in the capture".

THE DEFECT. `check_manuscripts` held the manifest to a DISK GLOB, while both the builder
(`docs/deliverable/build.sh`) and the emitter (`wt176_layout_manifest.py`) work from an
explicit PAPERS list. A manifest describes a BUILT PDF, so a manuscript written after the
capture cannot be in it — and on `paper-rebuild`, where the v1 drafts live beside the
manuscripts they replace, the guard fired a permanent false alarm ABOUT THE PDF. A guard
that is red for a reason nobody can fix is a guard people learn to ignore.

THE REPAIR keeps the glob's whole point. A NEW manuscript nobody has declared still turns
this red. What is added is a way to SAY SO, in a ledger, with a reason — and two new ways
to be wrong about the saying, both proven red.
"""
import pathlib, sys

P = pathlib.Path("scripts/wt179_manifest_guard.py")
s = P.read_text(encoding="utf-8")

def once(old, new, label):
    global s
    if s.count(old) != 1:
        sys.exit("ABORT %s: %d" % (label, s.count(old)))
    s = s.replace(old, new, 1)
    print("  ok", label)

once('    "MANUSCRIPT-MISSING-FROM-MANIFEST": "a manuscript on disk is not in the manifest",\n',
     '    "MANUSCRIPT-MISSING-FROM-MANIFEST": "a manuscript on disk is not in the manifest",\n'
     '    "MANUSCRIPT-DECLARED-BUT-CAPTURED": "NOT-IN-CAPTURE.tsv declares a manuscript the '
     'manifest lists anyway",\n'
     '    "CAPTURE-DECLARATION-STALE": "NOT-IN-CAPTURE.tsv declares a manuscript that is not '
     'on disk",\n',
     "TAGS")

OLD = '''def check_manuscripts(m, root, papers):
    """Exactly the manuscripts on disk -- both directions, so neither a deletion nor an
    addition can pass. A new paper turns this red until the capture is regenerated, which
    is the correct answer: the manifest describes a PDF that does not contain it."""
    out = []
    listed = m.get("manuscripts")
    if not isinstance(listed, dict):
        return out
    on_disk = {str(p.relative_to(root)) for p in sorted(Path(papers).glob("*/paper-*.md"))}
    for path in sorted(set(listed) - on_disk):
        out.append(_tag("MANUSCRIPT-NOT-ON-DISK",
                        "the manifest lists %s and it is not there" % path))
    for path in sorted(on_disk - set(listed)):
        out.append(_tag("MANUSCRIPT-MISSING-FROM-MANIFEST",
                        "%s is on disk and the manifest does not list it" % path))
    return out'''

NEW = '''def declared_out_of_capture(deliverable):
    """Manuscripts on disk that are deliberately NOT in the built capture.

    `-108`: the manifest describes a PDF, and a PDF cannot contain a manuscript written
    after it was built. Before this ledger the guard could only say "you forgot to rebuild",
    which is false of a draft branch and made the check permanently red there. A row is a
    CLAIM, and deleting one turns the guard red again -- which is how the file is audited
    rather than trusted. Declaring nothing is the old behaviour exactly.
    """
    out = {}
    path = Path(deliverable) / "NOT-IN-CAPTURE.tsv"
    if not path.exists():
        return out
    for line in path.read_text(encoding="utf-8").split("\\n"):
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        f = line.split("\\t")
        if len(f) >= 2 and f[0].strip() and f[1].strip():
            out[f[0].strip()] = f[1].strip()
    return out


def check_manuscripts(m, root, papers, deliverable=None):
    """Exactly the manuscripts the CAPTURE was built from -- both directions, so neither a
    deletion nor an addition can pass. A new paper turns this red until it is either
    captured or declared in NOT-IN-CAPTURE.tsv with a reason; silence is still red."""
    out = []
    listed = m.get("manuscripts")
    if not isinstance(listed, dict):
        return out
    on_disk = {str(p.relative_to(root)) for p in sorted(Path(papers).glob("*/paper-*.md"))}
    declared = declared_out_of_capture(deliverable if deliverable
                                       else Path(root) / "docs/deliverable")
    for path in sorted(set(declared) - on_disk):
        out.append(_tag("CAPTURE-DECLARATION-STALE",
                        "NOT-IN-CAPTURE.tsv declares %s and it is not on disk" % path))
    for path in sorted(set(declared) & set(listed)):
        out.append(_tag("MANUSCRIPT-DECLARED-BUT-CAPTURED",
                        "NOT-IN-CAPTURE.tsv declares %s is outside the capture and the "
                        "manifest lists it anyway" % path))
    for path in sorted(set(listed) - on_disk):
        out.append(_tag("MANUSCRIPT-NOT-ON-DISK",
                        "the manifest lists %s and it is not there" % path))
    for path in sorted(on_disk - set(listed) - set(declared)):
        out.append(_tag("MANUSCRIPT-MISSING-FROM-MANIFEST",
                        "%s is on disk, the manifest does not list it, and "
                        "NOT-IN-CAPTURE.tsv does not declare it" % path))
    return out'''

once(OLD, NEW, "check_manuscripts")
once('    ("manuscripts", lambda c: check_manuscripts(c["m"], c["root"], c["papers"])),',
     '    ("manuscripts", lambda c: check_manuscripts(c["m"], c["root"], c["papers"],\n'
     '                                                c["deliverable"])),',
     "CHECKS wiring")

P.write_text(s, encoding="utf-8")

# ---- the red-proof gains two probes -------------------------------------------------
R = pathlib.Path("scripts/redproof_wt179_manifest.py")
r = R.read_text(encoding="utf-8")
old_probe = '''    probe("a manuscript on disk the manifest forgot", "MANUSCRIPT-MISSING-FROM-MANIFEST",
          lambda m: m["manuscripts"].pop(sorted(m["manuscripts"])[0]))'''
new_probe = old_probe + '''

    # -108: the two ways to be wrong about NOT-IN-CAPTURE.tsv. Both drive the REAL reader
    # against a real temp tree, because a probe that mocks the reader proves the mock.
    _capture_declaration_probes()'''
if r.count(old_probe) != 1:
    sys.exit("ABORT redproof anchor: %d" % r.count(old_probe))
r = r.replace(old_probe, new_probe, 1)

helper = '''

def _capture_declaration_probes():
    """NOT-IN-CAPTURE.tsv, both of its failure modes, on a real tree."""
    import tempfile
    m = fresh()
    listed = sorted(m["manuscripts"])
    with tempfile.TemporaryDirectory() as td:
        deliv = Path(td) / "deliverable"
        deliv.mkdir()

        # (1) declaring a manuscript the manifest captured anyway
        (deliv / "NOT-IN-CAPTURE.tsv").write_text(
            "# probe\\n%s\\tdeclared out while the manifest still lists it\\n" % listed[0],
            encoding="utf-8")
        findings, _ = G.check_all(fresh(), deliverable=deliv)
        got = tags_of(findings)
        record("a manuscript declared out of the capture that the manifest lists anyway",
               "MANUSCRIPT-DECLARED-BUT-CAPTURED",
               "MANUSCRIPT-DECLARED-BUT-CAPTURED" in got
               and "MANUSCRIPT-DECLARED-BUT-CAPTURED" not in BASELINE_TAGS)

        # (2) a declaration for a file that is not on disk
        (deliv / "NOT-IN-CAPTURE.tsv").write_text(
            "# probe\\ndocs/papers/paper-IX-ghost/paper-IX.md\\tnever existed\\n",
            encoding="utf-8")
        findings, _ = G.check_all(fresh(), deliverable=deliv)
        got = tags_of(findings)
        record("a declaration for a manuscript that is not on disk",
               "CAPTURE-DECLARATION-STALE",
               "CAPTURE-DECLARATION-STALE" in got
               and "CAPTURE-DECLARATION-STALE" not in BASELINE_TAGS)

'''
anchor = "def record(name, tag, ok, note=\"\"):"
if r.count(anchor) != 1:
    sys.exit("ABORT record anchor")
r = r.replace(anchor, helper.lstrip("\n") + "\n" + anchor, 1)
R.write_text(r, encoding="utf-8")
print("  ok redproof probes")
