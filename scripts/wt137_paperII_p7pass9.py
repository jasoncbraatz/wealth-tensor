#!/usr/bin/env python3
"""wt137 -- Paper II's SEVENTH independent P7 read (wealthTensor-77, REVIEW-017).

THE FIRST FROZEN-INSTRUMENT PASS IN THIS PROJECT'S HISTORY. No axis was invented here.
All five of A1..A5 were run against Paper II before a word of prose was read, exactly as
docs/p7-passes.tsv's matrix required, and three findings landed anyway.

GUARD HONESTY (WT-118, wt129's rule, no exception): every OLD string below is asserted
present BEFORE any backup or write, and every NEW string is asserted absent. A guard that
cannot fail and a guard that cannot pass are the same bug wearing different clothes.

WHAT THIS PATCHES
  II-32  TWO SITES, ONE DEFECT, AND IT IS THE RESIDUE OF -76's OWN REPAIR.
         S7's opening sentence (edited at -76) says S3.4's Gini ceiling (N-1)/N = 0.99875
         "is printed by no command here". SEVEN LINES BELOW, S7's regeneration bullet
         promises `wt030_report.py` regenerates every number in S3 "except S3.1's four
         closed-form quantities" -- a list that does not contain the ceiling. And S1's
         contribution 5 says "every number below is regenerated ... by the two commands
         S7 names", with no exception at all. Confirmed mechanically: 0.99875 appears
         ZERO times in the stdout of either named command.
         This is II-27's shape at II-27's own site, one pass later. -76 repaired II-31 at
         S7-intro and S5.5 and did not carry it to the two universal claims.
         REPAIRED BY MOVING THE PROSE, NOT THE PROMISE -- the inverse of II-27, and
         deliberately so (-76(iii): ask which one is RIGHT before deciding which moves).
         S7-intro is right: the ceiling is arithmetic in N, and printing it from a
         simulation script would blur the very distinction S5.5 and S7 both draw.

  II-33  S3.4 CONFLATES A SATURATED READING WITH THE CEILING -- IN THE SECTION WHOSE ENTIRE
         METHODOLOGICAL CONTRIBUTION IS SEPARATING THEM. Twelve lines above, S3.4 says the
         unopposed process "reads Gini 0.994 and flat -- short of the 0.99875 ceiling it is
         pinned against". Then: "a gap of 0.103 whose upper edge is the saturation ceiling
         itself". Falsified by the section's own arithmetic: 0.994 - 0.891 = 0.103, while
         0.99875 - 0.891 = 0.10775. The repair preserves the argument -- the upper edge is
         N-dependent either way, which is what "redrawn for every N" needs.

  II-34  S5.5's MITIGATION IS MEASURED AT HALF THE HORIZON OF THE FIGURES IT MITIGATES.
         S5.5 offers `test_the_result_is_not_a_lucky_seed` as the answer to "one seed per
         reported figure". Every reported figure is at T = 1200 (S2.1, and wt030_report.py).
         That test runs through econ(), and tests/test_redistribution.py sets T = 600. S3.4
         states, in the manuscript's own words, that "the top-share statistic is also
         horizon-stable where the Gini is not" -- and the band is on the GINI.
         MEASURED BEFORE ASSERTED (-76(iii), and -75(iii) on guard honesty):
           T =  600  stock 0.4300 0.4361 0.4354 0.4186 0.4442 | flow 0.3852 0.3924 0.3912 0.3744 0.3961
           T = 1200  stock 0.4430 0.4398 0.4451 0.4318 0.4361 | flow 0.3948 0.3936 0.3957 0.3867 0.3894
         Both bands hold at both horizons. THE CLAIM IS TRUE AND THE GUARD WAS SHORT, so
         this one repairs the PROMISE (II-27's shape): the test now runs both horizons.
         The prose also loses "a stated band" (singular) for the two bands that exist.
         TEST COUNT DELIBERATELY UNCHANGED AT 18 -- three manuscript sites and
         tests/test_paper_test_counts_are_derived.py all pin it. The body moves, not the count.

NOT DONE HERE (per wt134's pattern):
  * A6, the docstring axis, is PARKED by the handoff and was not spent. Nineteen unasserted
    prose claims in tests/test_redistribution.py remain unread -- including this file's own
    new docstring line, and including "Verified horizon-stable at T = 600 and T = 1200" on
    test_periodicity_is_second_order_at_a_matched_average_rate, which is asserted by nothing
    and is the nearest neighbour of II-34. Spend it on Paper III, or on Paper II after the
    frozen pair resolves.
  * The nine uncited reference entries (card 1217568192511533) -- untouched, as at -76.
  * The version stamp (card 1217568297674954) -- untouched; the ruling is Jason's.
  * wt077_tail_index.py is still covered by no per-file pin (REVIEW-016 S4 item 1).
  * Paper I's L568 non-circularity sentence, still the untested third instance.
"""
import pathlib, re, subprocess, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
PAPER = ROOT / "docs/papers/paper-II-redistribution/paper-II.md"
TEST = ROOT / "tests/test_redistribution.py"
TAG = ".bak-wt137"

