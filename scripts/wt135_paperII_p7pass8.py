#!/usr/bin/env python3
"""wealthTensor-76 · Paper II's SIXTH independent P7 read -- five repairs, one new axis paid twice.

GUARD HONESTY (WT-118, wt129's rule, no exception): every OLD string is asserted present
EXACTLY ONCE in the ORIGINAL before any substitution runs, and the guards run BEFORE the
backups, so a failed guard writes nothing.

THE INSTRUMENT THIS PASS BROUGHT (-75's fifth axis, applied to Paper II for the first time):
grep every script section 7 names for its imports, pair it against the module section 7 pairs
it with, and RUN every command section 7 names with its RC recorded, before a word of prose.
  wt030_report.py   imports wealth_tensor.redistribution        RC 0
  wt077_tail_index.py  imports numpy/scipy ONLY -- no src/ code  RC 0  (correctly disclosed)
  pytest tests/test_redistribution.py                            RC 0, 18 passed
That sequence produced II-27 and II-30. Reading produced II-28, II-29, II-31.

FINDINGS REPAIRED
  II-27  Section 7 promises `python3 scripts/wt030_report.py` regenerates EVERY number in
         section 3. Two numbers in 3.3 are not in its output: "the minimum is **interior**,
         0.451 at *P* = 30" and "the whole sweep spans 0.035". The script's periodicity tuple
         is (1,2,4,10,20,50) -- its printed span is 0.030. Both numbers were added by
         wealthTensor-74, from a TEST's sweep, in the same pass that edited section 7.
         Measured today at T = 1200: P = 30 -> 0.4507, span 0.0353. Repaired by making the
         promise TRUE rather than by weakening the prose: P = 30 joins the sweep.
  II-28  Section 3.2 claims the rho = 0 identity holds "agent by agent rather than merely on
         the summary statistics" and that "The identity is structural, and saying so is
         stronger than calling it a near-match." The only committed check WAS a near-match:
         pytest.approx(abs=0.01) on the Gini plus top_share > 0.95. The claim is TRUE --
         np.array_equal on the 800-vector, max abs diff 0.0 -- and now asserted.
         GUARD HONESTY, both halves verified at T = 600: passes at rho = 0.00, fails at
         rho = 0.10 / 0.25 / 1.00.
  II-29  Limitation 5 still scopes the non-simulation numbers to "section 3.1's three
         Var[log a] values" and cites section 7 in the same sentence -- where wealthTensor-74
         moved that count to FOUR in two places and missed this third site.
  II-30  Section 7's two overclaiming guards: `test_excess_demand_is_monotone_...` is said to
         be "in the same suite", four lines under a bullet naming `tests/test_redistribution.py`
         as the suite. It lives in `tests/test_excess_demand.py`. A replicator greps the named
         file and finds one of the two. Section 1's contribution 5 already says it correctly --
         "in a companion module of the same suite" -- so the repair copies the manuscript's
         own pattern, and names the module.
  II-31, THE SOFTEST AND NAMED AS SUCH  Section 7 enumerates the numbers that are not
         simulation output as "the four closed-form quantities the next bullet names".
         Section 3.4's Gini ceiling (N-1)/N = 0.99875 is a fifth: stated at L85 and L313,
         printed by neither wt030_report.py nor wt077_tail_index.py. It is soft because
         0.99875 is arguably not a "measured" number -- but neither are the four, and
         section 7 lists those, so the category is section 7's own.

NOT DONE HERE, written down at the moment of not-doing:
  * Section 7's `wt077_tail_index.py` imports NO code from `src/`. Section 7's commit pin
    already discloses that it does not cover the two scripts/ commands, so the pairing is
    honest as written and was left alone. If a later pass wants a pin that covers the
    quadrature values it needs a SECOND per-file pin, not an edit here.
  * The nine uncited reference entries (wt133 sweep 2) belong to card 1217568192511533 and
    are not touched.
  * The front-matter stamp "Version 0.2, 2026-08-11" is wrong -- the References note dates
    its own re-verification 2026-08-17, INSIDE the document. Card 1217568297674954 asks Jason
    for the rule; a sixth data point is commented there instead of guessed at here.
"""
from __future__ import annotations

import pathlib
import shutil
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
PAPER = ROOT / "docs/papers/paper-II-redistribution/paper-II.md"
REPORT = ROOT / "scripts/wt030_report.py"
TEST = ROOT / "tests/test_redistribution.py"
TAG = "bak-wt135"

