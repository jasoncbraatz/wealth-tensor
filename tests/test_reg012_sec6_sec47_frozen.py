"""`REG-012` §6 · **"no sentence of the manuscript's §4.7 is changed by any outcome of it."**

A REGISTRATION CAN FREEZE A SECTION, AND A FREEZE IS PINNABLE
--------------------------------------------------------------
`REG-012` measures the band count's edge phase. Its §6 pre-commits both branches and closes
with a sentence common to all three: the measurement *"produces no new answer to §7.5's
decision rule, and no sentence of the manuscript's §4.7 is changed by any outcome of it."*
`REG-012` is closed on branch F by ruling. **Nothing has ever checked the clause.**

The other constraints in `CONSTRAINT-INVENTORY-001` §3 are about what a sentence may SAY.
This one is about whether a section MOVED, which is the shape `test_pin001_code_state.py`
already handles for code: hash the thing, commit the hash, and let the next edit be the alarm.
`RESULT-PIN-001`'s defect is the precedent — §11's pin rotted for nine days *because nobody
edited the sentence*, and no source-text guard could see it.

THE WARRANT SUBTLETY, WHICH IS THE WHOLE DESIGN
------------------------------------------------
A bare hash of §4.7 goes red on **any** edit, and `REG-012` forbids only the edits that come
from ITS outcome. A future session correcting a typo in §4.7, or landing a repair registered
somewhere else entirely, would be told it had violated `REG-012` — a guard crying a violation
it cannot possibly have observed, which is worse than no guard, because the next session
learns to re-pin without reading.

So the file records **two** digests and the warranted path between them:

* `SEC_47_AT_REGISTRATION` — §4.7 as it stood at `ba59370`, the commit that registered
  `REG-012`. **This constant is immutable.** It is a fact about 2026-08-13 and no later
  session can make it a different fact.
* `SEC_47_CURRENT` — §4.7 as the working tree carries it today. This one moves, and may
  move only alongside an `AMENDMENTS` entry naming what licensed the move.
* `AMENDMENTS` — one entry per commit that moved §4.7 since the registration, each carrying
  the commit, the licence, and the digest the section landed on. The chain is checked
  against git: an entry whose commit did not move §4.7, or did not land on the digest it
  claims, is a warrant for an edit that did not happen.

WHY IT IS TWO CONSTANTS AND NOT ONE — `-65`'s ruling, `WT-096`
----------------------------------------------------------------
`-43` wrote this file with a single `SEC_47_SHA256` serving both roles, and a red message
that told the next session to *"re-pin `SEC_47_SHA256` in the SAME commit as the edit"*.
That instruction is **forbidden by this same file**: `test_the_pinned_digest_is_the_version_
REG_012_saw` requires the pin to equal §4.7 **at `ba59370`**. Once §4.7 moves for a
legitimate reason the two demands name different values and no single constant satisfies
both — so the prescribed remedy could be executed exactly **zero** times, and the first
warranted edit wedged the guard red permanently.

It happened on 2026-08-17 at `6314302`: a repair licensed by `ASC 350-30-35-15`, an outside
accounting standard, which corrected §4.7's *"For three of the four classes"* to *"two"* and
named why the repair does not reach the unamortised classes. That is reading (b) —
legitimate, and it moves **against** the paper's own interest, which is the opposite of
what `REG-012` §6 was written to stop. `-65` verified by walking every commit that touched
paper-III since the registration (`scripts/wt113_sec47_history.py`): §4.7 held byte-identical
across eight of them and moved at exactly one.

The defect was never in the freeze. It was that a guard which anticipated a legitimate edit
had **no representation for one**. A freeze that cannot record an amendment is not stricter
than the clause it enforces; it is a freeze that must be either violated or disabled, and a
session facing that choice under time pressure will disable it.

`WT-092`'s question, asked of this file: *what is the widest object this check's own words
claim, and what is the narrowest thing it actually touches?* Its words claimed a re-pin path
for legitimate edits. What it touched was one constant nailed to one commit. Nobody found
out for four days, because the remedy had never been run.

WHAT IT CANNOT DO
-----------------
It cannot tell WHY §4.7 changed; nothing in a repository can. It cannot tell whether a
licence string is *true* — that a session wrote `ASC 350-30-35-15` does not make the standard
say what the amendment claims. What it can do is guarantee that the question is asked out
loud at the moment §4.7 moves, that the answer is written down beside the digest it produced,
and that the registration-era anchor survives every one of those moves — which is the only
moment at which `REG-012` §6 can be violated and the only moment anybody would have known to
look.
"""
from __future__ import annotations

import hashlib
import pathlib
import re
import subprocess
import typing

import pytest

ROOT = pathlib.Path(__file__).resolve().parents[1]
PAPER_REL = "docs/papers/paper-III-dual-tensor/paper-III.md"
PAPER = ROOT / PAPER_REL
REG_012 = ROOT / "docs/preregistration/REG-012-band-count-edge-phase.md"

