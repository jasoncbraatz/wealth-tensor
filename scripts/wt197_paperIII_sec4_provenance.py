#!/usr/bin/env python3
"""wt197 — Pass B repair of SHIP-LIST SL-7: paper-III §11's scope sentence, widened to
what the paper actually reports, with the §4 provenance the front matter promises.

The front matter claims EVERY computational result is produced by committed code in the
repository named in §11; §11 itself claimed only §A.2 and §§2-3.  §§4.1-4.9 carried no
Regenerate bullet at all, and that is where §4.4's tier table, §4.5's ladder table, the
66.2% robustness figure and §4.9's crossing figures live.  THE CODE EXISTS AND IS
COMMITTED -- what was missing was the signposting, which is why this scored S2 and not S1.

Every figure quoted in the new bullets was RE-RUN at wealthTensor-104 before it was
written down.  Where a figure is not printed by any command in the repository, the bullet
SAYS SO, copying §11's own existing honest form (the §5.3 bullet) rather than inventing a
new disclosure shape.

Idempotent: NO-OP on a second run, exit 0.  Exit 2 if a site matches neither state.
"""
import sys, pathlib

P = pathlib.Path.home() / "repos/wealth-tensor/docs/papers/paper-III-dual-tensor/paper-III.md"

SCOPE_OLD = ("Every simulation result in §A.2 and §§2–3 is produced by open code. "
             "The severe test in §5 uses only\npublic data.")
SCOPE_NEW = ("Every simulation result in §A.2, §§2–3 and §4 is produced by open code, and the bullets below\n"
             "name the command that prints it. Where a figure is printed by no command here, the bullet says\n"
             "so. The severe test in §5 uses only public data.")

ANCHOR = "- **Regenerate §A.2.3:** `python3 scripts/wt002_lambda_report.py`\n"

BULLETS = (
    "- **Regenerate §4.2:** `python3 scripts/wt084_identification_closed_form.py` — the two coefficient\n"
    "  equations, the mirror agreeing to **2 × 10⁻¹⁶** where the rival map fails by fourteen orders of\n"
    "  magnitude, and §4.2's one-parameter family: the factor of **1.67** in the unobserved physical\n"
    "  scale, the implied φ at each assumed scale, and the **51%** opening gap the φ = 0 end requires.\n"
    "  The **31.7%** share is printed by no command here: it is that same family restricted to opening\n"
    "  gaps within ten per cent, and the restriction is applied in §4.2's prose rather than in the script.\n"
    "- **Regenerate §4.4 and §4.5:** `python3 scripts/wt083_tier_ladder_antialignment.py` prints §4.4's\n"
    "  four-tier ladder at the calibration — φ, δ, (1 − φ)δ and **R** both simulated and in closed form —\n"
    "  with both Kendall τ and the log-decomposition §4.4 reads the step direction from. `python3\n"
    "  scripts/wt088_disclosed_ladder.py` prints §4.4's crossing rate **δ₃\\* = 0.007895**, the asserted\n"
    "  rectangle's admissible shares, and §4.5's ladder statistics under both draws — the lag ordering\n"
    "  and the magnitude measure, with the durability ordering imposed and dropped, at each ladder count\n"
    "  §4.5 quotes. The tier table's two measured-rate columns are printed by neither: they are §4.4's\n"
    "  own R = (1 − φ)δ/(α − δ) evaluated at §5.4's α̂ and at the adverse cut, over the φ and δ the first\n"
    "  columns carry.\n"
    "- **Regenerate §4.6, §4.7 and §4.8:** `python3 scripts/wt085_returns_conditioning.py` is §4.6's run:\n"
    "  returns break the root swap, and the scale continuum survives them because a return is a ratio.\n"
    "  `python3 scripts/wt086_exponent_robustness.py` re-fits §4.7's two exponents across nine regimes,\n"
    "  which is why §4.7 quotes neither as a constant of the problem. `python3\n"
    "  scripts/wt087_goodwill_gradient.py` prints §4.7's δ-sweep at a fixed root gap — the volatility\n"
    "  exponent from **−0.386** at a property-like rate to **+0.163** at a goodwill-like one — and §4.8's\n"
    "  arithmetic, the level moving by **6.81×** as (α − δ)^−0.700.\n"
    "- **Regenerate §4.9:** `python3 scripts/wt090_age_dependent_alpha.py` prints the constant-hazard\n"
    "  pole at **0.435** per year, the overstatement column across the disclosed lives — **0.55%** at a\n"
    "  forty-year life to **43.87%** at a three-year one — α_eff across that same rectangle, and δ₃\\* at\n"
    "  both shapes, **0.00755** published and **0.00754** measured, beside the **0.00789** §4.4's closed\n"
    "  form returns at the calibration.\n"
)

EDITS = [("SL-7a · scope sentence", SCOPE_OLD, SCOPE_NEW),
         ("SL-7b · Regenerate §4 bullets", ANCHOR, ANCHOR + BULLETS)]

def main():
    text = P.read_text(encoding="utf-8")
    orig, rc = text, 0
    for tag, old, new in EDITS:
        if new in text and old != new:
            print(f"{tag}: NO-OP (already repaired)"); continue
        if old in text:
            if text.count(old) != 1:
                print(f"{tag}: old text is not unique ({text.count(old)}x)"); return 2
            text = text.replace(old, new); print(f"{tag}: APPLIED")
        else:
            print(f"{tag}: NOT FOUND — neither old nor new text present"); rc = 2
    if rc: return rc
    if text != orig:
        P.write_text(text, encoding="utf-8"); print("wrote", P.name)
    else:
        print("no write needed")
    return 0

sys.exit(main())
