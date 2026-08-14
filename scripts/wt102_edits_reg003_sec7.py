"""T1 · `REG-003` §7 forbids rounding α̂ to "the recognition rate." Six sites did.

THE REGISTERED CONSTRAINT
-------------------------
`docs/preregistration/REG-003-p3-recognition-rate-and-off-diagonal.md` §7:

    **α̂ is the recognition rate of the quantity PRE-002's instrument identifies**, under
    PRE-002's onset bridge. It is not "the" recognition rate of US GAAP, and **no sentence
    anywhere may round it to that.**

The registration is public. An abstract that rounds it, checked against a registration
that says no sentence anywhere may, is the single most quotable object in the repository
(`SCOUT-001` §1.3). The repair is four sentences of work and it buys back the paper's one
unusual credibility asset.

SIX SITES, NOT THE FIVE THE SCOUTING REPORT NAMED
--------------------------------------------------
`SCOUT-001` T1 tabulates five rounding sites -- the abstract (67), §4.4 (614), §4.9 (931),
the §7 ledger (1574), §9 limitation 4 (1747) -- and grades §5.4 (1369-1397) as complying
**in full**, because the paragraph names the instrument, both registered biases and the
adverse cut. The paragraph does. **Its lead sentence does not:**

    **The recognition rate is 0.41 per year, and the calibration was low by an order of
    magnitude.**

That is a sentence, it rounds, and §7 governs sentences. The report graded a paragraph
against a constraint written at sentence resolution, and the bolded lead is the one line
in §5.4 a skimming referee reads. **This is the `-40` tell one turn further on**: a
qualification that exists in the right paragraph and does not travel had *already* been
named as the defect's characteristic shape, and the report that named it applied its own
lesson at paragraph granularity. So the guard below asserts an ABSENCE over the whole
document rather than six presences -- presences are what a short list already satisfies
(the `-101`/TERM-001 rule, which is here for the second time and now has two victims).

WHY THE LEGAL USES SURVIVE UNTOUCHED
------------------------------------
"the recognition rate" is also the correct English for **the model's α** -- an unmeasured
structural parameter -- and the manuscript uses it that way at seven sites (64, 66, 521,
598, 612, 614's first clause, 1012). §7 does not govern those: they round nothing, because
they attach the phrase to no estimate. The defect is exclusively the phrase **predicated of
the measurement**, and that is what `tests/test_reg003_sec7_rounding.py` tests: a sentence
is a violation when it carries a measurement of α̂ *and* no qualifier. A guard that banned
the phrase outright would fail every legal site and force the paper into vagueness, which
is the failure mode `defensive_count.py`'s own docstring warns about in its lexicon.

TWO REPLACEMENT PHRASES, AND WHY NOT ONE
-----------------------------------------
* **"peak-to-charge recognition rate"** where the sentence is short and the number is the
  point (abstract, §5.4's lead, the §7 ledger row). It is PRE-002's own registered name for
  the interval -- `PRE-002-wt026-peak-to-charge.md` -- so the qualifier is not new prose,
  it is the instrument's title.
* **"the recognition rate PRE-002's instrument identifies"** at first use in a section that
  goes on to reason about it (§4.4, §4.9), which is §7's own wording. Bare α̂ thereafter.

Both are noun-phrase REPLACEMENTS. Charter §2's illegal move is ABSORB -- pasting the
objection in as a caveat -- and nothing below adds a hedge: the abstract gains four words
of fact ("on both known biases' inflating side"), §9 limitation 4 trades a false claim for
a true narrower one, and `defensive_count.py`'s lexicon matches none of it.

§9 LIMITATION 4 IS THE ONE THAT IS NOT A RENAME
------------------------------------------------
It currently reads *"α is no longer in that list"* -- a claim that the model's α has been
measured. It has not been. What was measured is the quantity PRE-002's instrument dates,
and the step from one to the other is a bridge in exactly §6.2's sense: *"a quantity in the
model was matched to a quantity in the world that shares its name and not its meaning."*
Writing that down is not a new concession. It is **§6.2's own discipline applied to §5.4's
own number**, in the section where the paper lists what it does not know, and it converts
the manuscript's most obvious internal inconsistency into a demonstration that the
discipline is live rather than retrospective.
"""
from __future__ import annotations

import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from patchkit import apply_edits  # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parents[1]
PAPER = ROOT / "docs/papers/paper-III-dual-tensor/paper-III.md"

#: PRE-002's registered name for the interval the instrument dates. Assembled once, so
#: there is no place to type either replacement that a later rename does not reach.
INSTRUMENT_ADJ = "peak-to-charge"

#: §7's own wording, for the sections that go on to reason about the number.
IDENTIFIED_BY = "PRE-002's instrument identifies"