#: `REG-012` §6's freeze clause. The warrant.
CONSTRAINT = "no sentence of the manuscript's §4.7 is changed by any outcome of it"

#: The commit that registered `REG-012` — `git log -1 -- docs/preregistration/REG-012-*`.
#: **The freeze is relative to this commit, not to today.**
REG_012_COMMIT = "ba59370e49bce580820183484f1e4c58bffdcdf6"

#: SHA-256 of §4.7 as `REG-012` saw it at that commit. **IMMUTABLE.** A session that finds
#: this red has either broken the extractor or rewritten history; neither is a re-pin.
#: Verified out of git by `test_the_pinned_digest_is_the_version_REG_012_saw`.
SEC_47_AT_REGISTRATION = "da24a9f91fc3c00e8aaae37f94754fe9a5ae069fd340f52c1d7c457aa64129bf"


class Amendment(typing.NamedTuple):
    """One warranted move of §4.7, recorded where the next session will read it."""

    #: the commit that moved §4.7
    sha: str
    #: what licensed it — a standard, a ruling, a registration OTHER than `REG-012`
    licence: str
    #: §4.7's digest immediately after that commit
    digest_after: str


#: Every warranted move of §4.7 since `REG-012`, oldest first. Append, never rewrite:
#: an amendment removed is a review that un-happened.
AMENDMENTS: tuple[Amendment, ...] = (
    Amendment(
        sha="6314302",
        licence=(
            "ASC 350-30-35-15 — indefinite-lived intangibles are tested for impairment "
            "rather than amortised, so no useful life is disclosed and there is nothing "
            "to pin delta to. -63's III-3 repair: 'For three of the four classes' -> 'two', "
            "and the reason the repair does not reach the two unamortised classes. An "
            "outside accounting standard, not an outcome of REG-012; ruled reading (b) by "
            "-65 (card 1217542940969153, LEDGER WT-096)."
        ),
        digest_after="69374513a57f699498da7568afb4ad6ad0af9c97ef4f7b4814a46d5fd375e7ad",
    ),
    Amendment(
        sha="74734de",
        licence=(
            "wealthTensor-73's first independent read of Paper III (wt131, III-7). "
            "Section 4.7 attributed its floor of 30 to Paper III's own section 5, which "
            "states no floor of 30 anywhere and whose published tier cells run as low "
            "as 21; the floor is REG-009 section 3b's inherited THIN line. The clause "
            "now names the floor without attributing it, so the sentence claims only "
            "what a reader can check. Licensed by a review of the manuscript against "
            "itself, not by any measurement of the band count's edge phase; nothing "
            "here reads REG-012's result or its branch."
        ),
        digest_after="8608601162cb03efef17083c5250faf1e9d4dfa7ec99bfb087b74190ce7df3c3",
    ),
    Amendment(
        sha="f44bf4b",
        licence=(
            "wealthTensor-105, Pass C of DEFINITION-OF-DONE-SHIP.md section 3. An S1 under "
            "that document's section 2 -- 'a cross-reference that resolves to the wrong "
            "place' -- found by Pass C's read against the frozen instrument set. Section "
            "4.7 said 'So section 4.6's question answers yes'; SECTION 4.6 POSES NO "
            "QUESTION, and there is no question mark anywhere in 4.1 through 4.6. The "
            "clause now states the question the section is answering -- whether anything "
            "outside the reported series restores phi -- so it claims only what a reader "
            "can check, and the matching pointer in section 7's survival ledger was "
            "repaired in the same commit because a repair landing at one of two sites "
            "leaves the document asserting both (SL-9's lesson). Licensed by a review of "
            "the manuscript against itself under the ship definition of done. NOTHING HERE "
            "READS REG-012's RESULT OR ITS BRANCH: the edit is about a dangling reference, "
            "not about the band count's edge phase, and it would have been made identically "
            "had REG-012 never run. Reading (b). The edit landed in the commit named above "
            "rather than in this one, per the guard's own instruction that the review the "
            "same-commit rule wanted is the review, not the SHA (-65, LEDGER WT-096)."
        ),
        digest_after="bdf7fcbb13eae1418cff5b4b9164eadab4b719bfad937093375711ae60724cf6",
    ),
    Amendment(
        sha="8fcb6a8",
        licence=(
            "wealthTensor-105, the adversarial verification of its own Pass C repairs. The "
            "amendment above replaced a dangling reference to a question section 4.6 does "
            "not ask with the clause 'the question this section opened with'. SECTION 4.7 "
            "DOES NOT OPEN WITH A QUESTION -- it opens with an assertion, 'the way out is "
            "visible in the theorem's own statement' -- so the repair had replaced one "
            "unresolvable anchor with a weaker form of the same defect. The sentence is now "
            "self-contained and names its own subject: 'So the answer is yes -- something "
            "outside the reported series does restore phi.' Licensed by a review of the "
            "manuscript against itself under the ship definition of done, and by nothing "
            "else. NOTHING HERE READS REG-012's RESULT OR ITS BRANCH: the edit concerns a "
            "sentence's referent, not the band count's edge phase, and would have been made "
            "identically had REG-012 never run. Reading (b). The edit landed in the commit "
            "named above rather than in this one, per the guard's own instruction."
        ),
        digest_after="1a33d57b021f45bd2ab029cbcb4569c3d75f67a7d61112357c6b131649e0169d",
    ),
)

