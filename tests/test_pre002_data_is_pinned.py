"""§11 pins the code per file. This binds the same discipline to the input that MOVES.

`companyfacts` is a live endpoint. §5.4 and §7 both say so in print — *"a re-pull is not the
original pull"*, 688 → 695 over one week — and until `wt106` the manuscript carried no
retrieval date and no digest, so **the sample grew every day the paper was not posted and
there was no sentence a replicator could hold it to.** §11 pinned three per-file source
commits: the right instinct, applied to the half of the input that does not change.

This test closes the other half. It recomputes SHA-256 for the two committed data files and
requires §11 to still print them. A re-pull that lands new data without the manuscript being
told fails here, loudly, in the same run that would otherwise have published a paper whose
stated digest describes a file that no longer exists.

`REG-009`'s `LIVES_SHA256` gate is the pattern; this is that pattern pointed at §5's sample.
"""
from __future__ import annotations

import hashlib
import pathlib

import pytest

ROOT = pathlib.Path(__file__).resolve().parents[1]
PAPER = ROOT / "docs/papers/paper-III-dual-tensor/paper-III.md"

PINNED = ["data/pre-002-events.json", "data/pre-002-riskset.json"]


@pytest.mark.parametrize("relative", PINNED)
def test_the_manuscript_prints_this_file_s_digest(relative):
    path = ROOT / relative
    assert path.exists(), f"{relative} is gone; §11 pins a file that is not there"
    digest = hashlib.sha256(path.read_bytes()).hexdigest()
    text = PAPER.read_text(encoding="utf-8")
    assert digest in text, (
        f"§11's pin for {relative} is stale. The file now hashes to {digest}. Either the "
        f"data was re-pulled — in which case every count in §5 and §5.4 is a count on a "
        f"different sample and the manuscript must say so — or the file was reformatted, "
        f"in which case re-run scripts/wt106_edits_t5_scope_and_pull.py."
    )


def test_the_pull_is_dated_and_committed():
    flat = " ".join(PAPER.read_text(encoding="utf-8").split())
    assert "The events analysed here were retrieved on" in flat
    assert "the 2013–2024 window selects registrants, not events" in flat, (
        "§11's statement that the stated window selects registrants rather than events is "
        "gone. That distinction is T5: a sixth of the sample falls outside 2013–2024."
    )
