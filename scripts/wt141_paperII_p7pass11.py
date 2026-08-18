#!/usr/bin/env python3
"""wt141 · wealthTensor-79 · Paper II's NINTH independent P7 read — THREE repairs, ZERO
manuscript edits, because all three make an EXISTING manuscript sentence true.

GUARD HONESTY (WT-118, wt129's rule, no exception): every OLD string is asserted present
EXACTLY ONCE in the ORIGINAL before any substitution runs, and the guards run BEFORE the
backups, so a failed guard writes nothing.

THE INSTRUMENT SET IS STILL FROZEN. A1-A5 as inherited; A6 (the docstring axis) stays
parked. Nothing was invented here. What this pass spent differently is DEPTH: -78(ii)
said that resolving a named artefact is not applying an axis to it, and then -78 itself
deferred two artefacts on their labels. Both findings below are those two artefacts,
read rather than resolved.

FINDINGS REPAIRED
  II-37  SEC 7 promises `python3 scripts/wt030_report.py` regenerates every number in
         SEC 3 save five closed-form quantities. SEC 3.1's four kappa residuals
         (-4.3 %, -4.6 %, -5.7 % at the tabulated flow rates, -6.8 % at r = 0.010) are
         SEC 3 numbers, are not closed-form quantities, and are printed by NEITHER named
         command. -78's own II-35 is the proof they cannot be recovered from what IS
         printed: the 4-dp kappa column yields -4.352 / -4.912 / -6.777, wrong by up to
         1.05 percentage points. SEC 1's contribution 5 makes the stronger claim -- every
         number "regenerated ... by the two commands SEC 7 names", exempting only the
         Gini ceiling -- and is false for the same four numbers.
         This is the THIRD member of a family already worked twice: II-27 (-76) found two
         SEC 3.3 numbers missing from wt030's output; II-31 (-76) found SEC 3.4's Gini
         ceiling missing from SEC 7's exception list. II-27's repair mode is the precedent
         and is followed here: MAKE THE PROMISE TRUE rather than weaken the prose.
         wt030_report.py now prints the residual for all seven flow rates, from the
         unrounded kappa, with E[eta+] IMPORTED from wt077_tail_index so the two commands
         SEC 7 names cannot fork on the constant.
  II-38  The References note defers the bibliographic details of the entries not marked
         with a tick to `docs/papers/PREPRINT-CHECKLIST.md`. That file carried NO such
         item -- SEC A is apparatus, B reproducibility, C venue, D pre-registration, and
         none of them mentions references. Ten of sixteen entries were deferred to a
         document that was not holding them. -78 put this on its OWN not-checked list
         (REVIEW-018 SEC 4 item 7, "deferred to submission per PREPRINT-CHECKLIST") and
         trusted the label. The checklist now carries the item; the manuscript sentence
         is true unedited.
  II-39  TOOLING, in the A1 instrument itself. wt130_quantifier_sweep.py's docstring
         documents `... paper-II   # one paper, full enumeration`. The selector is a bare
         substring test and `paper-II` is a PREFIX of `paper-III`, so that invocation
         sweeps TWO manuscripts and the LAST TOTAL a reader sees is Paper III's. `paper-I`
         is a prefix of all four and sweeps FOUR. This is the exact delivery mechanism for
         the misreading banked at -73 ("870 tokens on 673 lines" travelling three documents
         deep). -78's A1 line reads `--paper II`, which drops to sel=["II"] and also sweeps
         two. The selector now matches a manuscript's stem or its directory name exactly,
         or a hyphen-delimited prefix of the directory name -- so `paper-II` selects one
         paper and a bare `II` FAILS LOUDLY instead of silently sweeping two.

NOT DONE HERE, written down at the moment of not-doing:
  * A6, the docstring axis: still parked. tests/test_redistribution.py carries twenty-one
    unasserted prose claims.
  * The nine uncited reference entries -- card 1217568192511533. II-38 is a different
    object: it is about where the UNVERIFIED DETAILS were deferred to, not about whether
    an entry is cited.
  * II-25, the version stamp -- card 1217568297674954, NINTH data point.
  * SEC 3.1's closed form r*E[eta+] vs r*E[eta+]/(1+mu): Jason-sized, changes a stated
    contribution. Note that II-37's repair prints the residual against the form the
    PAPER states, deliberately, so adopting the other form remains a one-line change.
"""
from __future__ import annotations

import pathlib
import re
import shutil
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
REPORT = ROOT / "scripts" / "wt030_report.py"
SWEEP = ROOT / "scripts" / "wt130_quantifier_sweep.py"
CHECK = ROOT / "docs" / "papers" / "PREPRINT-CHECKLIST.md"
PAPER = ROOT / "docs" / "papers" / "paper-II-redistribution" / "paper-II.md"
TAG = ".bak-wt141"

