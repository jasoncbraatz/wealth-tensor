#!/usr/bin/env python3
"""wt120_scale_census.py -- CENSUS BEFORE PATCH for Paper IV's scale framing.

Jason ruled on 2026-08-17 (wealthTensor-66b) to NARROW Paper IV's title and abstract
leading clause: "from the household to the sovereign" -> "at the household, firm and
sovereign scales". Type identity across three named scales, not a ladder running up
through them -- because END-TO-END-001 leg E1 rejected the chain relation, and the
"from X to Y" phrasing keeps promising it.

WT-099: when anybody prices work as "N places", treat the number as a HYPOTHESIS and
the FILE LIST as the real claim. Write the census as a script BEFORE the patch -- it is
re-runnable afterwards as verification, and it is the only thing that separates "two
sites" from "two sites somebody could see from where they were standing".

WT-094: grep tests/ AND scripts/ for any manuscript string BEFORE editing it. A repair
that starves an instrument is worse than the defect.

THE SPECIFIC HAZARD THIS CENSUS EXISTS TO FIND, named in advance so a zero is a
measurement and not a shrug: PIN-001's SHA guard (tests/test_pin001_code_state.py) was
widened by -65 to glob("docs/papers/*/paper-*.md") with a floor of four asserted on the
glob. IF THAT REGISTRY PINS A CONTENT SHA FOR paper-IV.md, editing the manuscript turns
the suite red and the remedy is a registry update, NOT a revert. Find out before
editing, not after.

USAGE
    python3 scripts/wt120_scale_census.py [--json /tmp/wt120.json]
"""

import argparse
import json
import os
import re
import subprocess
import sys

# (label, regex, why it matters if it fires)
PATTERNS = [
    ("LADDER_PHRASE", r"from the household to the sovereign",
     "The exact phrase being narrowed. Every occurrence is a candidate edit site."),
    ("LADDER_LOOSE", r"household[^.\n]{0,40}\bto the sovereign",
     "Line-wrapped or reworded variants of the same ladder framing. The line-wrap grep "
     "trap (-62) runs both ways: normalise before asserting presence OR absence."),
    ("DRAFT_NARRATION", r"sooner than an earlier draft claimed|than an earlier draft",
     "The conduct-narration clause the narrowing lets us DELETE rather than defend "
     "(WT-098: the demotion is achieved by deleting the assertion)."),
    ("CHAIN_WORD", r"\bchain rather than\b|\ba chain\b",
     "The relation E1 rejected. Should survive ONLY where the paper reports the "
     "rejection -- flag any place it is still asserted."),
    ("PAPER_IV_TITLE", r"The tensor composes, the behaviour does not",
     "The title as a string. Anywhere it is quoted must move with the title."),
    ("PAPER_IV_SHA_PIN", r"paper-IV\.md['\"]?\s*[:=]\s*['\"][0-9a-f]{7,40}",
     "A CONTENT SHA PINNED AGAINST PAPER IV. If this fires, editing the manuscript "
     "turns the suite red and the registry must be updated in the same commit."),
    ("PAPER_IV_REF", r"paper-IV",
     "Any reference to the file at all -- the widest net, reported as a count so the "
     "narrower patterns can be judged against it."),
]

# Directories the census must cross. Named explicitly: a census that silently skips a
# tree is the thing it exists to prevent.
ROOTS = ["docs", "tests", "scripts", "src"]
SKIP_EXT = {".pyc", ".png", ".jpg", ".pdf", ".gz", ".zip", ".json"}


def is_backup(path):
    return bool(re.search(r"\.bak-|\.wt\d+\w*-dryrun$|\.orig$", path))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--json")
    a = ap.parse_args()

    files = []
    for root in ROOTS:
        if not os.path.isdir(root):
            print("WARNING: root %r does not exist -- census coverage is incomplete" % root)
            continue
        for dirpath, dirnames, filenames in os.walk(root):
            dirnames[:] = [d for d in dirnames if not d.startswith((".", "__"))]
            for fn in filenames:
                p = os.path.join(dirpath, fn)
                if os.path.splitext(fn)[1].lower() in SKIP_EXT:
                    continue
                files.append(p)

    live = [f for f in files if not is_backup(f)]
    backups = [f for f in files if is_backup(f)]

    results = {label: [] for label, _, _ in PATTERNS}
    for path in live:
        try:
            text = open(path, errors="ignore").read()
        except Exception:                                       # noqa: BLE001
            continue
        # NORMALISE before matching: these manuscripts are hard-wrapped, so a phrase
        # can straddle a newline and a naive grep reports a correct-looking zero.
        flat = re.sub(r"\s+", " ", text)
        for label, rx, _why in PATTERNS:
            for m in re.finditer(rx, flat, re.I):
                lo = max(0, m.start() - 90)
                results[label].append({
                    "file": path,
                    "match": m.group(0)[:120],
                    "context": flat[lo:m.end() + 130],
                })

    print("census scope: %d live files across %s (+%d backups EXCLUDED)"
          % (len(live), ", ".join(ROOTS), len(backups)))
    print()
    payload = {"scope": {"roots": ROOTS, "live_files": len(live),
                         "backups_excluded": len(backups)}, "findings": {}}
    for label, rx, why in PATTERNS:
        hits = results[label]
        by_file = {}
        for h in hits:
            by_file.setdefault(h["file"], 0)
            by_file[h["file"]] += 1
        payload["findings"][label] = {"why": why, "total": len(hits), "by_file": by_file,
                                      "hits": hits[:12]}
        print("== %-18s %d hit(s) in %d file(s)" % (label, len(hits), len(by_file)))
        for f, n in sorted(by_file.items()):
            print("     %-62s x%d" % (f, n))
        if label in ("LADDER_PHRASE", "LADDER_LOOSE", "DRAFT_NARRATION",
                     "PAPER_IV_SHA_PIN") and hits:
            for h in hits[:6]:
                print("       ...%s" % h["context"][:190].strip())
        print()

    # The named hazard gets an explicit verdict rather than being left to the reader.
    pin = payload["findings"]["PAPER_IV_SHA_PIN"]["total"]
    print("-" * 78)
    print("HAZARD VERDICT -- content SHA pinned against paper-IV.md: %s"
          % ("NONE FOUND (%d). Editing the manuscript should not, on this evidence, "
             "turn the SHA guard red -- but RUN THE SUITE, WT-095 stands: the gate "
             "does not run a test suite." % pin if pin == 0 else
             "%d FOUND -- update the registry in the SAME commit as the edit." % pin))
    print("-" * 78)

    if a.json:
        json.dump(payload, open(a.json, "w"), indent=1)
        print("wrote %s" % a.json)
    return 0


if __name__ == "__main__":
    sys.exit(main())
