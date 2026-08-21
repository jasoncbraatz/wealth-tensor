#!/usr/bin/env python3
"""wt184 — A3' MECHANISED: does the referent CARRY what the pointer says?

wt133 (A3) asks whether a `§N.M` reference RESOLVES: does a section with that number
exist? It has printed `0 unresolved` on every manuscript for twenty sessions.

wealthTensor-99 (Paper II, II-40) opened the CORRECTNESS question by hand: §7 pointed a
number at §3.2 when the number lives in §3.3, and wt133 was green because §3.2 exists.
wealthTensor-100 applied it to Paper IV by hand, on all 97 references, and wrote down as
its biggest tee-up that the check should be SCRIPTED, with two rules and a negative
control.  This is that script.

    RULE 1 — NUMBER CARRIED.  A clause that names a section AND states a numeric literal
             asserts that the number is in that section.  The number must appear in the
             named section's own text.
    RULE 2 — PHRASE CARRIED.  A clause that names a section AND quotes a phrase asserts
             the phrase is in that section.  The phrase must appear there AFTER markdown
             emphasis is stripped from BOTH sides.  (wealthTensor-100 lost a finding to
             exactly this: a checker called "emphatically not" ABSENT from §A.2.2, which
             contains `emphatically **not**`.)

WHAT IT CANNOT SEE, stated so no pass credits it with more than it does:
  * bare `§N` forms with no subsection are resolved, but a claim pointed at a whole
    top-level section is weak evidence either way; they are reported in their own bucket.
  * a pointer at ANOTHER document's section (`paper-II §3.1`) is out of scope: this
    script reads one manuscript.  They are counted and listed, never adjudicated.
  * a number that is CORRECT but stated in different units in the target section
    (0.05% vs 5e-4) is flagged.  Flags are CANDIDATES for a human read, not verdicts.
  * it says nothing about whether the number is TRUE — only about whether the pointer
    points at a section that carries it.  A2/A4/A5 own truth.

SECTION BOUNDING: a section runs from its own heading to the NEXT heading of ANY level.
`§4` therefore does NOT contain `§4.4`'s text.  That is deliberate and is the strict
reading; a claim that relies on the loose reading shows up as a flag and gets read.

Exit 0 always in report mode; --postconditions exits non-zero if a post-condition fails.
"""
from __future__ import annotations
import re, sys, unicodedata
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]

# ---------------------------------------------------------------- normalisation
def strip_emphasis(s: str) -> str:
    """Remove markdown emphasis and code ticks; collapse whitespace; unify quotes/dashes."""
    s = s.replace(' ', ' ')
    s = re.sub(r'\*\*\*|\*\*|\*|__|_|`', '', s)
    s = s.replace('’', "'").replace('‘', "'")
    s = s.replace('“', '"').replace('”', '"')
    s = s.replace('—', '-').replace('–', '-').replace('−', '-')
    s = re.sub(r'\s+', ' ', s)
    return s.strip()

def norm_num(tok: str) -> str:
    """Normalise a numeric literal: strip commas, thin spaces, trailing zeros are KEPT
    (0.40 and 0.4 are different display precisions and the paper cares)."""
    return tok.replace(',', '').replace(' ', '').replace(' ', '')

# ---------------------------------------------------------------- section model
HEAD = re.compile(r'^(#{1,6})\s+(.*?)\s*$')
# "## 4 · title", "### 4.10 · title", "## A.1 · ...", "### A.2.3 · ...", "## References"
NUMBERED = re.compile(r'^(A?\.?[0-9A-Z][0-9A-Za-z.]*?)\s*[·:.—-]\s')

