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

THE INVARIANT NOW MEANS THE ESTATE, NOT ONE PAPER (wealthTensor-31)
-------------------------------------------------------------------
`-30` shipped this against paper III alone, and the charter says "the manuscript" without
naming one. Papers I and II were therefore covered by a rule with no instrument -- the
exact shape the tool was built to end, one level out. Both now carry a committed baseline
and run through the same parametrised tests. Paper II's baseline is ZERO outside
§Limitations, which is a real state and not an empty check: the tests below prove the
counter fires, so a zero is a measurement.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
PAPERS = ROOT / "docs" / "papers"

# Every manuscript in the estate. A paper added here without a baseline fails
# `test_the_baseline_exists_and_describes_this_manuscript` rather than being skipped.
# The `-v1` entries are the paper-rebuild drafts; each carries its OWN per-stem baseline,
# because two manuscripts now share a directory (see _baseline).
MANUSCRIPTS = {
    "paper-I": PAPERS / "paper-I-price-formation" / "paper-I.md",
    "paper-II": PAPERS / "paper-II-redistribution" / "paper-II.md",
    "paper-II-v1": PAPERS / "paper-II-redistribution" / "paper-II-v1.md",
    "paper-III": PAPERS / "paper-III-dual-tensor" / "paper-III.md",
    "paper-III-v1": PAPERS / "paper-III-dual-tensor" / "paper-III-v1.md",
    "paper-IV": PAPERS / "paper-IV-composition" / "paper-IV.md",
}

sys.path.insert(0, str(ROOT / "scripts"))


def _baseline(md: Path) -> Path:
    """One baseline per MANUSCRIPT, not per directory.

    `-108`: the v1 rebuild put a second manuscript in `paper-II-redistribution/` and in
    `paper-III-dual-tensor/`, and a directory-keyed baseline silently makes two papers share
    one committed count -- so a hedge added to the rebuild would have been measured against
    the v0.x draft's baseline and passed. The per-stem name is the fix; the legacy
    directory-keyed name is still honoured for the four manuscripts that already carry it,
    because renaming a committed baseline would reset the very history it exists to hold.
    """
    per_stem = md.parent / ("DEFENSIVE-BASELINE-%s.json" % md.stem)
    if per_stem.exists():
        return per_stem
    legacy = md.parent / "DEFENSIVE-BASELINE.json"
    if legacy.exists() and md.stem in ("paper-I", "paper-II", "paper-III", "paper-IV"):
        return legacy
    return per_stem


@pytest.fixture(scope="module")
def module():
    import defensive_count

    return defensive_count


@pytest.fixture(scope="module")
def counts(module):
    return {k: module.count(p.read_text(encoding="utf-8")) for k, p in MANUSCRIPTS.items()}


def test_every_manuscript_in_the_estate_is_covered():
    """The census, so a fourth paper cannot arrive uncounted."""
    found = {p for p in PAPERS.glob("*/paper-*.md") if ".bak" not in p.name}
    assert found == set(MANUSCRIPTS.values()), sorted(str(p) for p in found)


@pytest.mark.parametrize("name", sorted(MANUSCRIPTS))
def test_the_baseline_exists_and_describes_this_manuscript(name):
    md = MANUSCRIPTS[name]
    base_path = _baseline(md)
    assert base_path.exists(), (
        "G-COACH-3 needs a committed baseline. Regenerate with:\n"
        "  python3 scripts/defensive_count.py " + str(md.relative_to(ROOT))
        + " --json " + str(base_path.relative_to(ROOT)))
    base = json.loads(base_path.read_text())
    assert set(base) == {"totals", "sections"}


@pytest.mark.parametrize("name", sorted(MANUSCRIPTS))
def test_no_section_gained_a_defensive_sentence_since_the_baseline(module, counts, name):
    now = counts[name]
    base = json.loads(_baseline(MANUSCRIPTS[name]).read_text())["sections"]
    grew = {}
    for heading, v in now.items():
        if module.LIMITATIONS_RE.search(heading):
            continue                                    # charter §3.2, exempt
        if v["defensive"] > base.get(heading, 0):
            grew[heading] = (base.get(heading, 0), v["defensive"], v["examples"])
    assert not grew, (
        "G-COACH-3: a revision added hedging prose to " + name + " without declaring it.\n"
        + "\n".join(f"  {h}: {b} -> {a}\n    e.g. {ex[0] if ex else ''}"
                    for h, (b, a, ex) in grew.items())
        + "\n\nCharter §2: if a finding seems to demand new hedging, it demands a "
          "NARROWER CLAIM.\nRewrite the claim and delete the hedge — or, if the hedge is "
          "right, raise the baseline\nin the same commit so the increase is visible in a "
          "diff.")


@pytest.mark.parametrize("name", sorted(MANUSCRIPTS))
def test_the_total_outside_limitations_has_not_grown(module, counts, name):
    inv, _lim = module.totals(counts[name])
    base = json.loads(_baseline(MANUSCRIPTS[name]).read_text())["totals"]["invariant"]
    assert inv <= base


def test_the_counter_is_not_vacuous(module):
    """A guard that cannot fire is a phantom tag (METHOD-001). Prove it counts — which is
    also what makes paper II's baseline of zero a measurement rather than a silence."""
    hedged = "## 1 · A\n\nThe result holds. Arguably it might well be otherwise.\n"
    assert module.count(hedged)["1 · A"]["defensive"] == 1
    clean = "## 1 · A\n\nThe result holds on 683 pairs across 577 firms.\n"
    assert not module.count(clean)
    # and a SCOPE statement is not a hedge -- narrowing a claim is charter §2's legal
    # repair, and a counter that punished it would push revisions toward vagueness
    scope = ("## 1 · A\n\nThis registration does not measure the economic decay rate, "
             "and §10 says so.\n")
    assert not module.count(scope)


def test_a_table_row_is_not_prose(module):
    """§7 is a table of restatements; hedging words inside a cell are not the paper
    hedging, and counting them would make every ledger row a violation."""
    md = "## 7 · X\n\n| claim | test |\n|---|---|\n| **A** | arguably not necessarily |\n"
    assert not module.count(md)
