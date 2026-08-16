#!/usr/bin/env python3
"""wealthTensor-54 · generate the P1x / P3x / P5x apparatus rows from ONE template.

WHY A GENERATOR. -53 cloned Paper III's twelve rows onto Paper IV by hand and the clone
worked, because Papers III and IV happen to share a section numbering and a bold-prefix
house style. Paper II does not. Measured this session: SIX of the twelve legs were keyed to
Paper III's FORMATTING (hard-coded '## 8', '## 9', '## 1[01]', a '^N. **' bold prefix, and
two phrase greps that a line wrap defeats) rather than to the criterion. All six went red on
Paper II for reasons that have nothing to do with whether Paper II satisfies the criterion.

The repair is not to fix six expressions. It is to STOP HAND-CLONING: the rows are emitted
from one template with a per-paper parameter block, so a leg can only differ between papers
where the PAPER genuinely differs. Regenerate with:  python3 scripts/gen_apparatus_rows.py
"""

R = "$HOME/repos/wealth-tensor"

PAPERS = {
    # prefix -> (paper-id, path, comfort-phrase-in-limitation-1, abstract-loss-markers)
    "P1": dict(
        pid="paper-III",
        path="docs/papers/paper-III-dual-tensor/paper-III.md",
        comfort="severe test failed and this paper does not know why",
        loss=("failed", "Jonckheere"),
        loss_desc="The failed prediction appears in the ABSTRACT as well as the body "
                  "(PREPRINT-CHECKLIST D; charter 3.4 -- reported once, and not given the last word)",
    ),
    "P3": dict(
        pid="paper-II",
        path="docs/papers/paper-II-redistribution/paper-II.md",
        comfort="Endogenising ρ would make the flow base",
        loss=("falsified", "nested"),
        loss_desc="The half-failed prediction of 3.1 appears in the ABSTRACT as well as the body. "
                  "II carries no PRE-REGISTERED prediction (PREPRINT-CHECKLIST D scopes those to III and IV), "
                  "but 3.1's 'regardless of rate' claim was tested by this paper's own sweep and lost, and "
                  "charter 3.4 does not care whether a loss was registered -- only that it is not buried",
    ),
    "P5": dict(
        pid="paper-IV",
        path="docs/papers/paper-IV-composition/paper-IV.md",
        comfort="A composed state nobody can read",
        loss=("undecided",),
        loss_desc="The result's own adverse reading appears in the ABSTRACT as well as the body "
                  "(PREPRINT-CHECKLIST D; charter 3.4). REG-013 SURVIVED, so what must reach the abstract is "
                  "the pair that goes UNDECIDED under a stricter ceiling -- the nearest thing this paper has "
                  "to a loss, and it does not get the last word",
    ),
}

