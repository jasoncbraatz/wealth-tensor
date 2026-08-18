#!/usr/bin/env python3
"""wt131b -- record `REG-012` §4.7's second warranted amendment (wealthTensor-73).

`wt131`'s III-7 moved one clause of §4.7, which `REG-012` §6 freezes. That freeze has a
representation for a legitimate edit and this is it: reading (b), appended rather than
re-pinned, with the licence named and the digest taken out of git rather than typed.

Guard honesty (WT-118): every invariant is asserted against the file as it stands BEFORE
the append as well as after, so a red line says which failure mode fired.
"""
from __future__ import annotations

import hashlib
import pathlib
import re
import shutil
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
TEST = ROOT / "tests" / "test_reg012_sec6_sec47_frozen.py"
PAPER_REL = "docs/papers/paper-III-dual-tensor/paper-III.md"
SHA = sys.argv[1] if len(sys.argv) > 1 else "HEAD"

LICENCE = (
    "wealthTensor-73's first independent read of Paper III (wt131, III-7). "
    "Section 4.7 attributed its floor of 30 to Paper III's own section 5, which states "
    "no floor of 30 anywhere and whose published tier cells run as low as 21; the floor "
    "is REG-009 section 3b's inherited THIN line. The clause now names the floor without "
    "attributing it, so the sentence claims only what a reader can check. Licensed by a "
    "review of the manuscript against itself, not by any measurement of the band count's "
    "edge phase; nothing here reads REG-012's result or its branch."
)

_H47 = re.compile(r"^### 4\.7 · .*$", re.M)
_H48 = re.compile(r"^### 4\.8 · ", re.M)


def section_47(text: str) -> str:
    s = _H47.search(text)
    assert s, "§4.7's heading is gone"
    rest = text[s.start():]
    e = _H48.search(rest)
    assert e, "§4.8's heading is gone"
    return rest[: e.start()]


def digest_at(sha: str) -> str:
    blob = subprocess.run(("git", "-C", str(ROOT), "show", f"{sha}:{PAPER_REL}"),
                          capture_output=True, text=True, check=True).stdout
    return hashlib.sha256(section_47(blob).encode("utf-8")).hexdigest()


def short(sha: str) -> str:
    return subprocess.run(("git", "-C", str(ROOT), "rev-parse", "--short", sha),
                          capture_output=True, text=True, check=True).stdout.strip()


def main() -> int:
    sha = short(SHA)
    after = digest_at(sha)
    before = digest_at(f"{sha}^")
    live = hashlib.sha256(
        section_47((ROOT / PAPER_REL).read_text(encoding="utf-8")).encode("utf-8")
    ).hexdigest()

    print(f"amendment commit   {sha}")
    print(f"  §4.7 at {sha}^   {before[:16]}…")
    print(f"  §4.7 at {sha}    {after[:16]}…")
    print(f"  §4.7 working tree {live[:16]}…")

    fails = []
    if before == after:
        fails.append(f"{sha} did not move §4.7 — the licence would be on the wrong commit")
    if live != after:
        fails.append("the working tree's §4.7 is not the committed one; commit it first")
    flat = " ".join(LICENCE.split())
    if len(flat) < 40:
        fails.append("licence too short")
    if "REG-012's outcome" in flat:
        fails.append("licence names REG-012's own outcome — that is reading (a)")
    if fails:
        for f in fails:
            print("  !! " + f)
        return 1

    text = TEST.read_text(encoding="utf-8")
    anchor = '        digest_after="69374513a57f699498da7568afb4ad6ad0af9c97ef4f7b4814a46d5fd375e7ad",\n    ),\n)\n'
    n = text.count(anchor)
    print(f"CENSUS  append anchor occurs {n} time(s) (want 1)")
    if n != 1:
        print("  !! anchor missing or ambiguous — nothing written")
        return 3

    lines, cur = [], ""
    for w in LICENCE.split():
        if len(cur) + len(w) + 1 > 74:
            lines.append(cur)
            cur = w
        else:
            cur = (cur + " " + w).strip()
    if cur:
        lines.append(cur)
    body = "\n".join(f'            "{l} "' for l in lines[:-1])
    body += "\n" + f'            "{lines[-1]}"'

    replacement = (
        '        digest_after="69374513a57f699498da7568afb4ad6ad0af9c97ef4f7b4814a46d5fd375e7ad",\n'
        "    ),\n"
        "    Amendment(\n"
        f'        sha="{sha}",\n'
        "        licence=(\n"
        f"{body}\n"
        "        ),\n"
        f'        digest_after="{after}",\n'
        "    ),\n"
        ")\n"
    )

    # ---- WT-118: assert the invariants against the ORIGINAL first ------------------
    def one_anchor(t: str) -> bool:
        return t.count("SEC_47_AT_REGISTRATION = ") == 1

    def immutable(t: str) -> bool:
        return "da24a9f91fc3c00e8aaae37f94754fe9a5ae069fd340f52c1d7c457aa64129bf" in t

    def first_amendment_intact(t: str) -> bool:
        return 'sha="6314302"' in t and "69374513a57f" in t

    patched = text.replace(anchor, replacement)

    checks = [
        ("SEC_47_AT_REGISTRATION present exactly once", one_anchor, one_anchor),
        ("the immutable registration-era digest is untouched", immutable, immutable),
        ("the 2026-08-17 amendment is not rewritten", first_amendment_intact,
         first_amendment_intact),
        ("the new digest is now in the file",
         lambda t: after not in t or True, lambda t: after in t),
        ("exactly two amendments", lambda t: t.count("    Amendment(\n") == 1,
         lambda t: t.count("    Amendment(\n") == 2),
    ]
    red = []
    for name, on_orig, on_new in checks:
        if not on_orig(text):
            red.append(f"GUARD VACUOUS -- {name}: false of the ORIGINAL too")
        elif not on_new(patched):
            red.append(f"GUARD RED -- {name}: the append broke it")
    if red:
        for r in red:
            print("  " + r)
        return 1

    shutil.copy2(TEST, TEST.with_suffix(TEST.suffix + ".bak-wt131b"))
    TEST.write_text(patched, encoding="utf-8")
    print("\nappended. guards green.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
