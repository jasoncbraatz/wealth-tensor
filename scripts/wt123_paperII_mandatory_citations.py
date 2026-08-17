#!/usr/bin/env python3
"""
wt123 -- Paper II's TWO MANDATORY CITATIONS (card 1217556375636027).
Session wealthTensor-67.  Follows the census in wt122, which is what set the
edits below; read that script's output before this one.

WHAT THE CENSUS CHANGED ABOUT THE CARD'S INSTRUCTIONS
-----------------------------------------------------
The card gave two placement rules.  wt122 measured both, with a fired positive
control on every probe:

  H1  "B&M wherever Paper II contrasts the STOCK levy with the FLOW levy"
      -> 1 site in paper-II.md (sec 3.1, the 'different objects' paragraph).
         Probe control fired.  PLACED.

  H2  "BBZ 2011 sec 4.1 wherever the r = 1 cap appears"
      -> *** 0 sites in ALL FOUR manuscripts. ***  The R1_CAP probe fired on
         its control (DECISION-001, 3 hits) and found 8 docs/ files and 5
         scripts carrying the cap -- and no manuscript.  The r = 1 cap is a
         PROJECT-NOTEBOOK claim, not a Paper II claim.  So BBZ is NOT placed
         at a cap Paper II does not assert.  It is placed where it actually
         binds on what Paper II DOES assert (sec 6), and sec 4.1 is named there
         as the thing an extension would meet, explicitly flagged as a claim
         this paper does not make.
         Citing BBZ at an r=1 cap in Paper II would have meant inventing the
         claim to hold the citation.  That is the failure this script refuses.

  H3  Bouchaud / Mezard / Benhabib / Bisin / Zhu: body=0, references=1, all
      five.  LISTED AND NEVER CITED -- the same defect paper-I's REVIEW-002
      A10 caught.  A reference list entry is not a credit.  That is the real
      bug the card was pointing at, and ED1/ED2/ED3 fix it.

  H4  No proposed anchor occurs in tests/, scripts/ or src/ (WT-094 clear).

AND ONE BIBLIOGRAPHIC ERROR FOUND WHILE VERIFYING
-------------------------------------------------
Crossref 10.1016/S0378-4371(00)00205-3 gives Physica A issue "3-4".
paper-II.md and paper-IV.md both say 282(3).  Corrected in both (ED4, ED7).
Crossref 10.3982/ECTA8416 confirms Econometrica 79(1) 123-157, which RESOLVES
the standing "page range to re-check" flag on the BBZ entry (ED5).

SAFETY (the house pattern: wt119, wt120, wt121)
-----------------------------------------------
  * whole-paragraph / whole-entry anchors, never sentence fragments
  * edit labels are ED1..ED7, NOT the bare E-prefixed form. `tests/
    test_reg002_sec5_e4_extension_label.py::test_the_third_surface_scope_is_warranted` is a
    HOMOGRAPH CANARY over scripts/: it asserts that raw substring hits for the estate's
    FOURTH EXHIBIT LABEL, minus the flake8 `noqa` homograph, equal the word-boundary hits.
    That label is a per-script LOCAL name in this estate, so any new identifier that merely
    CONTAINS it -- an `_NEW`-suffixed constant, which is what this script's first draft
    used -- breaks the identity and reds the suite. It did: 1 failed, 1077 passed.
    The canary is working as designed; the name was the bug. DO NOT WIDEN THE TEST.
    And note that this very comment is written without spelling the token, because the
    first version of the comment tripped the canary it was written to document.
  * EVERY anchor asserted to occur exactly once BEFORE any file is written
  * .bak written first
  * --dry prints the diff and writes nothing
  * idempotence guard: refuses to run twice
  * inserted lines wrapped and asserted at <= 100 CHARACTERS (not bytes --
    the text carries mu, kappa, section signs and em dashes)

Usage:  python3 scripts/wt123_paperII_mandatory_citations.py [--dry]
Exit 0 applied / 0 dry-run ok / 2 refusal (anchor miscount or already applied).
"""