# ---------------------------------------------------------------- II-37 -----
OLD_HEAD = """import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "src"))
import numpy as np
from wealth_tensor.redistribution import (RedistributiveEconomy as E, stationary_gini,
                                          top_share, is_bounded, reachable_frontier)"""

NEW_HEAD = """import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "src"))
sys.path.append(str(pathlib.Path(__file__).resolve().parent))   # scripts/, appended so it
#   can never shadow stdlib or site-packages
import numpy as np
from wealth_tensor.redistribution import (RedistributiveEconomy as E, stationary_gini,
                                          top_share, is_bounded, reachable_frontier)
# wealthTensor-79 (II-37): SEC 3.1's kappa residuals are SEC 3 numbers that neither command
# named in SEC 7 printed, and II-35 proved they cannot be recovered from the 4-dp kappa
# column below. E[eta+] is IMPORTED rather than restated so the two commands SEC 7 names
# cannot fork on the constant that II-36 had already been wrong about once.
from wt077_tail_index import eta_plus_closed_form"""

OLD_LOOP = """for base in ("stock","flow"):
    for r in (0.01,0.025,0.05,0.10,0.25,0.50,1.00):
        g,k,t,b = row(base=base, rate=r)
        print(f"{base+' r='+format(r,'.3f'):34s} {g:6.3f} {k:7.4f} {t:7.3f}  {b}")"""

NEW_LOOP = """FLOW_KAPPA = {}
for base in ("stock","flow"):
    for r in (0.01,0.025,0.05,0.10,0.25,0.50,1.00):
        g,k,t,b = row(base=base, rate=r)
        if base == "flow": FLOW_KAPPA[r] = k
        print(f"{base+' r='+format(r,'.3f'):34s} {g:6.3f} {k:7.4f} {t:7.3f}  {b}")"""

OLD_TAIL = """print("\\nPERIODICITY (stock, rate*P held constant at 0.02/period)")
for P in (1,2,4,10,20,30,50):
    g,k,t,b = row(base="stock", rate=min(1.0,0.02*P), periodicity=P)
    print(f"  every {P:3d} periods at r={min(1.0,0.02*P):.2f}  Gini={g:.3f}  bounded={b}")"""

NEW_TAIL = OLD_TAIL + """

print("\\nFLOW-BASE KAPPA RESIDUAL vs the closed form r*E[eta+]   (SEC 3.1)")
print("  From the UNROUNDED kappa, reusing the MAIN TABLE's runs -- no extra simulation.")
print("  The 4-dp kappa column above is too coarse to reproduce these: at r=0.025 its")
print("  display quantum is +/-2 % of kappa itself, wider than the spread SEC 3.1 reports")
print("  (wealthTensor-78, II-35). E[eta+] is imported from wt077_tail_index.")
_ep = eta_plus_closed_form()
for r in (1.00,0.50,0.25,0.10,0.05,0.025,0.010):
    k = FLOW_KAPPA[r]
    print(f"  flow r={r:.3f}  kappa={k:.9f}  r*E[eta+]={r*_ep:.9f}  "
          f"residual={100.0*(k/(r*_ep)-1.0):+.3f} %")"""

# ---------------------------------------------------------------- II-38 -----
OLD_CHECK = """- [ ] **Related work as positioning, not survey.** State what is established, then what is new."""

NEW_CHECK = """- [ ] **Related work as positioning, not survey.** State what is established, then what is new.
- [ ] **Every reference entry's bibliographic details verified against a publisher page, a
      library catalogue or a Crossref record — including the entries a draft left unmarked,
      and the marks in the manuscript updated to say so.** Added 2026-08-18
      (wealthTensor-79) after a measured gap: Paper II's References note defers exactly this
      work to *this file* — *"The remainder are standard works whose details are to be
      re-checked at submission per `docs/papers/PREPRINT-CHECKLIST.md`"* — and until now
      this file carried no such item, so **ten of its sixteen entries were deferred to a
      document that was not holding them.** That is §7's own failure mode (*"a provenance
      claim that reads as checked and is not"*) applied to the bibliography, and it is the
      cheaper half of a pair: `REFERENCE-POLICY` §1 states the evidentiary requirement and
      §4 the marks, so the work is specified — what was missing was anything that would ask
      for it at the moment it comes due. **A deferral whose target does not carry the item
      is not a deferral; it is a dropped ball with a citation.**"""

# ---------------------------------------------------------------- II-39 -----
OLD_DOC = """    python3 scripts/wt130_quantifier_sweep.py                 # all four manuscripts, counts
    python3 scripts/wt130_quantifier_sweep.py paper-II        # one paper, full enumeration
    python3 scripts/wt130_quantifier_sweep.py paper-II --md   # markdown, for a REVIEW doc
\"\"\""""

