#!/usr/bin/env python3
"""G-SEC. A section number a handoff names must EXIST in the paper it names.

WHY (SM 1217564707330383, filed by big-wealthTensor-70 off WT-112). `-69`'s HANDOFF.md
assigned `-70` to read "Paper IV §4-§11" -- in the prose at-bat, in the `next_at_bat`
front-matter field and in the forcing line. Paper IV's last numbered section is §10; §11
is PAPER III's number for Limitations. The wrong number was inherited from a sibling
manuscript, repeated three times, and survived a full gate pass (v2.60, PASS, CANNOT
VERIFY: 0). Nothing was missed that day -- but the next reader of that phrase goes looking
for a section that does not exist, and the gate that reads the file had nothing to say.

The board already locates paper sections BY NAME per paper, precisely because hard-coding
`## 8` was a defect once (done-criteria.tsv P5h records "III is 11, IV is 10, II is 7").
A handoff that names a section RANGE is making the same hard-coded claim.

TWO DESIGN CONSTRAINTS, both inherited from checks that got them wrong:

1. THE SCOPE IS REPORTED, NEVER INFERRED-AND-ROUNDED-UP. `wealthTensor-95` shipped a
   self-discovering claims check that found 9 of 14 assertions and printed FULL COVERAGE;
   a check whose scope is discovered reports the scope it managed to PARSE, and from the
   outside that is indistinguishable from the scope that exists. So this leg prints four
   numbers every run -- checked, unscoped, in-code-span, unknown-paper -- and an unscoped
   reference is loudly NOT CHECKED rather than quietly counted as fine.

2. A NEGATIVE GREP CANNOT TELL USE FROM MENTION. `placeholders_left()` in handoff_gate.py
   already carries that lesson (wealthTensor-94: the gate refused a handoff whose only
   offence was DOCUMENTING the markers it bans). A `§5.4` inside backticks is a quotation
   of somebody else's text, so inline code spans are blanked before scanning and counted
   separately, not asserted against.

Falsifier, run by --selftest on every invocation of the drill: a handoff naming "Paper IV
§4-§11" MUST fail, and one naming "Paper IV §4-§10" MUST pass. A control that has never
been shown to fire is a note, not a control.

  python3 scripts/wt_handoff_sections.py            # check docs/HANDOFF.md
  python3 scripts/wt_handoff_sections.py --selftest # positive + negative controls

Exit 0 = pass, 1 = BLOCKER (a named section does not exist), 2 = CANNOT VERIFY (no papers
found on disk, so the assertion could not be made at all -- which is not a pass).
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
HANDOFF = ROOT / "docs" / "HANDOFF.md"

# How far back from a section reference we will look for the paper it belongs to. Same
# LINE only: a paper named two paragraphs up is not scope, it is a guess.
SCOPE_CHARS = 140

PAPER_RE = re.compile(r"\bpapers?[\s-]+(IV|III|II|I)\b", re.IGNORECASE)
# A reference is a section sign followed by a number, optionally dotted (§4.10 -> §4) and
# optionally a range (§4-§11, §§2-3, §4--§11, §4–’11). Endpoints are asserted;
# the interior is not, because a gap between two real headings is a different defect.
REF_RE = re.compile(
    r"§{1,2}\s*(\d+)(?:\.\d+)*"
    r"(?:\s*(?:-{1,2}|–|—|to)\s*§{0,2}\s*(\d+)(?:\.\d+)*)?"
)
CODE_SPAN_RE = re.compile(r"`[^`\n]*`")


def strip_code_spans(text):
    """Blank inline code spans, PRESERVING LENGTH so offsets stay meaningful."""
    return CODE_SPAN_RE.sub(lambda m: " " * len(m.group(0)), text)


def discover_papers(root=ROOT):
    """roman numeral -> path, globbed the same way handoff_gate.PAPERS is."""
    found = {}
    for path in sorted((root / "docs" / "papers").glob("*/paper-*.md")):
        m = re.fullmatch(r"paper-(IV|III|II|I)", path.stem)
        if m:
            found[m.group(1).upper()] = path
    return found


def paper_sections(path):
    """The numbered level-2 headings a paper actually has."""
    nums = set()
    for line in path.read_text().split("\n"):
        m = re.match(r"##\s+(\d+)\b", line)
        if m:
            nums.add(int(m.group(1)))
    return nums


def scan(text, sections_by_paper):
    """-> (problems, stats). sections_by_paper maps 'IV' -> set of section numbers."""
    stripped = strip_code_spans(text)
    stats = {"checked": 0, "unscoped": 0, "in_code_span": 0, "unknown_paper": 0}
    stats["in_code_span"] = len(REF_RE.findall(text)) - len(REF_RE.findall(stripped))
    problems, unknown = [], set()

    for line in stripped.split("\n"):
        papers = [(m.end(), m.group(1).upper()) for m in PAPER_RE.finditer(line)]
        for ref in REF_RE.finditer(line):
            prior = [p for p in papers if p[0] <= ref.start()
                     and ref.start() - p[0] <= SCOPE_CHARS]
            if not prior:
                stats["unscoped"] += 1
                continue
            roman = prior[-1][1]
            known = sections_by_paper.get(roman)
            if known is None:
                stats["unknown_paper"] += 1
                unknown.add(roman)
                continue
            for n in {int(g) for g in ref.groups() if g is not None}:
                stats["checked"] += 1
                if n not in known:
                    problems.append(
                        "G-SEC: the handoff names Paper %s %s, but paper-%s has no §%d "
                        "(its numbered sections are %s). A section number inherited from a "
                        "sibling manuscript reads exactly like a correct one."
                        % (roman, ref.group(0).strip(), roman, n,
                           "§" + ", §".join(str(x) for x in sorted(known))))
    for roman in sorted(unknown):
        problems.append(
            "G-SEC CANNOT VERIFY: the handoff cites Paper %s and no docs/papers/*/paper-%s.md "
            "is on disk, so the section numbers were NOT checked." % (roman, roman))
    return problems, stats


def sections_leg(path=None, quiet=False):
    """The gate's entry point. Returns a list of problem strings."""
    path = Path(path) if path else HANDOFF
    papers = discover_papers()
    if not papers:
        msg = ("G-SEC CANNOT VERIFY: no docs/papers/*/paper-*.md found, so no section "
               "reference in the handoff could be checked against anything.")
        if not quiet:
            print("  " + msg)
        return [msg]
    sections_by_paper = {roman: paper_sections(p) for roman, p in papers.items()}
    problems, stats = scan(path.read_text(), sections_by_paper)
    if not quiet:
        print("G-SEC: %d paper(s) on disk (%s); %d section ref(s) checked, %d unscoped "
              "(NOT checked -- no paper named within %d chars on the line), %d inside code "
              "spans (mention, not use), %d citing a paper not on disk."
              % (len(papers), ", ".join(sorted(papers)), stats["checked"], stats["unscoped"],
                 SCOPE_CHARS, stats["in_code_span"], stats["unknown_paper"]))
    return problems