# Legs shared verbatim by all three papers. {p} = paper path, {t} = a per-paper temp file.
SHARED = [
    ("b", "Author block carries the name, *Independent researcher* and an email",
     r"""grep -q '^\*\*Jason C. Braatz\*\*' {p} && grep -q '^\*Independent researcher\*' {p} && grep -qE '^[a-z.]+@[a-z.]+' {p}"""),

    ("c", "Keywords line carries 6-8 keywords. The lines are JOINED FIRST: a markdown wrap falling "
          "mid-keyword survives 'tr' as a separator and counts that keyword twice (found by -53 on P1c; "
          "Paper II is the case that proves it -- unjoined it reads 9, joined it reads 8)",
     r"""grep -A1 '^\*\*Keywords:\*\*' {p} | tr '\n' ' ' | tr '·' '\n' | grep -c '[a-z]' | awk '{{exit !($1>=6 && $1<=8)}}'"""),

    ("d", "JEL classification codes present",
     r"""grep -q '^\*\*JEL classification:\*\*' {p}"""),

    ("e", "Explicit numbered contributions list in the introduction. Counts NUMBERED ITEMS, not "
          "numbered-items-that-open-in-bold: Paper II's five contributions open in plain prose and the "
          "bold-prefix form scored them ZERO",
     r"""sed -n '/^\*\*Contributions.\*\*/,/^## 2 /p' {p} | grep -cE '^[0-9]+\. ' | awk '{{exit !($1>=5)}}'"""),

    ("f", "Abandoned approaches is a BODY section, not an appendix (ADR-001: load-bearing in every paper). "
          "Body-ness is now MEASURED -- at least one further numbered section must follow it -- rather than "
          "implied by hard-coding '## 8', which is Paper III's number and Paper II's is 4",
     r"""grep -qE '^## [0-9]+ · Abandoned approaches' {p} && awk '/^## [0-9]+ · Abandoned approaches/{{f=1;next}} f && /^## [0-9]+ · /{{n++}} END{{exit !(n>=1)}}' {p}"""),

    ("h", "Data and code availability names the repo URL, module paths, a regeneration command and the test "
          "command. Section located by NAME (III is 11, IV is 10, II is 7)",
     r"""awk '/^## [0-9]+ · Data and code availability/{{f=1;next}} f && /^## /{{exit}} f' {p} > {t} && grep -q 'github.com/jasoncbraatz/wealth-tensor' {t} && grep -q 'src/wealth_tensor/' {t} && grep -q 'python3 scripts/' {t} && grep -q 'pytest' {t}"""),

    ("i", "No live placeholders. The existence leg is FIRST on purpose: an absence predicate passes vacuously "
          "on a missing file (-49's rule), proved red in-session. The MARKER is what is forbidden, not the "
          "English word: 'placeholder' as a common noun is a MENTION and Paper II 7 legitimately contains one, "
          "so the bare word counts only in caps or delimiters while every other marker stays case-insensitive",
     r"""test -f {p} && ! grep -qiwE 'TBD|TODO|FIXME|XXX' {p} && ! grep -qi 'to be migrated' {p} && ! grep -qE 'PLACEHOLDER|\[[^]]*[Pp]laceholder[^]]*\]|<[^>]*[Pp]laceholder[^>]*>' {p}"""),

    ("j", "The reproducibility paragraph names BOTH overclaim-forbidding tests (PREPRINT-CHECKLIST B)",
     r"""grep -q 'test_excess_demand_is_monotone_here_so_this_is_not_an_SMD_result' {p} && grep -q 'test_a_flat_gini_does_not_mean_a_bounded_one' {p}"""),
]

# Legs whose EXPRESSION is shared but whose ARGUMENT is per-paper.
def leg_a(P):
    return ("Abstract is 150-250 words AND <=1920 characters -- arXiv's hard metadata ceiling "
            "(info.arxiv.org/help/prep.html, re-verified 2026-08-16). Counted on the DECODED string by the "
            "one script all three papers use; wc -w and awk NF disagree across platforms",
            "cd %s && python3 scripts/check_abstract_size.py %s" % (R, P["path"]))


def leg_g(P):
    p, ph = P["path"], P["comfort"]
    return ("Limitations is a numbered list and THE FIRST ITEM runs against the paper's own comfort. Both legs "
            "are now measured where the criterion says they live: the list is found by section NAME, and the "
            "phrase must appear IN ITEM 1 rather than anywhere in the file -- and the item is whitespace-joined "
            "first, because a markdown wrap defeated Paper II's phrase",
            (r"""awk '/^## [0-9]+ · Limitations/{{f=1;next}} f && /^## /{{exit}} f' {p} | grep -cE '^[0-9]+\. \*\*' | awk '{{exit !($1>=4)}}' && """
             r"""awk '/^## [0-9]+ · Limitations/{{f=1;next}} f && /^## /{{exit}} f' {p} | awk '/^1\. /{{g=1}} g && /^2\. /{{exit}} g' | tr '\n' ' ' | tr -s ' ' | grep -qF '{ph}'"""
             ).format(p=p, ph=ph))


def leg_l(P):
    p = P["path"]
    conds = " and ".join("'%s' in t" % m for m in P["loss"])
    py = ("import pathlib;p=pathlib.Path('%s').read_text(encoding='utf-8').split(chr(10));"
          "s=p.index('## Abstract');k=[i for i,l in enumerate(p) if l.startswith('**Keywords')][0];"
          "t=' '.join(p[s+1:k]);raise SystemExit(0 if (%s) else 1)" % (p, conds))
    return (P["loss_desc"],
            'cd %s && python3 scripts/check_abstract_size.py %s >/dev/null && python3 -c "%s"' % (R, p, py))


