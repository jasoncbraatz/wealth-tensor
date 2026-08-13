"""The guard for the defect REG-006 §1 found: a tag name that matches NOTHING.

WHY THIS EXISTS
---------------
`TIER_TAGS[0]` named `ImpairmentOfLongLivedAssetsHeldAndUsed`. That element does not
exist in the us-gaap taxonomy. It matched zero facts across all 307 firms of the
registered sample, for the life of the project, and nothing noticed -- because

    A TAG THAT MATCHES NOTHING IS INDISTINGUISHABLE, IN EVERY DOWNSTREAM STATISTIC,
    FROM A TAG THAT MATCHES NOTHING *IN THIS SAMPLE*.

Both contribute zero events. Neither raises. The tier simply came back thin, and a thin
tier looks exactly like a sector that impairs less. Tier 0 was seeing 52.6% of retail and
44.4% of computer-services firms and the cause was a spelling.

This is the same shape as `-16`'s underflowed tail (a survival that hit zero read as an
exhausted one) and `-17`'s truncated tail (running off the end of an array read as
convergence): a guard that cannot tell EMPTY from ABSENT. It is the third instance and
it is the first one mechanised.

Offline, like every test here: it checks the committed audit artifact, not the network.
Re-running the audit is `scripts/wt092_tag_audit.py`.
"""

from __future__ import annotations

import json
import pathlib

import pytest

from wealth_tensor import edgar as E

AUDIT = (pathlib.Path(__file__).resolve().parent.parent
         / "data" / "tag-resolution-audit.json")

DEAD = "ImpairmentOfLongLivedAssetsHeldAndUsed"


@pytest.fixture(scope="module")
def audit():
    return json.loads(AUDIT.read_text())["tags"]


def _named_tags():
    named = set()
    for tags in E.TIER_TAGS.values():
        named |= set(tags)
    for tags in getattr(E, "TIER_TAGS_REG006", {}).values():
        named |= set(tags)
    named.add(E.COMBINED_TAG)
    return named


def test_every_named_tag_appears_in_the_audit(audit):
    """Adding a tag without auditing it re-opens the exact hole REG-006 §1 found."""
    missing = sorted(_named_tags() - set(audit))
    assert not missing, (
        f"{missing} are named in edgar.py but absent from {AUDIT.name}. A tag whose "
        f"resolution has never been checked may be a misspelling that will silently "
        f"contribute zero events forever. Run scripts/wt092_tag_audit.py and commit it."
    )


def test_the_reg006_corrected_tiers_all_resolve(audit):
    """Every element REG-006 relies on must match something in our own sample."""
    dead = {t: audit[t]["facts"]
            for tags in E.TIER_TAGS_REG006.values() for t in tags
            if audit[t]["facts"] == 0}
    assert not dead, (
        f"{sorted(dead)} match ZERO facts in the registered sample. Either the element "
        f"name is wrong or the tier is genuinely empty here -- and the whole point of "
        f"this guard is that those two look identical downstream. Resolve it explicitly."
    )


def test_the_registered_element_is_pinned_as_dead(audit):
    """REG-006 §1's finding, pinned so it cannot be quietly un-found.

    If this ever fails, `ImpairmentOfLongLivedAssetsHeldAndUsed` started matching facts,
    which would mean the taxonomy changed and REG-006 §1's premise needs re-reading.
    """
    assert audit[DEAD]["facts"] == 0
    assert audit[DEAD]["firms"] == 0


def test_pre001_tier0_still_carries_the_dead_element():
    """PRE-001's constants are a contract; the correction is ADDITIVE, not a rewrite.

    `TIER_TAGS` is what was registered and what produced the published RESULT-REG-003.
    Editing it in place would make the code and the published table disagree about what
    was measured. REG-006's correction therefore lives in `TIER_TAGS_REG006`, and this
    test exists so that a future session tidying up the "typo" has to read REG-006 first.
    """
    assert DEAD in E.TIER_TAGS[0], (
        "TIER_TAGS[0] no longer carries the element PRE-001 registered. If you meant to "
        "amend the registration, RESULT-REG-003 and §5.4 need amending in the same "
        "commit -- see REG-006 §1 and RESULT-REG-006."
    )
    assert DEAD not in E.TIER_TAGS_REG006[0]


def test_the_correction_is_a_strict_superset_of_what_still_resolves(audit):
    """Whatever the corrected list does, it must not LOSE a tag that was working."""
    old_live = {t for t in E.TIER_TAGS[0] if audit[t]["facts"] > 0}
    assert old_live <= set(E.TIER_TAGS_REG006[0]), (
        f"the corrected tier 0 drops {sorted(old_live - set(E.TIER_TAGS_REG006[0]))}, "
        f"which was matching facts. A correction that removes live tags is a different "
        f"amendment and needs its own registration."
    )
