#!/usr/bin/env python3
"""wealthTensor-78 -- Paper II's EIGHTH independent P7 read, frozen instrument set.

TWO findings, both repaired here, and NEITHER is residue of -77.

II-35  SEC 3.1's three kappa residuals are computed from the four-decimal kappa values
       DISPLAYED by wt030_report.py, not from the quantities. All three reproduce
       exactly from the rounded display:
           r=1.000  (0.1026 - r*E)/(r*E) = -4.352%  -> paper's -4.4 %
           r=0.100  (0.0102 - r*E)/(r*E) = -4.912%  -> paper's -4.9 %
           r=0.025  (0.0025 - r*E)/(r*E) = -6.777%  -> paper's -6.8 %
       Measured at full precision at the REPORTED horizon T = 1200:
           r=1.000  kappa=0.102609046638  resid = -4.344 %
           r=0.100  kappa=0.010236878093  resid = -4.568 %
           r=0.025  kappa=0.002527559116  resid = -5.749 %
       Two of the three are wrong by 0.33 and 1.05 PERCENTAGE POINTS -- far outside any
       rounding of the reported figures. At r = 0.025 the display quantum (+/-0.00005) is
       +/-2 % of kappa itself, i.e. LARGER than the spread the sentence reports. The
       -6.8 % figure is real, but it belongs to r = 0.010, the sweep's lowest rate and a
       row that is NOT in this table.
       The range "4-7 %" survives, because across the FULL sweep behind the table the
       residual does reach -6.831 % at r = 0.010; the sentence's fault is that it attaches
       that endpoint to a tabulated rate. Scope is therefore made explicit rather than
       deleted. "Monotone in the rate" is also made exact: the residual is flat from
       r = 1.000 to r = 0.500 (-4.344 %, -4.338 %) and widens monotonically below r = 0.5.
       NOT RESIDUE: blame 2b3e24b5 (2026-08-17), predates -77's 6b0655b (2026-08-18).

II-36  tests/test_redistribution.py:195-196 -- the guard for the manuscript's ONLY named
       closed-form scalar asserts  ceiling == approx(0.10734, abs=1e-4)  and carries the
       inline comment  # 0.10734...  . The closed form's exact value is 0.1072689396.
       The reference constant is wrong in the fourth decimal; the guard survives on
       71.1 % of its tolerance budget. Tightening abs to 1e-5 -- the obvious "make this
       stricter" move -- turns the suite RED against a CORRECT implementation. This is the
       paper's own SEC 4 failure mode ("it survived initial review because it looked like a
       convergence check and convergence checks look like that") inside the guard that
       exists to prevent it.
       NOT RESIDUE: blame 3b11f236 (2026-08-05) -- the very commit SEC 7 pins.

Test COUNT is unchanged at 18: II-36 edits two lines inside an existing test body.
"""
import pathlib, re, subprocess, sys, math

ROOT = pathlib.Path(__file__).resolve().parents[1]
PAPER = ROOT / "docs/papers/paper-II-redistribution/paper-II.md"
TEST = ROOT / "tests/test_redistribution.py"

OLD_PAPER = """  **E[η⁺] = μΦ(μ/σ) + σφ(μ/σ) = 0.1073** for the parameters above. The simulated κ runs
  **4–7 % below** that form at every rate tabulated, and the residual is monotone in the
  rate — −4.4 %, −4.9 %, −6.8 % at *r* = 1.000, 0.100, 0.025 — which makes it a
  denominator convention rather than noise: the implementation measures κ against
  post-growth wealth. The test suite asserts agreement within 10 %."""

NEW_PAPER = """  **E[η⁺] = μΦ(μ/σ) + σφ(μ/σ) = 0.1073** for the parameters above. The simulated κ runs
  **4–7 % below** that form across the full rate sweep behind the table — −4.3 %, −4.6 %,
  −5.7 % at the three flow rates tabulated here (*r* = 1.000, 0.100, 0.025), reaching
  −6.8 % at the sweep's lowest rate, *r* = 0.010. The residual is flat between *r* = 1.000
  and *r* = 0.500 and widens monotonically below it, which makes it a denominator
  convention rather than noise: the implementation measures κ against post-growth wealth.
  *These residuals are computed from the unrounded κ rather than from the four-decimal
  values the table displays; at *r* = 0.025 that display quantum is ±2 % of κ itself, which
  is wider than the spread being reported.* The test suite asserts agreement within 10 %."""

OLD_TEST = """    ceiling = mu * Phi + sigma * phi                    # 0.10734...
    assert ceiling == pytest.approx(0.10734, abs=1e-4)"""

