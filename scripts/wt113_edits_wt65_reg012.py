#!/usr/bin/env python3
"""wealthTensor-65 · the `REG-012` §4.7 freeze repair, applied as one batched patch.

Every anchor is asserted unique BEFORE any file is written, every touched file gets a
`.bak-wt65-reg012`, and `--dry` writes `*.wt65-dryrun` siblings instead so the diff can be
read in the cloud container before anything lands on darwin (`-64`'s convention, which
caught four ragged rewraps).

WHAT IT DOES
------------
1. `scripts/mutation_control.py` — two new git-axis probes for machinery that did not exist
   until this session: laundering reading (a) into the amendment ledger, and re-pinning the
   registration-era anchor. `G13` already probes the freeze itself and stays as it is.
2. `docs/preregistration/CONSTRAINT-INVENTORY-001.md` — two prose sites that assert §4.7 has
   never moved and that the red message's remedy is a re-pin. Both went stale at `6314302`
   and neither is derived, so neither could go red.

The guard file itself is replaced wholesale rather than patched, because the change is
structural; it is staged separately and dry-run under the real suite first.
"""
from __future__ import annotations

import pathlib
import shutil
import sys

DRY = "--dry" in sys.argv
ROOT = pathlib.Path(__file__).resolve().parents[1]

MC = "scripts/mutation_control.py"
INV = "docs/preregistration/CONSTRAINT-INVENTORY-001.md"

PROBE_FNS = '''

def _launder_reading_a(root: Path):
    """G14 - edit §4.7 AND record an amendment whose licence is REG-012's own outcome.

    `-65` replaced the single `SEC_47_SHA256` with a registration anchor, a current digest
    and an `AMENDMENTS` ledger, because the old file's prescribed remedy - re-pin in the same
    commit - was forbidden by its own sibling test and could be executed zero times. A ledger
    that records warranted edits opens a door the freeze did not have: write the violation
    down and it becomes a record instead of a violation. This probe walks through that door.
    `G13` cannot express it, because `G13` predates the ledger.
    """
    _edit_sec_47_today(root)
    p = root / GUARD
    text = p.read_text()
    old = "AMENDMENTS: tuple[Amendment, ...] = ("
    if old not in text:
        raise SystemExit("PROBE SITE MISSING: no AMENDMENTS ledger in the REG-012 guard")
    entry = (
        "AMENDMENTS: tuple[Amendment, ...] = (\\n"
        "    Amendment(\\n"
        '        sha="HEAD",\\n'
        "        licence=(\\n"
        "            \\"REG-012's outcome licenses this edit, padded well past the length \\"\\n"
        '            "floor so that only the citation limb can possibly catch it."\\n'
        "        ),\\n"
        '        digest_after="' + "0" * 64 + '",\\n'
        "    ),\\n"
    )
    p.write_text(text.replace(old, entry, 1))


def _repin_the_registration_anchor(root: Path):
    """G15 - move `SEC_47_AT_REGISTRATION`, which the guard declares immutable.

    The forbidden move the OLD file's own red message invited: it told the next session to
    re-pin, and the only way to make a one-constant guard green after a legitimate edit was
    to point the freeze at today. That is a snapshot wearing a freeze's clothes - `-43`'s own
    words for it, in a file that then made it the prescribed remedy. The anchor is a fact
    about `ba59370`; this probe asserts a session cannot quietly make it a fact about now.
    """
    p = root / GUARD
    text = p.read_text()
    anchor = 'SEC_47_AT_REGISTRATION = "'
    if anchor not in text:
        raise SystemExit("PROBE SITE MISSING: no SEC_47_AT_REGISTRATION in the REG-012 guard")
    head, _, rest = text.partition(anchor)
    _old, _, tail = rest.partition('"')
    p.write_text(head + anchor + "0" * 64 + '"' + tail)
'''

PROBE_ROWS = '''    ("G14", "record REG-012's own outcome as an amendment licence, laundering "
            "reading (a) into the ledger [git]",
     _launder_reading_a, {"git": True}),
    ("G15", "re-pin SEC_47_AT_REGISTRATION, the constant the guard calls immutable [git]",
     _repin_the_registration_anchor, {"git": True}),
'''

