#!/usr/bin/env python3
"""wealthTensor-20 — close F11 against the CFR text in force."""
import sys

sys.path.insert(0, "scripts")
from patchkit import apply_edits

RESULT = "docs/preregistration/RESULT-REG-007.md"

apply_edits([
    (
        RESULT,
        """**F11 · THE S-K CITATION — still unverified, and still flagged.** The *Financial Reporting
Manual* §9510.2 cites S-K **303(a)(3)(ii)**, pre-Release-33-10890 numbering. Nothing in this
result prints an S-K citation, so nothing turns on it; it carries forward.""",
        """**F11 · THE S-K CITATION — verified and closed, `wealthTensor-20`.** The *Financial Reporting
Manual* §9510.2 cites S-K **303(a)(3)(ii)**. That designation **no longer exists.** Release
33-10890 (Nov 2020) restructured Item 303 so that paragraph (a) is the Objective and carries no
numbered subdivisions at all; the "known trends or uncertainties" requirement §9510.2 is reaching
for now sits at **17 CFR 229.303(b)(2)(ii)** — "Describe any known trends or uncertainties that
have had or that are reasonably likely to have a material favorable or unfavorable impact on net
sales or revenues or income from continuing operations" — with the liquidity twin at (b)(1)(i).
Checked against the eCFR text in force, not against a practitioner reproduction.

The FRM is not so much wrong as **frozen**: Topic 9 still carries "Last updated: December 31,
2009", eleven years before the amendment it has not absorbed. That is a caution about the manual
generally, not about this one citation — REG-007 §1 leans on §9510.1–9510.3 for the proposition
that the no-charge case is MD&A-driven, and that proposition survives (the requirement moved, it
did not disappear), but any *numbering* taken from the FRM is presumptively stale.

Nothing in this result or in the manuscript prints an S-K paragraph citation. If one ever does it
cites **303(b)(2)(ii)** and does not inherit the FRM's numbering.""",
        "RESULT-REG-007 F11 · closed against the eCFR",
    ),
])
print("\nOK — F11 closed.")