PAPER_EDITS = [
    ("II-29 §5", """   `seed = 0` rather than an ensemble average — the exception is §3.1's three Var[log *a*]
   values, which are quadrature rather than simulation output (§7). Seed-robustness is asserted""",
     """   `seed = 0` rather than an ensemble average — the exceptions are the five closed-form
   quantities §7 names: §3.1's E[η⁺] and its three Var[log *a*] values, which are quadrature,
   and §3.4's Gini ceiling, which is arithmetic in *N*. Seed-robustness is asserted"""),

    ("II-31 §7", """used, because no empirical data is used at all — every measured number is generated by
simulation, save the four closed-form quantities the next bullet names.""",
     """used, because no empirical data is used at all — every measured number is generated by
simulation, save five closed-form quantities: the four the next bullet names, and §3.4's Gini
ceiling (*N*−1)/*N* = 0.99875, which is arithmetic in *N* and is printed by no command here."""),

    ("II-30 §7", """  guard outlives it — in the same suite; it is a different companion from §3.2's work on the
  reporting layer.""",
     """  guard outlives it — in a companion module of the same suite,
  `tests/test_excess_demand.py`; it is a different companion from §3.2's work on the
  reporting layer."""),
]

REPORT_EDITS = [
    ("II-27 wt030 periodicity sweep",
     """for P in (1,2,4,10,20,50):""",
     """for P in (1,2,4,10,20,30,50):"""),
]

TEST_EDITS = [
    ("II-28 §3.2's agent-by-agent claim",
     """    unrealised = econ(base="flow", rate=1.0, realization=0.0)
    nothing = econ()
    assert stationary_gini(unrealised) == pytest.approx(stationary_gini(nothing), abs=0.01)""",
     """    unrealised = econ(base="flow", rate=1.0, realization=0.0)
    nothing = econ()
    # wealthTensor-76. §3.2 claims the two paths agree AGENT BY AGENT and calls the identity
    # structural -- "stronger than calling it a near-match". Until now the only committed
    # check WAS a near-match: abs=0.01 on one summary statistic. The manuscript's strongest
    # sentence in §3.2 was pinned by nothing able to see what it claims. GUARD HONESTY --
    # this line passes at rho = 0.00 and fails at rho = 0.10, 0.25 and 1.00, both verified.
    assert np.array_equal(unrealised["wealth"], nothing["wealth"])
    assert stationary_gini(unrealised) == pytest.approx(stationary_gini(nothing), abs=0.01)"""),
]


def guard(path, edits):
    text = path.read_text(encoding="utf-8")
    for name, old, _new in edits:
        n = text.count(old)
        if n != 1:
            sys.exit(f"GUARD FAILED [{name}] in {path.name}: OLD found {n} times, expected 1. "
                     f"Nothing written.")
    return text


def apply(path, text, edits):
    shutil.copy2(path, path.with_name(path.name + "." + TAG))
    for _name, old, new in edits:
        text = text.replace(old, new, 1)
    path.write_text(text, encoding="utf-8")


def main():
    # ---- GUARDS FIRST, ALL OF THEM, BEFORE ANY BACKUP OR WRITE (WT-118) ----
    paper_text = guard(PAPER, PAPER_EDITS)
    report_text = guard(REPORT, REPORT_EDITS)
    test_text = guard(TEST, TEST_EDITS)

    abstract_before = paper_text.split("## 1 · Introduction")[0]
    refs_before = paper_text.split("## References")[1]

    apply(PAPER, paper_text, PAPER_EDITS)
    apply(REPORT, report_text, REPORT_EDITS)
    apply(TEST, test_text, TEST_EDITS)
    print(f"wrote 3 files, backups tagged .{TAG}")

    # ---- POST-CONDITIONS ----
    after = PAPER.read_text(encoding="utf-8")

    assert after.split("## 1 · Introduction")[0] == abstract_before, \
        "POST-CONDITION FAILED: front matter or abstract changed"
    print("post 1/4 OK  front matter + abstract byte-identical")

    assert after.split("## References")[1] == refs_before, \
        "POST-CONDITION FAILED: reference list changed"
    print("post 2/4 OK  reference list byte-identical")

    r = subprocess.run([sys.executable, str(ROOT / "scripts/wt133_crossref_sweep.py")],
                       cwd=str(ROOT), stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    assert r.returncode == 0, "POST-CONDITION FAILED: wt133 red on the patched text\n" + \
        r.stdout.decode("utf-8", "replace")
    print("post 3/4 OK  wt133 cross-reference sweep RC 0 on the patched text")

    # the one that makes II-27's repair checkable rather than asserted: run the PATCHED
    # command and demand the row the manuscript names.
    r = subprocess.run([sys.executable, str(REPORT)], cwd=str(ROOT),
                       stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    out = r.stdout.decode("utf-8", "replace")
    assert r.returncode == 0, "POST-CONDITION FAILED: patched wt030_report.py exits nonzero\n" + out
    line = [l for l in out.splitlines() if "every  30 periods" in l]
    assert line, "POST-CONDITION FAILED: patched wt030_report.py prints no P = 30 row\n" + out
    assert "Gini=0.451" in line[0], \
        f"POST-CONDITION FAILED: P = 30 row is {line[0]!r}, manuscript says 0.451"
    print(f"post 4/4 OK  §7's command now prints §3.3's own number:{line[0]}")


if __name__ == "__main__":
    main()