EDITS = [
    # ---------------------------------------------------------------- mutation_control.py
    (MC, "GUARD path constant",
     'MS = "docs/papers/paper-III-dual-tensor/paper-III.md"\n',
     'MS = "docs/papers/paper-III-dual-tensor/paper-III.md"\n'
     'GUARD = "tests/test_reg012_sec6_sec47_frozen.py"\n'),

    (MC, "G14/G15 probe functions",
     '\n\n# --------------------------------------------------------------------------- THE GIT AXIS',
     PROBE_FNS + '\n\n# --------------------------------------------------------------------------- THE GIT AXIS'),

    (MC, "G14/G15 probe rows",
     '     _edit_sec_47_today, {"git": True}),\n]',
     '     _edit_sec_47_today, {"git": True}),\n' + PROBE_ROWS + ']'),

    # ------------------------------------------------------- CONSTRAINT-INVENTORY-001.md
    (INV, "C48 row compliance cell",
     "§4.7 is unchanged since `REG-012` — **compliant**, and now pinned at `ba59370`",
     "§4.7 moved once since `REG-012` — at `6314302`, licensed by `ASC 350-30-35-15` and "
     "recorded — **compliant**; the `ba59370` anchor is immutable",),

    (INV, "C48 mechanised note",
     "`tests/test_reg012_sec6_sec47_frozen.py`, pinned at `ba59370`, the commit that registered\n"
     "   `REG-012`. **The pin records which version it froze**, and a git test reads §4.7 out of that\n"
     "   commit and requires it to hash to the pin — otherwise the freeze silently re-anchors to\n"
     "   whenever somebody last ran the file, which is a snapshot wearing a freeze's clothes. The red\n"
     "   message states both readings (REG-012's outcome → revert; anything else → re-pin in the same\n"
     "   commit and name the licence), because a guard that cannot tell them apart teaches the next\n"
     "   session to re-pin without reading.",

     "`tests/test_reg012_sec6_sec47_frozen.py`, anchored at `ba59370`, the commit that registered\n"
     "   `REG-012`. **The anchor records which version it froze**, and a git test reads §4.7 out of\n"
     "   that commit and requires it to hash to the anchor — otherwise the freeze silently re-anchors\n"
     "   to whenever somebody last ran the file, which is a snapshot wearing a freeze's clothes.\n"
     "   **`-43` wrote that anchor and the working-tree freeze as ONE constant, and the red message\n"
     "   told the next session to re-pin it — an instruction this same file forbids**, since the git\n"
     "   test nails the constant to `ba59370` and no single value can also equal an edited §4.7. The\n"
     "   remedy could be executed zero times, so the first warranted edit (`6314302`, `ASC\n"
     "   350-30-35-15`) wedged the guard red and it stayed red for four days under a gate that\n"
     "   reports `PASS` without running a suite. `-65` split it: `SEC_47_AT_REGISTRATION` is\n"
     "   immutable, `SEC_47_CURRENT` follows an `AMENDMENTS` ledger, and each amendment is checked\n"
     "   against git for having moved §4.7 to the digest it claims — a warrant is checkable or it is\n"
     "   decoration. Probes `G14` and `G15` fire the two doors the ledger opens. `WT-096`.",),
]


def main() -> int:
    src = {}
    for rel, label, old, new in EDITS:
        p = ROOT / rel
        if rel not in src:
            src[rel] = p.read_text(encoding="utf-8")
        n = src[rel].count(old)
        if n != 1:
            print(f"ABORT · anchor not unique ({n}x) · {rel} · {label}")
            return 1
        src[rel] = src[rel].replace(old, new, 1)
        print(f"ok  {rel:52s}  {label}")

    for rel, text in src.items():
        p = ROOT / rel
        if DRY:
            out = p.with_suffix(p.suffix + ".wt65-dryrun")
            out.write_text(text, encoding="utf-8")
            print(f"DRY  wrote {out}")
        else:
            shutil.copy2(p, p.with_suffix(p.suffix + ".bak-wt65-reg012"))
            p.write_text(text, encoding="utf-8")
            print(f"WROTE {rel}  (.bak-wt65-reg012 kept)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
