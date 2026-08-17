#!/usr/bin/env python3
"""wt119_roads_tick.py -- tick ROADS-001's open literature-search question.

ROADS-001 ends its Road One case with a section headed "What I could not check and you
should", naming the optimal-taxation-with-Pareto-tails literature as the single search to
run before writing.  wealthTensor-66 ran it (docs/SCOUT-001-...) and it came back KNOWN.
A live proposal that has been answered must SAY so on its own page, or the next session
reads it as still open -- which is exactly how this item survived six sessions.

Anchored on the WHOLE PARAGRAPH (the -65 rule: sentence anchors collide with whatever
survived on the same source line in re-wrapped prose).  assert count == 1 before any
write; .bak first; --dry writes a *.wt66-dryrun beside the original for diffing.
"""
import argparse
import shutil
import sys

PATH = "docs/ROADS-001-two-reconstructions.md"

OLD = """### What I could not check and you should

Whether the truncation-versus-scaling effect on the tail index is already known. The
optimal-taxation-with-Pareto-tails literature is where it would live. **This is the single search I
would run before writing, precisely because it is the thing I am telling you to lead with.**"""

NEW = """### What I could not check and you should

> ### ☑ CHECKED, 2026-08-17, `wealthTensor-66` — AND THE ANSWER IS **KNOWN**.
>
> **Do not read the section below as a live proposal.** The search ran; see
> `docs/SCOUT-001-truncation-vs-scaling-prior-art.md` and `LEDGER` `WT-100`.
>
> **Bouchaud & Mézard (2000), *Physica A* 282, 536–545, eqs. (11)–(13)** already derive the
> Pareto tail exponent µ in closed form as a function of an income (**flow**) tax rate, a
> capital (**stock**) tax rate, and the fraction of *each* redistributed per capita — and
> report the ranking, more strongly than Road One proposes it: the flow levy raises µ, while
> the stock levy *lowers* µ unless enough of it is rebated. The rebate fraction that §2 above
> proposes to introduce as a novel "fifth coordinate" is a coordinate in their equation (13).
> They also state the organising contrast itself: an extra term that *"breaks the symmetry
> under wealth rescaling"* is what leaves *"the Pareto tail truncated for large wealths."*
>
> **And the `r = 1` cap below — called here "the strongest claim and the one most likely to be
> wrong" — is Benhabib, Bisin & Zhu (2011) §4.1**, who call it *"straightforward to show."*
> It is not wrong. It is theirs, and it must be **cited, not claimed**.
>
> **This was not a failure of effort but of address.** This section, `REVIEW-004` and
> `HANDOFF-PROMPT` all send the searcher to *optimal-taxation-with-Pareto-tails*. The result
> lives in **statistical physics**, which has asked what operations on a random multiplier do
> to its exponent since the 1990s. Search prior art by the **shape of the equation**, not by
> the subject matter — a within-field search cannot find a result written in another field's
> vocabulary.
>
> **What survives is narrow:** the *asymmetric* flow levy (realised gains only, **no loss
> offset**, hence a true truncation rather than an affine contraction) is in nobody's corpus,
> and nobody compares at matched **revenue**. That is a remark inside a paper. It is not a
> thesis to lead one with, and Road One's headline is unavailable.

Whether the truncation-versus-scaling effect on the tail index is already known. The
optimal-taxation-with-Pareto-tails literature is where it would live. **This is the single search I
would run before writing, precisely because it is the thing I am telling you to lead with.**"""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry", action="store_true")
    a = ap.parse_args()
    src = open(PATH).read()
    n = src.count(OLD)
    print("anchor occurrences: %d (require exactly 1)" % n)
    if n != 1:
        print("REFUSING: anchor is not unique.")
        return 2
    if src.count("CHECKED, 2026-08-17"):
        print("REFUSING: tick already present (idempotence guard).")
        return 3
    out = src.replace(OLD, NEW)
    dest = PATH + ".wt66-dryrun" if a.dry else PATH
    if not a.dry:
        shutil.copyfile(PATH, PATH + ".bak-wt66-tick")
        print("backed up -> %s.bak-wt66-tick" % PATH)
    open(dest, "w").write(out)
    print("wrote %s  (%d -> %d chars)" % (dest, len(src), len(out)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
