#!/usr/bin/env python3
"""wt204 — POST-SHIP: what Pass B found that does not block, and what Pass C inherits
BECAUSE OF PASS B rather than in spite of it.

DoD §1.2 says a finding made after the freeze goes here.  §3.0 says a pass closes only
when its successor can start AND finish, which means the successor's scope must be
EXPLICIT rather than discoverable.  Both halves live in this append.

Idempotent: NO-OP on a second run, exit 0.
"""
import sys, pathlib

P = pathlib.Path.home() / "repos/wealth-tensor/docs/POST-SHIP.md"
MARK = "## From `wealthTensor-104` (Pass B)"

BLOCK = """

---

## From `wealthTensor-104` (Pass B)

**Nothing here blocks. Nothing here is an at-bat until the corpus ships.**

### Findings made while repairing, filed here rather than on the list (§ 1.2)

- **`wc -w` is locale-dependent on GNU `coreutils` and locale-INDEPENDENT on macOS.** On the same
  bytes (`md5 eb56ef67162df6db0fabf50819db78f0`) macOS `wc -w` returns **7 527** under `LC_ALL=C`,
  `LC_ALL=C.UTF-8` and `LC_ALL=en_US.UTF-8` alike; GNU `wc` returns **7 367** under `LC_ALL=C` and
  **7 527** under `LC_ALL=C.UTF-8`. **`SL-6`'s defect could not be reproduced on darwin at all** —
  it was found and confirmed from the cloud side of the session. *The general shape, which is the
  part worth keeping: a check this repository runs on one platform can be green there and red for a
  reader on another, and the manuscript is read by the reader, not by darwin.*
- **`paper-I` sits outside `#scope` in `docs/promises-adjudicated.tsv`** and therefore carries 13
  unadjudicated promises the sweep prints and does not gate. That is a deliberate scope line, not a
  gap, and it is named here so no later pass reads the sweep's own output as a defect. Widening
  `#scope` is a decision with a real cost (13 rows, each needing evidence re-run) and it belongs
  after the ship, if ever — `paper-I` is superseded and is not one of the papers this corpus joins.
- **The one §4 figure with no command is `§ 4.2`'s 31.7%.** It is `wt084`'s printed family
  restricted to a ten-per-cent opening gap; the restriction is applied in the prose. `SL-7`'s repair
  DISCLOSES this rather than implying a command. If a future session wants it printed, the change is
  four lines in `wt084_identification_closed_form.py` — **and it is a new instrument under § 1.1
  until the corpus ships.**

### What PASS C inherits FROM PASS B, stated so it is not discovered

**REVIEW-038 § 4's C-class census was taken before Pass B's edits existed.** Pass B added prose in
four places; here is what moved, so Pass C can add to that census rather than re-take it.

| where | what Pass B added | C-class effect |
|---|---|---|
| `paper-III` § 11 | four **Regenerate** bullets, ~30 lines | **Zero hard C-e.** Every artefact named is a committed `scripts/wt###.py` a reader can fetch — the § 2.5 repair clause's own permitted case. No session number, no `REVIEW` doc, no `p7-passes.tsv` reference. |
| `paper-IV` § 10 | one **Regenerate** bullet, 4 lines | Zero hard C-e, same reason. |
| `paper-II`/`III`/`IV` front matter | one revision line each | Written as a claim about the work, not about the working. `defensive_count` +0. |
| `paper-II` References | Piketty (2014) removed | One entry fewer: **15**, not 16. |

**No section moved and no section was reordered.** Every Pass B edit is inside an existing section,
so the 13 C-d fold problems and the 1 C-c orphan Pass C inherits are exactly REVIEW-038's, unchanged
in identity and in location-by-section. **The line numbers in REVIEW-038 have moved** — find those
items by their quoted text, the same rule `SHIP-LIST` set for Pass B.

**The layout baseline moved: 145 pages → 147.** `docs/deliverable/LAYOUT-MANIFEST.json` is
regenerated and `verify-layout.sh` reproduces at the new count. Any doc still saying 145 is stale.

### Ideas that arrived with the repairs

- **A locale-pinning guard.** Every command a manuscript names as checkable could carry its locale,
  and a test could assert that any `wc`/`sort`/`uniq` a manuscript names is written with one.
  `SL-6` is the only known instance; the guard is the general form. New instrument — after the ship.
- **A reference-entry reachability sweep run per-section rather than per-document.** `wt133` sweep 2
  answers *is this entry cited anywhere*; it cannot answer *is it cited at the sentence that relies
  on it*, which is the actual `IV-7`/`SL-8` standard and was applied by hand both times.
"""

def main() -> int:
    text = P.read_text(encoding="utf-8")
    if MARK in text:
        print("wt204: NO-OP (already appended)"); return 0
    P.write_text(text.rstrip("\n") + BLOCK, encoding="utf-8")
    print("wt204: APPENDED Pass B's POST-SHIP block")
    return 0

sys.exit(main())