import os
import re
import shutil
import sys
import textwrap

REPO = os.path.expanduser("~/repos/wealth-tensor")
P2 = os.path.join(REPO, "docs/papers/paper-II-redistribution/paper-II.md")
P4 = os.path.join(REPO, "docs/papers/paper-IV-composition/paper-IV.md")
TAG = "wt67-cites"
WIDTH = 100

IDEMPOTENCE_SENTINEL = "Bouchaud and Mézard (2000) carry a flow levy"


def norm_ws(s):
    """Collapse whitespace runs. The manuscripts are hard-wrapped at 100
    columns, so every phrase of interest straddles a newline."""
    return re.sub(r"\s+", " ", s)


def wrap(text):
    """Wrap a logical paragraph to <=100 CHARACTERS. Deterministic."""
    out = []
    for logical in text.split("\n"):
        if not logical.strip():
            out.append("")
            continue
        indent = re.match(r"^\s*", logical).group(0)
        out.extend(
            textwrap.wrap(
                logical.strip(),
                width=WIDTH,
                initial_indent=indent,
                subsequent_indent=indent,
                break_long_words=False,
                break_on_hyphens=False,
            )
        )
    return "\n".join(out)


# ----------------------------------------------------------------- anchors --

A1 = """**The two bases do not merely differ in budget. They act on different objects.** Matched at
κ ≈ 0.10, the two levies compress the cross-section unequally — Gini 0.222 against 0.125 — but the
more telling comparison is what each does to the variance of the log multiplier: the generator of
the process rather than its outcome. Write that multiplier, normalised by aggregate growth, as
*a*(η) — a different object from §2.1's wage *a*, with which it unhappily shares a letter — so the
quantity is Var[log *a*]. Unlevied, Var[log *a*] = 0.076542. Under the
**stock** levy at that budget it is **0.076536** — a change of six parts in a million, which is to
say none at all. Under the **flow** levy it is **0.051189**, a third lower. A levy on stock rescales
what a holder has and leaves the process that got them there exactly as it found it; a levy on flow
reaches into the multiplicative term itself. The stock base truncates the outcome, the flow base
damps the generator — and both register as a smaller Gini, which is why the distinction is invisible
in the statistic normally reported. An outcome measure records that the distribution was compressed.
It does not record whether the mechanism producing next period's distribution was touched."""

ED1_NEW = wrap(
    "**This contrast is not new, and the credit belongs precisely.** Bouchaud and Mézard (2000) "
    "carry a flow levy, a stock levy and the per-capita redistribution of each in a single wealth "
    "balance, and give the stationary Pareto exponent in closed form in all four coordinates. They "
    "write that exponent μ — a different object from §2.1's growth drift μ, with which it unhappily "
    "shares a letter, and the second such collision this paper has had to disclose. "
    "Their ranking is the one measured here, and they state it more strongly: income taxes *\"tend "
    "to reduce the inequalities of wealth (i.e., lead to an increase of μ), even more so if part of "
    "this tax is redistributed\"*, while *\"quite surprisingly, capital tax, if used simultaneously "
    "to income tax and not redistributed, leads to a decrease of μ\"*. Their stock levy can "
    "*reverse* the sign of the effect; the one measured here merely buys less compression per unit "
    "of budget. What this section adds is not the contrast but the pair of witnesses for it — κ, "
    "which says how much budget a base has, and Var[log *a*], which says whether the levy spent it "
    "on the outcome or on the generator — in a discrete process where the two can be matched and "
    "separated. §6 states what that leaves."
)

A2 = """The condensation result is standard in kinetic exchange (Chakrabarti, Chatterjee, Chakravarty and
the surrounding literature), where the effect of saving propensity, taxation and redistribution
on stationary wealth distributions has been examined from several directions. The contribution
here is not that redistribution opposes condensation — that is established — but that the
mechanisms sort by **observability of the base** rather than by rate or institutional form, and
that the budget through which they operate has a closed form (κ) rather than being a simulation
regularity — though the sorting is not a function of that budget alone (§3.1)."""