NEW_TEST = """    ceiling = mu * Phi + sigma * phi                    # 0.1072689396...
    # wealthTensor-78 (II-36): this asserted 0.10734 at abs=1e-4 from 3b11f23 until
    # 2026-08-18. The closed form is 0.1072689396; the old constant was wrong in the
    # FOURTH decimal and passed on 71 % of its tolerance budget, so tightening abs to
    # 1e-5 would have gone red against a CORRECT implementation. The manuscript quotes
    # this scalar to four decimals (0.1073), so the guard now pins it far tighter.
    assert ceiling == pytest.approx(0.1072689396, abs=1e-7)
    assert round(ceiling, 4) == 0.1073          # exactly what SEC 3.1 and SEC 7 print"""


def main() -> int:
    p = PAPER.read_text(encoding="utf-8")
    t = TEST.read_text(encoding="utf-8")

    assert p.count(OLD_PAPER) == 1, "paper anchor not unique: %d" % p.count(OLD_PAPER)
    assert t.count(OLD_TEST) == 1, "test anchor not unique: %d" % t.count(OLD_TEST)

    before_tests = len(re.findall(r"^def test_", t, re.M))
    abstract_before = p.split("## 1 · Introduction")[0]
    refs_before = p.split("## References")[1]

    PAPER.write_text(p.replace(OLD_PAPER, NEW_PAPER), encoding="utf-8")
    TEST.write_text(t.replace(OLD_TEST, NEW_TEST), encoding="utf-8")

    p2 = PAPER.read_text(encoding="utf-8")
    t2 = TEST.read_text(encoding="utf-8")
    flat = re.sub(r"\s+", " ", p2)

    # ---- POST-CONDITIONS -------------------------------------------------
    # 1. the three wrong residuals are GONE, at every site, on flattened text
    assert "−4.4 %, −4.9 %, −6.8 %" not in flat, "P1 old triple survives"
    # 2. the corrected triple is present exactly once
    assert flat.count("−4.3 %, −4.6 %, −5.7 %") == 1, "P2 new triple not unique"
    # 3. -6.8 % is retained but now ATTACHED to r = 0.010, not to a tabulated rate
    assert flat.count("−6.8 %") == 1, "P3 -6.8% count moved"
    assert "−6.8 % at the sweep's lowest rate, *r* = 0.010" in flat, "P4 -6.8% unattached"
    # 4. the "4-7 %" range survives and is now explicitly scoped to the FULL sweep
    assert "**4–7 % below** that form across the full rate sweep" in flat, "P5 range unscoped"
    # 5. SEC 1's independent "within 7 %" claim is UNTOUCHED -- it is true at full precision
    #    (max residual 6.831 % at r = 0.010) and was NOT part of this repair.
    assert flat.count("to within 7 % at every rate tabulated") == 1, "P6 sec1 claim disturbed"
    # 6. the manuscript's "within 10 %" sentence survives AND the test still asserts rel=0.10
    assert "The test suite asserts agreement within 10 %." in flat, "P7 10% sentence lost"
    assert "pytest.approx(ceiling, rel=0.10)" in t2, "P8 the 10% assertion itself moved"
    # 7. test COUNT unchanged -- the abstract, SEC 1 and SEC 7 all assert 18
    after_tests = len(re.findall(r"^def test_", t2, re.M))
    assert before_tests == after_tests == 18, "P9 test count moved: %d -> %d" % (before_tests, after_tests)
    # 8. abstract, front matter and references byte-identical
    assert p2.split("## 1 · Introduction")[0] == abstract_before, "P10 front matter moved"
    assert p2.split("## References")[1] == refs_before, "P11 references moved"
    # 9. the guard's new constant IS the closed form, computed here independently
    z = 0.05 / 0.20
    Phi = 0.5 * (1 + math.erf(z / math.sqrt(2)))
    phi = math.exp(-z * z / 2) / math.sqrt(2 * math.pi)
    exact = 0.05 * Phi + 0.20 * phi
    assert abs(exact - 0.1072689396) < 1e-9, "P12 new constant is not the closed form"
    assert abs(exact - 0.10734) > 1e-5, "P13 old constant was not actually wrong"
    assert round(exact, 4) == 0.1073, "P14 manuscript's 4-dp value not reproduced"
    # 10. the old wrong constant appears NOWHERE in the test file except the audit comment
    assert t2.count("0.10734") == 1, "P15 stale constant count: %d" % t2.count("0.10734")
    assert "# wealthTensor-78 (II-36)" in t2, "P16 audit trail missing"
    # 11. SEC 7's per-file pin is untouched and still exact
    sha = subprocess.run(["git", "-C", str(ROOT), "log", "-1", "--format=%h", "--",
                          "src/wealth_tensor/redistribution.py"],
                         capture_output=True, text=True, check=True).stdout.strip()
    assert sha == "3b11f23", "P17 sec7 pin no longer exact: %s" % sha
    assert "**3b11f23**" in p2, "P18 pin text moved"

    print("wt139: 1 manuscript edit, 1 test edit, 18 post-conditions PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
