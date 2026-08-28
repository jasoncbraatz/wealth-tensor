#!/usr/bin/env python3
"""wealthTensor-110 · the voice pass — em-dash texture, measured and converted.

WHY THIS EXISTS
---------------
voice-box's docs/VOICE-SELF-REPORT.md records a MEASUREMENT, not an opinion: against the
pure-Jason band (n=117, measured 2026-08-28) the author's em-dash rate is **zero** --
p75 = 0.0 per thousand words -- and the report names the em-dash-heavy texture explicitly as
"the drafting assistant's habit, not his", with the remedy spelled out in its own words:
*convert them to parentheses, commas, or '..'*.

The v1 manuscripts run 13.5/1k (paper II) and 10.8/1k (paper III). That single statistic is
the largest MEASURABLE distance between these drafts and the author's hand, and it is the
one a script can close without touching an argument.

WHAT THIS IS NOT
----------------
It is not the voice-box. The voice-box is mid-BLUEPRINT, its seven blessed voices were
orphaned by the 2026-08-28 re-ingest, and tools/tier-gate.py --phase 4 refuses a non-FABLE
session outright. A retrieval-driven render is a different, later, human-gated job. This is
the mechanical floor of that job: the one conversion the corpus states as a rule.

WHY IT WORKS ON PARAGRAPHS AND NOT ON LINES
-------------------------------------------
The first cut of this script worked line by line and was wrong, visibly, in the diff. The
manuscripts are hard-wrapped at ~100 columns, so a PAIR of dashes routinely straddles a line
break:

    The process responds to five numbers — the levy's four coordinates and the share
    — and it cannot see where any of them came from.

Line-at-a-time, that is two singles, and the second one produces a line that OPENS with a
comma. Both halves of the pair have to be visible at once, which means the unit of work is
the logical paragraph -- joined, converted, then re-wrapped at the paragraph's own original
measure. Only paragraphs that actually changed are re-wrapped, so the v1-to-v2 diff stays
readable.

WHAT IT DELIBERATELY LEAVES ALONE
---------------------------------
STRUCTURAL em-dashes -- typography rather than prose:

  * a figure caption's label:   **Figure 3 — The design and its own observable...**
  * a run-in bold heading:      **The surviving claim is narrower and better** — ...
  * a markdown heading, a table row, a fenced block, a display-math block

Jason's own standing brief writes headings that way ("## The geography — GitHub is the
SSOT"), so the band's zero is a claim about PROSE, and converting scaffolding would be
applying a prose measurement outside its support. Every skipped instance is reported with
its reason, so the skip list is reviewable rather than invisible.

THE PROSE RULES
---------------
  PAIRED   X — Y — Z    ->  X (Y) Z        the parenthetical the corpus asks for
  SINGLE   X — Y        ->  X, Y           comma, the default
                        ->  X: Y           colon when Y is a definition or a list -- a
                                           comma in front of a phrase that already has
                                           commas in it makes soup, which is a different
                                           defect, not a fix

USAGE
    wt224_voice_pass.py SRC DST            convert, write DST, print the report
    wt224_voice_pass.py SRC --dry-run      print the report only, write nothing
    wt224_voice_pass.py SRC --measure      print the punctuation rates and stop
    wt224_voice_pass.py --selftest         prove the rules on fixtures, touch no manuscript
"""
from __future__ import annotations

import argparse
import pathlib
import re
import sys
import textwrap

EM = "—"
HOLD = "\ue000"   # a dash this pass deliberately left standing, hidden from later rules

LIST_MARK = re.compile(r"^(\s*)(?:[-*+]|\d+\.)\s+")
QUOTE = re.compile(r"^(\s*>\s?)")
HEADING = re.compile(r"^\s{0,3}#")
FENCE = re.compile(r"^\s*(?:```|~~~)")
MATHFENCE = re.compile(r"^\s*\$\$\s*$")


# ---- structural contexts ----------------------------------------------------------------
def structural_reason(para: str, pos: int) -> str | None:
    """Why the em-dash at `pos` in the JOINED paragraph is scaffolding, or None for prose."""
    m = re.match(r"\s*\*\*(.+?)\*\*", para)
    if m:
        if m.start(1) <= pos < m.end(1):
            return "label inside the opening bold run"
        if pos > m.end() and para[m.end() : pos].strip() == "":
            return "run-in bold heading"
    return None


# what follows the dash opens a definition or an enumeration -> colon, not comma
COLON_OPENERS = re.compile(
    r"^\s*(?:the\s+\w+|one|two|three|four|five|six|seven|eight|nine|ten|either|both)\b",
    re.I,
)


def _prose_dashes(para: str) -> list[int]:
    return [i for i, c in enumerate(para) if c == EM and not structural_reason(para, i)]


