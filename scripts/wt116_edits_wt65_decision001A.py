#!/usr/bin/env python3
"""wealthTensor-65 · DECISION-001 option A, applied.

Jason ticked **A** on 2026-08-17: demote kappa from *mechanism* to *budget*, add the sentence
saying what the paper's own numbers already show, and fold in `II-2` and `II-3`, which
`REVIEW-005` §2 left unrepaired precisely because they are edits of whichever option is ticked.
The title stays (B is not taken) and Road One stays available (C is not foreclosed) — Jason's
sequencing ruling: run the literature search first and price C with information.

WHAT THE CENSUS CHANGED ABOUT THE JOB (`scripts/wt115_kappa_census.py`)
-----------------------------------------------------------------------
`DECISION-001` prices A as *"5 places, one file"*. Swept across the manuscripts, the tests, the
scripts and the source, kappa-as-mechanism has **six** sites, and the sixth is not in a
manuscript: `tests/test_redistribution.py`'s docstring opens *"kappa ... is the mechanism"* and
closes *"That gap, not the rate, is the mechanism."* Nothing asserts a docstring. Left alone, the
paper would retract a claim that its own test suite goes on making — the abstract-versus-body
defect this estate keeps finding, one file out. The census also cleared five false positives
(paper-III's z-transform, REG-009's bin rule, handoff_gate's layout note, and `wt112`'s
historical anchors, which are a RECORD of an edit and are not rewritten).

WHAT THE CODE CHANGED ABOUT `II-3` (`scripts/wt115_rho_zero.py`)
-----------------------------------------------------------------
`REVIEW-005` §2 says rho = 0 *"sets the base and kappa to EXACTLY ZERO: the levied path IS the
unlevied path."* The first half is false. `redistribution.py:131` is

    recognised_flow += self.rho * gain + self.wage

so at rho = 0 the flow base is the accrued **wage**, not nothing: measured kappa = 0.000565 over
1200 assessments that really fire. The second half is true and is stronger than the paper claims
— `np.array_equal` on the two wealth vectors is **True**, max difference **0.0** — because
`self.wage` is a scalar identical for every agent, so the levy is a uniform assessment with a
uniform per-capita rebate, which is the identity on the wealth vector. The paper says
*"statistically indistinguishable"*; the truth is exact, and structural. Repaired upward.

Every anchor is asserted unique before any write; `.bak-wt65-decA` on every touched file;
`--dry` writes `*.wt65-dryrun` siblings for diffing in the cloud container first.
"""
from __future__ import annotations

import pathlib
import shutil
import sys

DRY = "--dry" in sys.argv
ROOT = pathlib.Path(__file__).resolve().parents[1]

PAPER = "docs/papers/paper-II-redistribution/paper-II.md"
TEST = "tests/test_redistribution.py"

