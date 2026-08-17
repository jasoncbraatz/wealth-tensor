#!/usr/bin/env python3
"""wt124 — Paper II P7 pass 4 (second independent read, wealthTensor-68): two repairs.

ED1  (finding II-13) §3.1's table states no configuration for its flow rows. They run at
     full realisation, rho = 1 — the implementation's default (redistribution.py:89) —
     and the reader can only reverse-engineer that from §2.3 plus the half-failed-
     prediction paragraph. Same species as repaired II-12, one section over. Repair:
     a one-sentence table note.

ED2  (finding II-14) "a change of six parts in a million" describes 0.076542 -> 0.076536.
     The absolute change IS 6e-6; the conventional *relative* reading of "parts in a
     million" gives ~78 ppm, so the phrase misstates the quantity by ~13x under its most
     natural reading. Repair: write the number.

Hazards stated in advance (wt122's rule): the anchors below are manuscript strings; this
script is itself a new file in scripts/, so the tree's guards read it too. Edit labels are
ED-prefixed per -67's renamed convention (the exhibit-label canary polices the shorter
shape; a warning about the landmine is not exempt from the landmine, so the shape is not
spelled here). Post-conditions are ASSERTED, not printed (-67's guard lesson).
"""
import pathlib, re, shutil, sys, unicodedata

DRY = "--dry" in sys.argv
ROOT = pathlib.Path.home() / "repos" / "wealth-tensor"
PAPER = ROOT / "docs/papers/paper-II-redistribution/paper-II.md"
BAK = PAPER.with_name(PAPER.name + ".bak-wt68-p7")

SENTINEL = "flow rows are assessed at full realisation"

ED1_ANCHOR = (
    "| flow, *r* = 1.000 | 0.125 | 0.1026 | 0.138 | yes |\n"
    "\n"
    "At a matched rate the two bases sit"
)
ED1_NEW = (
    "| flow, *r* = 1.000 | 0.125 | 0.1026 | 0.138 | yes |\n"
    "\n"
    "*The flow rows are assessed at full realisation, ρ = 1 — §2.3's "
    "mark-to-market case and the\nimplementation's default; §3.2 is the sweep that "
    "lowers it.*\n"
    "\n"
    "At a matched rate the two bases sit"
)

ED2_ANCHOR = "a change of six parts in a million"
ED2_NEW = "a change of 6 × 10⁻⁶"


def norm(s):
    return re.sub(r"\s+", " ", s)


def main():
    text = PAPER.read_text(encoding="utf-8")

    # idempotence guard, normalised and ASSERTED
    if norm(SENTINEL) in norm(text):
        print("already applied; refusing (exit 2)")
        sys.exit(2)

    # every anchor asserted to occur exactly once, before any write
    for label, anchor in (("ED1", norm(ED1_ANCHOR)), ("ED2", norm(ED2_ANCHOR))):
        n = norm(text).count(anchor)
        assert n == 1, f"{label}: anchor count {n} != 1"
    # non-normalised presence too (the replace below is literal)
    assert text.count(ED1_ANCHOR) == 1, "ED1 literal anchor not unique/present"
    assert text.count(ED2_ANCHOR) == 1, "ED2 literal anchor not unique/present"

    new = text.replace(ED1_ANCHOR, ED1_NEW).replace(ED2_ANCHOR, ED2_NEW)

    # glyph guard: no MICRO SIGN may enter a manuscript
    assert "µ" not in new, "U+00B5 MICRO SIGN found in output"
    # character-width guard (characters, not bytes; em-dash is multi-byte)
    wide = [ln for ln in new.splitlines() if len(ln) > 100 and not ln.startswith("|")]
    old_wide = [ln for ln in text.splitlines() if len(ln) > 100 and not ln.startswith("|")]
    assert len(wide) <= len(old_wide), f"introduced long lines: {wide}"

    if DRY:
        print("DRY: both edits would apply cleanly")
        return

    shutil.copy2(PAPER, BAK)  # the undo path comes FIRST
    PAPER.write_text(new, encoding="utf-8")

    # post-conditions ASSERTED against a fresh read
    after = PAPER.read_text(encoding="utf-8")
    assert norm(SENTINEL) in norm(after), "ED1 sentinel absent after apply"
    assert ED2_NEW in after, "ED2 absent after apply"
    assert ED2_ANCHOR not in after, "ED2 old phrase survived"
    assert "µ" not in after
    print("APPLIED: ED1 + ED2; bak =", BAK.name)


if __name__ == "__main__":
    main()
