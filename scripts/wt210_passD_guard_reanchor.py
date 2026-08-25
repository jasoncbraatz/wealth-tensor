#!/usr/bin/env python3
"""wt210 — Pass D (wealthTensor-106): re-anchor two frozen guards whose SUBJECT moved.

Both repairs are FALSE-POSITIVE REDUCTIONS under DEFINITION-OF-DONE-SHIP.md § 1.1's narrow
exception.  Neither makes an instrument look at anything new; each re-points a check at the
FINDING it was written to hold, and away from an incidental property of the prose that a
later, mandated pass was always going to move.  This is the ninth and tenth instance of this
repo's standing tell, and the third and fourth time the answer has been a TIGHTER SUBJECT
rather than a deleted check.

  wt186 · `64e11e7bc4` adjudicated the §11 clause "Until wealthTensor-101 this section named
        no command for §4.10".  That clause is a HARD C-e apparatus leak — a session number a
        reader cannot fetch — and DoD § 2.5 obliges Pass D to delete it.  The promise ceased to
        exist, and `sentence_for` sys.exits on a pid wt148 no longer emits.  wt186 now honours
        the ledger's `#retired` convention, exactly as wt170 already honours `#superseded`:
        a row whose promise was retired is dropped, not fatal.  READING AT THE PIN: the check
        was right that the pid was gone and wrong that its absence is a defect.

  wt188 · II-44b's post-condition pinned "all four of their own tax parameters" at EXACTLY
        TWO occurrences.  Two was never the finding.  The finding (II-44) is that the paper
        credited Bouchaud and Mézard with two coordinates they never model, and its checkable
        form is the NEGATIVE one this file already carries — "in closed form in all four
        coordinates" occurs EXACTLY ZERO times.  The count of two was an artefact of the
        credit being restated at two sites, and REVIEW-039 § 7 names that restatement as a
        C-b duplication and assigns it to Pass D by name.  A guard that pins the count forbids
        the repair its own successor was told to make.  Re-asserted as AT LEAST ONE with the
        count PRINTED rather than pinned — the same repair `-105` made to this file's
        wt184-flag count, for the same reason.  READING AT THE PIN: the guard was wrong about
        the file.

Idempotent: NO-OP and exit 0 on a second run.  Exit 2 if a site matches neither state.
"""
import pathlib, sys

ROOT = pathlib.Path(__file__).resolve().parents[1]

