#!/usr/bin/env python3
"""wt189 — re-adjudicate the promises wt188's §7 repair MOVED (wealthTensor-102).

wt188 rewrote Paper II §7's exception clause for finding II-43 — "except five quantities
neither command prints" became "except six", and the sixth was enumerated. wt148 went RED
the same commit with FOUR unadjudicated promises on paper-II and THREE STALE rows, which is
the guard doing its job: a sentence that names an artefact is a claim, promise_ids are keyed
on the sentence, and a sentence that changed is a claim nobody has run.

WHAT MOVED, AND WHAT DID NOT.  Three of the four are the SAME artefact making the SAME claim
in a sentence that gained one clause, so they are `#superseded` re-keys and carry their
predecessor's evidence, RE-RUN today rather than copied forward:
    fbd08a63f6 -> 5524790d1f   `python3 scripts/wt030_report.py`
    c6f855de23 -> 9893969707   `python3 scripts/wt077_tail_index.py`
    7ed9443301 -> 3ae14bfb6a   `wt030_report.py`
The FOURTH is genuinely new and supersedes nothing: before this pass the clause named
`wt077_tail_index.py` only in its runnable form, and II-43's sixth item names the bare token
for the first time.  A new bare mention is a new promise and gets its own evidence.

RE-CHECK, DO NOT RE-KEY (the wt186 pattern).  Every evidence cell below was RUN in
wealthTensor-102, every note quotes what it printed, and the seventh column is DERIVED from
`wt148.emit()` rather than transcribed.

EXIT 0 = rows written/verified and every post-condition holds.
EXIT 2 = refused or a post-condition failed; the TSV is rolled back to its pre-run bytes.
"""
import pathlib, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
TSV = ROOT / "docs/promises-adjudicated.tsv"
sys.path.insert(0, str(ROOT / "scripts"))
import wt148_promise_sweep as wt148

PAPER_II = ROOT / "docs/papers/paper-II-redistribution/paper-II.md"

SUPERSEDES = [
    ("b9dea67210 → fbd08a63f6 → 5524790d1f", "fbd08a63f6", "5524790d1f", "wt188",
     "wt188 R1/R2 repaired section 7's exception clause for II-43 (five enumerated quantities, six exist); same artefact, same claim, new promise_id"),
    ("5f6d5c4fb9 → c6f855de23 → 9893969707", "c6f855de23", "9893969707", "wt188",
     "same sentence as fbd08a63f6, keyed on wt077_tail_index.py; the claim about THIS artefact never changed"),
    ("7ed9443301 → 3ae14bfb6a", "7ed9443301", "3ae14bfb6a", "wt188",
     "same sentence, keyed on the bare token wt030_report.py; the clause it carries gained the sixth exception and nothing else"),
]