def parse_sections(text: str):
    """-> list of (key, start_line, end_line, body_text). Bounded at the NEXT heading of ANY level."""
    lines = text.split('\n')
    heads = []
    for i, ln in enumerate(lines):
        m = HEAD.match(ln)
        if not m:
            continue
        title = m.group(2)
        km = NUMBERED.match(title)
        key = None
        if km:
            key = km.group(1).rstrip('.')
        heads.append((i, key, title))
    out = []
    for idx, (i, key, title) in enumerate(heads):
        end = heads[idx + 1][0] if idx + 1 < len(heads) else len(lines)
        body = '\n'.join(lines[i + 1:end])
        out.append({'key': key, 'title': title, 'start': i + 1, 'end': end, 'body': body})
    return out

def section_index(sections):
    idx = {}
    for s in sections:
        if s['key']:
            idx.setdefault(s['key'], []).append(s)
    return idx

# ---------------------------------------------------------------- clause model
REF = re.compile(r'§\s*([0-9A]+(?:\.[0-9]+)*)')
# `§§4.4, 4.6 and 4.9` — the 2nd and 3rd members carry no § of their own.
REF_RANGE = re.compile(r'(§§?\s*[0-9A][0-9A-Za-z.]*)\s*[-–—]\s*[0-9A][0-9A-Za-z.]*')
REF_RUN = re.compile(r'§§\s*[0-9A][0-9A-Za-z.]*((?:\s*,\s*[0-9A][0-9A-Za-z.]*)*(?:\s*(?:and|&)\s*[0-9A][0-9A-Za-z.]*)?)')
# a pointer that belongs to ANOTHER document
FOREIGN = re.compile(r'(paper[-\s]?(?:I{1,3}V?|IV)\b|companion paper|the (?:first|second|third|fourth) paper|METHOD-001|REG-0|RESULT-|REVIEW-|POSITIONING-|SCOUT-|NOTE-|LEDGER)', re.I)

NUMTOK = re.compile(r'(?<![A-Za-z0-9.])(-?\d[\d,  ]*(?:\.\d+)?)(?![\d.]*\s*[·])')
QUOTED = re.compile(r'[“"]([^“”"]{6,240})[”"]')

REFS_HEADING = re.compile(r'^#{1,6}\s+References\s*$', re.M)

def split_clauses(text: str, stop_at_references=True):
    """Yield (line_no, clause).

    PARAGRAPH FIRST, THEN SENTENCE.  The manuscript is hard-wrapped at ~100 columns, so a
    quotation routinely opens on one line and closes two lines later, and a figure is
    routinely wrapped away from the pointer it belongs to.  A line-at-a-time reader sees
    ONE quoted phrase in 2,741 lines and reports RULE 2 as vacuously clean.  Paragraphs
    are blank-line separated; a table row (leading `|`) and a heading stay their own unit,
    because joining rows would merge cells across records.

    THE REFERENCES SECTION IS OUT OF SCOPE.  Its entries carry volume and page numbers
    beside a `cited in §N.M` claim, and every page range reads as a numeric claim about
    the section.  wt133 sweep 2 already adjudicates the 'cited in' claims; this axis would
    only add ~40 false flags.  Stated, not silently dropped.
    """
    lines = text.split('\n')
    limit = len(lines)
    if stop_at_references:
        m = REFS_HEADING.search(text)
        if m:
            limit = text[:m.start()].count('\n')

    blocks, buf, buf_start = [], [], None
    def flush():
        nonlocal buf, buf_start
        if buf:
            blocks.append((buf_start, ' '.join(buf)))
        buf, buf_start = [], None

    for i, ln in enumerate(lines[:limit], start=1):
        st = ln.strip()
        if not st:
            flush(); continue
        if st.startswith('|') or st.startswith('#'):
            flush(); blocks.append((i, st)); continue
        if buf_start is None:
            buf_start = i
        buf.append(st)
    flush()

    for start, block in blocks:
        parts = re.split(r'(?<=[.!?])(?<!\d\.)\s+(?=[^a-z0-9])', block)
        for p in parts:
            if '§' in p:
                yield start, p


