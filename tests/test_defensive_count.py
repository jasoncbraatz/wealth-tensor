"""G-COACH-3, enforced: the manuscript's defensive-sentence count is non-increasing.

`CO-AUTHOR-CHARTER.md` §2 has stated this invariant since 2026-08-12 and nothing has ever
evaluated it. `scripts/defensive_count.py` counts; this file is what makes the count
BINDING, and the mechanism is the important part:

    The baseline is COMMITTED. A revision that legitimately raises a count -- and there
    are such revisions -- must raise the baseline in the same commit, where the increase
    appears in a diff with a message beside it. The invariant is therefore not
    "never hedge"; it is "never hedge SILENTLY", which is the only version of it a
    session can actually be held to.

§Limitations is exempt by charter §3.2: limitations appear once, in one honest room.
The counter's LEVEL is meaningless on its own -- see the tool's docstring on why a lexicon
counter is only evidence as a delta. This suite reads it only as a delta against the
committed baseline.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
PAPER = ROOT / "docs" / "papers" / "paper-III-dual-tensor" / "paper-III.md"
BASELINE = ROOT / "docs" / "papers" / "paper-III-dual-tensor" / "DEFENSIVE-BASELINE.json"

sys.path.insert(0, str(ROOT / "scripts"))


@pytest.fixture(scope="module")
def counted():
    import defensive_count

    return defensive_count, defensive_count.count(PAPER.read_text(encoding="utf-8"))


def test_the_baseline_exists_and_describes_this_manuscript():
    assert BASELINE.exists(), (
        "G-COACH-3 needs a committed baseline. Regenerate with:\n"
        "  python3 scripts/defensive_count.py docs/papers/paper-III-dual-tensor/"
        "paper-III.md --json docs/papers/paper-III-dual-tensor/DEFENSIVE-BASELINE.json")
    base = json.loads(BASELINE.read_text())
    assert set(base) == {"totals", "sections"}


def test_no_section_gained_a_defensive_sentence_since_the_baseline(counted):
    module, now = counted
    base = json.loads(BASELINE.read_text())["sections"]
    grew = {}
    for heading, v in now.items():
        if module.LIMITATIONS_RE.search(heading):
            continue                                    # charter §3.2, exempt
        if v["defensive"] > base.get(heading, 0):
            grew[heading] = (base.get(heading, 0), v["defensive"], v["examples"])
    assert not grew, (
        "G-COACH-3: a revision added hedging prose without declaring it.\n"
        + "\n".join(f"  {h}: {b} -> {a}\n    e.g. {ex[0] if ex else ''}"
                    for h, (b, a, ex) in grew.items())
        + "\n\nCharter §2: if a finding seems to demand new hedging, it demands a "
          "NARROWER CLAIM.\nRewrite the claim and delete the hedge — or, if the hedge is "
          "right, raise the baseline\nin the same commit so the increase is visible in a "
          "diff.")


def test_the_total_outside_limitations_has_not_grown(counted):
    module, now = counted
    inv, _lim = module.totals(now)
    assert inv <= json.loads(BASELINE.read_text())["totals"]["invariant"]


def test_the_counter_is_not_vacuous(counted):
    """A guard that cannot fire is a phantom tag (METHOD-001). Prove it counts."""
    module, _ = counted
    hedged = "## 1 · A\n\nThe result holds. Arguably it might well be otherwise.\n"
    assert module.count(hedged)["1 · A"]["defensive"] == 1
    clean = "## 1 · A\n\nThe result holds on 683 pairs across 577 firms.\n"
    assert not module.count(clean)
    # and a SCOPE statement is not a hedge -- narrowing a claim is charter §2's legal
    # repair, and a counter that punished it would push revisions toward vagueness
    scope = ("## 1 · A\n\nThis registration does not measure the economic decay rate, "
             "and §10 says so.\n")
    assert not module.count(scope)


def test_a_table_row_is_not_prose(counted):
    """§7 is a table of restatements; hedging words inside a cell are not the paper
    hedging, and counting them would make every ledger row a violation."""
    module, _ = counted
    md = "## 7 · X\n\n| claim | test |\n|---|---|\n| **A** | arguably not necessarily |\n"
    assert not module.count(md)
