"""T6 · §5.3 overclaims about its own failure — plus S1's free censoring column.

T6 · THE ONE PLACE THE PAPER'S DISCIPLINE LAPSES IS AGAINST ITSELF
-------------------------------------------------------------------
§5.3 currently ends the failure analysis with:

    A four-rung ladder whose *third* rung is the tallest cannot be rescued by appeal to
    the top rung's behaviour, and **no reading of the tier ordering as a noisy version of
    the predicted one survives that pattern.**

The point estimates are right — 5.5 against 5.0, 6.0 against 5.0. The inference resting on
them is not, and the paper establishes why in a different section: §9's ninth limitation and
§5.4 both report that events are **not independent**, at 4.12× and 2.02× the independence
rate. Resample firms rather than events — which is the unit the paper's own finding demands
— and the shape the sentence rests on appears in **33.9%** of pilot draws and 52.6% of
replication draws (`docs/scouting/probes/tier2_tallest.py`, 20,000 draws, seed 20260814).

**The robust statistic is already in hand and it is SHORTER than the rhetoric it replaces:**
the predicted ordering itself appears in **5.7%** of firm-clustered resamples in the pilot
and **5.8%** in the replication. That is the claim §5.3 wants, it holds in both universes,
and it uses the resampling unit §5.4's own finding requires.

Why this ticket is worth the most to the paper's character: §7's commentary already says a
survivals ledger containing only survivals is an advertisement, and names the row that cost
the paper its neatest sentence. **This is the mirror case.** The paper's scrupulousness is
calibrated against the temptation to flatter itself and has no guard against the temptation
to be dramatically hard on itself. Both are overclaims; only one was being watched. And the
tier-2 bootstrap is the one a referee *will* run, because it is the paper's most assertive
empirical sentence.

S1 · THE FREE STEELMAN, AND THE CLAIM IT DOES *NOT* SUPPORT
------------------------------------------------------------
The natural mechanical attack on a null about long lags is that the instrument's twenty-
quarter ceiling hides the tail of the tier predicted to be tallest. §5.3's PRE-001-versus-
PRE-002 table already carries half the answer — censoring rose from 0% to 7.8%/14.2% — and
never draws the tier-level conclusion, which costs four numbers.

**Measured here, gated on §5.3's eight published tier medians before anything else is
reported** (`data/pre-002-events.json`):

    pilot        4.8 · 17.6 · 11.8 · 5.1 %      (tiers 0 · 1 · 2 · 3)
    replication 17.6 · 15.7 · 17.0 · 12.5 %

**`SCOUT-001` §3 states this one step too strongly and its own table shows it.** The report's
prose reads *"Goodwill is the least-censored tier in retail and the least in computer
services."* In retail, tier 0 is 4.8% against goodwill's 5.1% — the report's own printed
table, one line above the sentence. Goodwill is the least-censored tier in the replication
and the **second**-least in the pilot, and that is what goes in the manuscript. An inherited
claim is a claim, not a measurement, even when the document that carries it did the
measuring; this one would have entered the paper as prose nobody re-derived. `SCOUT-001` is
corrected in the same commit.

The surviving version still closes the attack outright, because the attack needs goodwill's
tail to be the hidden one and goodwill sits at the bottom of the censoring distribution in
both universes. **Nothing here re-tests the lag gradient** — censoring share by tier is a
property of the instrument, like `annual_test_date.py`'s concentration statistic, and
PRE-002 §5's stopping rule is untouched.
"""
from __future__ import annotations

import json
import pathlib
import statistics
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from patchkit import apply_edits  # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parents[1]
PAPER = ROOT / "docs/papers/paper-III-dual-tensor/paper-III.md"
SCOUT = ROOT / "docs/scouting/SCOUT-001-paper-III-opposing-team.md"
EVENTS = ROOT / "data/pre-002-events.json"

#: §5.3's published tier medians. The gate: reproduce these from the committed data or
#: write nothing. Same gate all four scouting probes use.
PUBLISHED_MEDIANS = {"pilot": [5.0, 4.0, 5.5, 5.0], "replication": [5.0, 4.5, 6.0, 5.0]}

#: `probes/tier2_tallest.py`, 20,000 firm-clustered draws, seed 20260814. Bound to the
#: manuscript by `tests/test_t6_predicted_ordering.py`, which re-runs the probe.
PREDICTED_ORDERING = {"pilot": "5.7%", "replication": "5.8%"}