ROWS = []
for prefix, P in PAPERS.items():
    p, pid = P["path"], P["pid"]
    tmp = "/tmp/wt-sec-%s.txt" % pid
    desc, cmd = leg_a(P)
    ROWS.append((prefix + "a", pid, desc, "cmd:" + cmd))
    for suffix, desc, tmpl in SHARED:
        c = tmpl.format(p=p, t=tmp)
        ROWS.append((prefix + suffix, pid, desc, "cmd:cd %s && %s" % (R, c)))
        if suffix == "e":  # keep alphabetical: e then f then g
            d, c2 = leg_g(P)
            # g is emitted after f below; placeholder to preserve order handled later
    # f and h and i and j already emitted by the loop above in SHARED order (b,c,d,e,f,h,i,j)
    dg, cg = leg_g(P)
    ROWS.append((prefix + "g", pid, dg, "cmd:cd %s && %s" % (R, cg)))
    dl, cl = leg_l(P)
    ROWS.append((prefix + "l", pid, dl, "cmd:" + cl))

# per-paper k and m
K = {
    "P1": ("Pre-registrations cited WITH their registering commit SHAs (PREPRINT-CHECKLIST D)",
           "cmd:cd %s && grep -q 'PRE-001-wt026-observability-lag.md' %s && grep -q 'PRE-002-wt026-peak-to-charge.md' %s && grep -q '9722342' %s && grep -q 'd655501' %s"
           % (R, PAPERS["P1"]["path"], PAPERS["P1"]["path"], PAPERS["P1"]["path"], PAPERS["P1"]["path"])),
    "P5": ("Pre-registration cited WITH its registering commit SHA (PREPRINT-CHECKLIST D)",
           "cmd:cd %s && grep -q 'REG-013-citation-graph-whitespace.md' %s && grep -q 'fff7063' %s"
           % (R, PAPERS["P5"]["path"], PAPERS["P5"]["path"])),
    "P3": ("Pre-registration, scoped by the ratified list rather than waved past. PREPRINT-CHECKLIST D says in "
           "terms that 'Papers III and IV carry empirical predictions; I and II do not', so II owes no "
           "registration -- and this row asserts that CLAUSE is still what the list says, plus a tripwire: the "
           "day Paper II cites a registration it must cite a SHA with it. A criterion that passes because it "
           "does not apply should say WHY, in a check, or it is a blank line wearing a tick",
           "cmd:cd %s && grep -qF 'Papers III and IV carry empirical predictions; I and II do not' docs/papers/PREPRINT-CHECKLIST.md && { ! grep -q 'docs/preregistration/' %s || grep -qE '[0-9a-f]{7}' %s; }"
           % (R, PAPERS["P3"]["path"], PAPERS["P3"]["path"])),
}
M = {
    # RESCOPED 2026-08-16: was "submission-time head-of-repository SHA" (manual, deferred to
    # posting) until Jason ruled posting out of this project. A criterion that can never
    # close is not deferred, it is unreachable, and it reads exactly like the former.
    "_desc": "The data-and-code statement pins a RESOLVABLE commit for the state of the code that produced the numbers -- a pin, never a promise. RESCOPED 2026-08-16 (Jason's ruling): this row said 'submission-time head-of-repository SHA', and posting is outside this project's scope, so it could never close here -- which is worse than a failing row, because it reads as deferred rather than unreachable. The in-scope leg is what a replicator needs TODAY and it is checkable: every 7-hex pin in the section must resolve to a commit in this repository, and the section may not defer its pin to posting",
    "_check": 'cmd:cd $HOME/repos/wealth-tensor && awk \'/^## [0-9]+ · Data and code availability/{f=1;next} f && /^## /{exit} f\' %s > /tmp/wt-pin-%s.txt && ! grep -qi \'to be pinned\' /tmp/wt-pin-%s.txt && PINS=$(grep -ohE \'[*][*][0-9a-f]{7}[*][*]|`[0-9a-f]{7}`\' /tmp/wt-pin-%s.txt | tr -d \'*`\' | sort -u) && test -n "$PINS" && for s in $PINS; do git cat-file -e "${s}^{commit}" || exit 1; done',
}

