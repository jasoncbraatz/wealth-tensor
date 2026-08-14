"""SCOUTING probe (read-only): 4.2's continuum is presented as a freedom in ONE unobserved
quantity, the physical scale E0.  wt084's own E7 table shows each member also demands a
different OPENING GAP g0.  Price the continuum in g0 -- the quantity an accounting referee
will object to.  ASSERTS against wt084's committed printed table before reporting anything.
"""
from pathlib import Path
ROOT = Path(__file__).resolve().parents[3]   # <repo>/docs/scouting/probes/x.py
import numpy as np
ALPHA, DELTA, PHI, E0 = 0.050, 0.020, 0.60, 1.0
G0 = 0.15                                    # wt084's E6/E7 baseline: the books do NOT open square
x_true = (1.0 - PHI) * DELTA / (DELTA - ALPHA)
k_A, k_D = E0 * (G0 + x_true), E0 * (1.0 - x_true)
E0_phi1, E0_phi0 = k_D, k_D * (ALPHA - DELTA) / ALPHA

def member(e):
    xa = 1.0 - k_D / e
    return 1.0 - xa * (DELTA - ALPHA) / DELTA, k_A / e - xa

# --- gate: reproduce wt084's printed E7 row endpoints exactly, or say nothing ---
p0, g0_lo_end = member(E0_phi0); p1, g0_hi_end = member(E0_phi1)
assert abs(E0_phi0 - 0.76) < 5e-3 and abs(E0_phi1 - 1.2667) < 5e-3
assert abs(g0_lo_end - 0.513158) < 1e-5, g0_lo_end
assert abs(g0_hi_end - (-0.092105)) < 1e-5, g0_hi_end
print(f"GATE OK -- reproduces wt084 E7: E0 {E0_phi0:.4f}..{E0_phi1:.4f} (factor "
      f"{E0_phi1/E0_phi0:.2f}), g0 {g0_lo_end:+.6f} (phi=0) .. {g0_hi_end:+.6f} (phi=1)")
print(f"         and the family is built around a world that ALREADY opens with g0 = {G0:+.2f},"
      f" not the square books 4.2 introduces two paragraphs earlier.\n")

E = np.linspace(E0_phi0, E0_phi1, 400001)
phi = np.array([member(e)[0] for e in E]); g0 = np.array([member(e)[1] for e in E])
print(f"{'opening-gap cap':>18}  {'phi reachable':>22}  {'width':>7}  {'of the unit interval':>21}")
for cap, lab in [(0.02,'|g0| <= 0.02'),(0.05,'|g0| <= 0.05'),(0.10,'|g0| <= 0.10'),
                 (0.15,'|g0| <= 0.15'),(0.25,'|g0| <= 0.25'),(0.52,'|g0| <= 0.52')]:
    m = np.abs(g0) <= cap
    lo, hi = phi[m].min(), phi[m].max()
    print(f"{lab:>18}  [{lo:7.4f}, {hi:7.4f}]{'':>4}  {hi-lo:7.4f}  {hi-lo:20.1%}")
print("\nOne-sided -- a POSITIVE opening gap (books above the asset) is the state impairment")
print("accounting exists to prevent, and it is the end of the family that delivers phi = 0:")
for cap in (0.05, 0.10, 0.15, 0.25):
    m = g0 <= cap
    lo, hi = phi[m].min(), phi[m].max()
    print(f"  g0 <= {cap:+.2f}  ->  phi in [{lo:.4f}, {hi:.4f}], width {hi-lo:.4f}")
