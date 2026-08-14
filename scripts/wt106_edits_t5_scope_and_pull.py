"""T5 · the demotion's scope sentence does not describe the sample, and no pull is pinned.

THE SENTENCE
------------
§6.1 is the paper's single most carefully worded sentence — the exact statement of what was
demoted — and its window is the wrong one:

    **Not supported:** ... in US-listed retail trade or computer and data processing
    services **over 2013–2024**, at the firm level, at effect sizes of one quarter per tier
    or larger.

**2013–2024 is the REGISTRANT selection window, not the EVENT window.**
`RESULT-002-*-run.log` line 2 reads *"673 registrants ever filing in range 2013-2024"*: a
firm qualifies by filing inside the window, and then every event `companyfacts` serves for
that firm is retained. Measured from `data/pre-002-events.json` (gated on §5.3's eight
published tier medians first):

    charges  2012 Q2 – 2026 Q2      onsets  2010 Q1 – 2026 Q1
    outside 2013–2024:  39 of 247 (15.8%) pilot · 68 of 448 (15.2%) replication

A sixth of the sample sits outside the stated period, and a replicator finds that in ten
minutes. REPLACE: longer by a line, narrower by a lot, and it is the sentence the paper
actually earned.

THE SECOND HALF IS WORSE THAN THE FIRST
----------------------------------------
§5.4 and §7 both document that `companyfacts` serves a live endpoint — *"a re-pull is not
the original pull"*, 688 → 695 in a week — and **no retrieval date appears anywhere in the
manuscript.** §11 pins three per-file commits, which is exactly the right instinct applied
to the code and not to the data. **The sample grows every day the paper is not posted and
there is no sentence a replicator can hold it to.**

The machinery already exists: `REG-009`'s `LIVES_SHA256` gate is the pattern. So §11 gets a
retrieval date, the commit that carries the pull, and a SHA-256 for each of the two data
files — the same discipline §11 already applies to `src/`, applied to the input that
actually moves. The digests below are computed here rather than typed, and
`tests/test_pre002_data_is_pinned.py` recomputes them from the committed files, so the pin
fails loudly if the data is ever re-pulled without the manuscript being told.
"""
from __future__ import annotations

import hashlib
import json
import pathlib
import statistics
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from patchkit import apply_edits  # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parents[1]
PAPER = ROOT / "docs/papers/paper-III-dual-tensor/paper-III.md"
EVENTS = ROOT / "data/pre-002-events.json"
RISKSET = ROOT / "data/pre-002-riskset.json"

#: The commit that carries the rebuilt pull, and its date. `git log -1 -- data/…`.
PULL_COMMIT = "0569ab6"
PULL_DATE = "2026-08-12"

PUBLISHED_MEDIANS = {"pilot": [5.0, 4.0, 5.5, 5.0], "replication": [5.0, 4.5, 6.0, 5.0]}


def quarter(index: int) -> str:
    return f"{index // 4} Q{index % 4 + 1}"


def measure() -> dict:
    """The event window, after reproducing §5.3's published medians."""
    data = json.loads(EVENTS.read_text(encoding="utf-8"))
    charges, onsets = [], []
    for name, universe in data["universes"].items():
        events = universe["events"]
        medians = [statistics.median([e["lag"] for e in events if e["tier"] == t])
                   for t in range(4)]
        if [float(m) for m in medians] != PUBLISHED_MEDIANS[name]:
            raise SystemExit(f"wt106 GATE FAILED · {name} medians {medians}; nothing written.")
        charges += [e["q_star"] for e in events]
        onsets += [e["onset"] for e in events]
    out = {"charge_lo": quarter(min(charges)), "charge_hi": quarter(max(charges)),
           "onset_lo": quarter(min(onsets)), "onset_hi": quarter(max(onsets))}
    print(f"wt106 gate · medians reproduced · charges {out['charge_lo']} – {out['charge_hi']} · "
          f"onsets {out['onset_lo']} – {out['onset_hi']}")
    return out


W = measure()
SHA_EVENTS = hashlib.sha256(EVENTS.read_bytes()).hexdigest()
SHA_RISKSET = hashlib.sha256(RISKSET.read_bytes()).hexdigest()

EDITS = [
    # ---- §6.1 · the registrant window is not the event window ---------------------------
    (PAPER,
     "unobservability is identified with GAAP asset class, in US-listed retail trade or computer and",  # noqa: E501
     "unobservability is identified with GAAP asset class, in US-listed retail trade (SIC 5200–5999)\n"
     "or computer and",
     "§6.1 · the SIC ranges, named where the claim is stated"),
    (PAPER,
     "data processing services over 2013–2024, at the firm level, at effect sizes of one quarter per",
     f"data processing services (SIC 7370–7379), among registrants filing in 2013–2024, on charges\n"
     f"recognised {W['charge_lo']} – {W['charge_hi']}, at the firm level, at effect sizes of one quarter per",  # noqa: E501
     "§6.1 · registrant window vs event window"),

    # ---- §11 · pin the pull -------------------------------------------------------------
    (PAPER,
     "- **Drop accounting for §5**, as required by the registrations: the per-bucket attrition from",
     f"- **Data retrieval, pinned.** `companyfacts` serves each firm's *latest* view of its own\n"
     f"  history, so a re-pull is not the original pull and the sample grows with every filing —\n"
     f"  §5.4 reports 688 → 695 over one week. The events analysed here were retrieved on\n"
     f"  **{PULL_DATE}** and are committed rather than re-fetched, at commit **{PULL_COMMIT}**:\n"
     f"  `data/pre-002-events.json`, SHA-256 **`{SHA_EVENTS}`**,\n"
     f"  and `data/pre-002-riskset.json`, SHA-256 **`{SHA_RISKSET}`**.\n"
     f"  Charges in that file run **{W['charge_lo']} – {W['charge_hi']}** and onsets\n"
     f"  **{W['onset_lo']} – {W['onset_hi']}**; the 2013–2024 window selects registrants, not events.\n"
     f"- **Drop accounting for §5**, as required by the registrations: the per-bucket attrition from",
     "§11 · the pull date and two digests, the src/ discipline applied to the data"),
]


def main() -> int:
    apply_edits(EDITS)
    flat = " ".join(PAPER.read_text(encoding="utf-8").split())
    if "services over 2013–2024" in flat:
        raise SystemExit("wt106: the registrant window still describes the events")
    for needed in (SHA_EVENTS, SHA_RISKSET, PULL_DATE, PULL_COMMIT,
                   f"{W['charge_lo']} – {W['charge_hi']}",
                   "among registrants filing in 2013–2024"):
        if needed not in flat:
            raise SystemExit(f"wt106: missing {needed!r}")
    print(f"wt106 ok · §6.1 scoped to {W['charge_lo']} – {W['charge_hi']} · §11 pins the pull")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
