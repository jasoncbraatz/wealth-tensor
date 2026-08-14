"""Every commit SHA the manuscript names is also named by an instrument.

WHY THIS EXISTS
---------------
`RESULT-PIN-001.md` records the defect and `RESULT-TERM-002.md` records its shape in the
general: **a load-bearing identifier that occurs only in prose, and never in `scripts/`,
`tests/` or `src/`, is unguarded by construction.** §11 told a replicator that `d655501`
was "the last commit touching `src/`"; `d655501` occurred six times in this repository and
every one of them was prose, so the sentence went on being asserted for nine days after
four commits falsified it. Five sessions of grepping walked past it because grepping
compares text to text, and no amount of text can tell you that a SHA has been overtaken.

PIN-001 repaired the sentence. This repairs the CLASS, in the one place it is mechanical:
a SHA is the only load-bearing identifier in this manuscript that a machine can recognise
on sight. So the rule is stated once, here, and it is checkable — *if paper III names a
commit, some instrument names it too* — and the instrument is then free to assert whatever
that particular pin is supposed to guarantee, as `test_pin001_code_state.py` does.

WHAT IT BUYS, STATED SO NOBODY READS IT AS MORE THAN IT IS
----------------------------------------------------------
It buys the *possibility* of a guard, not a guard. A SHA present in `scripts/` with nothing
asserted about it passes here and is worth almost nothing; that is why this test's failure
message asks for the assertion and not merely for the mention. What it does buy outright is
that the PIN-001 shape cannot be reintroduced silently: the next SHA written into the
manuscript makes this red on the same commit that adds it, which is the only moment anyone
is thinking about what the SHA is supposed to promise. §11 already plans one more — the
submission-time head-of-repository pin, deferred to posting — and this test will meet it
there and ask the question then.

It cannot check a *stale* SHA that is instrumented; that is the instrument's job, and
`LATEST_TOUCH` in `test_pin001_code_state.py` is what does it for the three current pins.
It cannot see a load-bearing identifier that is not SHA-shaped — a section number, a tag
name, a count over a list — which is why `test_term002_count.py` exists separately and why
the corollary is written down in prose as well as in code. And it skips outside a git work
tree, because a source tarball is a legitimate way to read this repository and a red suite
there would be a lie about the paper.
"""

import pathlib
import re
import subprocess

import pytest

ROOT = pathlib.Path(__file__).resolve().parents[1]
PAPER = ROOT / "docs/papers/paper-III-dual-tensor/paper-III.md"
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


def test_every_commit_the_manuscript_names_is_named_by_an_instrument(
    git_repo, instrument_text
):
    paper = PAPER.read_text(encoding="utf-8")
    orphans = []
    for sha in sorted(set(_SHA_SHAPED.findall(paper))):
        if _git("rev-parse", "--verify", "--quiet", f"{sha}^{{commit}}").returncode != 0:
            continue  # hex-shaped, but names no commit — not a pin
        if sha not in instrument_text:
            orphans.append(sha)
    assert not orphans, (
        f"paper III pins {orphans} and no file under {'/, '.join(INSTRUMENT_DIRS)}/ "
        f"mentions them. This is the PIN-001 shape: a SHA that lives only in prose is "
        f"unguarded by construction, because its truth depends on the repository's "
        f"present state and nothing in the repository is watching. Do not fix this by "
        f"pasting the SHA into a comment — write down, in an instrument, the thing the "
        f"pin is supposed to GUARANTEE, and assert it. "
        f"tests/test_pin001_code_state.py is the worked example: it pins per file, and it "
        f"goes red on the next commit that touches a pinned module, which is the only "
        f"moment §11 needs re-reading."
    )