ED2_NEW = "\n\n".join(
    wrap(p)
    for p in [
        "The condensation result is standard in kinetic exchange (Chakrabarti, Chatterjee, "
        "Chakravarty and the surrounding literature), where the effect of saving propensity, "
        "taxation and redistribution on stationary wealth distributions has been examined from "
        "several directions. **Two results in that literature are prior to this paper's central "
        "contrast, and are cited here rather than restated.**",

        "**Bouchaud and Mézard (2000)** carry a flow levy, a stock levy and the per-capita "
        "redistribution of each in one wealth balance and give the stationary Pareto exponent in "
        "closed form in all four coordinates, together with the stock-versus-flow ranking (§3.1). "
        "The contrast between the two bases — in terms of what each does to the shape of the "
        "stationary distribution — is theirs, and the per-capita rebate fraction is a coordinate in "
        "their solution rather than an extension awaiting one.",

        "**Benhabib, Bisin and Zhu (2011)** supply three further results that bound what is left. "
        "Their Proposition 3 has the tail index rising in both the estate tax and the capital "
        "income tax, so the *nested* frontiers this paper reaches in §3.1 — by falsifying a sharper "
        "prediction of its own — were already visible in a different metric and a different model. "
        "Their Proposition 4 has tail inequality rising with a mean-preserving spread of the return "
        "process, which is the general form of §3.1's finding that the flow levy reaches the "
        "dispersion of the multiplier and the stock levy does not. And their §4.1 notes that an "
        "economy whose multiplier is bounded below one has a stationary distribution bounded above, "
        "with no power-law tail at all — a claim this paper does not make and does not need, but "
        "the first one any extension of §3.1 toward tail indices would meet.",

        "**What remains is narrower than the contrast, and is stated as such.** It is not that "
        "redistribution opposes condensation, and it is not that the two bases act differently on "
        "the shape of the distribution. It is that the mechanisms sort by **observability of the "
        "base** (§3.2) rather than by rate or institutional form; that the budget through which "
        "they operate has a closed form (κ) rather than being a simulation regularity, though the "
        "sorting is not a function of that budget alone (§3.1); and that a single sweep separates "
        "the two by measuring the generator and the outcome side by side. Three further differences "
        "are of construction rather than of claim, and none is offered as a result: the levy here "
        "is on the **realised gain only**, with no loss offset, so the multiplier is asymmetrically "
        "truncated rather than symmetrically contracted toward one; the two bases are compared at "
        "matched compressive **budget** rather than at matched rate; and the process is a discrete "
        "Kesten-type recursion with an explicit per-period budget identity rather than a "
        "continuous-time mean-field one.",
    ]
)

A3 = """   to within 7 % at every rate tabulated (§3.1)."""

ED3_NEW = (
    "   to within 7 % at every rate tabulated (§3.1). The stock-versus-flow contrast this result\n"
    "   sharpens is prior and is credited in §6; what is new is κ itself — the levy's budget,\n"
    "   separated from its mechanism — and the closed form for it."
)

A4 = """Bouchaud, J.-P., & Mézard, M. (2000). Wealth condensation in a simple model of economy.
*Physica A*, 282(3), 536–545. ✓"""

ED4_NEW = wrap(
    "Bouchaud, J.-P., & Mézard, M. (2000). Wealth condensation in a simple model of economy. "
    "*Physica A: Statistical Mechanics and its Applications*, 282(3–4), 536–545. "
    "`doi:10.1016/S0378-4371(00)00205-3` ✓⧗ *(issue and pagination checked against the Crossref "
    "record, 2026-08-17; an earlier draft gave the issue as 282(3). Text consulted: arXiv "
    "`cond-mat/0002374`, read in full. The quotations in §3.1 are attributed to that preprint and "
    "may not appear verbatim in the article of record. Consulted 2026-08-17 / published 2000.)*"
)

A5 = """Benhabib, J., Bisin, A., & Zhu, S. (2011). The distribution of wealth and fiscal policy in economies
with finitely lived agents. *Econometrica*, 79(1), 123–157. ✓ *(journal and volume
verified; page range to re-check)*"""

