#!/usr/bin/env python3
"""
wt122 -- CENSUS BEFORE PATCH for Paper II's two MANDATORY citations.
Session wealthTensor-67.  Card 1217556375636027.

WHY THIS EXISTS (stated in advance, per WT-099 and the wt120 precedent):

Card 1217556375636027 names two placement rules, and BOTH are hypotheses about
counts, not measurements:

  H1  "Bouchaud & Mezard wherever Paper II contrasts the STOCK levy with the
       FLOW levy in terms of the multiplier's shape."       -> how many sites?
  H2  "BBZ 2011 sec 4.1 wherever the r = 1 cap appears."     -> how many sites?

The specific hazard this census exists to find, named before it ran:
  *** IS THE r = 1 CAP ACTUALLY IN A MANUSCRIPT AT ALL, OR ONLY IN docs/ ? ***
A patch script that goes looking for an anchor that does not exist will either
fail loudly (fine) or, worse, be "repaired" by a session that relaxes the anchor
until something matches -- which is how a citation lands on a claim the paper
does not make.  WT-099 says treat "N places" as a hypothesis.  H2's N may be 0.

H3  Are the two works CITED IN THE BODY, or merely LISTED in the reference list?
    "Listed and never cited" is a real defect with a precedent in this project:
    paper-I REVIEW-002 A10.  A reference list entry is not a credit.

H4  WT-094: does any string this patch would anchor on also live in tests/ or
    scripts/ ?  Editing a manuscript string that a test asserts turns a prose
    edit into a red suite.

PREDICATE POSITIVE CONTROLS (WT-101 / SCOUT-001 sec 5.3, the -66 lesson):
  A dark predicate is not evidence of absence until a document you KNOW contains
  the thing has made it fire.  Every probe below names a control document that
  certainly contains its target.  If a probe reports zero live hits AND its
  control did not fire, the zero is a broken matcher, not a finding, and this
  script says so in those words rather than printing a clean table.

WHAT THIS CENSUS EXCLUDES, said out loud:
  - every *.bak-* file (they are history; wt120's rule)
  - .venv/ and .git/ (third-party and object store)
  - non-text extensions
Roots walked are printed at run time, not assumed by the reader.

Whitespace is normalised (runs of whitespace -> single space) before phrase
matching, because the manuscripts are hard-wrapped at 100 columns and every
phrase of interest straddles a newline.  This is wt120's rule and it is the
reason a naive grep under-counts here.

Read-only.  Writes nothing.  Exit 0 always; the verdict is the printed text.
"""

import os
import re
import sys

REPO = os.path.expanduser("~/repos/wealth-tensor")

PROSE_ROOTS = ["docs"]                      # includes docs/papers/**
CODE_ROOTS = ["tests", "scripts", "src"]
EXCLUDE_DIR_PARTS = {".git", ".venv", "__pycache__", "node_modules"}
BAK = re.compile(r"\.bak[-.]")

PAPER_II = os.path.join(REPO, "docs/papers/paper-II-redistribution/paper-II.md")


def norm(s):
    return re.sub(r"\s+", " ", s)


def walk(roots, exts):
    out = []
    for root in roots:
        base = os.path.join(REPO, root)
        for dirpath, dirnames, filenames in os.walk(base):
            dirnames[:] = [d for d in dirnames if d not in EXCLUDE_DIR_PARTS]
            for fn in filenames:
                if not fn.endswith(exts):
                    continue
                if BAK.search(fn):
                    continue
                if fn.startswith("._"):          # macOS AppleDouble sidecars
                    continue
                out.append(os.path.join(dirpath, fn))
    return sorted(out)


def read(path):
    with open(path, "r", encoding="utf-8", errors="replace") as fh:
        return fh.read()


def rel(path):
    return os.path.relpath(path, REPO)


# ---------------------------------------------------------------- probes ----
# Each probe: (name, compiled regex, control file, why the control must fire)