NEW_DOC = """    python3 scripts/wt130_quantifier_sweep.py                 # all four manuscripts, counts
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
\"\"\""""

OLD_SEL = """    md = "--md" in argv
    sel = [a for a in argv if not a.startswith("--")]
    papers = [p for p in PAPERS if not sel or any(s in str(p) for s in sel)]"""

NEW_SEL = """    md = "--md" in argv
    sel = [a for a in argv if not a.startswith("--")]
    papers = [p for p in PAPERS if not sel or any(_selects(s, p) for s in sel)]"""

OLD_ANCHOR_FN = """def n_lines(path):"""

NEW_ANCHOR_FN = """def _selects(s, p):
    \"\"\"Does selector `s` name manuscript `p`? (wealthTensor-79, II-39.)

    Exact on the stem or the directory name, or a hyphen-delimited prefix of the directory
    name. NOT a bare substring test: `paper-II` is a prefix of `paper-III` and `paper-I` of
    all four, so the substring form silently swept the wrong SET and printed someone else's
    TOTAL last. `paper-II` -> stem match, one paper. `paper-II-redistribution` -> directory
    match. `II` -> no match, and main() exits non-zero rather than sweeping two.
    \"\"\"
    return s == p.stem or s == p.parent.name or p.parent.name.startswith(s + "-")


def n_lines(path):"""


