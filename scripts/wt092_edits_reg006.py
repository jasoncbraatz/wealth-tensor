#!/usr/bin/env python3
"""REG-006's manuscript amendments. patchkit only; anchors copied out of the real text.

Registered in REG-006 §7: two of these are owed regardless of any ladder (a wrong ASC
citation and a scope error), and ladder C's return makes the third a correction of
printed numbers rather than a taste call. Structure delta: NONE -- no heading, no rule.
"""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from patchkit import apply_edits

P = str(pathlib.Path(__file__).resolve().parent / "paper-III.md")

CONCESSION_OLD = """**The mechanical reading has to be excluded before the economic one is available, and §9 already
named it:** ASC 360 requires the recoverability screen on long-lived assets *before* the goodwill
test, so one triggering event can produce two charges in one quarter by the ordering of the
standards rather than by the coupling of the assets. This design cannot separate those. What it
establishes is the magnitude of the departure from diagonality, which was previously unmeasured, and
that §5's treatment of 695 events as independent draws overstates the information they carry."""

CONCESSION_NEW = """**The mechanical reading has to be excluded before the economic one is available, §9 already
named it, and it is two readings rather than one.** The ordering is imposed by ASC 350-20-35-31,
which requires that any other asset or asset group of a reporting unit be tested before goodwill,
and by ASC 350-20-35-32, which extends that requirement to every asset tested rather than only to
those within ASC 360-10 — so it governs the intangible cells above as well as the property one. On
one channel the rule creates joint *testing*: ASC 350-20-35-3C(f) names the testing for
recoverability of a significant asset group as an event requiring an interim goodwill test, so a
single trigger fires two tests. On the other it suppresses joint *recognition*: the other charge is
recognised first and reduces the reporting unit's carrying amount, and under ASC 350-20-35-2 and
35-8 the goodwill charge is the excess of that carrying amount over fair value, so the prior charge
is subtracted from it one for one until zero or the goodwill cap binds. **Under the ordering alone
the two charges are substitutes at the margin, and this sample shows them as complements.** Signing
the net requires the two charges at the reporting-unit level, which US filings do not disclose;
`REG-006` registered an entity-level test of the suppressing channel and it returned no consistent
sign in either sector. What this design establishes is the magnitude of the departure from
diagonality, which was previously unmeasured, and that §5's treatment of the events as independent
draws overstates the information they carry."""

CELLS_OLD = """The pairwise cells put the
strongest coupling on goodwill with indefinite-lived intangibles in retail (5.83×) and on goodwill
with finite-lived intangibles in computer services (2.22×), and property with goodwill runs at
4.35× and 4.03× — the one cell that replicates its magnitude across two sectors."""

CELLS_NEW = """The pairwise cells put the
strongest coupling on goodwill with indefinite-lived intangibles in retail (5.83×) and on goodwill
with finite-lived intangibles in computer services (2.22×), and it is these two
intangible-with-goodwill cells that replicate across both sectors — 5.83× and 2.34×, 3.33× and
2.22×, all four surviving Holm correction. Property with goodwill runs at 4.35× and 4.03× on a
tier whose tag list omitted the element most filers use for it; `REG-006` repairs the omission and
re-derives that cell at **3.99×** and **2.17×**, the second no longer significant, so its
cross-sector agreement does not survive the repair. The headline does: **4.01× and 2.10×**
repaired, against 4.01× and 2.01× from the same crawl unrepaired."""

LIM9_OLD = """   state. What the design cannot do is separate an economic coupling from the sequencing the
   standards impose, and §5.4 says so where the number is. It is registered before its instrument is coded, or it
   is not run."""

LIM9_NEW = """   state. What the design cannot do is separate an economic coupling from the sequencing the
   standards impose — though that sequencing, imposed by ASC 350-20-35-31 and extended to every
   asset class by 35-32, is itself two channels of opposite sign, one creating joint testing and
   one suppressing joint recognition, and §5.4 says so where the number is. It is registered
   before its instrument is coded, or it is not run."""

LEDGER_OLD = """| **The framework's guards can fail** | audit of the guards themselves | a guard that could not fail passing silently | **six found and retired**, before publication, recorded in `METHOD-001` |"""

LEDGER_NEW = """| **The framework's guards can fail** | audit of the guards themselves | a guard that could not fail passing silently | **six found and retired**, before publication, recorded in `METHOD-001` |
| **The departure from diagonality is not an artefact of tier 0's tag list** | §5.4's permutation re-derived with the omitted element restored, both arms on one crawl | the lift moving with the tag list, which would make it a property of the instrument | **4.01× → 4.01×** and **2.01× → 2.10×**; every cell not involving tier 0 identical to two decimals |
| **Testing another asset first REDUCES the goodwill charge** | the single-step measurement run against a published worked example | the sequenced and goodwill-first branches agreeing, which would make the ordering inert | a \\$850 prior charge converts a \\$700 goodwill impairment to **\\$0**; the offset is one-for-one inside the region |
| **The suppressing channel is not visible in entity-level filings** | censored slope of the goodwill charge on the other charge, by sector and by ASU 2017-04 regime, with a placebo date | a consistent negative slope, or a regime contrast the placebo could not reproduce | **failed as registered** — no consistent sign, and the placebo moved further than the true date |"""

if __name__ == "__main__":
    apply_edits([
        (P, CONCESSION_OLD, CONCESSION_NEW, "§5.4 · the concession: ASC 350-20-35-31, its scope, and its two signs"),
        (P, CELLS_OLD, CELLS_NEW, "§5.4 · the pairwise cells corrected for tier 0"),
        (P, LIM9_OLD, LIM9_NEW, "Limitation 9 · the sequencing is two channels"),
        (P, LEDGER_OLD, LEDGER_NEW, "§7 · three ledger rows"),
    ], expect_structure={})
