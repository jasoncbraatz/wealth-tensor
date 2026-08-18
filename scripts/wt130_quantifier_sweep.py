#!/usr/bin/env python3
"""wt130 — the QUANTIFIER SWEEP, as an instrument (WT-115, wealthTensor-72).

WHY THIS EXISTS. Every review technique this project had built reads a sentence and
asks whether it is true. A quantifier defect is not a property of a sentence — it is
a claim about a SET, and the set a quantifier ranges over is finished BELOW it. So the
falsifier is never local and never upstream, and a census (what does the text say), an
identity guard (did this body survive) and a positional criterion (where does this sit)
are all structurally incapable of finding one. Three axes; this is the third.

WHAT IT DOES. Enumerates every quantifier token in a manuscript with its line number.
That list is the COVERAGE CLAIM: unlike "I read it carefully", it is countable, it is
reproducible, and a later pass can diff it. The tool does NOT decide whether a
quantifier is false — that is the reviewer's read-forward. It guarantees the reviewer
knows how many there were and misses none by inattention.

HOW TO USE IT. For each line printed, read FORWARD to the end of the document asking
one question: does anything below this sentence belong to the set it just counted, and
is it in it? Both II-17 and II-18 (wealthTensor-71) and all three of II-19/II-20/II-21
(wealthTensor-72) fell out of exactly that, after surviving four to five prior passes.

A COUNTING NOTE, because the first reading of this output was wrong and travelled three
documents deep. "N lines" means LINES THAT CARRY A QUANTIFIER, never manuscript length --
Paper III is 864 tokens on 668 such lines and is 2,685 lines long. Every print site below
now says so; do not restate it as a manuscript size (wealthTensor-73, LEDGER WT-119 §1).

    python3 scripts/wt130_quantifier_sweep.py                 # all four manuscripts, counts
    python3 scripts/wt130_quantifier_sweep.py paper-II        # one paper, full enumeration
    python3 scripts/wt130_quantifier_sweep.py paper-II --md   # markdown, for a REVIEW doc

A SELECTOR NOTE, because the second line above was ambiguous for as long as it existed
(wealthTensor-79, II-39). The selector was a bare substring test, and `paper-II` is a
PREFIX of `paper-III` while `paper-I` is a prefix of all four -- so `paper-II` swept TWO
manuscripts and `paper-I` swept FOUR, and the LAST TOTAL printed belonged to a paper the
caller had not asked for. That is the precise delivery mechanism for the misreading banked
at -73. A selector now matches a manuscript's STEM or its DIRECTORY NAME exactly, or a
hyphen-delimited prefix of the directory name; anything else exits non-zero and says so,
because a loud failure is worth more than a silent second manuscript.
"""
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
PAPERS = sorted((ROOT / "docs" / "papers").glob("*/paper-*.md"))

# Deliberately literal and deliberately short. A clever regex here would be a guard
# that cannot fail. Add a token when a real defect escapes the list, not before.
TOKENS = (
    "every", "all", "none", "no", "only", "never", "both", "two", "three", "four",
    "exactly", "any", "each", "always", "single", "entire", "everything", "nothing",
    "one of", "sole", "solely", "whole", "the whole", "at every",
)
PAT = re.compile(r"\b(" + "|".join(re.escape(t) for t in TOKENS) + r")\b", re.I)


def sweep(path):
    """-> (rows, token_count). rows = [(lineno, sorted tokens, text)]."""
    rows, n = [], 0
    for i, line in enumerate(path.read_text(encoding="utf-8").split("\n"), 1):
        ms = PAT.findall(line)
        if ms:
            n += len(ms)
            rows.append((i, sorted({m.lower() for m in ms}), line.strip()))
    return rows, n


def _selects(s, p):
    """Does selector `s` name manuscript `p`? (wealthTensor-79, II-39.)

    Exact on the stem or the directory name, or a hyphen-delimited prefix of the directory
    name. NOT a bare substring test: `paper-II` is a prefix of `paper-III` and `paper-I` of
    all four, so the substring form silently swept the wrong SET and printed someone else's
    TOTAL last. `paper-II` -> stem match, one paper. `paper-II-redistribution` -> directory
    match. `II` -> no match, and main() exits non-zero rather than sweeping two.
    """
    return s == p.stem or s == p.parent.name or p.parent.name.startswith(s + "-")


def n_lines(path):
    """The manuscript's own length. Kept beside the sweep's count because the two were
    conflated once: `wt130`'s "N lines" is lines that CARRY a quantifier (wealthTensor-73,
    LEDGER WT-119 §1)."""
    return len(path.read_text(encoding="utf-8").splitlines())


def main(argv):
    md = "--md" in argv
    sel = [a for a in argv if not a.startswith("--")]
    papers = [p for p in PAPERS if not sel or any(_selects(s, p) for s in sel)]
    if not papers:
        sys.exit(f"no manuscript matched {sel!r}; have: {[p.parent.name for p in PAPERS]}")

    for p in papers:
        rows, n = sweep(p)
        rel = p.relative_to(ROOT)
        if len(papers) > 1 and not sel:
            print(f"{p.parent.name:28s} {n:4d} quantifier tokens on "
                  f"{len(rows):4d} of its {n_lines(p):5d} lines")
            continue
        head = (f"{rel} — {n} quantifier tokens on {len(rows)} lines that carry one, "
                f"of {n_lines(p)} in the manuscript")
        print(f"**{head}**\n" if md else f"{head}\n{'=' * len(head)}")
        for ln, toks, text in rows:
            t = ",".join(toks)
            body = text[:150]
            print(f"| {ln} | `{t}` | {body} |" if md else f"{ln:5d} [{t}]  {body}")
        print(f"\nTOTAL: {n} tokens on {len(rows)} lines that carry one; "
              f"the manuscript is {n_lines(p)} lines long")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