def convert_paragraph(para: str, log: list, where: str) -> str:
    if EM not in para:
        return para
    for p in (i for i, c in enumerate(para) if c == EM):
        why = structural_reason(para, p)
        if why:
            log.append(("skip", where, why, para[max(0, p - 55) : p + 55]))

    # ---- PAIRED, first: the parenthetical the corpus asks for --------------------------
    guard, skip = 0, 0
    while guard < 60:
        guard += 1
        d = _prose_dashes(para)
        if len(d) < skip + 2:
            break
        a, b = d[skip], d[skip + 1]
        inner = para[a + 1 : b]
        # a pair is only a pair when what sits between the dashes is a PHRASE: no sentence
        # boundary inside it, and short enough to read as an aside rather than a clause
        if inner.strip() and not re.search(r"[.!?]\s+[A-Z(]", inner):
            # Two shapes this pass refuses to convert, and BOTH must be checked before the
            # length gate rather than after it -- an early cut checked length first, so a
            # 250-character parenthesised list fell through to the singles rule and came
            # out as a colon on each side of itself. Refusing is a HUMAN call, not a rule:
            # the dashes stay, and the report says which and why.
            #   * an inner phrase that already carries parentheses would NEST them
            #   * an aside long enough to be a clause is not an aside
            refuse = ("inner phrase already parenthesised (would nest)" if "(" in inner
                      else "aside is %d chars -- a clause, not an aside" % len(inner)
                      if len(inner) > 320 else None)
            if refuse:
                log.append(("defer", where, refuse, inner.strip()[:90]))
                # park BOTH dashes so the singles pass below cannot pick them up either
                para = para[:a] + HOLD + para[a + 1 : b] + HOLD + para[b + 1 :]
                continue
            head, tail = para[:a].rstrip(), para[b + 1 :].lstrip()
            joiner = "" if tail[:1] in ",.;:)" else " "
            # The SECOND dash was sometimes carrying comma duty, and a paren cannot carry it.
            # Two narrow cases where dropping it breaks the sentence, and no others:
            #   * the tail opens with a word that cannot continue a phrase (not, rather, ...)
            #   * the head is a short FRONTED ADVERBIAL ("At rho = 0 — ... — a levy ...")
            sent_head = re.split(r"(?<=[.!?])\s", head)[-1].strip()
            needs_comma = bool(
                re.match(r"(?:not|rather|never|nor|whereas|which|whose)\b", tail, re.I)
            ) or bool(
                len(sent_head) <= 60
                and re.match(r"(?:at|in|on|for|under|with|after|before|by|from|when|if|because|"
                             r"across|through|during|beyond|below|above)\b", sent_head, re.I)
            )
            para = f"{head} ({inner.strip()}){',' if needs_comma else ''}{joiner}{tail}"
            log.append(("paired", where, "-> parentheses" + (" + comma" if needs_comma else ""),
                        f"({inner.strip()[:80]}){',' if needs_comma else ''} {tail[:30]}"))
            skip = 0
            continue
        # THIS candidate is not a pair -- but the SECOND dash may still open one with the
        # third. Abandoning here left "A — B. C — D — E" with three singles, one of which
        # became a colon in front of a subordinate clause.
        skip += 1

    # ---- SINGLES -----------------------------------------------------------------------
    guard = 0
    while guard < 40:
        guard += 1
        d = _prose_dashes(para)
        if not d:
            break
        p = d[0]
        head, rest = para[:p].rstrip(), para[p + 1 :].lstrip()
        if not rest:
            log.append(("defer", where, "trailing dash, nothing follows", head[-70:]))
            para = para[:p] + HOLD + para[p + 1 :]
            continue
        # to the end of this sentence: a tail that already carries commas gets a colon,
        # because a comma in front of it makes soup rather than a parenthetical
        sent = re.split(r"(?<=[.!?])\s", rest)[0]          # forward, to the sentence end
        head_sent = re.split(r"(?<=[.!?])\s", head)[-1]      # backward, to the sentence start
        if head.endswith((",", ":", ";", "(")):
            sep = ""
        elif re.match(r"(?:and|but|or|nor|yet|so|while|whereas|although|though|because|"
                      r"since|unless|whether)\b", rest, re.I):
            # a colon in front of a coordinating conjunction is simply wrong, whatever the
            # rest of the sentence looks like
            sep = ","
        elif COLON_OPENERS.match(rest) or "," in sent or "," in head_sent:
            # a comma here would be the THIRD in one sentence (soup) or, worse, a splice
            sep = ":"
        else:
            sep = ","
        para = f"{head}{sep} {rest}"
        log.append(("single", where, f"-> '{sep or 'space'}'", f"...{head[-45:]}{sep} {rest[:45]}..."))
    return para.replace(HOLD, EM)


