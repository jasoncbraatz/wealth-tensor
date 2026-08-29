#!/usr/bin/env python3
"""
wt226_public_cut.py — the PUBLIC cut of the v2 pair.

    docs/papers-v2/<dir>/<name>.md   ->   docs/papers-public/<dir>/<name>.md

WHY THIS IS A SEPARATE CUT AND NOT AN EDIT.
docs/papers-v2/ is a GENERATED tree: wt225_build_v2.py rewrites it from the v1 sources on
every build-v2-review.sh run, so a hand edit there survives exactly until the next build.
The public cut is therefore its own generated tree from the same generated input, and the
edit lives HERE, in code, where it is repeatable.

WHAT IT CHANGES, AND WHAT IT DELIBERATELY DOES NOT.
The repository is PUBLIC (github.com/jasoncbraatz/wealth-tensor, and both papers say so in
their Data-and-code section). That single fact settles most of what a naive "strip the
internal references" pass would have destroyed: a reader CAN follow docs/SURVIVALS.md and
docs/RESULT-END-TO-END-001-E1.md, and a supplementary-material section pointing at them is
scholarship, not leakage. So the repo paths STAY. Four things go:

  1. the internal version string  ("Draft -- not yet submitted. Version 1.0, <date>")
     -> a plain preprint line, which is what a public posting actually needs
  2. the contact address          (jason@braatzresearch.com -> jason@braatz.ai)
  3. the AI-assistance disclaimer, which moves FRONT -> END. Convention puts it at the end
     with the other statements about how the work was made, not above the abstract.
  4. one genuinely inside-baseball pointer: PREPRINT-CHECKLIST.md is a process to-do, not a
     record a reader wants.

and one thing is added: a rights line, because the manuscripts carry none (LICENSE is MIT and
covers the software, which is not the prose).

THE SECTION NUMBER IS DERIVED, NOT TYPED. The disclaimer ends "...the repository named in
SS7." In paper III that number was wrong -- it said SS11 while Data-and-code is SS13, a stale
pointer inherited from the canonical cut where it genuinely was SS11. Hardcoding the fix
would just move the bug, so this reads the heading out of the document. A hand-typed
cross-reference is a bug with a delay on it.

Every transform below REFUSES if its subject is missing. A cut that silently no-ops is worse
than one that stops, because the PDF still builds and looks right.
"""
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
SRC_ROOT = REPO / "docs" / "papers-v2"
DST_ROOT = REPO / "docs" / "papers-public"

PAPERS = [
    "paper-II-redistribution/paper-II.md",
    "paper-III-dual-tensor/paper-III.md",
]

OLD_EMAIL = "jason@braatzresearch.com"
NEW_EMAIL = "jason@braatz.ai"

POSTED = "2026-08-29"

RIGHTS = (
    "*© 2026 Jason C Braatz. All rights reserved. This manuscript is made available for "
    "reading and citation; contact the author at " + NEW_EMAIL + " for any other reuse. The "
    "code in the accompanying repository is MIT licensed and carries its own terms.*"
)


def die(msg):
    sys.exit("wt226 REFUSED: " + msg)


def split_front(text, who):
    """Front matter is everything before the first standalone --- rule."""
    lines = text.split("\n")
    for i, ln in enumerate(lines):
        if ln.strip() == "---" and i > 3:
            return lines[:i], lines[i:]
    die(who + ": no front-matter terminator (a standalone --- rule) found")


def take_para(front, opener, who):
    """Pull the paragraph that STARTS with `opener` out of the front matter, return it."""
    start = None
    for i, ln in enumerate(front):
        if ln.startswith(opener):
            start = i
            break
    if start is None:
        die(who + ": front matter has no paragraph starting " + repr(opener))
    end = start
    while end < len(front) and front[end].strip() != "":
        end += 1
    para = front[start:end]
    del front[start:end]
    # collapse the blank line the paragraph left behind
    if start < len(front) and front[start].strip() == "":
        del front[start]
    return para


def reflow_front(front, who):
    """Join each front-matter PROSE paragraph onto one line.

    build.sh pre-processes front matter by appending two trailing spaces to every line
    (a markdown hard break) so the author block stacks -- name / affiliation / address on
    three lines, which is what an author block is. The rule is applied per LINE, so a
    prose paragraph that happens to be hard-wrapped in the source inherits three hard
    breaks and typesets as ragged fragments mid-sentence. Visible in the review build too;
    this pass does not reach into that one, it just does not ship the artefact.

    The fix is on this side of the seam: a paragraph that is ONE source line gets ONE hard
    break, which is a paragraph. The author block is the exception and is left stacked --
    it is identified as the paragraph carrying the contact address rather than by position,
    because position is what rots.
    """
    out, para = [], []

    def flush():
        if not para:
            return
        if any(NEW_EMAIL in ln for ln in para):
            out.extend(para)              # the author block stays stacked
        else:
            out.append(" ".join(ln.strip() for ln in para))
        para.clear()

    for ln in front:
        if ln.strip() == "":
            flush()
            out.append("")
        else:
            para.append(ln)
    flush()
    while out and out[-1].strip() == "":
        out.pop()
    return out


