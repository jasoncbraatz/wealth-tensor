#!/usr/bin/env python3
"""wt125 — Paper IV §1-§3 re-read after the narrowing (wealthTensor-69): four repairs.

Context. `WT-102` narrowed Paper IV's TITLE and ABSTRACT only. Diffed against
`.bak-wt66b-narrow`, that patch touched three places: the title, the abstract's leading
clause, and one reference page range. §1-§3 body prose was never read against the new
framing. Every site that AGREED with the old wording now disagrees with the new one --
`-61`'s tell, in its created-defect direction rather than its missed-defect direction.

ED1  (finding IV-11) §1 ¶3, the sentence the paper labels its own claim, still carries the
     ladder shape the abstract gave up 35 lines above it: "the same atomic unit, a
     household's, aggregates to a firm's and to a sovereign's". "aggregates to A and to B"
     is a verb of derivation -- a stronger ladder than the "from X to the Y" that `WT-102`
     removed, and the trailing "without changing type" is the very defence `WT-102` called
     a retreat. Repair: restate flat, in the abstract's post-narrowing shape (one type at
     three NAMED scales), keeping the addition mechanism.

ED2  (finding IV-12) §3 opens claiming "the operator that moves between them is addition"
     and closes, fifty lines later, "what joins the scales is the question and the fact
     that each scale answers it quantitatively, which is what this section now claims and
     NO MORE." Addition is a joiner. Read straight through, the section's own closing
     deletes its opening, and a referee cannot tell which is the paper's position. The
     closing is what over-reaches -- `E1` removed the CHAIN (rho vs phi), never §2.2's
     addition. Repair: name addition in the closing so "no more" is true as written.

ED3  (finding IV-13a) §3 "**Firm.** A balance sheet is the household's holding, summed and
ED4  (finding IV-13b) reported." and "**Sovereign.** National accounts are firms summed."
     Both are written as PART-WHOLE identities: firm = households summed, sovereign =
     firms summed. As set composition both are false -- households are not constituents of
     firms, and national accounts carry the household sector directly (the paper's own §3
     Household paragraph is a household, not a firm). And nesting is precisely the
     "one structure" the narrowed abstract now disclaims. The intended claim is type
     identity plus addition WITHIN a scale. Repair: say the kind, not the nesting.

Hazards stated in advance (wt122's rule). The anchors are manuscript strings and this
script is itself a new file in scripts/, which the tree's guards read. Edit labels are
ED-prefixed per -67's convention. Post-conditions are ASSERTED, not printed (-67).
Census run BEFORE writing (`WT-099`), 7757 files: each anchor occurs exactly once in the
corpus except ED2's, which also appears inside `scripts/patch_wt56_e1_remedy.py` as that
one-shot's quoted replacement text -- a RECORD of what the paper said when it was written,
left alone per `WT-102`'s rule for a patch script's own anchors. It is referenced by no
test and by no Makefile target; verified before this edit, not assumed.
G-COACH-3: no CONDUCT or CONCESSIVE string enters any replacement, so Paper IV's
conduct_outside_allowed stays at its baseline 1 and concessive at 0.
"""
import pathlib, re, shutil, sys

DRY = "--dry" in sys.argv
ROOT = pathlib.Path.home() / "repos" / "wealth-tensor"
PAPER = ROOT / "docs/papers/paper-IV-composition/paper-IV.md"
BAK = PAPER.with_name(PAPER.name + ".bak-wt69-p7")

SENTINEL = "has one type wherever it appears"

ED1_ANCHOR = (
    "This paper is the claim that they are layers of one stack, and that the object at the bottom of it\n"
    "composes: **the same atomic unit, a household's, aggregates to a firm's and to a sovereign's\n"
    "without changing type.** That claim is worth stating carefully, because a nearby and stronger\n"
)
ED1_NEW = (
    "This paper is the claim that they are layers of one stack, and that the object at the bottom of\n"
    "it has one type wherever it appears: **a household's holding, a firm's balance sheet and a\n"
    "sovereign's accounts are the same kind of object, and summing holdings does not change the\n"
    "kind.** That claim is worth stating carefully, because a nearby and stronger\n"
)

ED2_ANCHOR = (
    "question and the fact that each scale answers it quantitatively, which is what this section now\n"
    "claims and no more. The demotion was written into that document's §2 **before** the leg was run,\n"
)
ED2_NEW = (
    "question, the fact that each scale answers it quantitatively, and the addition of §2.2 — which is\n"
    "what this section now claims and no more. The demotion was written into that document's §2\n"
    "**before** the leg was run,\n"
)