def censoring() -> dict[str, list[str]]:
    """Per-tier right-censoring, after reproducing the published medians."""
    data = json.loads(EVENTS.read_text(encoding="utf-8"))
    out = {}
    for name, universe in data["universes"].items():
        events = universe["events"]
        medians = [statistics.median([e["lag"] for e in events if e["tier"] == t])
                   for t in range(4)]
        if [float(m) for m in medians] != PUBLISHED_MEDIANS[name]:
            raise SystemExit(
                f"wt105 GATE FAILED · {name} tier medians are {medians}, §5.3 prints "
                f"{PUBLISHED_MEDIANS[name]}. Nothing was written.")
        shares = []
        for t in range(4):
            tier = [e for e in events if e["tier"] == t]
            shares.append(100.0 * sum(1 for e in tier if e["censored"]) / len(tier))
        out[name] = [f"{s:.1f}" for s in shares]
        rank = sorted(range(4), key=lambda t: shares[t]).index(3) + 1
        print(f"wt105 gate · {name}: medians reproduced; censoring by tier "
              f"{out[name]}; goodwill ranks {rank} of 4 from the bottom")
        if rank > 2:
            raise SystemExit(
                f"wt105: goodwill is not at the bottom of {name}'s censoring distribution, "
                f"so S1's claim does not hold. Fix the prose, not this check.")
    return out


CENS = censoring()


def tier_cell(name: str) -> str:
    """`a · b · c · **d** %` — goodwill bolded, because goodwill is the claim."""
    s = CENS[name]
    return f"{s[0]} · {s[1]} · {s[2]} · **{s[3]}** %"


EDITS = [
    # ---- S1 · the censoring column ------------------------------------------------------
    (PAPER,
     "| right-censored | 0% | 7.8% pilot, 14.2% replication |",
     "| right-censored | 0% | 7.8% pilot, 14.2% replication |\n"
     f"| right-censored by tier, 0 · 1 · 2 · 3 | 0% throughout | pilot {tier_cell('pilot')}; "
     f"replication {tier_cell('replication')} |",
     "§5.3 · per-tier censoring row"),
    (PAPER,
     "long lags looks like.",
     "long lags looks like. **And the ceiling is not where the gradient went:** goodwill, the tier\n"
     "predicted to lag longest, carries the least censoring of the four in the replication and the\n"
     "second-least in the pilot, so the twenty-quarter cap is not hiding its tail.",
     "§5.3 · the ceiling attack, closed with four numbers"),

    # ---- T6 · the inference replaced by the statistic ------------------------------------
    (PAPER,
     "5.0 in the replication). A four-rung ladder whose *third* rung is the tallest cannot be rescued by",  # noqa: E501
     "5.0 in the replication). Those are point estimates, and the ordering is the claim: **the\n"
     f"predicted ordering appears in {PREDICTED_ORDERING['pilot']} of firm-clustered resamples in the\n"
     f"pilot and {PREDICTED_ORDERING['replication']} in the replication**,",
     "§5.3 · T6, the robust statistic"),
    (PAPER,
     "appeal to the top rung's behaviour, and no reading of the tier ordering as a noisy version of the",  # noqa: E501
     "resampling firms rather than events because §5.4's own finding says events are not",
     "§5.3 · T6, the resampling unit"),
    (PAPER,
     "predicted one survives that pattern.",
     "the unit.",
     "§5.3 · T6, the inference deleted"),

    # ---- SCOUT-001's own prose, corrected against its own table --------------------------
    (SCOUT,
     "Goodwill is the *least*-censored tier in retail and the least in computer services. **The",
     "Goodwill is the least-censored tier in computer services and the *second*-least in retail —\n"
     "tier 0 is 4.8% there, one line above in this table, and the first draft of this sentence said\n"
     "\"least in retail\" anyway. **The",
     "SCOUT-001 §3 · S1's prose, against S1's own table"),
]


def main() -> int:
    apply_edits(EDITS)
    flat = " ".join(PAPER.read_text(encoding="utf-8").split())

    for gone in ("no reading of the tier ordering as a noisy version",
                 "A four-rung ladder whose *third* rung is the tallest"):
        if gone in flat:
            raise SystemExit(f"wt105: the inference survives — {gone!r}")
    for name, pct in PREDICTED_ORDERING.items():
        if pct not in flat:
            raise SystemExit(f"wt105: {name}'s {pct} is not in the manuscript")
    for name in CENS:
        if tier_cell(name) not in flat:
            raise SystemExit(f"wt105: {name}'s censoring cells are not in §5.3's table")
    scout = " ".join(SCOUT.read_text(encoding="utf-8").split())
    if "Goodwill is the *least*-censored tier in retail" in scout:
        raise SystemExit("wt105: SCOUT-001's overstated sentence survives")

    print("wt105 ok · T6's inference replaced by the statistic · censoring row live · "
          "SCOUT-001 corrected")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