# ---- paragraph machinery ----------------------------------------------------------------
def split_paragraphs(lines: list[str]) -> list[tuple[int, int, str]]:
    """Yield (start, end_exclusive, kind) over `lines`. kind is 'prose' or 'verbatim'."""
    out: list[tuple[int, int, str]] = []
    i, in_fence = 0, False
    n = len(lines)
    while i < n:
        ln = lines[i]
        if FENCE.match(ln) or MATHFENCE.match(ln):
            in_fence = not in_fence
            out.append((i, i + 1, "verbatim"))
            i += 1
            continue
        if in_fence or not ln.strip() or HEADING.match(ln) or ln.lstrip().startswith("|"):
            out.append((i, i + 1, "verbatim"))
            i += 1
            continue
        # a prose paragraph: consecutive non-blank lines, broken at a NEW list marker, at a
        # markdown hard break (two trailing spaces), and at any verbatim line
        j = i + 1
        while j < n:
            nxt = lines[j]
            if (
                not nxt.strip()
                or HEADING.match(nxt)
                or FENCE.match(nxt)
                or MATHFENCE.match(nxt)
                or nxt.lstrip().startswith("|")
                or LIST_MARK.match(nxt)
                or lines[j - 1].endswith("  ")
                or lines[j - 1].endswith("\\")
            ):
                break
            # a blockquote may not merge with a non-quote line, either way round
            if bool(QUOTE.match(lines[j - 1])) != bool(QUOTE.match(nxt)):
                break
            j += 1
        out.append((i, j, "prose"))
        i = j
    return out


def rewrap(text: str, first_prefix: str, cont_prefix: str, width: int) -> list[str]:
    body = text
    wrapped = textwrap.wrap(
        body,
        width=width,
        initial_indent=first_prefix,
        subsequent_indent=cont_prefix,
        break_long_words=False,
        break_on_hyphens=False,
        replace_whitespace=True,
        drop_whitespace=True,
    )
    return wrapped or [first_prefix.rstrip()]


def convert_text(text: str, log: list, name: str) -> str:
    lines = text.split("\n")
    out: list[str] = []
    for start, end, kind in split_paragraphs(lines):
        chunk = lines[start:end]
        if kind == "verbatim" or EM not in "\n".join(chunk):
            out.extend(chunk)
            continue
        q = QUOTE.match(chunk[0])
        lm = LIST_MARK.match(chunk[0])
        if q:
            first_prefix = q.group(1)
            cont_prefix = q.group(1)
            stripped = [QUOTE.sub("", l) for l in chunk]
            inner_lm = LIST_MARK.match(stripped[0])
            if inner_lm:
                first_prefix = q.group(1) + stripped[0][: inner_lm.end()]
                cont_prefix = q.group(1) + " " * inner_lm.end()
                stripped[0] = stripped[0][inner_lm.end() :]
            joined = " ".join(s.strip() for s in stripped)
        elif lm:
            first_prefix = chunk[0][: lm.end()]
            cont_prefix = " " * lm.end()
            joined = " ".join([chunk[0][lm.end() :].strip()] + [l.strip() for l in chunk[1:]])
        else:
            indent = re.match(r"\s*", chunk[0]).group(0)
            first_prefix = cont_prefix = indent
            joined = " ".join(l.strip() for l in chunk)

        where = f"{name}:{start + 1}"
        new = convert_paragraph(joined, log, where)
        if new == joined:
            out.extend(chunk)
            continue
        # the block's own measure, but never wider than the corpus wrap -- one long line
        # (a quoted passage, a formula) must not re-wrap the whole paragraph to its width
        width = min(max(max(len(l) for l in chunk), 72), 100)
        out.extend(rewrap(new, first_prefix, cont_prefix, width))
    return "\n".join(out)


def measure(text: str) -> dict:
    w = len(text.split())
    out = {"words": w}
    for name, ch in (("em_dash", EM), ("en_dash", "–"), ("semicolon", ";"), ("paren", "(")):
        n = text.count(ch)
        out[name] = n
        out[name + "_per_1k"] = round(n * 1000 / w, 2) if w else 0.0
    return out


