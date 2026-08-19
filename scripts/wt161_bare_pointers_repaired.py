#!/usr/bin/env python3
"""wt161 — repair the ten bare pointers wt160 flagged, and prove the instrument did not move.

RED-PROOF, in two directions:
  * This script REFUSES to change anything unless `wt160`'s flag set on the working tree is
    EXACTLY the ten pointers it is written to repair. A drifted flag set means the repair
    set and the criterion have come apart, and the right answer is to stop, not to patch.
  * After the repair it re-runs `wt160` at the PRE-REPAIR revision and requires all ten to
    flag there still. The repair must move the FILE, not the instrument.

One of the ten is not merely vague. Paper III §7's ledger row *"The repair's strength is the
asset's, not the analyst's"* said the σ exponents *"are given in the two rows above"*. The two
rows above it are *"Returns cannot touch the scale continuum"* and *"News, not returns,
restores identification"*, and neither carries an exponent in σ. The σ exponents are two rows
BELOW, and §4.7 states both ranges in prose. The pointer resolved to the wrong place — the
III-2 class exactly, found this time by machine rather than by a reader.

EXIT CODES: 0 = repaired and every post-condition holds · 2 = refused, or a post-condition failed.
"""
from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
P3 = "docs/papers/paper-III-dual-tensor/paper-III.md"
P4 = "docs/papers/paper-IV-composition/paper-IV.md"
TAG = "wt161"

PRE_REPAIR_REV = "07cd47e"      # the commit that carries the PREDICTED count and PENDING measured

# (file, anchor, replacement, why)
REPAIRS = [
    (P3,
     "in the repository named in the data-availability statement.",
     "in the repository named in §11.",
     "front matter: name the section instead of the statement"),
    (P3,
     "which §4.4 now states in the table where it belongs.",
     "which §4.4's tier table now states.",
     "§4.5: the pointer named no table; §4.4 has exactly one"),
    (P3,
     "the σ exponents are not, and are given in the two rows above",
     "the σ exponents are not, and §4.7 gives both ranges",
     "§7 ledger: the two rows above carry NO σ exponent — they are two rows BELOW, "
     "and §4.7 states both ranges in prose. The pointer resolved to the wrong place."),
    (P3,
     "The section is placed in the body, not an\n"
     "appendix, for the reason given in the companion papers of this programme.*",
     "The section is placed in the body, not an\n"
     "appendix, and for the reason Papers I, II and IV each state at the head of theirs: a\n"
     "result reported without the routes that failed is a result the reader cannot calibrate —\n"
     "they are shown the one path that worked and left to assume it was the only one\n"
     "considered.*",
     "§8: the reason is stated here rather than promised elsewhere"),
    (P3,
     "result named in its\nown title.",
     "result its title carries verbatim — *the asymmetric\ntimeliness of earnings*.",
     "Basu (1997): quote the title's phrase instead of pointing at the title"),
    (P3,
     "decomposition named in its own title.",
     "decomposition its title carries verbatim — *biases and lags in book value*.",
     "Beaver & Ryan (2000): same"),
    (P3,
     "Characterised from the result named in the title;",
     "Characterised from the result its title carries — *L = λW*;",
     "Little (1961): same"),
    (P4,
     "in the repository named in the data-availability statement.",
     "in the repository named in §10.",
     "front matter: name the section instead of the statement"),
    (P4,
     "seed works named in the registration,",
     "seed works named in `REG-013`,",
     "§6: name the registration §6 already names two paragraphs earlier"),
    (P4,
     "stated in the registration before the numbers\nexisted:**",
     "stated in `REG-013` before the numbers\nexisted:**",
     "§6: same"),
]

# The exact flag set wt160 must report BEFORE this script is allowed to touch anything.
EXPECTED_FLAGS = sorted([
    (P3, "the data-availability statement"),
    (P3, "the table where it belongs"),
    (P3, "the two rows above"),
    (P3, "the companion papers of this programme"),
    (P3, "its own title"),
    (P3, "its own title"),
    (P3, "the title"),
    (P4, "the data-availability statement"),
    (P4, "the registration"),
    (P4, "the registration before the numbers existed"),
])


def sh(cmd, **kw):
    return subprocess.run(cmd, cwd=REPO, capture_output=True, text=True, **kw)


def wt160(rev=None):
    cmd = [sys.executable, "scripts/wt160_bare_pointer_sweep.py", "--json", "--skip-postconditions"]
    if rev:
        cmd += ["--rev", rev]
    r = sh(cmd)
    if r.returncode == 2:
        raise RuntimeError(f"wt160 broken: {r.stderr}")
    return json.loads(r.stdout), r.returncode


def flagset(payload):
    return sorted((f["file"], f["target"]) for pf in payload["per_file"] for f in pf["flags"])


def die(msg):
    print(f"{TAG}: REFUSED — {msg}", file=sys.stderr)
    return 2