ROWS = [
 ("paper-II", "5524790d1f", "python3 scripts/wt030_report.py", "H",
  "python3 -c \"import subprocess;o=subprocess.check_output(['python3','scripts/wt030_report.py'],text=True);print('prints the section 3 values the clause says it prints:',{n:(n in o) for n in ('0.443','0.222','0.812','0.596','0.125','0.994','0.486','0.451','0.469','0.770','0.891','0.861','0.100','0.336','0.193','0.734','0.481','0.138','0.395','0.444')});print('does NOT print the six exceptions:',{n:(n in o) for n in ('0.99875','0.035','0.103','0.039','0.000006')});print('prints the 0.90 criterion:', '0.90 ' in o or '0.9000' in o)\"",
  "prints \"prints the section 3 values the clause says it prints: {'0.443': True, '0.222': True, '0.812': True, '0.596': True, '0.125': True, '0.994': True, '0.486': True, '0.451': True, '0.469': True, '0.770': True, '0.891': True, '0.861': True, '0.100': True, '0.336': True, '0.193': True, '0.734': True, '0.481': True, '0.138': True, '0.395': True, '0.444': True}\" and \"does NOT print the six exceptions: {'0.99875': False, '0.035': False, '0.103': False, '0.039': False, '0.000006': False}\" and 'prints the 0.90 criterion: False'. The clause's positive half holds and its negative half holds in the repaired SIX-item form -- 0.000006 is the sixth, which is II-43. Superseding fbd08a63f6, whose sentence gained that item.",
  ),
 ("paper-II", "9893969707", "python3 scripts/wt077_tail_index.py", "H",
  "python3 -c \"import subprocess;o=subprocess.check_output(['python3','scripts/wt077_tail_index.py'],text=True).split(chr(10));print([l.strip() for l in o if 'closed form' in l]);print([l.strip() for l in o if 'Var[log a] =' in l])\"",
  "prints ['E[eta+] closed form = 0.107269   quadrature = 0.107269'] and ['unlevied Var[log a] = 0.076542', 'stock r=0.10: Var[log a] = 0.076536   (kappa=0.10000)', 'flow  r=0.10: Var[log a] = 0.073276   (kappa=0.01022)', 'flow  r=1.00: Var[log a] = 0.051189   (kappa=0.10216)']. Section 3.1's E[eta+] = 0.1073 and its three Var[log a] values are exactly these four, so the clause's attribution of the four closed-form quantities to this command holds. Superseding c6f855de23 verbatim in substance; the evidence was RE-RUN, not carried over.",
  ),
 ("paper-II", "3ae14bfb6a", "wt030_report.py", "H",
  "python3 -c \"import subprocess;o=subprocess.check_output(['python3','scripts/wt030_report.py'],text=True);print('prints each number the repaired clause says it prints:',{n:(n in o) for n in ('0.486','0.451','0.994','0.891','0.861')});print('prints the 0.90 criterion:', '0.90 ' in o or '0.9000' in o)\"",
  "prints \"prints each number the repaired clause says it prints: {'0.486': True, '0.451': True, '0.994': True, '0.891': True, '0.861': True}\" and 'prints the 0.90 criterion: False'. The bare token appears in the clause twice -- '0.035 periodicity span and section 3.4's 0.103 Gini gap, each a difference of two values wt030_report.py prints' and '0.039 top-decile margin, the distance from that command's printed 0.861' -- and both hold: 0.486/0.451 give 0.035, 0.994/0.891 give 0.103, 0.861 is printed and 0.90 is not. Superseding 7ed9443301.",
  ),
 ("paper-II", "e92cf2c97f", "wt077_tail_index.py", "H",
  "python3 -c \"import subprocess;o=subprocess.check_output(['python3','scripts/wt077_tail_index.py'],text=True);print('prints both inputs:',('0.076542' in o,'0.076536' in o));print('their difference:',round(0.076542-0.076536,8));print('prints the difference itself:',any(f in o for f in ('6e-06','6e-6','0.000006','6 x 10')))\"",
  "prints 'prints both inputs: (True, True)', 'their difference: 6e-06' and 'prints the difference itself: False'. THIS ROW IS NEW, NOT A RE-KEY: before wealthTensor-102 the clause named wt077_tail_index.py only in its runnable form, and II-43's sixth item is the first bare mention. It asserts exactly what the three lines show -- section 3.1's 6 x 10^-6 is the difference of two values this command prints, and the command does not print the difference -- which is why the quantity belongs in section 7's exception list and why the list said five.",
  ),
]


def sentence_for(pid: str) -> str:
    """The SEVENTH column is derived from wt148's own emitter, never transcribed."""
    for e in wt148.emit(PAPER_II):
        if e["pid"] == pid:
            return e["sentence"]
    sys.exit("PRECONDITION FAILED: wt148 emits no promise %s for paper-II" % pid)


