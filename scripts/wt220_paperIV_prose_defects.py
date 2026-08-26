#!/usr/bin/env python3
"""wt220 — two prose defects in paper-IV that NOTHING in this repository could see.

BOTH WERE INTRODUCED BY PASS D's OWN wt211 CORRECTIONS, AND wt211 IS THE ONE BATCH NO
ADVERSARIAL VERIFIER EVER READ -- the two verifiers were scoped to the first 166 repairs and
the corrections came after them. The stitch-checker was run over the first batch and not the
second. So the gap is not that the apparatus is weak; it is that a LATE correction round
inherits none of the verification the round it corrects received.

  1. "a confiscatory levy on flow is / leaves the wealth vector exactly unchanged" -- a
     STRANDED AUXILIARY. The edit replaced the predicate and left the old copula standing.
     This shipped in a tagged corpus, past 1168 tests, 30 green guards, 41 re-run claims,
     a page-for-page layout reproduction and two adversarial verifiers. NOTHING IN THIS
     REPOSITORY READS ENGLISH, and SHIP-STATEMENT section 6.6 now has its sharpest instance.

  2. "its compressive budget κ — which Paper II is explicit is a budget and not a mechanism —"
     -- parseable, and clumsy in the same shape as the first: two finite verbs colliding at a
     clause boundary. Rewritten to say the same thing without the collision.

Idempotent; exit 2 if a site matches neither state.
"""
import pathlib, sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
P4 = ROOT / "docs/papers/paper-IV-composition/paper-IV.md"

EDITS = [
 ("stranded-copula",
  "state the assessing layer can see*, and at zero realisation a confiscatory levy on flow is\n"
  "leaves the wealth vector exactly unchanged, agent by agent.",
  "state the assessing layer can see*, and at zero realisation a confiscatory levy on flow\n"
  "leaves the wealth vector exactly unchanged, agent by agent."),
 ("colliding-verbs",
  "a statement kinetic exchange can absorb directly, and its compressive budget κ — which Paper II is\n"
  "explicit is a budget and not a mechanism — is the sort of closed-form\nquantity that literature likes.",
  "a statement kinetic exchange can absorb directly, and κ — its compressive budget rather than\n"
  "its mechanism, in Paper II's own words — is the sort of closed-form\nquantity that literature likes."),
]

def main():
    t = P4.read_text(encoding="utf-8"); applied = already = 0; fail = []
    for tag, old, new in EDITS:
        if t.count(old) == 1 and t.count(new) == 0:
            t = t.replace(old, new, 1); applied += 1; print("APPLIED         %s" % tag)
        elif t.count(old) == 0 and t.count(new) == 1:
            already += 1; print("ALREADY-APPLIED %s" % tag)
        else:
            fail.append(tag); print("!! NEITHER      %s  old=%d new=%d" % (tag, t.count(old), t.count(new)))
    if fail:
        print("\nFAIL: %d site(s); NOTHING WRITTEN" % len(fail)); return 2
    if t != P4.read_text(encoding="utf-8"):
        bak = P4.with_suffix(".md.bak-wt220")
        if not bak.exists(): bak.write_text(P4.read_text(encoding="utf-8"), encoding="utf-8")
        P4.write_text(t, encoding="utf-8"); print("WROTE paper-IV.md")
    print("\napplied=%d already=%d" % (applied, already)); return 0

if __name__ == "__main__":
    sys.exit(main())