SHORT = f"the {INSTRUMENT_ADJ} recognition rate"
LONG = f"the recognition rate {IDENTIFIED_BY}"


#: Every anchor below is free of internal newlines -- patchkit's WT-058 rule, because the
#: only anchors that have ever missed in this project missed on a line break. Where a
#: replacement is longer than the line it lands in, the NEW text carries the re-wrap.
EDITS = [
    # ---- 1 · the abstract. The site the forum bench finds. -----------------------------
    (PAPER,
     "establish it: **the recognition rate is",
     f"establish it: **the {INSTRUMENT_ADJ}",
     "abstract · noun phrase"),
    (PAPER,
     "0.41 per year against a calibration of 0.05**, so the",
     "recognition rate is 0.41 per year against a calibration of 0.05, on both known"
     " biases' inflating\nside**, so the",
     "abstract · REG-003 §3.3's R1 sentence, in the same sentence as the number"),

    # ---- 2 · §4.4, first use in the section that reasons about it ----------------------
    (PAPER,
     "On the registered sample the recognition rate is **α̂ = 0.408 per year**, 95% interval",
     f"On the registered sample {LONG} is\n**α̂ = 0.408 per year**, 95% interval",
     "§4.4 · first use qualified"),

    # ---- 3 · §4.9 ----------------------------------------------------------------------
    (PAPER,
     "§5.4 measures the recognition rate and, in the same fit, rejects the shape the model assumes:",
     f"§5.4 measures {LONG} and, in the same fit,\nrejects the shape the model assumes:",
     "§4.9 · first use qualified"),

    # ---- 4 · §5.4's lead. The site SCOUT-001 graded compliant. --------------------------
    (PAPER,
     "**The recognition rate is 0.41 per year, and the calibration was low by an order of magnitude.**",
     f"**{SHORT.capitalize()} is 0.41 per year, and the calibration was low by an order\n"
     "of magnitude.**",
     "§5.4 · the bolded lead the paragraph beneath already qualifies"),

    # ---- 5 · the §7 survivals ledger ---------------------------------------------------
    (PAPER,
     "| **The recognition rate is an order of magnitude above the calibration** |",
     f"| **{SHORT.capitalize()} is an order of magnitude above the calibration** |",
     "§7 ledger · row label"),

    # ---- 6 · §9 limitation 4. Not a rename: a false claim replaced by a true one. -------
    (PAPER,
     "§4.** α is no longer",
     "§4.** α is measured, but",
     "§9 limitation 4 · strike the claim that α is off the list"),
    (PAPER,
     "   in that list: §5.4 estimates it at 0.408 per year on the registered sample, against the 0.05",
     "   for the quantity PRE-002's instrument dates rather than for the model's α: §5.4 estimates\n"
     "   that rate at 0.408 per year on the registered sample, against the 0.05",
     "§9 limitation 4 · what was measured, and of what"),
    (PAPER,
     "   swept through the body, and finds the constant hazard the model assumes to be rejected. §4.9",
     "   swept through the body, and finds the constant hazard the model assumes to be rejected. The\n"
     "   bridge from that rate to the model's α is the one §6.2 requires of every registration, and\n"
     "   this paper has not written it. §4.9",  # noqa: E501
     "§9 limitation 4 · §6.2's discipline applied to §5.4's own number"),
]


def main() -> int:
    apply_edits(EDITS)
    # Every phrase below can legitimately straddle a hard wrap, so the guard reads a
    # whitespace-flattened document. A guard that a line break can satisfy is not a guard.
    flat = " ".join(PAPER.read_text(encoding="utf-8").split())

    # The guard is an ABSENCE and a COUNT, never a list of presences: a patch that
    # resolves every anchor it was given reports total success while a site nobody
    # listed sits two hundred lines away. SCOUT-001 listed five; there were six.
    forbidden = [
        "**the recognition rate is 0.41",
        "the recognition rate is **α̂",
        "**The recognition rate is 0.41",
        "**The recognition rate is an order of magnitude",
        "§5.4 measures the recognition rate and",
        "α is no longer in that list",
    ]
    still_there = [f for f in forbidden if f in flat]
    if still_there:
        raise SystemExit(f"wt102: rounding survives at {len(still_there)} site(s): {still_there}")

    n_short = flat.count(SHORT) + flat.count(SHORT.capitalize())
    n_long = flat.count(LONG)
    if n_short != 3 or n_long != 2:
        raise SystemExit(
            f"wt102: expected 3 short + 2 long qualified phrases, found {n_short} + {n_long}")

    print(f"wt102 ok · {n_short} × '{SHORT}' · {n_long} × '{LONG}' · 0 rounding sites")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
