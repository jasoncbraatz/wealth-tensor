import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "src"))
from wealth_tensor.lambda_sensitivity import (sweep_coupling, invariance_report,
                                              scaling_exponent, DIMENSIONLESS)
rows = sweep_coupling(observable_share=0.3)
print("LAMBDA SENSITIVITY SWEEP (phi=0.3, 400 periods, coupling 1e-6 .. 1e+6 currency/J)\n")
print(f"{'eta':>10s} {'deferred [cur]':>16s} {'Lambda_T':>12s} {'L/eta':>10s} "
      f"{'lag':>4s} {'vsupp':>7s} {'vconc':>7s} {'events':>7s} {'relmag':>8s}")
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


def scaling_collapse() -> None:
    """The Buckingham-pi collapse, promoted out of the test suite into the report.

    Paper III section 3.3 quotes these figures. Until 2026-08-10 they existed ONLY inside
    tests/test_lambda_sensitivity.py, which meant the paper cited numbers no regeneration
    command produced -- the exact hole PREPRINT-CHECKLIST section A was amended to close the
    same day, after WT-027's hand-transcribed table was found not to regenerate. Note the
    horizon: the collapse runs 300 periods (matching the test it came from), where the sweep
    above runs 400. The paper states both.
    """
    from wealth_tensor.lambda_sensitivity import DimensionedSystem, diagnostics, collapses_onto

    PHI = 0.3
    a = DimensionedSystem(energy_scale=1.0, coupling=1e-6, observable_share=PHI).run(300)
    b = DimensionedSystem(energy_scale=6.02e23, coupling=42.0, observable_share=PHI).run(300)

    print()
    print("SCALING COLLAPSE (phi=%.1f, 300 periods -- note: the sweep above runs 400)" % PHI)
    print("  system A: energy scale 1.0        coupling 1e-06")
    print("  system B: energy scale 6.02e+23   coupling 4.2e+01")
    da, db = diagnostics(a), diagnostics(b)
    print("  %-28s %18s %18s %12s" % ("dimensionless diagnostic", "A", "B", "difference"))
    for k in sorted(set(da) & set(db)):
        va, vb = da[k], db[k]
        try:
            print("  %-28s %18.10g %18.10g %12.3g" % (k, va, vb, abs(va - vb)))
        except TypeError:
            print("  %-28s %18s %18s %12s" % (k, va, vb, "n/a"))
    print("  collapses_onto(A, B): %s" % collapses_onto(a, b))


scaling_collapse()
