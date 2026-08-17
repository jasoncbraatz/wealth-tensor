#!/usr/bin/env python3
"""wealthTensor-65 · what ACTUALLY happens at rho = 0, measured.

`REVIEW-005` §2's `II-3` says: *"rho is defined as the share of a gain recognised as flow, and
kappa = r*E[eta+] on the flow base, so rho = 0 sets the base and kappa to EXACTLY ZERO: the
levied path IS the unlevied path."*

`src/wealth_tensor/redistribution.py:131` says otherwise:

    recognised_flow += self.rho * gain + self.wage

At rho = 0 the flow base is not empty. It is the ACCUMULATED WAGE — and `self.wage` is a
scalar, identical for every agent. So the levy is assessed, wealth IS moved (kappa > 0), and
the distribution does not change because the base carries NO DISPERSION, not because there is
no base.

This script measures kappa at rho = 0 and checks the per-agent levy is uniform, so the
manuscript's sentence can be written from the number instead of from the prose. `-64`'s rule:
the defects live in the sections whose numbers are NOT in the table.
"""
from __future__ import annotations

import pathlib
import sys

import numpy as np

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from wealth_tensor.redistribution import (  # noqa: E402
    RedistributiveEconomy, stationary_gini)

T = 1200


def run(**kw):
    return RedistributiveEconomy(**kw).run(periods=T)


unlevied = run()
rho0 = run(base="flow", rate=1.0, realization=0.0)
rho1 = run(base="flow", rate=1.0, realization=1.0)

print(f"{'case':<28} {'gini':>8} {'kappa':>10} {'assessments':>12}")
for name, r in (("unlevied", unlevied), ("flow r=1 rho=0", rho0), ("flow r=1 rho=1", rho1)):
    print(f"{name:<28} {stationary_gini(r):>8.4f} {r['kappa']:>10.6f} {r['assessments']:>12d}")

print()
print("IS kappa EXACTLY ZERO AT rho=0?  ", rho0["kappa"] == 0.0)
print("kappa at rho=0                  ", repr(rho0["kappa"]))
print("per-assessment kappa range      ",
      f"{rho0['reallocation'].min():.6f} .. {rho0['reallocation'].max():.6f}")
print()
print("IS the levied path the unlevied path (wealth vectors identical)?  ",
      bool(np.array_equal(rho0["wealth"], unlevied["wealth"])))
print("max |w_rho0 - w_unlevied| / mean w  ",
      float(np.abs(rho0["wealth"] - unlevied["wealth"]).max() / unlevied["wealth"].mean()))
print()
print("stationary gini rho0 vs unlevied   ",
      stationary_gini(rho0), stationary_gini(unlevied),
      abs(stationary_gini(rho0) - stationary_gini(unlevied)))

# The claim that actually explains it: the rho=0 flow base is uniform across agents.
econ = RedistributiveEconomy(base="flow", rate=1.0, realization=0.0)
print()
print("wage is a scalar, identical for every agent:", repr(econ.wage))
print("=> at rho=0 recognised_flow accumulates ONLY the wage, so the base has zero dispersion")
