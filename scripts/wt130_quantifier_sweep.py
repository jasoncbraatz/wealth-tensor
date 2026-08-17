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

    python3 scripts/wt130_quantifier_sweep.py                 # all four manuscripts, counts
    python3 scripts/wt130_quantifier_sweep.py paper-II        # one paper, full enumeration
    python3 scripts/wt130_quantifier_sweep.py paper-II --md   # markdown, for a REVIEW doc
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


def main(argv):
    md = "--md" in argv
    sel = [a for a in argv if not a.startswith("--")]
    papers = [p for p in PAPERS if not sel or any(s in str(p) for s in sel)]
    if not papers:
        sys.exit(f"no manuscript matched {sel!r}; have: {[p.parent.name for p in PAPERS]}")

    for p in papers:
        rows, n = sweep(p)
        rel = p.relative_to(ROOT)
        if len(papers) > 1 and not sel:
            print(f"{p.parent.name:28s} {len(rows):4d} lines  {n:4d} quantifier tokens")
            continue
        head = f"{rel} — {n} quantifier tokens on {len(rows)} lines"
        print(f"**{head}**\n" if md else f"{head}\n{'=' * len(head)}")
        for ln, toks, text in rows:
            t = ",".join(toks)
            body = text[:150]
            print(f"| {ln} | `{t}` | {body} |" if md else f"{ln:5d} [{t}]  {body}")
        print(f"\nTOTAL: {n} tokens / {len(rows)} lines")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