# --------------------------------------------------------------------------- controls
# Hermetic, sub-second, no network, no repo state. Every case names what it proves.
CONTROLS = [
    ("NEGATIVE -- the WT-112 defect itself must FAIL",
     "next_at_bat: read Paper IV §4-§11 and report.", 1),
    ("NEGATIVE -- en-dash range, the form the ledger actually used",
     "Your at-bat is Paper IV §4–§11.", 1),
    ("NEGATIVE -- a bare over-range single ref must FAIL",
     "See Paper II §9 for the limitations.", 1),
    ("NEGATIVE -- a dotted subsection whose PARENT does not exist must FAIL",
     "Paper IV §11.2 is the one to read.", 1),
    ("POSITIVE -- the correct range must PASS",
     "next_at_bat: read Paper IV §4-§10 and report.", 0),
    ("POSITIVE -- a real single ref must PASS", "Paper III §11 is Limitations.", 0),
    ("SCOPE -- a ref with no paper named on the line is UNSCOPED, not a pass and not a fail",
     "because §911 opens with a floor that three passes read as a ceiling", 0),
    ("SCOPE -- a paper named too far away does not silently claim the ref",
     "Paper IV " + "x" * (SCOPE_CHARS + 10) + " §911 here", 0),
    ("MENTION -- a ref inside a code span is not asserted against",
     "Paper IV `§911` is quoted, not claimed.", 0),
    ("MENTION -- an unknown paper is CANNOT VERIFY, never a silent pass",
     "Paper I §1 is fine.", 1),
]
# The last control's paper is deliberately absent from the fixture registry below.
FIXTURE = {"II": {1, 2, 3, 4, 5, 6, 7}, "III": set(range(1, 12)), "IV": set(range(1, 11))}


def selftest():
    failures = 0
    for name, text, want in CONTROLS:
        problems, stats = scan(text, FIXTURE)
        got = 1 if problems else 0
        mark = "ok  " if got == want else "FAIL"
        if got != want:
            failures += 1
        print("  %s %s" % (mark, name))
        if got != want:
            print("       wanted %d problem-state, got %d: %s" % (want, got, problems))
    # The scope controls must be UNSCOPED, not merely problem-free -- a check that stopped
    # finding references at all would pass every POSITIVE case above.
    _, stats = scan(CONTROLS[6][1], FIXTURE)
    if stats["unscoped"] != 1:
        print("  FAIL scope accounting: expected 1 unscoped, got %r" % (stats,))
        failures += 1
    _, stats = scan(CONTROLS[8][1], FIXTURE)
    if stats["in_code_span"] != 1 or stats["checked"] != 0:
        print("  FAIL code-span accounting: %r" % (stats,))
        failures += 1
    print("G-SEC selftest: %d control(s), %d failed." % (len(CONTROLS) + 2, failures))
    return 1 if failures else 0


def main():
    if "--selftest" in sys.argv[1:]:
        return selftest()
    problems = sections_leg()
    if not problems:
        print("G-SEC OK: every section number the handoff names exists in the paper it names.")
        return 0
    for p in problems:
        print("  - %s" % p)
    return 2 if all("CANNOT VERIFY" in p for p in problems) else 1


if __name__ == "__main__":
    sys.exit(main())