# ---------------------------------------------------------------- the two rules
def bad_number(tok: str) -> bool:
    """Numbers that are never a claim ABOUT a section's content."""
    t = norm_num(tok)
    if t.startswith('-'):
        t = t[1:]
    if t in {'1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '0'}:
        return True          # almost always a section/item/footnote ordinal
    if re.fullmatch(r'(19|20)\d\d', t):
        return True          # a year
    return False

def run(paper: Path, verbose=True):
    text = paper.read_text()
    sections = parse_sections(text)
    idx = section_index(sections)
    normbody = {k: strip_emphasis(' '.join(s['body'] for s in v)) for k, v in idx.items()}

    stats = dict(clauses=0, refs=0, foreign=0, toplevel=0, unresolved=0,
                 num_checked=0, num_flag=0, phr_checked=0, phr_flag=0)
    flags = []

    for lineno, clause in split_clauses(text):
        refs = REF.findall(clause)
        if not refs:
            continue
        stats['clauses'] += 1
        stats['refs'] += len(refs)
        if FOREIGN.search(clause):
            stats['foreign'] += len(refs)
            continue
        targets = []
        for r in refs:
            if '.' not in r:
                stats['toplevel'] += 1
                continue
            if r not in normbody:
                stats['unresolved'] += 1
                continue
            targets.append(r)
        if not targets:
            continue
        pool = ' || '.join(normbody[t] for t in targets)
        cnorm = strip_emphasis(clause)
        cnorm = REF_RANGE.sub(lambda m: m.group(1) + ' SECTIONRANGE ', cnorm)
        cnorm = REF_RUN.sub(lambda m: m.group(0)[:m.start(1) - m.start(0)] + ' SECTIONRUN ', cnorm)
        # THE SECTION NUMBER IS NOT A NUMERIC CLAIM.  Without this the checker reads
        # `§2.1` as the literal 2.1, asks whether §2.1 contains "2.1", and flags every
        # reference in the corpus.  The negative control caught it on the first run and
        # that is the whole reason the control exists.
        cnum = REF.sub(' SECTIONREF ', cnorm)
        # ATTRIBUTION WINDOW.  A number is a claim ABOUT the named section only if it sits
        # NEAR the pointer.  A markdown table row is one 'clause' with six cells; §7's
        # ledger rows put a `§5.4` in one cell and unrelated figures in three others.
        # Fragment on cell and clause boundaries, keep the fragments carrying a pointer.
        frags = [f for f in re.split(r'\s*\|\s*|\s;\s', cnum) if 'SECTIONREF' in f]
        cnum = ' ~ '.join(frags) if frags else ''

        # RULE 1 -------------------------------------------------------------
        for tok in NUMTOK.findall(cnum):
            tok = tok.strip()
            if not tok or bad_number(tok):
                continue
            stats['num_checked'] += 1
            t = norm_num(tok)
            pool_n = norm_num(pool)
            if t not in pool_n:
                stats['num_flag'] += 1
                flags.append(('NUMBER', lineno, '§' + '/§'.join(targets), t, cnorm[:200]))

        # RULE 2 -------------------------------------------------------------
        for q in QUOTED.findall(cnorm):
            qn = strip_emphasis(q).rstrip('.,;: ')
            if len(qn) < 6:
                continue
            stats['phr_checked'] += 1
            if qn.lower() not in pool.lower():
                stats['phr_flag'] += 1
                flags.append(('PHRASE', lineno, '§' + '/§'.join(targets), qn[:90], cnorm[:200]))

    if verbose:
        print(f"=== wt184 pointer-CORRECTNESS · {paper.name} ===")
        print(f"  sections parsed        : {len(sections)}  ({len(idx)} numbered keys)")
        print(f"  clauses carrying a §   : {stats['clauses']}")
        print(f"  § references seen      : {stats['refs']}")
        print(f"    another document's   : {stats['foreign']}  (out of scope, not adjudicated)")
        print(f"    bare top-level §N    : {stats['toplevel']}  (own bucket, weak either way)")
        print(f"    unresolved           : {stats['unresolved']}")
        print(f"  RULE 1 numbers checked : {stats['num_checked']}   FLAGGED {stats['num_flag']}")
        print(f"  RULE 2 phrases checked : {stats['phr_checked']}   FLAGGED {stats['phr_flag']}")
        print()
        for kind, ln, tgt, item, ctx in flags:
            print(f"  [{kind}] L{ln} -> {tgt}   {item!r}")
            print(f"          {ctx}")
    return stats, flags

# ---------------------------------------------------------------- negative control
CONTROL_DOC = """# Doc
## 1 · One
Nothing numeric lives here at all.

## 2 · Two
### 2.1 · Two point one
The measured value is 0.4137 and the phrase is emphatically **not** a coincidence.

### 2.2 · Two point two
This subsection holds 91.44 and nothing else.

## 3 · Three
GOOD: §2.1 reports 0.4137.

GOOD: §2.1 says the result is "emphatically not a coincidence".

BAD: §2.1 reports 0.9999.

BAD: §2.2 says the result is "emphatically not a coincidence".

BAD: §2 reports 91.44 -- top-level, must NOT be adjudicated as a number claim.

UNION: §2.1 and §2.2 together hold 0.4137 -- a sentence naming TWO sections is checked
against the UNION of their bodies, which is the weaker test and is not flagged.
"""

RESULTS = []


def postconditions():
    import tempfile, os
    ok = True
    RESULTS.clear()
    def chk(label, cond, negative=False):
        nonlocal ok
        RESULTS.append(bool(negative))
        tag = 'NEGATIVE' if negative else 'positive'
        print(f"  [{'PASS' if cond else 'FAIL'}] ({tag}) {label}")
        if not cond:
            ok = False

    with tempfile.NamedTemporaryFile('w', suffix='.md', delete=False) as fh:
        fh.write(CONTROL_DOC); ctrl = Path(fh.name)
    print("=== wt184 post-conditions ===")
    print("-- negative control document --")
    st, fl = run(ctrl, verbose=False)
    kinds = [(k, i) for k, _, _, i, _ in fl]
    chk("control: the wrong NUMBER (0.9999 at §2.1) is flagged",
        ('NUMBER', '0.9999') in kinds, negative=True)
    chk("control: the wrong PHRASE (at §2.2) is flagged",
        any(k == 'PHRASE' for k, _ in kinds), negative=True)
    chk("control: the RIGHT number 0.4137 at §2.1 is NOT flagged",
        ('NUMBER', '0.4137') not in kinds)
    chk("control: the right phrase, whose target carries it with ** emphasis, is NOT flagged",
        st['phr_flag'] == 1)
    chk("control: emphasis stripping is symmetric (2 phrases checked, 1 flagged)",
        st['phr_checked'] == 2 and st['phr_flag'] == 1)
    chk("control: bare top-level §2 is bucketed, not adjudicated",
        st['toplevel'] == 1)
    chk("control: exactly 2 flags, no more -- a section number is NOT a numeric claim",
        len(fl) == 2, negative=True)
    # 0.4137 (L10) and 0.9999 (L12) are the ONLY numeric claims aimed at a subsection;
    # 91.44 (L14) is aimed at bare §2 and is bucketed, not adjudicated.  Before the
    # SECTIONREF mask this read 6, because every `§2.1` was itself read as "2.1".
    chk("control: 3 numbers adjudicated, not 9 (SECTIONREF masking works)",
        st['num_checked'] == 3, negative=True)
    # A sentence naming TWO sections is tested against the UNION of their bodies.  That is
    # the weaker test and the script does not pretend otherwise: it is why a multi-target
    # clause can never produce a finding, only fail to produce one.
    chk("control: a UNION clause (two targets) is not flagged",
        not any('UNION' in c for _, _, _, _, c in fl))
    chk("control: no flagged item is itself a section key",
        not any(i in {'2.1', '2.2', '2', '3'} for _, _, _, i, _ in fl), negative=True)
    os.unlink(ctrl)

    print("-- normalisation units --")
    chk("strip_emphasis kills ** and *", strip_emphasis("a **b** c") == "a b c")
    chk("strip_emphasis kills backticks", strip_emphasis("a `b` c") == "a b c")
    chk("strip_emphasis collapses newlines", strip_emphasis("a\n   b") == "a b")
    chk("norm_num strips a comma", norm_num("1,833") == "1833")
    chk("norm_num strips a thin space", norm_num("2 735") == "2735")
    chk("bad_number rejects a year", bad_number("2024") is True, negative=True)
    chk("bad_number rejects an ordinal", bad_number("7") is True, negative=True)
    chk("bad_number keeps a real measurement", bad_number("0.4137") is False)

    print("-- section bounding --")
    secs = parse_sections(CONTROL_DOC)
    idx = section_index(secs)
    chk("§2 does NOT contain §2.1's body (bounded at the next heading of ANY level)",
        '0.4137' not in idx['2'][0]['body'], negative=True)
    chk("§2.1 does contain its own body", '0.4137' in idx['2.1'][0]['body'])

    print("-- the real manuscript parses --")
    p3 = REPO / 'docs/papers/paper-III-dual-tensor/paper-III.md'
    if p3.exists():
        s3 = parse_sections(p3.read_text())
        k3 = section_index(s3)
        chk("paper-III: §4.10 is a parsed key", '4.10' in k3)
        chk("paper-III: §A.2.3 is a parsed key", 'A.2.3' in k3)
        chk("paper-III: no key is claimed twice with different bodies",
            all(len(v) == 1 for v in k3.values()))
    print("-- rule 2 reaches the manuscript's own quoting style --")
    if p3.exists():
        st3, _ = run(p3, verbose=False)
        chk("paper-III: RULE 2 adjudicates a non-zero number of quoted phrases",
            st3['phr_checked'] > 0)
        line_only = len([1 for _, c in split_clauses(p3.read_text()) if QUOTED.search(strip_emphasis(c))])
        chk("paper-III: paragraph joining is load-bearing (a line-at-a-time reader saw 1)",
            line_only > 1, negative=True)
        chk("paper-III: RULE 1 adjudicates a non-zero number of figures",
            st3['num_checked'] > 0)
        # NOT PINNED TO A LITERAL. This read 244 before wealthTensor-101 and 247 after, because
        # wt185's §11 repair cites §4.10 three more times -- a hard 244 would have turned the
        # instrument red on the repair it found. What must hold is that the parse reaches the
        # whole manuscript, so the floor is wt133's pre-repair count and the check is one-sided.
        chk("paper-III: the parse reaches the whole manuscript (>= wt133's 244 refs)",
            st3['refs'] >= 244)
        chk("paper-III: zero unresolved, agreeing with wt133",
            st3['unresolved'] == 0)

    # THE COUNT IS THE CLAIM, NOT THE VERDICT. A registry entry can only hold this script to
    # something that MOVES, and "ALL PASS" does not move when a check is deleted. Print both.
    print(" post-conditions: %d checks, %d NEGATIVE" % (len(RESULTS), sum(RESULTS)))
    print(" post-conditions: %s" % ("ALL PASS" if ok else "FAILURE"))
    return 0 if ok else 1

if __name__ == '__main__':
    if '--postconditions' in sys.argv:
        sys.exit(postconditions())
    args = [a for a in sys.argv[1:] if not a.startswith('-')]
    target = Path(args[0]) if args else REPO / 'docs/papers/paper-III-dual-tensor/paper-III.md'
    run(target)
    sys.exit(0)