#: SHA-256 of §4.7 as the working tree carries it now. Moves only with an `AMENDMENTS`
#: entry, in the same commit as the edit where that is possible and with the licensing
#: commit named where it is not — see `test_section_47_is_byte_identical_to_the_pin`.
SEC_47_CURRENT = AMENDMENTS[-1].digest_after if AMENDMENTS else SEC_47_AT_REGISTRATION

_HEADING_47 = re.compile(r"^### 4\.7 · .*$", re.M)
_HEADING_48 = re.compile(r"^### 4\.8 · ", re.M)


def section_47(text: str) -> str:
    """§4.7, from its heading to §4.8's, exactly as the file carries it.

    Byte-exact and NOT whitespace-flattened. `-42`'s tell: *a whitespace-identity guard
    certifies that no character moved, not that no meaning moved — and in a line-oriented
    format the line break is content.* The inverse applies here. A flattening extractor would
    let a re-wrap of §4.7 pass a freeze that says **no sentence is changed**, and this
    repository has already had one re-wrap silently collapse a list (`wt107`, repaired by
    `wt109`). The freeze is on the section as the file stores it.
    """
    start = _HEADING_47.search(text)
    assert start, "§4.7's heading is gone from the manuscript"
    rest = text[start.start():]
    end = _HEADING_48.search(rest)
    assert end, "§4.8's heading is gone from the manuscript"
    return rest[: end.start()]


def digest(section: str) -> str:
    return hashlib.sha256(section.encode("utf-8")).hexdigest()


def _git(*args: str) -> str | None:
    try:
        return subprocess.run(("git", "-C", str(ROOT), *args),
                              capture_output=True, text=True, check=True).stdout
    except (subprocess.CalledProcessError, FileNotFoundError):
        return None


def _digest_at(sha: str) -> str | None:
    blob = _git("show", f"{sha}:{PAPER_REL}")
    return None if blob is None else digest(section_47(blob))


def test_the_registration_still_says_this():
    flat = " ".join(REG_012.read_text(encoding="utf-8").split())
    assert CONSTRAINT in flat, (
        "REG-012 §6's freeze clause is gone or restated. This guard has lost its warrant; "
        "read the registration before trusting anything else in this file."
    )


def test_section_47_is_extractable_and_is_the_repair():
    """The freeze is worthless if it is pinning the wrong bytes.

    §4.7 is *The repair* — HANDOFF §2's ruling, **§4.8 IS NOT THE COINCIDENCE ARGUMENT; §4.7
    IS** — so the extractor is checked against what the section is, not only against a
    heading regex that would happily pin an empty string.
    """
    section = section_47(PAPER.read_text(encoding="utf-8"))
    assert section.startswith("### 4.7 · The repair")
    assert len(section.splitlines()) > 50, "§4.7 extracted suspiciously short"
    assert "### 4.8" not in section


def test_section_47_is_byte_identical_to_the_pin():
    found = digest(section_47(PAPER.read_text(encoding="utf-8")))
    assert found == SEC_47_CURRENT, (
        "§4.7 has moved since the last recorded amendment.\n"
        f"  expected  {SEC_47_CURRENT}\n  current   {found}\n\n"
        "REG-012 §6: 'no sentence of the manuscript's §4.7 is changed by any outcome of it.'\n"
        "TWO READINGS, AND ONLY THE AUTHOR OF THE EDIT KNOWS WHICH:\n"
        "  (a) the edit came from REG-012's outcome — that is the violation, and REG-012 is\n"
        "      closed on branch F, so the edit is reverted, not recorded;\n"
        "  (b) the edit came from anywhere else — legitimate. APPEND an Amendment to\n"
        "      AMENDMENTS in the SAME commit as the edit, carrying that commit's sha, the\n"
        "      licence (the standard, ruling or OTHER registration that permits it), and\n"
        "      the digest above. SEC_47_CURRENT follows the chain; do not edit it directly,\n"
        "      and NEVER touch SEC_47_AT_REGISTRATION — it is a fact about ba59370, not a\n"
        "      pin you own.\n"
        "  If the edit already landed in an earlier commit, name that commit in the\n"
        "  Amendment rather than back-dating anything: the review the same-commit rule\n"
        "  wanted is the review, not the SHA (-65's ruling, LEDGER WT-096)."
    )