PROBES = [
    (
        "R1_CAP",
        re.compile(r"0\.9524|ess-?sup|essential supremum|bounded above|no power[- ]law", re.I),
        "docs/DECISION-001-A2-and-road-one.md",
        "DECISION-001 line 21 states the r=1 cap in terms: 'ess-sup a = 0.9524'.",
    ),
    (
        "STOCK_VS_FLOW_SHAPE",
        re.compile(
            r"(stock (base|levy)[^.]{0,200}flow (base|levy)|flow (base|levy)[^.]{0,200}stock (base|levy))",
            re.I,
        ),
        "docs/papers/paper-II-redistribution/paper-II.md",
        "Paper II sec 3.1 is built on the stock-vs-flow contrast; if this is dark the matcher is broken.",
    ),
    (
        "TAIL_LANGUAGE",
        re.compile(r"Pareto|tail index|tail exponent|power law|power-law|exponent .?mu|heavy tail", re.I),
        "docs/SCOUT-001-truncation-vs-scaling-prior-art.md",
        "SCOUT-001 is entirely about the tail exponent; a dark result here means the regex is broken.",
    ),
]

NAMES = ["Bouchaud", "Mezard", "Mézard", "Benhabib", "Bisin", "Zhu"]

# Anchors the wt123 patch intends to use.  WT-094 check: each must be unique in
# paper-II.md AND absent from tests/ scripts/ src/.
PROPOSED_ANCHORS = [
    "A levy on stock rescales what a holder has and leaves the process that got them there exactly as it found it; a levy on flow reaches into the multiplicative term itself.",
    "The condensation result is standard in kinetic exchange (Chakrabarti, Chatterjee, Chakravarty and the surrounding literature), where the effect of saving propensity, taxation and redistribution on stationary wealth distributions has been examined from several directions.",
    "Bouchaud, J.-P., & Mézard, M. (2000). Wealth condensation in a simple model of economy. *Physica A*, 282(3), 536–545. ✓",
    "Benhabib, J., Bisin, A., & Zhu, S. (2011). The distribution of wealth and fiscal policy in economies with finitely lived agents. *Econometrica*, 79(1), 123–157. ✓ *(journal and volume verified; page range to re-check)*",
]