def main() -> int:
    rep, swp, chk = REPORT.read_text("utf-8"), SWEEP.read_text("utf-8"), CHECK.read_text("utf-8")
    paper_before = PAPER.read_bytes()

    for name, hay, needles in (
        ("wt030_report.py", rep, (OLD_HEAD, OLD_LOOP, OLD_TAIL)),
        ("wt130_quantifier_sweep.py", swp, (OLD_DOC, OLD_SEL, OLD_ANCHOR_FN)),
        ("PREPRINT-CHECKLIST.md", chk, (OLD_CHECK,)),
    ):
        for i, n in enumerate(needles):
            assert hay.count(n) == 1, "anchor %d in %s: %d occurrences" % (i, name, hay.count(n))

    for f in (REPORT, SWEEP, CHECK):
        shutil.copy2(f, f.with_name(f.name + TAG))

    REPORT.write_text(rep.replace(OLD_HEAD, NEW_HEAD)
                         .replace(OLD_LOOP, NEW_LOOP)
                         .replace(OLD_TAIL, NEW_TAIL), encoding="utf-8")
    SWEEP.write_text(swp.replace(OLD_DOC, NEW_DOC)
                        .replace(OLD_SEL, NEW_SEL)
                        .replace(OLD_ANCHOR_FN, NEW_ANCHOR_FN), encoding="utf-8")
    CHECK.write_text(chk.replace(OLD_CHECK, NEW_CHECK), encoding="utf-8")

    py = sys.executable

    def run(args):
        return subprocess.run([py] + args, cwd=ROOT, capture_output=True, text=True)

    # ---- POST-CONDITIONS ---------------------------------------------------
    # THE INVARIANT OF THIS PASS: no manuscript edit. All three repairs make an
    # EXISTING sentence true.  P1 is therefore the load-bearing one.
    assert PAPER.read_bytes() == paper_before, "P1 paper-II.md was modified"

    r = run(["scripts/wt030_report.py"])
    assert r.returncode == 0, "P2 wt030_report.py exits %d\n%s" % (r.returncode, r.stderr[-2000:])
    out = r.stdout
    assert "FLOW-BASE KAPPA RESIDUAL" in out, "P3 residual block absent"
    resid = {}
    for ln in out.splitlines():
        m = re.match(r"\s*flow r=([\d.]+)\s+kappa=([\d.]+)\s+r\*E\[eta\+\]=([\d.]+)\s+"
                     r"residual=([-+][\d.]+) %", ln)
        if m:
            resid[float(m.group(1))] = float(m.group(4))
    assert len(resid) == 7, "P4 expected 7 residual rows, got %d" % len(resid)

    # P5-P8: the four residuals SEC 3.1 states now come OUT of the named command, to the
    # precision SEC 3.1 states them.  This is the whole of II-37.
    for r_, want in ((1.000, -4.3), (0.100, -4.6), (0.025, -5.7), (0.010, -6.8)):
        got = round(resid[r_], 1)
        assert got == want, "P5-8 residual at r=%s is %s, SEC 3.1 says %s" % (r_, got, want)

    # P9: "flat between r = 1.000 and r = 0.500" -- SEC 3.1's word, made checkable.
    assert abs(resid[1.000] - resid[0.500]) < 0.01, "P9 not flat: %s vs %s" % (resid[1.0], resid[0.5])
    # P10: "widens monotonically below it".
    below = [resid[x] for x in (0.500, 0.250, 0.100, 0.050, 0.025, 0.010)]
    assert all(a > b for a, b in zip(below, below[1:])), "P10 not monotone below r=0.5: %s" % below
    # P11: the headline range "4-7 % below ... across the full rate sweep".
    assert all(-7.0 < v < -4.0 for v in resid.values()), "P11 a residual left 4-7 %%: %s" % resid

    # P12: the constant is wt077's, not a second copy of it. Both halves asserted: the
    # import is present AND the value agrees with what wt077 itself prints.
    assert "from wt077_tail_index import eta_plus_closed_form" in REPORT.read_text("utf-8"), \
        "P12a import missing"
    r77 = run(["scripts/wt077_tail_index.py"])
    assert r77.returncode == 0, "P12b wt077 exits %d" % r77.returncode
    m = re.search(r"E\[eta\+\] closed form = ([\d.]+)", r77.stdout)
    assert m, "P12c wt077 no longer prints E[eta+]"
    ep77 = float(m.group(1))
    m30 = re.search(r"flow r=1\.000\s+kappa=[\d.]+\s+r\*E\[eta\+\]=([\d.]+)", out)
    assert m30 and abs(float(m30.group(1)) - ep77) < 5e-7, \
        "P12d the two commands forked on E[eta+]: %s vs %s" % (m30 and m30.group(1), ep77)

    # P13: no extra simulation was bought -- the residual block reuses the MAIN TABLE's
    # kappa, so the printed kappa must equal the table's to 4 dp at every flow rate.
    for r_, k_ in resid.items():
        want = re.search(r"flow r=%s\s+[\d.]+\s+([\d.]+)" % format(r_, ".3f"), out)
        assert want, "P13 no MAIN TABLE row for flow r=%s" % r_
        got = re.search(r"flow r=%s\s+kappa=([\d.]+)" % format(r_, ".3f"), out)
        assert round(float(got.group(1)), 4) == float(want.group(1)), \
            "P13 residual block kappa disagrees with the table at r=%s" % r_

    # P14-P17: the selector. One header per manuscript for each of the four, and a bare
    # `II` -- the form -78's A1 line used -- now fails LOUDLY instead of sweeping two.
    for sel_, n_want in (("paper-I", 1), ("paper-II", 1), ("paper-III", 1), ("paper-IV", 1)):
        s = run(["scripts/wt130_quantifier_sweep.py", sel_])
        assert s.returncode == 0, "P14 %s exits %d" % (sel_, s.returncode)
        n_got = s.stdout.count("TOTAL: ")
        assert n_got == n_want, "P15 selector %s swept %d manuscripts" % (sel_, n_got)
    bad = run(["scripts/wt130_quantifier_sweep.py", "II"])
    assert bad.returncode != 0, "P16 bare 'II' still succeeds -- it must fail loudly"
    allp = run(["scripts/wt130_quantifier_sweep.py"])
    assert allp.returncode == 0 and allp.stdout.count("quantifier tokens on") == 4, \
        "P17 the no-selector census no longer lists four"

    # P18: Paper II's own count is unchanged by the selector fix.
    s2 = run(["scripts/wt130_quantifier_sweep.py", "paper-II"])
    assert "162 quantifier tokens on 124 lines that carry one, of 565" in s2.stdout, \
        "P18 Paper II's A1 count moved: %s" % s2.stdout.splitlines()[0]

    # P19-P21: the checklist now HOLDS what the manuscript defers to it, and the
    # manuscript's deferral sentence is the one still standing, unedited.
    c2 = CHECK.read_text("utf-8")
    assert c2.count("PREPRINT-CHECKLIST.md`\"*") == 1, "P19 checklist item not unique"
    assert "bibliographic details verified against a publisher page" in c2, "P20 item text lost"
    p2 = PAPER.read_text("utf-8")
    assert p2.count("re-checked at submission per\n`docs/papers/PREPRINT-CHECKLIST.md`") == 1, \
        "P21 the manuscript's deferral sentence moved"

    # P22: the suite the manuscript counts is still 18 and still green.
    t = subprocess.run([py, "-m", "pytest", "tests/", "-q"], cwd=ROOT,
                       capture_output=True, text=True)
    assert t.returncode == 0, "P22a suite red\n%s" % t.stdout[-3000:]
    n = len(re.findall(r"^def test_", (ROOT / "tests/test_redistribution.py").read_text("utf-8"), re.M))
    assert n == 18, "P22b test_redistribution.py count moved: %d" % n

    print("wt141: 3 repairs (2 scripts, 1 checklist), 0 manuscript edits, 22 post-conditions PASS")
    print("       A1 count unchanged at 162/124/565; suite green; residuals now printed by wt030.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
