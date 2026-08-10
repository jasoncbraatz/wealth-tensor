"""Regenerate every number Paper III reports from `lag.py`.

Paper II has `wt030_report.py`; Paper III had no equivalent, which meant its results
table could not satisfy the preprint checklist's "exact regeneration command" line.
This is that command.

    python3 scripts/wt027_report.py

Three tables, matching the three claims:

  A · WT-027 · the filter in isolation (crisis mechanism disabled). Recognition lag,
      inter-period smoothing and deferred information against observability phi.
  B · WT-028 · volatility is relocated, not suppressed. Inter-crisis smoothing against
      the share of reported movement occurring inside corrections.
  C · WT-027 · crisis frequency by entropy rate, at fixed observability.
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
    print("A · THE FILTER IN ISOLATION (crisis mechanism disabled, %d periods)" % PERIODS)
    print("   phi   recognition lag   smoothing   deferred information")
    for phi in PHIS:
        firm = LayeredFirm(observable_share=phi, crisis_threshold=np.inf)
        res = firm.run(PERIODS)
        print("  %4.1f   %15d   %9.3f   %20.1f"
              % (phi, recognition_lag(res), variance_suppression(res),
                 deferred_information(res)))
    print()


def table_b() -> None:
    print("B · VOLATILITY IS RELOCATED, NOT SUPPRESSED (crisis mechanism live)")
    print("   phi   inter-crisis smoothing   share of movement in corrections   crises")
    for phi in PHIS:
        res = LayeredFirm(observable_share=phi).run(PERIODS)
        vs = variance_suppression(res)
        print("  %4.1f   %22s   %32.2f   %6d"
              % (phi, "n/a" if np.isnan(vs) else "%.2f" % vs,
                 variance_concentration(res), res["n_crises"]))
    print()


def table_c() -> None:
    print("C · CRISIS FREQUENCY BY ENTROPY RATE (phi = 0.3, %d periods)" % PERIODS)
    print("   entropy rate   sector sketch                 crises")
    sectors = ((0.01, "warehouse retail"), (0.05, "industrial"), (0.20, "software"))
    for d, name in sectors:
        res = LayeredFirm(entropy_rate=d, observable_share=0.3).run(PERIODS)
        print("  %13.2f   %-28s %6d" % (d, name, res["n_crises"]))
    print()


def table_d() -> None:
    print("D · THE COUPLING IS A SAWTOOTH (phi = 0.3, %d periods)" % PERIODS)
    res = LayeredFirm(observable_share=0.3).run(PERIODS)
    lam = res["coupling"]
    lam = lam[np.isfinite(lam)]
    print("   mean Lambda      %.6f" % lam.mean())
    print("   min  Lambda      %.6f" % lam.min())
    print("   max  Lambda      %.6f" % lam.max())
    print("   crises           %d" % res["n_crises"])
    print("   Lambda == 1 at every correction: %s"
          % all(abs(res["coupling"][c["period"]] - 1.0) < 1e-12 for c in res["crises"]))
    print()


if __name__ == "__main__":
    print(__doc__.split("\n")[0])
    print("=" * 78)
    print()
    table_a()
    table_b()
    table_c()
    table_d()
