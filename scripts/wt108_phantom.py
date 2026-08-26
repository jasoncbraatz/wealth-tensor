"""wealthTensor-108 -- a phantom quotation, caught by wt148 and repaired.

`"one question asked three times"` was attributed to docs/RESULT-END-TO-END-001-E1.md in
docs/papers/README-v1.md (written at -107). grep says the phrase appears NOWHERE in that
document, or anywhere in the repository except the sentences quoting it. E1's actual verdict
is quoted below, verbatim from its own header block. METHOD-001, instance 7.
"""
import pathlib, sys

TRUE = ("put that assertion under test and **failed it at leg `E1a`**: *\"ρ and φ are not the same "
        "kind of object, so the join between Papers II and III is vocabulary at the sovereign scale.\"*")

EDITS = [
 ("docs/papers/README-v1.md",
  'Its thesis is that the three scales are one structure, and the corpus\'s own end-to-end check\n'
  '(`docs/RESULT-END-TO-END-001-E1.md`) demoted that to "one question asked three times".',
  'Its thesis is that the three scales are one structure — the manuscript\'s own phrase for it,\n'
  'quoted in the check below, is *"a chain rather than three analogies"*. The corpus\'s own\n'
  'end-to-end check (`docs/RESULT-END-TO-END-001-E1.md`) ' + TRUE),

 ("docs/papers/paper-IV-composition/paper-IV.md",
  "> thesis is that the three scales are one structure. The corpus's own end-to-end check,\n"
  '> `docs/RESULT-END-TO-END-001-E1.md`, demoted that to *"one question asked three times."* The\n'
  "> paper is left here intact",
  "> thesis is that the three scales are one structure — its own phrase for it is *\"a chain rather\n"
  "> than three analogies\"*. The corpus's own end-to-end check,\n"
  '> `docs/RESULT-END-TO-END-001-E1.md`, ' + TRUE.replace("**failed it at leg `E1a`**", "**failed it at leg `E1a`**") + " The\n"
  "> paper is left here intact"),

 ("docs/RESULT-CROSSING-HEIGHT-001.md",
  'end-to-end check (`docs/RESULT-END-TO-END-001-E1.md`) demoted the fourth paper\'s central thesis to\n'
  '"one question asked three times" for exactly this failure mode, and',
  'end-to-end check (`docs/RESULT-END-TO-END-001-E1.md`) failed the fourth paper\'s central thesis at\n'
  'leg `E1a` for exactly this failure mode — *"ρ and φ are not the same kind of object"* — and'),
]

for path, old, new in EDITS:
    p = pathlib.Path(path)
    s = p.read_text(encoding="utf-8")
    if s.count(old) != 1:
        sys.exit("ABORT %s: anchor count %d\n---\n%r" % (path, s.count(old), old[:200]))
    p.write_text(s.replace(old, new, 1), encoding="utf-8")
    print("  ok ", path)

import subprocess
r = subprocess.run(["grep", "-rn", "asked three times", "--include=*.md", "."],
                   capture_output=True, text=True)
live = [l for l in r.stdout.split("\n") if l and ".bak" not in l]
print("remaining live occurrences:", len(live))
for l in live: print("   ", l[:140])