EDITS = [
 ("wt186-retired", "scripts/wt186_paperIII_promises.py",
  '''def sentence_for(pid: str) -> str:
    """The SEVENTH column is derived from wt148's own emitter, never transcribed."""
    for e in wt148.emit(PAPER_III):
        if e["pid"] == pid:
            return e["sentence"]
    sys.exit("PRECONDITION FAILED: wt148 emits no promise %s for paper-III" % pid)''',
  '''def retired_pids() -> set:
    """Pids the ledger has RETIRED — the promise ceased to exist because the sentence that
    made it was deleted.  wt170 already honours `#superseded` (a reworded sentence with a
    living heir); this is its sibling for a sentence with no heir, and it is the only reason
    a pid in ROWS may legitimately be absent from wt148's emission."""
    out = set()
    for line in (ROOT / TSV).read_text(encoding="utf-8").splitlines():
        f = line.split("\\t")
        if f and f[0] == "#retired" and len(f) >= 2:
            out.add(f[1].strip())
    return out


def sentence_for(pid: str) -> str:
    """The SEVENTH column is derived from wt148's own emitter, never transcribed."""
    for e in wt148.emit(PAPER_III):
        if e["pid"] == pid:
            return e["sentence"]
    if pid in retired_pids():
        return None
    sys.exit("PRECONDITION FAILED: wt148 emits no promise %s for paper-III" % pid)'''),

 ("wt188-landed", "scripts/wt188_paperII_p7pass13.py",
  '''    elif n_old == 0 and n_new == 1:
        pass                                   # already landed; idempotent''',
  '''    elif n_old == 0 and (n_new == 1 or
                         (tag in LANDED and after.count(LANDED[tag]) == 1)):
        pass                                   # already landed; idempotent'''),

 ("wt188-landed-dict", "scripts/wt188_paperII_p7pass13.py",
  '''print("== E6 · the manuscript edits ==")''',
  '''# LANDED (wealthTensor-106).  A later pass may legitimately REPLACE the text this repair
# left behind, and then neither the anchor nor the replacement is present and the script
# refuses on its own success.  A LANDED marker is the DISTINCTIVE CLAIM the site carries
# after that later repair, so `applied` and `passes` cannot disagree.  II-44b's §6
# restatement was cut to a pointer by Pass D as a C-b duplication (REVIEW-039 § 7 names it),
# leaving the full credit at §3.1 where II-44a repaired it.
LANDED = {
    "II-44b": "are prior to the stock-versus-flow ranking used there.",
}

print("== E6 · the manuscript edits ==")'''),

 ("wt188-counts", "scripts/wt188_paperII_p7pass13.py",
  '''    chk("'all four of their own tax parameters' occurs EXACTLY twice (whitespace-normalised)",
        flat.count("all four of their own tax parameters") == 2)
    chk("'a rate and a redistributed fraction for each base' occurs EXACTLY twice",
        flat.count("a rate and a redistributed fraction for each base") == 2)''',
  '''    # -106: COUNTED AND PRINTED, NOT PINNED.  Two was the number of sites that restated the
    # credit, never the finding; Pass D cut the §6 restatement to a pointer as a C-b
    # duplication, and a guard that pinned two would have forbidden that repair.  What II-44
    # actually holds is that WHEREVER the credit is stated it names their own tax parameters,
    # and that the wrong form is gone -- the NEGATIVE check below, which is unchanged.
    n_par = flat.count("all four of their own tax parameters")
    n_fra = flat.count("a rate and a redistributed fraction for each base")
    print("     >> II-44 corrected credit, occurrences: 'their own tax parameters' %d, "
          "'a rate and a redistributed fraction for each base' %d" % (n_par, n_fra))
    chk("'all four of their own tax parameters' occurs AT LEAST once (whitespace-normalised)",
        n_par >= 1)
    chk("'a rate and a redistributed fraction for each base' occurs AT LEAST once",
        n_fra >= 1)'''),

 ("wt186-filter", "scripts/wt186_paperIII_promises.py",
  """    already = all(r[1] in present for r in ROWS)""",
  """    # -106: a RETIRED promise leaves the ledger without leaving this script's ROWS list.
    # Drop those rows here rather than at the write, so `already` is computed over the rows
    # that can still exist.
    live = [r for r in ROWS if sentence_for(r[1]) is not None]
    already = all(r[1] in present for r in live)"""),

 ("wt186-rows", "scripts/wt186_paperIII_promises.py",
  r"""    new_rows = ["\t".join(list(r) + [sentence_for(r[1])]) for r in ROWS]""",
  r"""    new_rows = ["\t".join(list(r) + [sentence_for(r[1])]) for r in live]"""),

 ("wt186-count", "scripts/wt186_paperIII_promises.py",
  """        print("wt186: all %d rows already present — verifying, not rewriting." % len(ROWS))""",
  """        print("wt186: all %d rows already present — verifying, not rewriting." % len(live))"""),

 ("wt188-nonvacuous", "scripts/wt188_paperII_p7pass13.py",
  """    chk("a byte-literal count would MISS one of them (that is why this is normalised)",
        cur.count("all four of their own tax parameters") == 1, negative=True)""",
  """    # The normalisation must be shown NON-VACUOUS, and after Pass D the surviving §3.1 site
    # wraps inside the SECOND phrase rather than the first -- so the proof moves with it.
    chk("a byte-literal count MISSES the wrapped phrase entirely -- that is why this is "
        "normalised",
        cur.count("a rate and a redistributed fraction for each base") < n_fra, negative=True)"""),
]

def main():
    applied = already = 0
    fail = []
    texts = {}
    for entry in EDITS:
        tag, rel, old, new = entry[0], entry[1], entry[2], entry[3]
        marker = entry[4] if len(entry) > 4 else None
        p = ROOT / rel
        t = texts.get(rel) or p.read_text(encoding="utf-8")
        landed = (t.count(marker) == 1) if marker else (t.count(new) == 1)
        if not landed and t.count(old) == 1:
            texts[rel] = t.replace(old, new, 1); applied += 1
            print("APPLIED         %s  %s" % (tag, rel))
        elif landed:
            texts[rel] = t; already += 1
            print("ALREADY-APPLIED %s  %s" % (tag, rel))
        else:
            texts[rel] = t
            fail.append(tag)
            print("!! NEITHER      %s  %s  old=%d new=%d" % (tag, rel, t.count(old), t.count(new)))
    if fail:
        print("\nFAIL: %d site(s) matched neither state; NOTHING WRITTEN" % len(fail)); return 2
    for rel, t in texts.items():
        p = ROOT / rel
        if p.read_text(encoding="utf-8") != t:
            bak = p.with_suffix(p.suffix + ".bak-wt210")
            if not bak.exists(): bak.write_text(p.read_text(encoding="utf-8"), encoding="utf-8")
            p.write_text(t, encoding="utf-8"); print("WROTE %s" % rel)
    print("\napplied=%d already=%d" % (applied, already))
    return 0

if __name__ == "__main__":
    sys.exit(main())