EDITS = [
    # ------------------------------------------------ abstract: kappa demotion + II-2 + II-3
    # ONE anchor spanning the whole abstract, deliberately. The first draft patched the two
    # sentences separately and left two RAGGED lines where the replacement's last line collided
    # with the surviving text -- `-63`'s rule (extend anchors to sentence boundaries) in its
    # cheapest form, caught by diffing the dry-run in the cloud container before anything landed.
    # Rewrapping the paragraph as a unit is the only way to guarantee the wrap.
    (PAPER, "abstract · kappa demoted (A), II-2's 'in compression'->'in κ', II-3 exact + rewrap",
     "inequality below unity. First, the **base sets a ceiling the rate cannot cross**: at a matched\n"
     "rate the two bases differ by roughly an order of magnitude in compression. The mechanism is κ,\n"
     "the share of aggregate wealth moved per assessment, for which the flow base admits a closed\n"
     "form. The stronger prediction it was built to test — that a flow levy fails to oppose the\n"
     "multiplicative term *regardless of rate* — is **false, and this paper's own sweep falsified\n"
     "it**: the frontiers are **nested**, stock 0.000 against flow 0.125. Second, the surviving claim\n"
     "is narrower and better: the decisive quantity is **realisation** — the share of a period's gain\n"
     "the base can see. At zero realisation a **100 % levy on flow is indistinguishable from no levy\n"
     "at all** (Gini 0.994 and top decile 1.000 in both). Third, periodicity and threshold are trim,",

     "inequality below unity. First, the **base sets a ceiling the rate cannot cross**: at a matched\n"
     "rate the two bases differ by roughly an order of magnitude in κ, the levy's compressive budget,\n"
     "for which the flow base admits a closed form. The stronger prediction it was built to test —\n"
     "that a flow levy fails to oppose the multiplicative term *regardless of rate* — is **false, and\n"
     "this paper's own sweep falsified it**: the frontiers are **nested**, stock 0.000 against flow\n"
     "0.125. Second, the surviving claim is narrower and better: the decisive quantity is\n"
     "**realisation** — the share of a period's gain the base can see. At zero realisation the flow\n"
     "base is uniform, so a **100 % levy on flow leaves wealth exactly unchanged** (Gini 0.994 and\n"
     "top decile 1.000 in both). Third, periodicity and threshold are trim,",),

    # ---------------------------------------------------------------------- §1 contribution 2
    (PAPER, "§1 c2 · kappa is the budget, not the mechanism",
     "2. The result that the **base caps the reachable region and the rate only moves you within it**,\n"
     "   with the mechanism identified as κ and a closed form for the flow base's κ that the\n"
     "   simulation reproduces to within 7 % at every rate tabulated (§3.1).",

     "2. The result that the **base caps the reachable region and the rate only moves you within it**,\n"
     "   with κ — the levy's compressive *budget*, not its mechanism — separating the bases by an\n"
     "   order of magnitude, and a closed form for the flow base's κ that the simulation reproduces\n"
     "   to within 7 % at every rate tabulated (§3.1).",),

    # ---------------------------------------------------------------------- §1 contribution 3
    (PAPER, "§1 c3 · the rho=0 limit is exact, and the base is uniform rather than absent",
     "3. The identification of **realisation as the decisive quantity**, including the limiting result\n"
     "   that a confiscatory levy on flow, at zero realisation, is indistinguishable from no levy\n"
     "   (§3.2). This is a statement about what a base can *observe*, not about how hard it squeezes.",

     "3. The identification of **realisation as the decisive quantity**, including the limiting result\n"
     "   that a confiscatory levy on flow, at zero realisation, leaves the wealth vector exactly\n"
     "   unchanged — its base is uniform, not absent (§3.2). This is a statement about what a base\n"
     "   can *observe*, not about how hard it squeezes.",),

    # ------------------------------------------------------------------------------- §2.4
    (PAPER, "§2.4 · 'the quantity through which the base does its work' retracted",
     "aggregate wealth actually moved per assessment — the levy's *compressive budget*, and the\n"
     "quantity through which the base does its work.",

     "aggregate wealth actually moved per assessment — the levy's *compressive budget*. It is a\n"
     "budget and not a mechanism: §3.1 matches two levies at κ and finds them compressing\n"
     "unequally, and §3.3 removes a quarter of κ at no measurable cost.",),

    # --------------------------------------------------------------------------- §3.1 gloss
    (PAPER, "§3.1 gloss · 'the mechanism is visible' -> the budget is",
     "tested. The mechanism is visible in the third column and is not a fitted relationship:",
     "tested. The budget is visible in the third column and is not a fitted relationship:",),

    # ------------------------------------------- §3.1 · the sentence DECISION-001 option A adds
    (PAPER, "§3.1 · NEW — kappa is necessary and not sufficient, with both witnesses",
     "in the statistic normally reported. An outcome measure records that the distribution was compressed.\n"
     "It does not record whether the mechanism producing next period's distribution was touched.",

     "in the statistic normally reported. An outcome measure records that the distribution was compressed.\n"
     "It does not record whether the mechanism producing next period's distribution was touched.\n"
     "\n"
     "**κ is necessary and it is not sufficient, and this paper reports both witnesses.** The\n"
     "paragraph above matches the two levies at κ ≈ 0.10 and finds them compressing unequally, 0.222\n"
     "against 0.125. §3.3 supplies the converse from the other side: a threshold at 0.25× the mean\n"
     "removes a quarter of κ at no measurable cost in compression, 0.444 against 0.443. κ can hold\n"
     "while the outcome moves and move while the outcome holds, so **no function of κ alone\n"
     "reproduces this section's table.** κ is what a base makes available to spend — which is why the\n"
     "bases sort, and why the closed form is worth having — but what the spending buys is fixed by\n"
     "the object the levy acts on, which is the distinction the preceding paragraph draws.",),

    # -------------------------------------------------------------------------------- §3.2
    (PAPER, "§3.2 · II-3 primary site — exact, structural, and the base is the wage",
     'At ρ = 0 — the holder whose gains accrue but are never realised — a **100 % levy on flow is\n'
     'statistically indistinguishable from no levy at all**: Gini 0.994 against 0.994, top decile 1.000\n'
     'in both. That is the true "regardless of rate" result, and note what kind of statement it is. It',

     'At ρ = 0 — the holder whose gains accrue but are never realised — a **100 % levy on flow leaves\n'
     'the wealth vector exactly unchanged**: Gini 0.994 against 0.994, top decile 1.000 in both, and\n'
     'the two paths agree agent by agent rather than merely on the summary statistics. The identity is\n'
     'structural, and saying so is stronger than calling it a near-match. The levy is still assessed —\n'
     'at ρ = 0 the flow base is not empty but is the accrued **wage**, and the assessments do fire —\n'
     'but the wage is identical for every agent, so the levy takes the same amount from each and\n'
     'returns it per capita. A uniform assessment with a uniform rebate is the identity on the wealth\n'
     'vector. What ρ = 0 removes is not the levy but the **dispersion in its base**.\n'
     '\n'
     'That is the true "regardless of rate" result, and note what kind of statement it is. It',),

    # --------------------------------------------------------------------------------- §6
    (PAPER, "§6 · the closed form belongs to the budget, not to the sorting",
     "mechanisms sort by **observability of the base** rather than by rate or institutional form, and\n"
     "that this sorting has a closed-form mechanism (κ) rather than being a simulation regularity.",

     "mechanisms sort by **observability of the base** rather than by rate or institutional form, and\n"
     "that the budget through which they operate has a closed form (κ) rather than being a simulation\n"
     "regularity — though the sorting is not a function of that budget alone (§3.1).",),

    # ------------------------------------------------------- the SIXTH site, in an instrument
    (TEST, "tests · the docstring that asserted kappa-as-mechanism, which nothing checked",
     '    """kappa -- the share of aggregate wealth moved per assessment -- is the mechanism.\n',
     '    """kappa -- the share of aggregate wealth moved per assessment -- is the levy\'s BUDGET.\n'
     '\n'
     '    NOT its mechanism, and this docstring said otherwise until `-65`. DECISION-001 prices\n'
     '    option A as "demote kappa from mechanism to budget in FIVE places" and all five are in\n'
     '    paper-II.md; this file was the sixth. Nothing asserts a docstring, so the retraction in\n'
     '    the manuscript would have left the test suite still making the claim -- the\n'
     '    abstract-versus-body defect one file out. What refutes it is the paper\'s own table: two\n'
     '    levies matched at kappa ~ 0.10 compress to Gini 0.222 and 0.125, and a threshold at 0.25x\n'
     '    the mean removes a quarter of kappa at no measurable cost. kappa is necessary, not\n'
     '    sufficient. The assertions below were always budget facts; only the prose overreached.\n',),

    (TEST, "tests · the docstring's closing line, same claim",
     "    flow base here, and it is still not close. That gap, not the rate, is the mechanism.",
     "    flow base here, and it is still not close. That gap, not the rate, is what the base caps.",),
]


