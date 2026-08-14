"""The defensive-sentence counter — charter §7's G-COACH-3, mechanised.

WHY THIS EXISTS
---------------
`CO-AUTHOR-CHARTER.md` §2 states a hard invariant: *defensive-sentence count in the
manuscript is non-increasing across a revision pass.* §7 lists it as gate item
G-COACH-3. It has been declared since 2026-08-12 and checked exactly zero times, because
nothing in the repository could count one. An invariant nobody can evaluate is a
preference, and the charter's whole point is that ABSORB -- pasting an objection into the
manuscript as a caveat -- is the illegal move that feels like diligence while it happens.

WHAT IT IS, AND THE OBJECTION IT HAS TO SURVIVE FIRST
-----------------------------------------------------
This is a LEXICON counter, and this repository's own doctrine says a green assertion that
proves nothing is worse than an absent one, because it reads as coverage. A lexicon
cannot tell a hedge from a scope statement; "the design does not measure the economic δ"
is a scope statement and "the result may not generalise" is a hedge, and no word list
separates them.

So this tool does not emit a verdict about a document. **It emits a DELTA between two
versions of one document**, and the crudeness cancels: the same crude counter applied
before and after a revision pass detects hedges the pass ADDED, which is exactly and only
what the invariant is about. A count is never reported without the version it is a count
against.

Two exclusions, both from the charter rather than from convenience:

  * **§Limitations is counted separately and excluded from the invariant** (charter §3.2:
    limitations appear once, in one honest room). Hedging there is the design.
  * **Table rows and fenced code are not prose** and are skipped.

WHAT IT CANNOT DO, STATED SO NOBODY READS IT AS MORE THAN IT IS
---------------------------------------------------------------
It cannot tell a hedge from a scope statement, so its LEVEL is meaningless and only its
DELTA is evidence. It cannot see a claim weakened by deletion of its magnitude. It cannot
see hedging carried by sentence structure rather than by a marker word. A pass that adds
none of the markers below and still guts a claim passes this check; that is what the
coach's eye is for, and this tool exists to catch the failure mode the eye has already
proven it misses -- the slow accumulation nobody notices in any single sitting.

USAGE
-----
    python3 scripts/defensive_count.py PATH [--against OTHER] [--json OUT]

With `--against`, prints the per-section delta and exits non-zero if any section outside
§Limitations gained a defensive sentence.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

# --------------------------------------------------------------------------------------
# THE LEXICON. Every entry is a HEDGE ON A CLAIM THE PAPER IS MAKING, not a statement of
# scope. Scope words ("this paper does not measure", "out of scope", "not registered")
# are deliberately absent: narrowing a claim is the legal repair under charter §2, and a
# counter that punished it would push a revision toward vagueness instead of precision.
# --------------------------------------------------------------------------------------
MARKERS = (
    r"arguably", r"admittedly", r"of course,", r"it should be noted",
    r"it is worth noting", r"it is possible that", r"one might object",
    r"it could be argued", r"some readers may", r"a sceptical reader might",
    r"cannot be ruled out", r"we cannot rule out", r"may well be", r"might well",
    r"to some extent", r"to a degree", r"in some sense", r"broadly speaking",
    r"more or less", r"reasonably confident", r"fairly confident",
    r"should be interpreted with caution", r"with appropriate caution",
    r"with some caution", r"caveat", r"with the caveat",
    r"does not necessarily", r"not necessarily", r"need not be",
    r"we do not claim", r"we make no claim", r"we would not claim",
    r"tentatively", r"provisionally", r"suggestive rather than",
    r"at least in principle", r"in principle at least",
    r"this is not to say", r"that said,", r"having said that",
    r"it remains possible", r"remains an open question whether",
)
_MARKER_RE = re.compile("|".join(MARKERS), re.I)

LIMITATIONS_RE = re.compile(r"limitation", re.I)


def _prose_by_section(text: str) -> dict:
    """Map heading -> prose text, skipping tables and fenced code."""
    sections: dict[str, list] = {}
    current = "(front matter)"
    sections[current] = []
    fenced = False
    for line in text.split("\n"):
        if line.lstrip().startswith("```"):
            fenced = not fenced
            continue
        if fenced:
            continue
        m = re.match(r"^(#{1,6}) +(.*)$", line)
        if m:
            current = m.group(2).strip()
            sections.setdefault(current, [])
            continue
        if line.lstrip().startswith("|"):
            continue                      # a table row is data, not prose
        if line.lstrip().startswith(">"):
            line = line.lstrip()[1:]      # a block quote is still the paper's voice
        sections.setdefault(current, []).append(line)
    return {k: " ".join(v) for k, v in sections.items()}


def _sentences(prose: str):
    prose = re.sub(r"\s+", " ", prose).strip()
    if not prose:
        return []
    # Crude, and deliberately so: the unit only has to be STABLE between two versions of
    # one document, not linguistically correct.
    return [s for s in re.split(r"(?<=[.!?]) +(?=[A-Z*_\"'(])", prose) if s.strip()]


def count(text: str) -> dict:
    out = {}
    for heading, prose in _prose_by_section(text).items():
        hits = [s for s in _sentences(prose) if _MARKER_RE.search(s)]
        if hits:
            out[heading] = {"defensive": len(hits),
                            "examples": [h[:120] for h in hits[:3]]}
    return out


def totals(counts: dict) -> tuple:
    """(counted toward the invariant, inside §Limitations)."""
    invariant = sum(v["defensive"] for k, v in counts.items()
                    if not LIMITATIONS_RE.search(k))
    limits = sum(v["defensive"] for k, v in counts.items() if LIMITATIONS_RE.search(k))
    return invariant, limits


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("path", type=Path)
    ap.add_argument("--against", type=Path,
                    help="a previous version; prints the delta and enforces the invariant")
    ap.add_argument("--json", type=Path, help="write the per-section counts here")
    args = ap.parse_args(argv)

    now = count(args.path.read_text(encoding="utf-8"))
    inv, lim = totals(now)
    print(f"{args.path.name}: {inv} defensive sentence(s) outside §Limitations, "
          f"{lim} inside it")
    for heading, v in sorted(now.items()):
        tag = "  (§Limitations — exempt)" if LIMITATIONS_RE.search(heading) else ""
        print(f"  {v['defensive']:>3}  {heading[:70]}{tag}")
        for ex in v["examples"]:
            print(f"         · {ex}")

    if args.json:
        args.json.write_text(json.dumps(
            {"totals": {"invariant": inv, "limitations": lim},
             "sections": {k: v["defensive"] for k, v in sorted(now.items())}},
            indent=2) + "\n")
        print(f"  written: {args.json}")

    if not args.against:
        print("\n  NOTE: a LEVEL is not evidence. Re-run with --against a previous "
              "version;\n  only the delta means anything (see this file's docstring).")
        return 0

    before = count(args.against.read_text(encoding="utf-8"))
    b_inv, b_lim = totals(before)
    print(f"\nagainst {args.against.name}: {b_inv} outside §Limitations, {b_lim} inside")
    worse = []
    for heading in sorted(set(now) | set(before)):
        a = now.get(heading, {}).get("defensive", 0)
        b = before.get(heading, {}).get("defensive", 0)
        if a != b:
            arrow = "+" if a > b else ""
            print(f"  {b} -> {a}  ({arrow}{a - b})  {heading[:66]}")
            if a > b and not LIMITATIONS_RE.search(heading):
                worse.append(heading)
    print(f"\n  TOTAL outside §Limitations: {b_inv} -> {inv} ({inv - b_inv:+d})")
    if worse or inv > b_inv:
        print("\n  G-COACH-3 FAILS. A revision pass added hedging prose. Charter §2: if a "
              "finding\n  seems to demand new hedging, it demands a NARROWER CLAIM — "
              "rewrite the claim,\n  delete the hedge. Sections that grew: "
              f"{worse or '(total only)'}")
        return 1
    print("\n  G-COACH-3 holds: the defensive-sentence count is non-increasing.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