def main():
    original = TSV.read_text()
    lines = original.split("\n")
    present = {l.split("\t")[1] for l in lines if l.startswith("paper-") and l.count("\t") >= 2}
    RETIRED = {o for _lbl, o, _n, _w, _note in SUPERSEDES}
    # A SUPERSEDED ROW MUST BE REMOVED, NOT LEFT BESIDE ITS REPLACEMENT.  wt148 reports a
    # row whose sentence no longer exists verbatim as STALE and exits 1 -- correctly: the
    # check it records no longer applies to anything.  The convention this file already
    # uses (b9dea67210, 5f6d5c4fb9) is delete-the-row, keep-the-#superseded-line.
    already = all(r[1] in present for r in ROWS) and not (RETIRED & present)

    sup_lines = ["#superseded\t%s\t%s\t%s\t%s" % (o, n, who, note)
                 for _lbl, o, n, who, note in SUPERSEDES]
    new_rows = ["\t".join(list(r) + [sentence_for(r[1])]) for r in ROWS]
    # IDEMPOTENT AND STILL AUDIBLE (-101's rule): the already-applied path re-derives every
    # row, verifies it against the file on disk, and prints the SAME summary line, so a
    # count_re can hold this script to a number on the second run as well as the first.
    # A ROW THAT EXISTS WITH A DIFFERENT BODY MUST BE REWRITTEN, NOT LEFT ALONE.
    # wt172 --verify holds every paper-II row's note to the VERBATIM stdout of its own evidence
    # cell, and it caught this row's first note paraphrasing instead of quoting. An
    # already-present check keyed on the promise_id alone would have made that unfixable by
    # re-running the script, so `already` means present AND byte-identical.
    by_pid = {l.split("\t")[1]: l for l in lines if l.startswith("paper-")}
    already = already and all(by_pid.get(r[1]) == row for r, row in zip(ROWS, new_rows))
    if already:
        text = original
        print("wt189: all %d rows already present - verifying, not rewriting." % len(ROWS))
    else:
        while lines and lines[-1] == "":
            lines.pop()
        # supersede lines go beside the ones already there, rows at the end
        idx = max(i for i, l in enumerate(lines) if l.startswith("#superseded\t"))
        _mine = {r[1] for r in ROWS}
        kept = [l for l in lines
                if not (l.startswith("paper-") and l.split("\t")[1] in (RETIRED | _mine))]
        idx = max(i for i, l in enumerate(kept) if l.startswith("#superseded\t"))
        merged = kept[:idx + 1] + sup_lines + kept[idx + 1:] + new_rows
        text = "\n".join(merged) + "\n"
        TSV.write_text(text)

    # THE FIRST CUT OF Q1-Q3 WAS WRONG ABOUT THE FILE (-101's trap 3): it counted the id
    # across the WHOLE text, and a `#superseded` line legitimately names the NEW id in its
    # third column, so every re-key read as a duplicate.  The fix is a TIGHTER subject --
    # count among LIVE rows only -- not a loosened threshold.
    live = [l for l in text.split("\n") if l.startswith("paper-")]
    checks = []
    for i, r in enumerate(ROWS):
        checks.append(("Q%d row %s present exactly once among LIVE rows" % (i + 1, r[1]),
                       len([l for l in live if l.split("\t")[1] == r[1]]) == 1, True))
    checks.append(("Q5 every new row has SEVEN columns",
                   all(len(l.split("\t")) == 7 for l in new_rows), False))
    checks.append(("Q6 the seventh column is wt148's, not a transcription",
                   all(l.split("\t")[6] == sentence_for(l.split("\t")[1]) for l in new_rows), False))
    checks.append(("Q7 exactly three #superseded lines were added",
                   text.count("#superseded\t") == original.count("#superseded\t")
                   + (0 if already else 3), False))
    for _lbl, o, n, _w, _note in SUPERSEDES:
        checks.append(("Q8 %s is recorded as superseded by %s" % (o, n),
                       ("#superseded\t%s\t%s\t" % (o, n)) in text, False))
        checks.append(("Q9 the retired id %s no longer carries a live row" % o,
                       len([l for l in live if l.split("\t")[1] == o]) == 0, True))
    checks.append(("Q10 promise_ids are unique across the whole file",
                   len({l.split("\t")[1] for l in text.split("\n") if l.startswith("paper-")}) ==
                   len([l for l in text.split("\n") if l.startswith("paper-")]), True))
    # Q11 ASSUMED THIS SCRIPT ONLY EVER APPENDS. It does not: since wt172 caught a paraphrased
    # note, the write path also REWRITES a row of its own that is present with a different body,
    # and on that path the net change is 0, not +1. Derived from the actual before-state instead
    # of a hard-coded delta -- the same narrowing wt183's Q10 needed for the same reason.
    _orig_live = [l for l in original.split("\n") if l.startswith("paper-")]
    _orig_pids = {l.split("\t")[1] for l in _orig_live}
    _expected = (len(_orig_live)
                 - len(RETIRED & _orig_pids)
                 - len({r[1] for r in ROWS} & _orig_pids)
                 + len(ROWS))
    checks.append(("Q11 live-row count is what the row set implies (%d)" % _expected,
                   len(live) == _expected, True))
    checks.append(("Q12 no row carries an empty cell",
                   all("\t\t" not in l for l in new_rows), True))
    checks.append(("Q13 the scope line is untouched",
                   "#scope\tpaper-II\tpaper-III\tpaper-IV" in text, False))
    sup = [l for l in text.split("\n") if l.startswith("#superseded\t")]
    checks.append(("Q14 e92cf2c97f supersedes nothing (it is a NEW promise)",
                   not any(l.split("\t")[2] == "e92cf2c97f" for l in sup), True))
    checks.append(("Q15 each re-key IS named as a supersede target (positive control)",
                   all(any(l.split("\t")[2] == n for l in sup)
                       for _lbl, _o, n, _w, _note in SUPERSEDES), False))

    for label, cond, isneg in checks:
        print("  [%s] %s%s" % ("PASS" if cond else "FAIL", "(NEGATIVE) " if isneg else "", label))
    neg = sum(1 for _, _, n in checks if n)
    print("wt189: %d rows %s, %d superseded, %d post-conditions, %d NEGATIVE"
          % (len(ROWS), "verified" if already else "written", len(SUPERSEDES), len(checks), neg))

    if any(not c for _, c, _ in checks):
        if not already:
            TSV.write_text(original)
            print("ROLLED BACK - the TSV is at its pre-run bytes.")
        else:
            print("VERIFICATION FAILED against the committed TSV - nothing was written.")
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