ED5_NEW = wrap(
    "Benhabib, J., Bisin, A., & Zhu, S. (2011). The distribution of wealth and fiscal policy in "
    "economies with finitely lived agents. *Econometrica*, 79(1), 123–157. "
    "`doi:10.3982/ECTA8416` ✓⧗ *(page range checked against the Crossref record, 2026-08-17, "
    "which resolves the flag carried by earlier drafts. Text consulted: NBER Working Paper 14730 "
    "full text, read in full; §6's characterisation of Propositions 3 and 4 and of §4.1 is taken "
    "from that version and the numbering may differ in the article of record. Consulted "
    "2026-08-17 / published 2011.)*"
)

A6 = """*Bibliographic details for the entries marked ✓ were verified against live sources on
2026-08-10; the remainder are standard works whose details are to be re-checked at submission per
`docs/papers/PREPRINT-CHECKLIST.md`.*"""

ED6_NEW = wrap(
    "*Bibliographic details for the entries marked ✓ were verified against live sources on "
    "2026-08-10. The two marked ✓⧗ were re-verified against their Crossref records on 2026-08-17 "
    "and name, in the entry, the pre-publication version actually read, per `REFERENCE-POLICY` §4. "
    "The remainder are standard works whose details are to be re-checked at submission per "
    "`docs/papers/PREPRINT-CHECKLIST.md`.*"
)

A7 = """Bouchaud, J.-P., & Mézard, M. (2000). Wealth condensation in a simple model of economy. *Physica
A*, 282(3), 536–545. ✓"""

ED7_NEW = """Bouchaud, J.-P., & Mézard, M. (2000). Wealth condensation in a simple model of economy. *Physica
A*, 282(3–4), 536–545. ✓"""


EDITS = [
    (P2, "ED1 §3.1  append the Bouchaud & Mézard credit", A1, A1 + "\n\n" + ED1_NEW),
    (P2, "ED2 §6    credit both works, state what remains", A2, ED2_NEW),
    (P2, "ED3 §1    contribution 2 points at §6", A3, ED3_NEW),
    (P2, "ED4 refs  B&M -> ✓⧗, issue 3–4, DOI", A4, ED4_NEW),
    (P2, "ED5 refs  BBZ -> ✓⧗, DOI, pagination resolved", A5, ED5_NEW),
    (P2, "ED6 refs  preamble mentions ✓⧗", A6, ED6_NEW),
    (P4, "ED7 refs  B&M issue 282(3) -> 282(3–4)  [Crossref]", A7, ED7_NEW),
]