def data_section_number(body, who):
    """Derive the section number of 'Data and code availability' from the headings."""
    for ln in body:
        m = re.match(r"^##\s+(\d+)\s*·\s*Data and code availability\s*$", ln)
        if m:
            return m.group(1)
    die(who + ": no '## N · Data and code availability' heading to derive the cross-reference from")


def cut(rel):
    src = SRC_ROOT / rel
    if not src.is_file():
        die("missing input " + str(src))
    who = rel
    text = src.read_text(encoding="utf-8")
    front, body = split_front(text, who)

    # ---- 3. the AI disclaimer comes OUT of the front matter -----------------------------
    disclaimer = take_para(front, "**Use of AI assistance.**", who)

    # ---- 1. the internal version string goes, a preprint line takes its place -----------
    ver_idx = None
    for i, ln in enumerate(front):
        if ln.startswith("**Draft — not yet submitted.**"):
            ver_idx = i
            break
    if ver_idx is None:
        die(who + ": no '**Draft - not yet submitted.**' line to replace")
    front[ver_idx] = "**Preprint.** Posted " + POSTED + ". Not peer reviewed, not submitted."

    # ---- 2. the contact address --------------------------------------------------------
    hits = sum(ln.count(OLD_EMAIL) for ln in front)
    if hits != 1:
        die(who + ": expected exactly 1 " + OLD_EMAIL + " in the front matter, found " + str(hits))
    front = [ln.replace(OLD_EMAIL, NEW_EMAIL) for ln in front]

    # ---- 3b. and goes back on at the END, with a DERIVED cross-reference ----------------
    n = data_section_number(body, who)
    dtext = "\n".join(disclaimer)
    dtext = re.sub(r"named in §\d+\.", "named in §" + n + ".", dtext)
    if "§" + n + "." not in dtext:
        die(who + ": could not rewrite the disclaimer cross-reference to §" + n)
    # strip the bold run-in label; it becomes a real heading at the end of the paper
    dtext = dtext.replace("**Use of AI assistance.** ", "", 1)

    # ---- 4. the one inside-baseball pointer --------------------------------------------
    body_text = "\n".join(body)
    stale = "are to be re-checked at submission per\n`docs/papers/PREPRINT-CHECKLIST.md`."
    if stale in body_text:
        body_text = body_text.replace(stale, "are to be re-checked at submission.")
    elif "PREPRINT-CHECKLIST" in body_text:
        die(who + ": PREPRINT-CHECKLIST is present but not in the shape this pass knows how to rewrite")

    front = reflow_front(front, who)
    out = "\n".join(front).rstrip() + "\n\n" + body_text.rstrip() + "\n"
    out += "\n---\n\n## Use of AI assistance\n\n" + dtext.strip() + "\n\n---\n\n" + RIGHTS + "\n"

    # ---- belt and suspenders: check the output for what this pass exists to remove ------
    for bad, why in [
        (OLD_EMAIL, "the old contact address survived"),
        ("Draft — not yet submitted", "the internal version string survived"),
        ("PREPRINT-CHECKLIST", "the process-doc pointer survived"),
    ]:
        if bad in out:
            die(who + ": " + why)
    if out.index("## Use of AI assistance") < out.index("## Abstract"):
        die(who + ": the disclaimer is still ahead of the abstract")
    for ln in out.split("\n---\n")[0].split("\n"):
        if ln.startswith("**Declaration of interest.**") and len(ln) < 120:
            die(who + ": the declaration paragraph did not reflow onto one line")
    if out.count(NEW_EMAIL) < 2:
        die(who + ": expected the new address in both the author block and the rights line")

    dst = DST_ROOT / rel
    dst.parent.mkdir(parents=True, exist_ok=True)
    dst.write_text(out, encoding="utf-8")
    print("  ok    %-46s  §%s  %d lines" % (rel, n, out.count("\n")))


def main():
    print("== public cut (docs/papers-v2 -> docs/papers-public)")
    for rel in PAPERS:
        cut(rel)
    print("PUBLIC CUT OK")


if __name__ == "__main__":
    main()