def main():
    print("=" * 78)
    print("wt122 CENSUS -- Paper II citation sites (wealthTensor-67)")
    print("=" * 78)
    print(f"repo root      : {REPO}")
    print(f"prose roots    : {PROSE_ROOTS}  (*.md, live only)")
    print(f"code roots     : {CODE_ROOTS}  (*.py, live only)")
    print(f"excluded       : *.bak-* , ._* , {sorted(EXCLUDE_DIR_PARTS)}")
    print("whitespace     : normalised (runs -> single space) before matching")
    print()

    prose = walk(PROSE_ROOTS, (".md",))
    code = walk(CODE_ROOTS, (".py",))
    manuscripts = [p for p in prose if re.search(r"paper-(I|II|III|IV)\.md$", p)]

    print(f"live .md walked : {len(prose)}")
    print(f"live .py walked : {len(code)}")
    print(f"live manuscripts: {len(manuscripts)} -> {[rel(p) for p in manuscripts]}")
    print()

    bodies = {p: norm(read(p)) for p in prose + code}

    # ------------------------------------------------ probes + controls ----
    print("-" * 78)
    print("PROBES  (each with a positive control that MUST fire)")
    print("-" * 78)
    broken = []
    for name, rx, control_rel, why in PROBES:
        control_path = os.path.join(REPO, control_rel)
        control_txt = bodies.get(control_path)
        if control_txt is None:
            control_txt = norm(read(control_path))
        control_hits = len(rx.findall(control_txt))
        fired = control_hits > 0
        print(f"\n[{name}]  control = {control_rel}")
        print(f"    why       : {why}")
        print(f"    CONTROL   : {'FIRED' if fired else '*** DARK ***'}  ({control_hits} hits)")
        if not fired:
            broken.append(name)
            print("    !! This probe is BROKEN.  Its zeros below mean nothing.")

        print("    manuscripts (live):")
        for m in manuscripts:
            n = len(rx.findall(bodies[m]))
            print(f"        {n:4d}  {rel(m)}")
        docs_hits = [(rel(p), len(rx.findall(bodies[p])))
                     for p in prose if p not in manuscripts and rx.search(bodies[p])]
        code_hits = [(rel(p), len(rx.findall(bodies[p])))
                     for p in code if rx.search(bodies[p])]
        print(f"    other docs/ files with hits : {len(docs_hits)}")
        for r, n in docs_hits[:12]:
            print(f"        {n:4d}  {r}")
        print(f"    code files with hits        : {len(code_hits)}")
        for r, n in code_hits[:12]:
            print(f"        {n:4d}  {r}")

    # ------------------------------------------------------ H3: cited? -----
    print()
    print("-" * 78)
    print("H3  LISTED vs CITED IN BODY  (paper-II.md, split at '## References')")
    print("-" * 78)
    raw = read(PAPER_II)
    lines = raw.splitlines()
    ref_idx = next((i for i, l in enumerate(lines) if l.strip() == "## References"), None)
    if ref_idx is None:
        print("    !! no '## References' heading found -- split failed, treat below as unsplit")
        ref_idx = len(lines)
    body = norm("\n".join(lines[:ref_idx]))
    refs = norm("\n".join(lines[ref_idx:]))
    print(f"    body = lines 1..{ref_idx}, references = lines {ref_idx+1}..{len(lines)}")
    for nm in NAMES:
        b = len(re.findall(re.escape(nm), body))
        r = len(re.findall(re.escape(nm), refs))
        verdict = ""
        if r > 0 and b == 0:
            verdict = "  <== LISTED AND NEVER CITED"
        print(f"    {nm:10s} body={b:3d}  references={r:3d}{verdict}")

    # positive control for the body/refs split: paper-I cites Bouchaud in body
    p1 = os.path.join(REPO, "docs/papers/paper-I-price-formation/paper-I.md")
    p1_lines = read(p1).splitlines()
    p1_ref = next((i for i, l in enumerate(p1_lines) if l.strip() == "## References"), len(p1_lines))
    p1_body = norm("\n".join(p1_lines[:p1_ref]))
    ctrl = len(re.findall("Bouchaud", p1_body))
    print(f"\n    CONTROL for the split: 'Bouchaud' in paper-I BODY = {ctrl} "
          f"({'FIRED' if ctrl else '*** DARK -- split logic is broken ***'})")
    if not ctrl:
        broken.append("BODY_REFS_SPLIT")

    # --------------------------------------------- H4: anchor safety -------
    print()
    print("-" * 78)
    print("H4  PROPOSED ANCHOR SAFETY  (WT-094: grep tests/ and scripts/ first)")
    print("-" * 78)
    pii = norm(raw)
    unsafe = 0
    for i, a in enumerate(PROPOSED_ANCHORS, 1):
        na = norm(a)
        in_pii = pii.count(na)
        hits = []
        for p in code:
            c = bodies[p].count(na)
            if c:
                hits.append((rel(p), c))
        # also: other live .md that would be desynced by an edit here
        md_hits = []
        for p in prose:
            if p == PAPER_II:
                continue
            c = bodies[p].count(na)
            if c:
                md_hits.append((rel(p), c))
        flag = "OK" if (in_pii == 1 and not hits) else "*** UNSAFE ***"
        if flag != "OK":
            unsafe += 1
        print(f"\n  anchor {i}: {flag}")
        print(f"    count in paper-II.md (normalised) : {in_pii}   (patch requires exactly 1)")
        print(f"    occurrences in tests/scripts/src  : {hits if hits else 'none'}")
        print(f"    occurrences in other live docs/   : {md_hits if md_hits else 'none'}")
        print(f"    text: {na[:90]}...")

    # ------------------------------------------------------- verdict -------
    print()
    print("=" * 78)
    print("VERDICT")
    print("=" * 78)
    if broken:
        print(f"BROKEN PROBES: {broken}")
        print("Any zero reported by a broken probe is a matcher failure, NOT an absence.")
    else:
        print("predicates_proven_capable_of_firing: ALL")
    print(f"unsafe_anchors: {unsafe}")
    print("Counts above are measurements. Read them before writing wt123's anchors.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