def test_the_pinned_digest_is_the_version_REG_012_saw():
    """The anchor froze the REGISTRATION-era §4.7, not merely today's.

    Without this, the anchor is whatever the section happened to be when this file was
    written, and the freeze silently re-anchors to the wrong version — a snapshot wearing a
    freeze's clothes. Skips outside a git work tree, per `test_pin001_code_state.py`.
    """
    found = _digest_at(REG_012_COMMIT)
    if found is None:
        pytest.skip("not a git work tree")
    assert found == SEC_47_AT_REGISTRATION, (
        f"§4.7 at {REG_012_COMMIT[:7]}, the commit that registered REG-012, does not hash to "
        f"the anchor. The anchor describes some other version, so the freeze is not the "
        f"freeze REG-012 wrote. This is NOT repaired by re-pinning: SEC_47_AT_REGISTRATION "
        f"is immutable, so either section_47() changed meaning or history was rewritten."
    )


def test_an_amendment_is_declared_exactly_when_section_47_has_moved():
    """The two ends of the chain, and the emptiness case that keeps warrants honest.

    A warrant that may be declared while nothing moved is a warrant that can be written in
    advance, and a pre-written warrant licenses the next edit before anybody reads it. So
    the list must be empty when §4.7 sits on the registration-era bytes, and non-empty the
    moment it does not.

    **It compares the FILE to the anchor, not `SEC_47_CURRENT` to the anchor.** `-65` wrote
    it the second way first and the mutation pass killed it: `SEC_47_CURRENT` is *derived*
    from `AMENDMENTS`, so deleting the amendments collapses it back onto the anchor, the two
    constants agree, and a test named *"an amendment is declared exactly when §4.7 has
    moved"* reports that no amendment is correctly declared for a section that moved. The
    guard would have been measuring its own bookkeeping instead of the manuscript — `WT-092`
    in the repair for `WT-092`, caught only because every limb was fired before shipping.
    """
    found = digest(section_47(PAPER.read_text(encoding="utf-8")))
    if found == SEC_47_AT_REGISTRATION:
        assert not AMENDMENTS, (
            "§4.7 is byte-identical to the version REG-012 froze, yet AMENDMENTS is not "
            "empty. A warrant for a move that did not happen is a warrant waiting to "
            "license one nobody reviewed."
        )
    else:
        assert AMENDMENTS, (
            "§4.7 differs from the version REG-012 froze and no amendment says why. Either "
            "the edit came from REG-012's outcome (revert it) or it did not (record it)."
        )


def test_every_amendment_moved_section_47_to_the_digest_it_claims():
    """A warrant is checkable or it is decoration.

    Each entry names a commit and the digest §4.7 landed on. Both are facts in git, so both
    are asserted: an amendment whose commit left §4.7 untouched is a licence attached to the
    wrong edit, and an amendment whose digest does not match is a licence attached to a
    different version of the right one. `PIN-001`'s lesson in its own words — a pin with
    nothing watching it is the same defect in a smaller font.
    """
    if _git("rev-parse", "--git-dir") is None:
        pytest.skip("not a git work tree")
    for amendment in AMENDMENTS:
        after = _digest_at(amendment.sha)
        assert after is not None, (
            f"amendment names commit {amendment.sha}, which this repository does not have"
        )
        assert after == amendment.digest_after, (
            f"amendment {amendment.sha} claims §4.7 landed on "
            f"{amendment.digest_after[:16]}…, but at that commit it hashes to {after[:16]}…"
        )
        before = _digest_at(f"{amendment.sha}^")
        assert before is not None and before != after, (
            f"amendment {amendment.sha} did not move §4.7 at all. The licence is attached "
            f"to the wrong commit, and the commit that really moved it has none."
        )


def test_no_amendment_cites_REG_012_as_its_own_licence():
    """Reading (a) may not be laundered into reading (b) by writing it down.

    §6 forbids exactly the edits that come from `REG-012`'s outcome. An amendment whose
    licence is `REG-012` itself is that violation, recorded in the guard's own ledger and
    thereby made to pass — the single failure mode this file exists to prevent, arriving
    through the door the repair opened.
    """
    for amendment in AMENDMENTS:
        flat = " ".join(amendment.licence.split())
        assert "REG-012's outcome" not in flat, (
            f"amendment {amendment.sha} names REG-012's own outcome as its licence. That is "
            f"reading (a) — the violation §6 forbids — and it is reverted, not recorded."
        )
        assert len(flat) >= 40, (
            f"amendment {amendment.sha}'s licence is too short to name anything. A licence "
            f"is what a later reader checks the edit against; 'fixed a typo' is not one."
        )
