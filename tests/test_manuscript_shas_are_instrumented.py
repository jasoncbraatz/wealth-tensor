"""Every commit SHA **any** manuscript names is also named by an instrument.

WHY THIS EXISTS
---------------
`RESULT-PIN-001.md` records the defect and `RESULT-TERM-002.md` records its shape in the
general: **a load-bearing identifier that occurs only in prose, and never in `scripts/`,
`tests/` or `src/`, is unguarded by construction.** §11 told a replicator that `d655501`
was "the last commit touching `src/`" and that it "is verifiable now". It was true on
2026-08-05 and false by 2026-08-10, falsified not by an error but by four subsequent
commits. The manuscript went on asserting it for nine days because grepping compares text
to text, and no amount of text can tell you that a SHA has been overtaken.

PIN-001 repaired the sentence. It then said it repaired **the CLASS** — and hardcoded one
manuscript of four.

WHY IT IS A GLOB, `-65`
------------------------
`-64` measured the census across all four manuscripts and found the class defect intact in
the newest paper: Paper IV §10 pinned `5efe626` — *"the last commit touching
`scripts/reg013_citation_whitespace.py`"* — in prose, named by no file under `scripts/`,
`tests/` or `src/`. Paper II had carried the `d655501` sentence **verbatim** since
`f1ceac7`, false since 2026-08-10, and it was **absent from `PIN-001`'s own census** of six
prose occurrences. Two of the four papers, and the instrument written to prevent exactly
this could not see either of them, because its subject was a constant.

`WT-092`: *what is the widest object this check's own words claim, and what is the narrowest
thing it actually touches?* This file's own docstring said **CLASS**. It touched
`paper-III.md`. Widening it to `docs/papers/*/paper-*.md` is the smallest edit that makes
the words true, and the ordering matters — **widening this file BEFORE instrumenting Paper
IV's pin goes red**, which is how `-65` verified the orphan was real rather than a census
artefact: the widened test was run against the un-instrumented registry first, went red
naming exactly `paper-IV.md 5efe626`, and went green when `LATEST_TOUCH` learned the
module. A red that arrives on schedule is the measurement.

The glob is the subject now, so a **fifth** manuscript is covered on the day it is added
rather than on the day somebody remembers this file exists. That is the actual class
repair; the previous one was a repair of one instance wearing the word "class".

WHAT IT BUYS, STATED SO NOBODY READS IT AS MORE THAN IT IS
----------------------------------------------------------
It buys the *possibility* of a guard, not a guard. A SHA present in `scripts/` with nothing
asserted about it passes here and is worth almost nothing; that is why this test's failure
message asks for the assertion and not merely for the mention. What it does buy outright is
that the PIN-001 shape cannot be reintroduced silently: the next SHA written into **any**
manuscript makes this red on the same commit that adds it, which is the only moment anyone
is thinking about what the SHA is supposed to promise. §11 already plans one more — the
submission-time head-of-repository pin, deferred to posting — and this test will meet it
there and ask the question then.

It cannot check a *stale* SHA that is instrumented; that is the instrument's job, and
`LATEST_TOUCH` in `test_pin001_code_state.py` is what does it for the current pins. It
cannot see a load-bearing identifier that is not SHA-shaped — a section number, a tag name,
a count over a list — which is why `test_term002_count.py` exists separately and why the
corollary is written down in prose as well as in code. And it skips outside a git work
tree, because a source tarball is a legitimate way to read this repository and a red suite
there would be a lie about the papers.

A TRAP THE NEXT WIDENING SHOULD NOT FALL INTO
----------------------------------------------
`test_pin001_code_state.py`'s `ROTTED` check asserts the phrase *"last commit touching"* is
**absent** from paper III, because there it was the rotted whole-directory claim. Paper IV
§10 uses the same words correctly — *"the last commit touching
`scripts/reg013_citation_whitespace.py`"* — which is the per-file form `PIN-001` **chose as
the remedy**. Widening `ROTTED` by glob the way this file was widened would go red on a
correct pin. The rot was never the phrase; it was the phrase with a directory after it.
"""

import pathlib
import re
import subprocess

import pytest

ROOT = pathlib.Path(__file__).resolve().parents[1]

#: Every manuscript, discovered rather than listed. `*.bak-*` siblings do not end in `.md`
#: and are not matched; a new paper is covered the day its file lands.
PAPERS = sorted((ROOT / "docs/papers").glob("*/paper-*.md"))

INSTRUMENT_DIRS = ("scripts", "tests", "src")

#: Abbreviated-SHA shape, narrowed twice so English cannot trip it: the token must carry
#: both a digit and a hex letter, and it must resolve to a real commit in this repository.
#: "decade" has no digit, "1136838" has no letter, and a plausible-looking token that names
#: no commit is not a pin.
_SHA_SHAPED = re.compile(r"\b(?=[0-9a-f]*[0-9])(?=[0-9a-f]*[a-f])[0-9a-f]{7,12}\b")


def _git(*args: str) -> subprocess.CompletedProcess:
    return subprocess.run(
        ["git", "-C", str(ROOT), *args], capture_output=True, text=True
    )


@pytest.fixture(scope="module")
def git_repo() -> None:
    proc = _git("rev-parse", "--is-inside-work-tree")
    if proc.returncode != 0 or proc.stdout.strip() != "true":
        pytest.skip("not a git work tree — a SHA cannot be resolved here")


@pytest.fixture(scope="module")
def instrument_text() -> str:
    out = []
    for d in INSTRUMENT_DIRS:
        for path in sorted((ROOT / d).rglob("*.py")):
            out.append(path.read_text(encoding="utf-8", errors="ignore"))
    return "\n".join(out)


def test_the_glob_still_finds_every_manuscript():
    """The subject is discovered, so the discovery is the thing that can silently empty.

    A glob that matches nothing passes every downstream assertion vacuously — `-49`'s rule
    that an absence predicate passes on a missing file, arriving here through the door the
    widening opened. Four papers today; the floor is what stops a renamed directory from
    turning this file green by deleting its subject.
    """
    assert len(PAPERS) >= 4, (
        f"expected at least the four manuscripts, found {[p.name for p in PAPERS]}. "
        f"If a paper moved, this file's glob moved with it and the SHAs in the paper that "
        f"left are unguarded again."
    )


def test_every_commit_any_manuscript_names_is_named_by_an_instrument(
    git_repo, instrument_text
):
    orphans = []
    for paper_path in PAPERS:
        paper = paper_path.read_text(encoding="utf-8")
        for sha in sorted(set(_SHA_SHAPED.findall(paper))):
            if _git("rev-parse", "--verify", "--quiet",
                    f"{sha}^{{commit}}").returncode != 0:
                continue  # hex-shaped, but names no commit — not a pin
            if sha not in instrument_text:
                orphans.append(f"{paper_path.name} {sha}")
    assert not orphans, (
        f"these manuscripts pin {orphans} and no file under {'/, '.join(INSTRUMENT_DIRS)}/ "
        f"mentions them. This is the PIN-001 shape: a SHA that lives only in prose is "
        f"unguarded by construction, because its truth depends on the repository's "
        f"present state and nothing in the repository is watching. Do not fix this by "
        f"pasting the SHA into a comment — write down, in an instrument, the thing the "
        f"pin is supposed to GUARANTEE, and assert it. "
        f"tests/test_pin001_code_state.py is the worked example: it pins per file, and it "
        f"goes red on the next commit that touches a pinned module, which is the only "
        f"moment the disclosure needs re-reading."
    )