def main() -> int:
    src: dict[str, str] = {}
    for rel, label, old, new in EDITS:
        p = ROOT / rel
        if rel not in src:
            src[rel] = p.read_text(encoding="utf-8")
        n = src[rel].count(old)
        if n != 1:
            print(f"ABORT · anchor not unique ({n}x) · {rel} · {label}")
            return 1
        src[rel] = src[rel].replace(old, new, 1)
        print(f"ok  {label}")

    for rel, text in src.items():
        p = ROOT / rel
        if DRY:
            out = p.with_suffix(p.suffix + ".wt65-dryrun")
            out.write_text(text, encoding="utf-8")
            print(f"DRY  wrote {out}")
        else:
            shutil.copy2(p, p.with_suffix(p.suffix + ".bak-wt65-decA"))
            p.write_text(text, encoding="utf-8")
            print(f"WROTE {rel}  (.bak-wt65-decA kept)")

    # `-64`: awk 'length>100' before and after, and it counts BYTES -- measure characters.
    print()
    for rel, text in src.items():
        before = (ROOT / rel).with_suffix((ROOT / rel).suffix + ".bak-wt65-decA")
        base = before.read_text(encoding="utf-8") if before.exists() else ""
        b = sum(1 for l in base.split("\n") if len(l) > 100)
        a = sum(1 for l in text.split("\n") if len(l) > 100)
        widest = max(len(l) for l in text.split("\n"))
        print(f"  lines>100 chars  {rel}: {b} -> {a}   (widest now {widest})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