# ------------------------------------------------------------------ II-32, site 1 of 2: S1 c5
M1_OLD = """5. A **reproducible artefact**: every number below is regenerated from a public repository by
   the two commands §7 names, and the claims are held in place by the 18 tests in"""
M1_NEW = """5. A **reproducible artefact**: every number below is regenerated from a public repository by
   the two commands §7 names — save §3.4's Gini ceiling, which is arithmetic in *N* and is
   printed by neither — and the claims are held in place by the 18 tests in"""

# ------------------------------------------------------------------ II-32, site 2 of 2: S7 bullet
M2_OLD = """  simulation output and come from `python3 scripts/wt077_tail_index.py`. The two commands are named"""
M2_NEW = """  simulation output and come from `python3 scripts/wt077_tail_index.py`, and except §3.4's Gini
  ceiling, which is arithmetic in *N* and is printed by neither. The two commands are named"""

# ------------------------------------------------------------------ II-33: S3.4
M3_OLD = """0.994 — a gap of 0.103 whose upper edge is the saturation ceiling itself, so any Gini threshold
would have to be drawn inside it and redrawn for every *N*; their top"""
M3_NEW = """0.994 — a gap of 0.103 whose upper edge is a *saturated reading* and not the 0.99875 ceiling it
falls short of, so any Gini threshold would have to be drawn inside it and redrawn for every
*N*; their top"""

# ------------------------------------------------------------------ II-34: S5.5 prose
M4_OLD = """   in: `test_the_result_is_not_a_lucky_seed` holds two configurations inside a stated band
   across five seeds. The qualitative separations are large relative to that band, but the
   third decimal is not defended."""
M4_NEW = """   in: `test_the_result_is_not_a_lucky_seed` holds two configurations inside their stated
   bands across five seeds, at the reported *T* = 1200 as well as at the suite's *T* = 600.
   The qualitative separations are large relative to those bands, but the
   third decimal is not defended."""

# ------------------------------------------------------------------ II-34: the guard itself
T1_OLD = '''def test_the_result_is_not_a_lucky_seed():
    for base, rate, lo, hi in (("stock", 0.025, 0.35, 0.55), ("flow", 0.25, 0.30, 0.50)):
        gs = [stationary_gini(econ(base=base, rate=rate, seed=s)) for s in range(5)]
        assert all(lo < g < hi for g in gs)'''
T1_NEW = '''def test_the_result_is_not_a_lucky_seed():
    """wealthTensor-77, II-34. Paper II S5.5 offers THIS test as the mitigation for "one seed
    per reported figure" -- and every reported figure is at T = 1200 while econ() runs at
    T = 600. S3.4 says in the paper's own words that the top share "is also horizon-stable
    where the Gini is not", and the band below is on the Gini, so a band checked only at half
    the reported horizon did not reach the numbers it was offered for. Both horizons now.
    Measured before asserted: at T = 1200 the two configurations read 0.4318-0.4451 and
    0.3867-0.3957, inside the bands the T = 600 version already used.
    """
    for base, rate, lo, hi in (("stock", 0.025, 0.35, 0.55), ("flow", 0.25, 0.30, 0.50)):
        for horizon in (T, 1200):
            gs = [stationary_gini(RedistributiveEconomy(base=base, rate=rate, seed=s).run(horizon))
                  for s in range(5)]
            assert all(lo < g < hi for g in gs), f"{base} r={rate} T={horizon}: {gs}"'''