def main():
    dry = "--dry" in sys.argv

    originals = {}
    for path in {p for p, *_ in EDITS}:
        with open(path, encoding="utf-8") as fh:
            originals[path] = fh.read()

    # ------------------------------------------------ idempotence guard ----
    # WHITESPACE-NORMALISED, and that is not a detail. The first cut of this
    # guard compared the raw sentinel against the raw file and reported
    # "sentinel present: False" immediately AFTER a successful apply -- because
    # wrap() had broken the sentence across a line and the substring no longer
    # existed. A guard that cannot see its own edit is not a guard: a re-run
    # would have sailed past it and appended the paragraph twice. Every
    # comparison against a hard-wrapped corpus normalises first (wt120's rule);
    # an idempotence check is a comparison against a hard-wrapped corpus.
    if norm_ws(IDEMPOTENCE_SENTINEL) in norm_ws(originals[P2]):
        print("REFUSING: paper-II.md already contains the wt123 sentinel.")
        print(f"  sentinel: {IDEMPOTENCE_SENTINEL!r}")
        print("  This patch has already been applied. Nothing written.")
        return 2

    # ------------------------------- assert EVERY anchor before writing ----
    print("ANCHOR CHECK (all must be exactly 1 before anything is written)")
    bad = 0
    for path, label, old, _new in EDITS:
        n = originals[path].count(old)
        flag = "ok" if n == 1 else "*** MISCOUNT ***"
        if n != 1:
            bad += 1
        print(f"  {n:3d}  {flag:16s} {label}   [{os.path.basename(path)}]")
    if bad:
        print(f"\nREFUSING: {bad} anchor(s) did not occur exactly once. Nothing written.")
        return 2
    print("  all anchors unique.\n")

    # ------------------------------------- width check on inserted text ----
    print("WIDTH CHECK on inserted text (characters, not bytes; limit 100)")
    over = 0
    for path, label, old, new in EDITS:
        inserted = [ln for ln in new.split("\n") if ln not in old.split("\n")]
        worst = max((len(ln) for ln in inserted), default=0)
        mark = "ok" if worst <= WIDTH else "*** OVER ***"
        if worst > WIDTH:
            over += 1
            for ln in inserted:
                if len(ln) > WIDTH:
                    print(f"      {len(ln)}: {ln}")
        print(f"  {worst:3d}  {mark:12s} {label}")
    if over:
        print(f"\nREFUSING: {over} edit(s) exceed {WIDTH} characters. Nothing written.")
        return 2
    print("  all inserted lines within width.\n")

    # ---------------------------------------------- GLYPH CHECK (wt67) ----
    # paper-II.md uses U+03BC GREEK SMALL LETTER MU for the growth drift.
    # SCOUT-001 transcribed the Pareto exponent as U+00B5 MICRO SIGN, which
    # RENDERS IDENTICALLY and is a different codepoint -- so a grep for one
    # silently misses the other. No manuscript carries U+00B5 today; this
    # patch is not going to be the first. (U+00B5 is the SI prefix character;
    # LaTeX \mu maps to U+03BC, which is what the manuscripts already use.)
    MICRO = "µ"
    print("GLYPH CHECK: no U+00B5 MICRO SIGN may enter a manuscript")
    glyph_bad = 0
    for path, label, old, new in EDITS:
        n = new.count(MICRO)
        if n:
            glyph_bad += 1
            print(f"  *** {n} U+00B5 in {label} -- use U+03BC ***")
    if glyph_bad:
        print("\nREFUSING: micro sign would enter a manuscript. Nothing written.")
        return 2
    print("  clean (U+03BC only).\n")

    # ------------------------------------------------------- apply ---------
    updated = dict(originals)
    for path, label, old, new in EDITS:
        updated[path] = updated[path].replace(old, new, 1)

    if dry:
        print("--dry: showing what WOULD change, writing nothing.\n")
        for path, label, old, new in EDITS:
            print("=" * 74)
            print(label)
            print("-" * 74)
            print("OLD:")
            print(old)
            print("\nNEW:")
            print(new)
            print()
        for path in updated:
            print(f"{os.path.basename(path)}: "
                  f"{len(originals[path])} -> {len(updated[path])} chars")
        return 0

    for path in updated:
        bak = f"{path}.bak-{TAG}"
        shutil.copy2(path, bak)
        print(f"backup: {os.path.relpath(bak, REPO)}")
    for path, content in updated.items():
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(content)
        print(f"wrote : {os.path.relpath(path, REPO)}  "
              f"({len(originals[path])} -> {len(content)} chars)")

    # ------------------------------------------------ post-write proof ----
    print("\nPOST-WRITE VERIFICATION")
    p2 = updated[P2]
    body = p2.split("## References")[0]
    for nm in ["Bouchaud", "Mézard", "Benhabib", "Bisin", "Zhu"]:
        print(f"  body mentions {nm:10s}: {len(re.findall(re.escape(nm), body))}")
    print(f"  ✓⧗ marks in paper-II references: {p2.split('## References')[1].count('✓⧗')}")
    present = norm_ws(IDEMPOTENCE_SENTINEL) in norm_ws(p2)
    print(f"  sentinel present (normalised): {present}")
    if not present:
        print("  *** the guard cannot see its own edit -- a re-run would double-apply ***")
        return 2
    print("\nAPPLIED. Now: pytest, board.py --check, gate.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
