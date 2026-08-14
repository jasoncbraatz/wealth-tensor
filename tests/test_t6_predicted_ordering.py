"""§5.3's replacement claim has to keep coming out of the data that licensed it.

`wt105` replaced §5.3's *"no reading of the tier ordering as a noisy version of the predicted
one survives that pattern"* — an inference the paper's own non-independence finding does not
support — with the statistic: **the predicted ordering appears in 5.7% of firm-clustered
resamples in the pilot and 5.8% in the replication.**

A number in a manuscript is only as good as the thing that recomputes it. This runs the
committed probe, `docs/scouting/probes/tier2_tallest.py` (20,000 draws, seed 20260814, ~6 s),
and requires its two monotone-ordering probabilities to be the two percentages the manuscript
prints. No arithmetic is duplicated here: the probe is the instrument, the manuscript is the
claim, and this is the wire between them.

The `-38` shape it is written against: a statistic can be a tautology in measurement's
clothing. It is not one here, because the probe resamples FIRMS — the unit §5.4's own
co-occurrence finding demands — and the manuscript's sentence says so, so a future edit that
quietly swaps the resampling unit back to events changes the number and this goes red.
"""
from __future__ import annotations

import pathlib
import re
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
PAPER = ROOT / "docs/papers/paper-III-dual-tensor/paper-III.md"
PROBE = ROOT / "docs/scouting/probes/tier2_tallest.py"

#: The probe's universe names, in the order the manuscript names them.
UNIVERSES = ("pilot", "replication")


def test_the_manuscript_s_two_percentages_come_out_of_the_probe():
    run = subprocess.run([sys.executable, str(PROBE)], cwd=ROOT,
                         capture_output=True, text=True, timeout=600)
    assert run.returncode == 0, f"probe failed (exit {run.returncode}):\n{run.stderr}"

    measured = {}
    universe = None
    for line in run.stdout.splitlines():
        head = re.match(r"== (\w+):", line.strip())
        if head:
            universe = head.group(1)
        got = re.search(r"P\(ladder monotone in the predicted order\)\s*=\s*([0-9.]+)", line)
        if got and universe:
            measured[universe] = float(got.group(1))
    assert set(measured) == set(UNIVERSES), f"probe output not understood: {measured}"

    flat = " ".join(PAPER.read_text(encoding="utf-8").split())
    claim = re.search(
        r"the predicted ordering appears in ([0-9.]+)% of firm-clustered resamples in the "
        r"pilot and ([0-9.]+)% in the replication",
        flat)
    assert claim, "§5.3's predicted-ordering sentence is gone or reworded"

    for universe, printed in zip(UNIVERSES, claim.groups()):
        assert f"{measured[universe] * 100:.1f}" == printed, (
            f"§5.3 prints {printed}% for the {universe}; the probe measures "
            f"{measured[universe] * 100:.1f}%. One of them has moved."
        )


def test_the_deleted_inference_stays_deleted():
    flat = " ".join(PAPER.read_text(encoding="utf-8").split())
    assert "no reading of the tier ordering as a noisy version" not in flat, (
        "§5.3's overclaim is back. It rests on a tier-2-tallest pattern that survives 33.9% "
        "of pilot resamples; the paper's own §9 limitation 9 says events are not the unit."
    )