MAN_EDITS = [("II-32a", M1_OLD, M1_NEW), ("II-32b", M2_OLD, M2_NEW),
             ("II-33", M3_OLD, M3_NEW), ("II-34-prose", M4_OLD, M4_NEW)]
TEST_EDITS = [("II-34-guard", T1_OLD, T1_NEW)]


def guard(path, edits):
    text = path.read_text()
    for name, old, new in edits:
        n = text.count(old)
        assert n == 1, f"GUARD FAILED [{name}]: OLD string occurs {n} times in {path.name}, want 1"
        assert new not in text, f"GUARD FAILED [{name}]: NEW string already present in {path.name}"
    return text


def apply(path, text, edits):
    for _, old, new in edits:
        text = text.replace(old, new, 1)
    path.with_suffix(path.suffix + TAG).write_text(path.read_text())
    path.write_text(text)


def main():
    # ---- GUARDS FIRST, ALL OF THEM, BEFORE ANY BACKUP OR WRITE (WT-118) ----
    man = guard(PAPER, MAN_EDITS)
    tst = guard(TEST, TEST_EDITS)

    before_front = PAPER.read_text().split("## Abstract")[0]
    before_refs = PAPER.read_text().split("## References")[1]
    before_abstract = PAPER.read_text().split("## Abstract")[1].split("## 1 ")[0]

    apply(PAPER, man, MAN_EDITS)
    apply(TEST, tst, TEST_EDITS)

    # ---- POST-CONDITIONS ----
    now = PAPER.read_text()
    assert now.split("## Abstract")[0] == before_front, \
        "POST-CONDITION FAILED: front matter changed"
    assert now.split("## Abstract")[1].split("## 1 ")[0] == before_abstract, \
        "POST-CONDITION FAILED: abstract changed"
    assert now.split("## References")[1] == before_refs, \
        "POST-CONDITION FAILED: reference list changed"

    # the count three sites and a test pin must not move
    assert len(re.findall(r"^def test_", TEST.read_text(), re.M)) == 18, \
        "POST-CONDITION FAILED: tests/test_redistribution.py no longer holds 18 tests"

    r = subprocess.run([sys.executable, "scripts/wt133_crossref_sweep.py"],
                       cwd=ROOT, capture_output=True, text=True)
    assert r.returncode == 0, "POST-CONDITION FAILED: wt133 red on the patched text\n" + r.stdout

    # THE ONE THAT MATTERS FOR II-32: the manuscript must no longer promise a command
    # produces a number that command does not produce. Assert the exception exists at BOTH
    # universal sites, and re-run the named command to confirm the ceiling is still absent.
    flat = " ".join(now.split())
    sites = flat.count("§3.4's Gini ceiling")
    assert sites == 4, (
        "POST-CONDITION FAILED: the ceiling exception is stated at %d sites, want 4 "
        "(§1 c5, §5.5, §7 intro, §7 bullet)" % sites)
    r = subprocess.run([sys.executable, "scripts/wt030_report.py"],
                       cwd=ROOT, capture_output=True, text=True)
    assert r.returncode == 0, "POST-CONDITION FAILED: wt030_report.py exits nonzero"
    assert "0.99875" not in r.stdout, \
        "POST-CONDITION FAILED: wt030_report.py now prints 0.99875 -- II-32's repair moved the wrong object"

    # II-34: the patched guard must actually run at the reported horizon and must be able to FAIL
    r = subprocess.run([sys.executable, "-m", "pytest",
                        "tests/test_redistribution.py::test_the_result_is_not_a_lucky_seed", "-q"],
                       cwd=ROOT, capture_output=True, text=True)
    assert r.returncode == 0, "POST-CONDITION FAILED: patched lucky-seed test is red\n" + r.stdout
    assert "1200" in TEST.read_text(), "POST-CONDITION FAILED: reported horizon not in the guard"

    print("wt137 OK -- 4 manuscript edits, 1 test edit, all post-conditions green")


if __name__ == "__main__":
    main()