for prefix, P in PAPERS.items():
    ROWS.append((prefix + "k", P["pid"], K[prefix][0], K[prefix][1]))
    ROWS.append((prefix + "m", P["pid"], M["_desc"],
                 M["_check"] % (P["path"], P["pid"], P["pid"], P["pid"])))

# Paper II only: the count it asserts about its own suite must REGENERATE, not be trusted.
ROWS.append(("P3n", "paper-II",
             "Every count Paper II asserts about its own test suite regenerates from the command that "
             "produces it. The paper says '18 tests' in the abstract and in 1; this row DERIVES the number "
             "from pytest --collect-only and greps for whatever came back, so the check cannot be satisfied "
             "by a constant that drifted. This is Jason's -51 scoping proposal (a) applied to one claim: a "
             "claim naming a count must carry the command that regenerates it",
             "cmd:cd %s && N=$(python3 -m pytest tests/test_redistribution.py --collect-only -q 2>/dev/null | "
             "grep -oE '^[0-9]+ tests collected' | grep -oE '^[0-9]+') && test -n \"$N\" && "
             "grep -q \"$N tests\" %s" % (R, PAPERS["P3"]["path"])))

ORDER = "abcdefghijklmn"
ROWS.sort(key=lambda r: (["P1", "P3", "P5"].index(r[0][:2]), ORDER.index(r[0][2:])))

import io
out = io.StringIO()

# ---------------------------------------------------------------- write back
# Idempotent regenerator: the '#' header and the P1..P10 corpus rows are kept
# VERBATIM (they are hand-maintained judgment); every sub-row is replaced.
# Reversible by construction -- it writes one tracked file git can restore.
import pathlib
# A corpus row is any row whose id is P<digits> -- a SHAPE, not a list of the rows this
# script happened to know about when it was written. It was a tuple ("P1".."P10") until
# 2026-08-16, when Jason's DoD amendment added P11 and P12 and the next regeneration
# would have deleted both without a word. An allowlist that enumerates instances is a
# census that stops counting the day someone adds one.
import re
# THE PREDICATE IS THE COMPLEMENT OF WHAT THIS SCRIPT OWNS, and it took three tries to
# get there. It was a tuple ("P1".."P10"), which would have deleted P11/P12 when Jason
# amended the DoD; then ^P[0-9]+$, which would have deleted P13a..P13g when he specified
# the deliverable. Both asked "is this row one I recognise". The right question is "is this
# row one I EMIT" -- because a generator can enumerate its own output exactly, and can
# never enumerate everything a future session will legitimately add beside it.
# Anything not emitted here is preserved verbatim, in place.
OWNED = None  # set below, once ROWS exists
target = pathlib.Path(__file__).resolve().parent.parent / "docs" / "done-criteria.tsv"
OWNED = {r[0] for r in ROWS}
emit = {rid: "%s\t%s\t%s\t%s" % (rid, pid, " ".join(desc.split()), check)
        for rid, pid, desc, check in ROWS}

old = target.read_text(encoding="utf-8").split("\n")
out, seen = [], set()
for line in old:
    if not line:
        continue
    rid = line.split("\t")[0]
    if line.startswith("#") or rid not in OWNED:
        out.append(line)          # preserved verbatim, in place
        continue
    if rid not in seen:           # replaced in place, order untouched
        out.append(emit[rid])
        seen.add(rid)
for rid, _, _, _ in ROWS:         # newly-introduced rows land at the end
    if rid not in seen:
        out.append(emit[rid])
        seen.add(rid)
target.write_text("\n".join(out) + "\n", encoding="utf-8")
kept = len(out) - len(ROWS)
print("wrote %s: %d row(s) preserved verbatim, %d generated (%s)"
      % (target, kept, len(ROWS), " ".join(r[0] for r in ROWS)))