def main():
    # ---- guard: the flag set must be exactly the repair set -------------------------
    before, rc_before = wt160()
    got = flagset(before)
    if got != EXPECTED_FLAGS:
        print("  expected:", file=sys.stderr)
        for e in EXPECTED_FLAGS:
            print(f"    {e}", file=sys.stderr)
        print("  got:", file=sys.stderr)
        for g in got:
            print(f"    {g}", file=sys.stderr)
        return die("wt160's flag set is not the set this repair was written against. "
                   "The criterion and the repair have come apart — stop, do not patch.")
    if rc_before != 1:
        return die(f"wt160 returned RC {rc_before} before the repair; expected 1.")
    print(f"{TAG}: guard passed — wt160 flags exactly the {len(got)} pointers this repair targets.")

    # ---- back up, then repair -------------------------------------------------------
    texts = {}
    for path in (P3, P4):
        full = os.path.join(REPO, path)
        shutil.copyfile(full, f"{full}.bak-{TAG}")
        texts[path] = open(full, encoding="utf-8").read()

    for path, anchor, repl, why in REPAIRS:
        n = texts[path].count(anchor)
        if n != 1:
            return die(f"anchor occurs {n}× (expected 1) in {path}: {anchor[:60]!r}")
        texts[path] = texts[path].replace(anchor, repl)
        print(f"  repaired {path}: {why}")

    for path in (P3, P4):
        with open(os.path.join(REPO, path), "w", encoding="utf-8") as fh:
            fh.write(texts[path])

    # ---- post-conditions ------------------------------------------------------------
    p3 = texts[P3]
    p4 = texts[P4]
    after, rc_after = wt160()

    try:
        at_pre, _ = wt160(PRE_REPAIR_REV)
        pre_ok = at_pre["flagged"] == 10
        pre_detail = f"{at_pre['flagged']} flag(s) at {PRE_REPAIR_REV}"
    except Exception as exc:                            # noqa: BLE001
        pre_ok, pre_detail = False, f"raised {exc!r}"

    def rc(script):
        return sh([sys.executable, f"scripts/{script}"]).returncode

    checks = [
        ("D1", "POSITIVE", "wt160 RC 0 on the working tree, 0 flagged of 13 still considered "
                            "(4 pointers re-targeted, 6 constructions removed outright)",
         rc_after == 0 and after["flagged"] == 0 and after["considered"] == 13,
         f"RC {rc_after}, {after['flagged']}/{after['considered']}"),
        ("D2", "POSITIVE", f"wt160 at {PRE_REPAIR_REV} still flags all ten — the FILE moved, not the instrument",
         pre_ok, pre_detail),
        ("D3", "POSITIVE", "§4.7 still states both σ-exponent ranges in prose (the new §7 target is true)",
         "−1.07 to −0.38" in p3 and "−0.78 to −0.09" in p3, "both ranges present"),
        ("D4", "POSITIVE", "paper-III §11 is Data and code availability",
         "## 11 · Data and code availability" in p3, "heading present"),
        ("D5", "POSITIVE", "paper-IV §10 is Data and code availability",
         "## 10 · Data and code availability" in p4, "heading present"),
        ("D6", "POSITIVE", "paper-IV §6 already names REG-013, so both §6 repairs point at a name in scope",
         "(`REG-013`, committed before the instrument" in p4, "REG-013 in §6"),
        ("D7", "NEGATIVE", "'the two rows above' is gone from paper-III",
         "the two rows above" not in p3, "absent"),
        ("D8", "NEGATIVE", "'in the data-availability statement' is gone from both",
         "in the data-availability statement" not in p3 and "in the data-availability statement" not in p4,
         "absent"),
        ("D9", "NEGATIVE", "'named in its own title' / 'named in the title' are gone",
         "named in its own title" not in p3 and "named in its\nown title" not in p3
         and "named in the title" not in p3, "absent"),
        ("D10", "NEGATIVE", "'the companion papers of this programme' is gone",
         "the companion papers of this programme" not in p3, "absent"),
        ("D11", "POSITIVE", "paper-III now carries the companions' own calibration sentence",
         "a result the reader cannot calibrate" in p3, "present"),
        ("D12", "POSITIVE", "wt133 RC 0 after the repair", rc("wt133_crossref_sweep.py") == 0, "cross-refs"),
        ("D13", "POSITIVE", "wt154 RC 0 after the repair (the TSV's evidence column is untouched)",
         rc("wt154_evidence_discrimination_sweep.py") == 0, "evidence discrimination"),
    ]

    ok_all = True
    print(f"\n=== {TAG} post-conditions ===")
    for cid, kind, desc, ok, detail in checks:
        ok_all &= bool(ok)
        print(f"  [{'ok  ' if ok else 'FAIL'}] {cid} {kind:8s} {desc} — {detail}")

    n_neg = sum(1 for c in checks if c[1] == "NEGATIVE")
    print(f"\n{len(checks)} post-conditions, {n_neg} NEGATIVE.")

    if not ok_all:
        print(f"{TAG}: POST-CONDITIONS FAILED — rolling back.", file=sys.stderr)
        for path in (P3, P4):
            full = os.path.join(REPO, path)
            shutil.copyfile(f"{full}.bak-{TAG}", full)
        return 2

    print(f"{TAG}: ten bare pointers repaired; wt160 RC 0.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
