import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "src"))
from wealth_tensor.lambda_sensitivity import (sweep_coupling, invariance_report,
                                              scaling_exponent, DIMENSIONLESS)
rows = sweep_coupling(observable_share=0.3)
print("LAMBDA SENSITIVITY SWEEP (phi=0.3, 400 periods, coupling 1e-6 .. 1e+6 currency/J)\n")
print(f"{'eta':>10s} {'deferred [cur]':>16s} {'Lambda_T':>12s} {'L/eta':>10s} "
      f"{'lag':>4s} {'vsupp':>7s} {'vconc':>7s} {'crises':>7s} {'relmag':>8s}")
for r in rows:
    print(f"{r['coupling']:10.0e} {r['deferred_currency']:16.6e} {r['terminal_lambda']:12.6e} "
          f"{r['lambda_over_eta']:10.6f} {r['recognition_lag']:4d} "
          f"{r['variance_suppression']:7.4f} {r['variance_concentration']:7.4f} "
          f"{r['n_crises']:7d} {r['relative_crisis_magnitude']:8.5f} "
          f"{r['mean_coupling_ratio']:10.6f} {r['min_coupling_ratio']:9.6f}")
print("\nSPREAD of each dimensionless diagnostic across 12 orders of magnitude:")
sp = invariance_report(rows)
for k in DIMENSIONLESS:
    print(f"  {k:28s} {sp[k]:.1e}")
print("\nLOG-LOG SLOPE of dimensional quantities against the coupling (a numeraire gives 1):")
for col in ("deferred_currency", "terminal_lambda"):
    print(f"  {col:28s} {scaling_exponent(rows, col):.12f}")