# ---- selftest ---------------------------------------------------------------------------
FIXTURES = [
    # (input, expected, why this case is here)
    (
        "The process responds to five numbers — the levy's four coordinates and the share\n"
        "— and it cannot see where any of them came from.",
        "(the levy's four coordinates and the share)",
        "a PAIR straddling a hard-wrapped line break -- the defect that forced paragraphs",
    ),
    (
        "compared by identity — a wealth tax, zakat, a land value tax — and any comparison",
        "(a wealth tax, zakat, a land value tax)",
        "a pair whose inner phrase carries commas: parens, never comma soup",
    ),
    (
        "> **Figure 1 — Two firms, one filing.** the reported series C(t) for two worlds.",
        "**Figure 1 — Two firms",
        "a caption label is typography and must survive untouched",
    ),
    (
        "**The claim is narrower** — the decisive quantity is realisation.",
        "**The claim is narrower** —",
        "a run-in bold heading is typography and must survive untouched",
    ),
    (
        "## The geography — GitHub is the SSOT",
        "## The geography — GitHub is the SSOT",
        "a markdown heading is never prose",
    ),
    (
        "| **base** | what is assessed — the **stock** held |",
        "assessed — the **stock**",
        "a table row is verbatim",
    ),
    (
        "The frontiers are **nested** — stock 0.000, flow 0.125 — not disjoint.",
        "(stock 0.000, flow 0.125), not disjoint",
        "the second dash was carrying comma duty; a paren cannot, so the comma stays",
    ),
    (
        "At \u03c1 = 0 — the holder whose gains are never realised — a levy leaves it unchanged.",
        "realised), a levy",
        "a short fronted adverbial keeps its comma after the closing paren",
    ),
    (
        "leaves it unchanged — its base is uniform, not absent (\u00a73.2) — and the shape of it.",
        "unchanged — its base is uniform, not absent (\u00a73.2) — and",
        "an inner phrase that is already parenthesised is DEFERRED, never nested",
    ),
    (
        "for a stock base, \u03ba = r exactly — \u00a73.3 raises the threshold and \u03ba falls.",
        "exactly: \u00a73.3 raises",
        "a comma here would splice two clauses in a sentence that already has one",
    ),
    (
        "The stock base truncates the outcome, the flow base damps it — and both fall.",
        "damps it, and both fall",
        "a colon in front of a coordinating conjunction is wrong however soupy the sentence",
    ),
    (
        "It stopped rising — not because it settled but because it ran out. At T the run "
        "reads 0.994 and flat — short of the ceiling it is pinned against — while its top "
        "decile holds everything.",
        "(short of the ceiling it is pinned against),",
        "a rejected first candidate must not abandon the pair the SECOND dash opens",
    ),
    (
        "visible in a statistic nobody reports — the variance of the growth rate.",
        "reports: the variance",
        "a single dash opening a definition takes a colon",
    ),
    (
        "the sweep is what falsified it — and nothing else did.",
        "falsified it, and nothing",
        "an ordinary single dash takes a comma",
    ),
]


def selftest() -> int:
    bad = 0
    for src, expect, why in FIXTURES:
        log: list = []
        got = convert_text(src, log, "fixture")
        ok = expect in got
        print(f"  {'ok  ' if ok else 'FAIL'}  {why}")
        if not ok:
            bad += 1
            print(f"        expected to contain: {expect!r}")
            print(f"        got:                 {got!r}")
    print(f"\n{len(FIXTURES) - bad}/{len(FIXTURES)} fixtures pass")
    return 1 if bad else 0


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("src", nargs="?")
    ap.add_argument("dst", nargs="?")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--measure", action="store_true")
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--quiet", action="store_true")
    a = ap.parse_args()

    if a.selftest:
        return selftest()
    if not a.src:
        ap.error("SRC is required unless --selftest")

    src = pathlib.Path(a.src)
    text = src.read_text(encoding="utf-8")

    if a.measure:
        m = measure(text)
        print(f"{src.name}: {m['words']} words")
        for k in ("em_dash", "en_dash", "semicolon", "paren"):
            print(f"  {k:<10} {m[k]:>5}   {m[k + '_per_1k']:>6}/1k")
        return 0

    log: list = []
    out = convert_text(text, log, src.name)
    b, aft = measure(text), measure(out)
    kinds: dict[str, int] = {}
    for k, *_ in log:
        kinds[k] = kinds.get(k, 0) + 1

    if not a.quiet:
        for kind, where, why, txt in log:
            if kind == "skip":
                continue
            print(f"  {kind:<7} {where:<22} {why}")
            print(f"          {txt}")
    print(f"\n{src.name}")
    print(f"  converted : paired {kinds.get('paired', 0)}  single {kinds.get('single', 0)}")
    print(f"  skipped   : structural {kinds.get('skip', 0)}  deferred {kinds.get('defer', 0)}")
    print(
        f"  em-dash   : {b['em_dash']} ({b['em_dash_per_1k']}/1k)"
        f"  ->  {aft['em_dash']} ({aft['em_dash_per_1k']}/1k)   [Jason band p75 = 0.0/1k]"
    )
    print(
        f"  words     : {b['words']}  ->  {aft['words']}"
        f"    paren {b['paren']} -> {aft['paren']}"
    )
    if aft["words"] != b["words"]:
        print("  note      : word count moved -- a dash that was its own token became "
              "punctuation on a neighbour, which is the conversion working")

    if a.dry_run or not a.dst:
        return 0
    pathlib.Path(a.dst).write_text(out, encoding="utf-8")
    print(f"  wrote     : {a.dst}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
