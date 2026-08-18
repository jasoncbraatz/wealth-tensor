#!/usr/bin/env python3
"""wealthTensor-76 · rider part 1 -- the instrument fields, added to REVIEW-016's front matter.

Guarded the same way every patch in this project is: the OLD string is asserted present exactly
once before anything is written, and the backup is taken only after the guard passes (WT-118).
"""
import pathlib, shutil, sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
DOC = ROOT / "docs/REVIEW-016-P7-paperII-pass8.md"

OLD = """# REVIEW-016 · Paper II's SIXTH independent `P7` read
"""
NEW = """---
new_instrument: inherited-first-application
instrument_name: "A5 — grep each module a data-availability section names against the script it is paired with, and run every command it names (originated wealthTensor-75 on Paper IV; Paper II had never seen it)"
findings_from_new_instrument: 2 of 5
# FALSIFY THIS ROW. For a script instrument:
#   git log --diff-filter=A --format='%h %ad' --date=short -- scripts/<instrument_name>
# an earlier session's add-commit means the row is wrong. A5 is a NON-SCRIPT axis, so its
# falsifier is REVIEW-015 §2 IV-2: open it and find the axis described, or this row is wrong.
# The two findings claimed: II-27 (diffing the named command's output against §3) and II-30
# (grepping the file §7 names). II-28, II-29 and II-31 came from reading.
# THREE VALUES, NOT TWO, AND THIS ROW IS WHY: no axis was invented here, and five findings
# landed anyway. `new: no` would have recorded the exact opposite of what happened.
# Ledger of all six passes: docs/p7-passes.tsv
---

# REVIEW-016 · Paper II's SIXTH independent `P7` read
"""

text = DOC.read_text(encoding="utf-8")
n = text.count(OLD)
if n != 1:
    sys.exit(f"GUARD FAILED: title line found {n} times, expected 1. Nothing written.")
if "new_instrument:" in text:
    sys.exit("GUARD FAILED: front matter already present. Nothing written.")

shutil.copy2(DOC, DOC.with_suffix(".md.bak-rider"))
DOC.write_text(text.replace(OLD, NEW, 1), encoding="utf-8")

after = DOC.read_text(encoding="utf-8")
assert after.count("new_instrument: inherited-first-application") == 1
assert after.count("findings_from_new_instrument: 2 of 5") == 1
assert after.endswith(text[-200:]), "POST-CONDITION FAILED: tail of the document changed"
print("REVIEW-016 front matter added; tail byte-identical; backup .md.bak-rider")
