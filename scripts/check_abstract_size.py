#!/usr/bin/env python3
"""Abstract size, measured identically on every machine.

Rationale, recorded because it cost a round trip: `wc -w` and `awk NF` disagree across
platforms on this text — GNU wc in the cloud counts 248 words, BSD wc on darwin counts 266
for the same bytes, because the abstract carries em dashes, middots and Greek letters and a
byte-oriented word splitter breaks them differently. arXiv's ceiling is 1920 CHARACTERS, and
PREPRINT-CHECKLIST §A's bar is 150-250 WORDS; both must be counted on the decoded string or
the criterion means something different depending on who runs it.

exit 0 iff 150 <= words <= 250 and chars <= 1920.  --print reports the numbers.
"""
import pathlib
import sys

PAPER = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 and not sys.argv[1].startswith("--")
                     else "docs/papers/paper-III-dual-tensor/paper-III.md")

lines = PAPER.read_text(encoding="utf-8").split("\n")
body, on = [], False
for line in lines:
    if line.strip() == "## Abstract":
        on = True
        continue
    if line.startswith("**Keywords"):
        on = False
    if on:
        body.append(line)

text = " ".join(" ".join(body).split())
words, chars = len(text.split()), len(text)

if "--print" in sys.argv:
    print("words=%d chars=%d" % (words, chars))

sys.exit(0 if 150 <= words <= 250 and chars <= 1920 else 1)
