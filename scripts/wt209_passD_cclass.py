#!/usr/bin/env python3
"""wt209 — Pass D (wealthTensor-106) C-class repairs: apply the manifests.

Replace-only.  Every `old` must occur EXACTLY ONCE before the edit and ZERO times
after it, and every `new` must occur at least once after.  Writes a .bak beside each
manuscript before the first edit.  IDEMPOTENT BY DETECTION, NOT BY INSERTION: on a
second run every `old` is already gone and every `new` already present, and the script
reports ALREADY-APPLIED and exits 0 without writing.  Exit 2 if a site matches neither
state.  Run twice and diff the stdout.
"""
import importlib.util, pathlib, sys, shutil

HERE = pathlib.Path(__file__).resolve().parent

def load(mod, path):
    spec = importlib.util.spec_from_file_location(mod, str(HERE / path))
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m

blocks = load("wt209_blocks", "wt209_blocks.py")
LEGEND_NEW = load("wt209_manifest_IIIb", "wt209_manifest_IIIb.py")._LEGEND_NEW

JOBS = [
    ("paper-II",  "wt209_manifest_II.py",  None),
    ("paper-III", "wt209_manifest_III.py", None),
    ("paper-III", "wt209_manifest_IIIb.py", "blocks"),
    ("paper-IV",  "wt209_manifest_IV.py",  None),
]
PATHS = {
    "paper-II":  "docs/papers/paper-II-redistribution/paper-II.md",
    "paper-III": "docs/papers/paper-III-dual-tensor/paper-III.md",
    "paper-IV":  "docs/papers/paper-IV-composition/paper-IV.md",
}

def main(root):
    root = pathlib.Path(root)
    applied = already = 0
    failures = []
    texts = {}
    for k, rel in PATHS.items():
        texts[k] = (root / rel).read_text(encoding="utf-8")
    original = dict(texts)

    for paper, mf, extra in JOBS:
        edits = list(load(mf[:-3], mf).EDITS)
        if extra == "blocks":
            edits.append(("IIIb-LEGEND", "C-b", blocks.LEGEND_OLD, LEGEND_NEW))
            edits.append(("IIIb-TAIL",   "C-b", blocks.TAIL_OLD,   ""))
        for eid, ctype, old, new in edits:
            t = texts[paper]
            if t.count(old) == 1:
                texts[paper] = t.replace(old, new, 1)
                applied += 1
                print(f"APPLIED        {eid:14s} {ctype}  {paper}")
            elif t.count(old) == 0 and (new == "" or new in t):
                already += 1
                print(f"ALREADY-APPLIED {eid:14s} {ctype}  {paper}")
            else:
                failures.append((eid, paper, t.count(old)))
                print(f"!! NEITHER     {eid:14s} {ctype}  {paper}  count={t.count(old)}")

    if failures:
        print(f"\nFAIL: {len(failures)} site(s) matched neither state; NOTHING WRITTEN")
        return 2

    changed = [k for k in texts if texts[k] != original[k]]
    for k in changed:
        p = root / PATHS[k]
        shutil.copyfile(p, str(p) + ".bak-wt209-passD")
        # normalise a trailing run of blank lines to exactly one newline
        p.write_text(texts[k].rstrip("\n") + "\n", encoding="utf-8")
        print(f"WROTE {PATHS[k]}  (.bak-wt209-passD kept)")
    print(f"\napplied={applied} already={already} files_changed={len(changed)}")
    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else "."))
