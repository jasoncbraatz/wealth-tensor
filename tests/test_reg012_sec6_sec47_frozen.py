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

So the pin records **which version it froze**: the digest of §4.7 as it stood at `ba59370`,
the commit that registered `REG-012`, together with that SHA. Three consequences:

* the freeze is anchored to the registration rather than to whenever somebody last ran this
  file — the difference between a freeze and a snapshot;
* `test_the_pinned_digest_is_the_version_REG_012_saw` reads §4.7 out of git at `ba59370` and
  requires it to hash to the pinned value, so the pin cannot drift into describing a later
  state (it skips outside a git work tree, `test_pin001_code_state.py`'s convention, because
  a source tarball is a legitimate way to read this repository);
* the red message states both readings and names the re-pin path, so a legitimate edit moves
  the pin **in the same commit** and says which registration licensed it — the committed-
  baseline pattern `DEFENSIVE-BASELINE.json` uses for G-COACH-3.

WHAT IT CANNOT DO
-----------------
It cannot tell WHY §4.7 changed; nothing in a repository can. It can guarantee that the
question is asked out loud at the moment §4.7 moves, which is the only moment at which
`REG-012` §6 can be violated and the only moment anybody would have known to look.
"""
from __future__ import annotations

import hashlib
import pathlib
import re
import subprocess

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

#: SHA-256 of §4.7 as `REG-012` saw it at that commit. §4.7 has not moved since — verified
#: out of git by `test_the_pinned_digest_is_the_version_REG_012_saw`, not asserted here.
SEC_47_SHA256 = "da24a9f91fc3c00e8aaae37f94754fe9a5ae069fd340f52c1d7c457aa64129bf"

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
    assert found == SEC_47_SHA256, (
        "§4.7 has changed since REG-012 was registered at "
        f"{REG_012_COMMIT[:7]}.\n"
        f"  pinned  {SEC_47_SHA256}\n  current {found}\n\n"
        "REG-012 §6: 'no sentence of the manuscript's §4.7 is changed by any outcome of it.'\n"
        "TWO READINGS, AND ONLY THE AUTHOR OF THE EDIT KNOWS WHICH:\n"
        "  (a) the edit came from REG-012's outcome — that is the violation, and REG-012 is\n"
        "      closed on branch F, so the edit is reverted, not re-pinned;\n"
        "  (b) the edit came from anywhere else — legitimate. Re-pin SEC_47_SHA256 in the\n"
        "      SAME commit as the edit, and name the registration or ruling that licensed\n"
        "      it in the commit message. A pin moved in a later commit is a pin nobody\n"
        "      reviewed."
    )


def test_the_pinned_digest_is_the_version_REG_012_saw():
    """The pin froze the REGISTRATION-era §4.7, not merely today's.

    Without this, `SEC_47_SHA256` is whatever the section happened to be when this file was
    written, and the freeze silently re-anchors to the wrong version — a snapshot wearing a
    freeze's clothes. Skips outside a git work tree, per `test_pin001_code_state.py`.
    """
    blob = _git("show", f"{REG_012_COMMIT}:{PAPER_REL}")
    if blob is None:
        pytest.skip("not a git work tree")
    assert digest(section_47(blob)) == SEC_47_SHA256, (
        f"§4.7 at {REG_012_COMMIT[:7]}, the commit that registered REG-012, does not hash to "
        f"the pinned digest. The pin describes some other version, so the freeze is not the "
        f"freeze REG-012 wrote."
    )
