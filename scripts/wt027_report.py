"""Regenerate every number Paper III reports from `lag.py`.

Paper II has `wt030_report.py`; Paper III had no equivalent, which meant its results
table could not satisfy the preprint checklist's "exact regeneration command" line.
This is that command.

    python3 scripts/wt027_report.py

FIVE blocks. The module said "three tables" and printed four for as long as D existed;
section 11 of the manuscript repeated the miscount (wealthTensor-80, III-12). The count is
stated here and asserted in tests/test_lag.py so it cannot drift again:

  A · WT-027 · the filter in isolation (recognition mechanism disabled). Recognition lag,
      inter-period smoothing and deferred information against observability phi.
  A' · section 3.1's PROSE values -- the sigmoidal-lag readings at phi = 0.9 and phi = 0.1,
      and D(0) at four decimals. Section 3.1 quotes all three and table A prints none of
      them, because table A sweeps the five phi the manuscript tabulates and no others.
  B · WT-028 · volatility is relocated, not suppressed. Inter-event smoothing against
      the share of reported movement occurring inside corrections -- and, in the added
      column, the FULL-PATH ratio of reported to physical volatility, which is the number
      section 3.2's prose quotes as 1.56 / 2.71 / 3.27 and which no named command printed.
  C · WT-027 · recognition-event frequency by entropy rate, at fixed observability.
  D · WT-027 · the coupling as a sawtooth: section A.2.4's four figures. NOTE the object is
      lambda = C/E, the DIMENSIONLESS ratio of section A.2.1 -- not the dimensional
      Lambda = eta*C/E swept by wt002_lambda_report.py. Section A.2.4 opens by drawing that
      distinction; this table is labelled to respect it.

WHY A' AND B'S FIFTH COLUMN EXIST. Section 11 promises that "every simulation result in
section A.2 and sections 2-3 is produced by open code" and names this script for section 3.
Six numbers section 3 reports in prose were produced by no named command: the three
full-path volatility ratios, the two off-grid lags, and D(0) to four decimals. The promise
is made true here rather than narrowed in the manuscript -- the precedent is II-27/II-37 in
the sibling paper. No extra simulation is bought: A' is the only new run, and B's new column
is computed from the run table B already makes.
"""

from __future__ import annotations

import pathlib
import sys

import numpy as np

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "src"))

from wealth_tensor.lag import (  # noqa: E402
    LayeredFirm,
    deferred_information,
    recognition_lag,
    variance_concentration,
    variance_suppression,
)

PERIODS = 400
PHIS = (1.0, 0.8, 0.5, 0.2, 0.0)


def table_a() -> None:
    print("A · THE FILTER IN ISOLATION (recognition mechanism disabled, %d periods)" % PERIODS)
    print("   phi   recognition lag   smoothing   deferred information")
    for phi in PHIS:
        firm = LayeredFirm(observable_share=phi, crisis_threshold=np.inf)
        res = firm.run(PERIODS)
        print("  %4.1f   %15d   %9.3f   %20.1f"
              % (phi, recognition_lag(res), variance_suppression(res),
                 deferred_information(res)))
    print()


def full_path_volatility_ratio(res: dict) -> float:
    """std of reported changes over std of real changes, measured across the WHOLE path.

    `variance_suppression` deliberately excludes the recognition periods, because the
    smoothing claim is about ordinary periods. Section 3.2's prose quotes the other
    quantity -- "the full-path ratio of reported to physical volatility is 1.56, 2.71 and
    3.27" -- and until wealthTensor-80 nothing in the repository computed it.
    """
    dE, dC = np.diff(res["real"]), np.diff(res["reported"])
    if dE.std() == 0:
        return float("nan")
    return float(dC.std() / dE.std())


def table_a_prime() -> None:
    print("A' · SECTION 3.1's PROSE VALUES (recognition mechanism disabled, %d periods)" % PERIODS)
    print("   the sigmoidal lag off the tabulated grid, and D(0) to four decimals")
    print("   phi   recognition lag   deferred information")
    for phi in (1.0, 0.9, 0.8, 0.5, 0.2, 0.1, 0.0):
        firm = LayeredFirm(observable_share=phi, crisis_threshold=np.inf)
        res = firm.run(PERIODS)
        mark = "   <- quoted in 3.1's prose only" if phi in (0.9, 0.1) else ""
        print("  %4.1f   %15d   %20.4f%s"
              % (phi, recognition_lag(res), deferred_information(res), mark))
    print()


def table_b() -> None:
    print("B · VOLATILITY IS RELOCATED, NOT SUPPRESSED (recognition mechanism live)")
    print("   phi   inter-event smoothing   share of reported movement inside recognition events   events   full-path ratio")
    for phi in PHIS:
        res = LayeredFirm(observable_share=phi).run(PERIODS)
        vs = variance_suppression(res)
        print("  %4.1f   %22s   %32.2f   %6d   %15.2f"
              % (phi, "n/a" if np.isnan(vs) else "%.2f" % vs,
                 variance_concentration(res), res["n_crises"],
                 full_path_volatility_ratio(res)))
    print()


def table_c() -> None:
    print("C · RECOGNITION-EVENT FREQUENCY BY ENTROPY RATE (phi = 0.3, %d periods)" % PERIODS)
    print("   entropy rate   sector sketch                 events")
    sectors = ((0.01, "warehouse retail"), (0.05, "industrial"), (0.20, "software"))
    for d, name in sectors:
        res = LayeredFirm(entropy_rate=d, observable_share=0.3).run(PERIODS)
        print("  %13.2f   %-28s %6d" % (d, name, res["n_crises"]))
    print()


def table_d() -> None:
    print("D · THE COUPLING IS A SAWTOOTH (phi = 0.3, %d periods)" % PERIODS)
    print("   lambda = C/E, DIMENSIONLESS (section A.2.1) -- not the dimensional Lambda = eta*C/E")
    res = LayeredFirm(observable_share=0.3).run(PERIODS)
    lam = res["coupling"]
    lam = lam[np.isfinite(lam)]
    print("   mean lambda      %.6f" % lam.mean())
    print("   min  lambda      %.6f" % lam.min())
    print("   max  lambda      %.6f" % lam.max())
    print("   crises           %d" % res["n_crises"])
    print("   lambda == 1 at every recognition event: %s"
          % all(abs(res["coupling"][c["period"]] - 1.0) < 1e-12 for c in res["crises"]))
    print()


if __name__ == "__main__":
    print(__doc__.split("\n")[0])
    print("=" * 78)
    print()
    table_a()
    table_a_prime()
    table_b()
    table_c()
    table_d()