ED3_ANCHOR = (
    "**Firm.** A balance sheet is the household's holding, summed and reported. Paper III's result is\n"
    "that this reporting is a filter: a share φ of each true change passes through at once and the\n"
    "remainder is released at rate α from an unrecognised gap. The filter is a *per-class* object —\n"
    "Paper III indexes classes *i* and writes the recursion with a Hadamard product,\n"
)
ED3_NEW = (
    "**Firm.** A balance sheet is holdings of the household's kind, summed and reported. Paper III's\n"
    "result is that this reporting is a filter: a share φ of each true change passes through at once\n"
    "and the remainder is released at rate α from an unrecognised gap. The filter is a *per-class*\n"
    "object — Paper III indexes classes *i* and writes the recursion with a Hadamard product,\n"
)

ED4_ANCHOR = (
    "**Sovereign.** National accounts are firms summed, and Paper II's parameter space is what happens\n"
    "when a levy is assessed on that sum. Its central result is a composition result wearing different\n"
    "clothes: the base of a levy — stock or flow — is the question of *which component of the composed\n"
)
ED4_NEW = (
    "**Sovereign.** National accounts are the same holdings summed across every institutional sector,\n"
    "households and firms alike, and Paper II's parameter space is what happens when a levy is\n"
    "assessed on that sum. Its central result is a composition result wearing different clothes: the\n"
    "base of a levy — stock or flow — is the question of *which component of the composed\n"
)

EDITS = (("ED1", ED1_ANCHOR, ED1_NEW), ("ED2", ED2_ANCHOR, ED2_NEW),
         ("ED3", ED3_ANCHOR, ED3_NEW), ("ED4", ED4_ANCHOR, ED4_NEW))

CONDUCT = ("this programme", "this paper's earlier draft", "revision history",
           "an earlier draft", "the draft that preceded")
CONCESSIVES = ("Admittedly", "Of course", "It must be conceded", "To be fair",
               "It should be noted", "It is worth noting", "We acknowledge",
               "It must be admitted", "Needless to say", "In fairness",
               "It bears repeating", "It is important to note")


def norm(s):
    return re.sub(r"\s+", " ", s)


def main():
    text = PAPER.read_text(encoding="utf-8")

    # idempotence guard, normalised and ASSERTED (fire it, do not read it -- WT-096)
    if norm(SENTINEL) in norm(text):
        print("already applied; refusing (exit 2)")
        sys.exit(2)

    # every anchor asserted exactly once, literal AND normalised, before any write
    for label, anchor, _ in EDITS:
        n_lit = text.count(anchor)
        n_norm = norm(text).count(norm(anchor))
        assert n_lit == 1, f"{label}: literal anchor count {n_lit} != 1"
        assert n_norm == 1, f"{label}: normalised anchor count {n_norm} != 1"

    new = text
    for _, anchor, repl in EDITS:
        new = new.replace(anchor, repl)

    # glyph guard: no MICRO SIGN may enter a manuscript
    assert "µ" not in new, "U+00B5 MICRO SIGN found in output"
    # character-width guard (CHARACTERS, not bytes -- the em-dash is multi-byte).
    # SET subset, not a count: a count says "six became seven" and makes you find the
    # seventh yourself, which is how -69's first --dry printed five innocent pre-existing
    # lines alongside the one it had actually introduced. The guard should name the defect.
    wide = {ln for ln in new.splitlines() if len(ln) > 100 and not ln.startswith("|")}
    old_wide = {ln for ln in text.splitlines() if len(ln) > 100 and not ln.startswith("|")}
    assert wide <= old_wide, f"introduced long lines: {sorted(wide - old_wide)}"
    # G-COACH guard: counts must not rise from these edits
    for c in CONDUCT + CONCESSIVES:
        assert new.count(c) <= text.count(c), f"coach string {c!r} count rose"

    if DRY:
        print("DRY: all four edits would apply cleanly")
        for ln in new.splitlines():
            if len(ln) > 100 and not ln.startswith("|"):
                print("  long:", ln)
        return

    shutil.copy2(PAPER, BAK)  # the undo path comes FIRST
    PAPER.write_text(new, encoding="utf-8")

    # post-conditions ASSERTED against a fresh read
    after = PAPER.read_text(encoding="utf-8")
    assert norm(SENTINEL) in norm(after), "ED1 sentinel absent after apply"
    for label, anchor, repl in EDITS:
        assert repl in after, f"{label}: replacement absent after apply"
        assert anchor not in after, f"{label}: old text survived"
    assert "µ" not in after
    print("APPLIED: ED1 + ED2 + ED3 + ED4; bak =", BAK.name)


if __name__ == "__main__":
    main()
