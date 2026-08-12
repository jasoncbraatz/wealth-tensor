"""WT-084: the identification result, proved rather than checked -- and its two edges.

WHY THIS SCRIPT EXISTS
----------------------
`wt082` established the observational equivalence NUMERICALLY: it swapped the roots,
regenerated the series, and found agreement to 7e-14. That is a check, and a good one.
It is not a proof, and the paper's own Section 4 preamble promises "a one-line proof"
that the paper then never gives. An identification theorem whose only warrant is a
floating-point comparison is a theorem a referee will ask to see.

It is also, it turns out, not the whole result. Two independent readings of the algebra
disagreed about what the exchange preserves -- one said phi*delta, one said (1-phi)*delta --
and a disagreement about a conserved quantity is exactly the thing WT-080 exists to settle
before prose is written. Both readings are derivable; they differ in WHICH SERIES they hold
fixed, and only one of those series is reported by anybody.

WHAT IS ESTABLISHED HERE
------------------------
E1  THE CLOSED FORM. With C(0) = E(0) = E0, the recursion pair has the solution

        C(t) = E0 * [ delta*(1-phi)*A^t - (alpha - phi*delta)*D^t ] / (delta - alpha)

    where A = 1-alpha and D = 1-delta. Verified against the recursion itself.

E2  THE PROOF, NOT THE CHECK. Exchanging the roots and matching the coefficients of A^t
    and D^t gives TWO equations, and both reduce to the SAME condition, phi' * alpha =
    phi * delta. That coincidence IS the theorem: the exchange is exact because the
    system is overdetermined and consistent. Four lines, no floating point.

E3  THE DISAGREEMENT, SETTLED. The gap series G = C - E is NOT preserved by the exchange;
    the REPORTED series C is. The rival map phi' = 1 - (1-phi)*delta/alpha preserves G
    and fails on C. It fails because the exchange also swaps which root belongs to the
    physical layer, so E itself is a different series in the mirror world. E is not
    reported by anyone, which is why the distinction decides the result rather than
    decorating it.

E4  WHAT THE MIRROR WORLDS DISAGREE ABOUT. The two worlds agree about the books to 1e-14
    and disagree about the asset by a factor that grows without bound. The books are
    identical; the firm is not.

E5  THE GAP FACTORISES. G(t) = E0 * (1-phi) * delta * S(t), where the shape function
    S(t) = (A^t - D^t)/(delta - alpha) is symmetric under exchanging the roots. All of
    phi's influence on the gap is one scalar amplitude; the shape knows the roots only as
    an unordered pair.

E6  THE FIRST EDGE -- AN OPEN INITIAL GAP DOES NOT RESCUE IDENTIFICATION. If the series
    is observed from a state with the gap already open by g0 (in units of E0), the mirror
    survives with the SAME g0 and a shifted map, phi' = [phi*delta + g0*(alpha-delta)]/alpha,
    and the invariant generalises to (phi - g0)*delta = (phi' - g0)*alpha. The obvious
    referee escape -- "real firms are not observed from acquisition" -- makes it worse,
    not better, which E7 shows.

E7  THE SECOND EDGE, AND IT IS THE LARGER RESULT. The reported series has two roots and
    two amplitudes: four numbers. The model has five parameters (alpha, delta, phi, E0,
    g0). When the analyst does not observe the asset's physical scale E0 -- which is every
    firm-level series, because firm-level book value aggregates vintages -- the identified
    set is not two points but a ONE-PARAMETER FAMILY, and phi ranges over the WHOLE of
    [0, 1] within it. Not ill-conditioned, not two-valued: empty.

E8  THE DEFERRAL RATIO IS NOT IDENTIFIED EITHER, AND NOT MERELY RESCALED. R =
    (1-phi)*delta/(alpha-delta) is recovered as the t->infinity limit of G/E, so it is a
    model quantity and not an observable -- it is built from E. Under the mirror it does
    not shrink or stretch: it CHANGES SIGN. A paper claiming R is "what a reader can
    compute from filings" is claiming a quantity built from the one series nobody reports.

Each check ships a witness (scripts/severity.py). Where a claim is an exact identity, the
witness is the same identity with one parameter perturbed by an amount chosen to be far
larger than the tolerance -- so a check that would pass under a broken closed form is
caught.

    ./.venv/bin/python scripts/wt084_identification_closed_form.py
"""

from __future__ import annotations

import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
from severity import check, summary  # noqa: E402


def hr(title: str) -> None:
    print("\n" + "=" * 78)
    print(f"  {title}")
    print("=" * 78)


# --------------------------------------------------------------------------- model
def reported_series(alpha, delta, phi, periods, E0=1.0, g0=0.0):
    """The recursion itself. C(0) = E0*(1+g0); E(t) = E0*(1-delta)^t."""
    C = np.empty(periods + 1)
    E = E0 * (1.0 - delta) ** np.arange(periods + 1)
    C[0] = E0 * (1.0 + g0)
    for t in range(periods):
        C[t + 1] = C[t] * (1.0 - alpha) + E[t] * (alpha - phi * delta)
    return C, E


def closed_form(alpha, delta, phi, periods, E0=1.0, g0=0.0):
    """C(t) = k_A * A^t + k_D * D^t, with the amplitudes written out."""
    A, D = 1.0 - alpha, 1.0 - delta
    t = np.arange(periods + 1)
    x = (1.0 - phi) * delta / (delta - alpha)
    k_A = E0 * (g0 + x)
    k_D = E0 * (1.0 - x)
    return k_A * A**t + k_D * D**t


PERIODS = 400
ALPHA, DELTA, PHI = 0.050, 0.020, 0.60          # alpha > delta, the paper's regime
E0 = 1.0

hr("E1 - the closed form solves the recursion")

C_rec, E_phys = reported_series(ALPHA, DELTA, PHI, PERIODS)
C_cf = closed_form(ALPHA, DELTA, PHI, PERIODS)
err_cf = float(np.max(np.abs(C_rec - C_cf)))
print(f"  alpha={ALPHA}  delta={DELTA}  phi={PHI}  periods={PERIODS}")
print(f"  max |recursion - closed form| = {err_cf:.3e}")
check("the closed form reproduces the recursion",
      err_cf < 1e-13,
      witness=lambda: float(np.max(np.abs(C_rec - closed_form(ALPHA, DELTA, PHI + 0.05, PERIODS)))) < 1e-13)
print("  Witness perturbs phi by 0.05 in the closed form only. If the check survives that,")
print("  it is not touching phi and the agreement means nothing.")


hr("E2 - the proof: two coefficient equations, one condition")

# Coefficients of A^t and D^t in C(t)/E0, for params (alpha, delta, phi):
#     A^t :  delta*(1-phi) / (delta-alpha)
#     D^t : -(alpha - phi*delta) / (delta-alpha)
# For the mirror (delta, alpha, phi') the roles of A and D swap, giving
#     A^t :  (delta - phi'*alpha) / (delta-alpha)
#     D^t : -alpha*(1-phi')      / (delta-alpha)
# Matching each pair gives an equation for phi'.  They must agree, or there is no theorem.
PHI_MIRROR = PHI * DELTA / ALPHA

lhs_A, rhs_A = DELTA * (1 - PHI), DELTA - PHI_MIRROR * ALPHA          # from the A^t coefficient
lhs_D, rhs_D = ALPHA - PHI * DELTA, ALPHA * (1 - PHI_MIRROR)          # from the D^t coefficient
res_A, res_D = abs(lhs_A - rhs_A), abs(lhs_D - rhs_D)
print(f"  phi' = phi*delta/alpha = {PHI_MIRROR:.10f}")
print(f"  A^t coefficient equation residual : {res_A:.3e}")
print(f"  D^t coefficient equation residual : {res_D:.3e}")
print("  Two equations, one unknown, and they are consistent. That is the theorem;")
print("  everything below is a demonstration that the algebra was done correctly.")
check("both coefficient equations are solved by the same phi'",
      res_A < 1e-15 and res_D < 1e-15,
      witness=lambda: (abs(DELTA * (1 - PHI) - (DELTA - (PHI_MIRROR * 1.02) * ALPHA)) < 1e-15
                       and abs(ALPHA - PHI * DELTA - ALPHA * (1 - PHI_MIRROR * 1.02)) < 1e-15))


hr("E3 - the exchange preserves the REPORTED series, not the gap")

C_mirror, E_mirror = reported_series(DELTA, ALPHA, PHI_MIRROR, PERIODS)
err_mirror = float(np.max(np.abs(C_rec - C_mirror)))
err_mirror_norm = err_mirror / float(np.max(np.abs(C_rec)))
print(f"  mirror = (alpha,delta,phi) = ({DELTA}, {ALPHA}, {PHI_MIRROR:.6f})")
print(f"  max |C - C_mirror|            = {err_mirror:.3e}   (normalised {err_mirror_norm:.3e})")

# The rival map, which preserves the GAP amplitude (1-phi)*delta instead of phi*delta.
PHI_RIVAL = 1.0 - (1.0 - PHI) * DELTA / ALPHA
C_rival, _ = reported_series(DELTA, ALPHA, PHI_RIVAL, PERIODS)
err_rival = float(np.max(np.abs(C_rec - C_rival)))
print(f"  rival map phi' = 1-(1-phi)delta/alpha = {PHI_RIVAL:.6f}")
print(f"  max |C - C_rival|             = {err_rival:.3e}   <-- fails by {err_rival/max(err_mirror,1e-300):.1e}x")
check("phi*delta is the conserved quantity for the reported series, and (1-phi)*delta is not",
      err_mirror < 1e-13 and err_rival > 1e-4,
      witness=lambda: err_mirror < 1e-13 and abs(PHI_RIVAL - PHI_MIRROR) < 1e-12)
print("  Witness asserts the two maps coincide. They coincide only at alpha == delta,")
print("  where there is no exchange to perform, so a check that survives it is vacuous.")


hr("E4 - the two worlds agree about the books and disagree about the firm")

ratio = E_mirror / E_phys
print(f"  |C - C_mirror| / max|C|                   = {err_mirror_norm:.3e}")
print(f"  E_mirror / E at t = 100                   = {ratio[100]:.3e}")
print(f"  E_mirror / E at t = 400                   = {ratio[400]:.3e}")
print("  The mirror is a slow reporter of a fast-decaying asset. Its books stay above an")
print("  asset that has all but vanished -- which is a recognisable kind of firm, not a")
print("  mathematical curiosity, and it files the same statements.")
check("the physical series differ by orders of magnitude while the reported series agree",
      ratio[400] < 1e-3 and err_mirror_norm < 1e-13,
      witness=lambda: bool(np.allclose(E_mirror, E_phys, rtol=1e-6)))


hr("E5 - the gap factorises: one scalar carries phi, and the shape is symmetric")

A, D = 1.0 - ALPHA, 1.0 - DELTA
t = np.arange(PERIODS + 1)
S = (A**t - D**t) / (DELTA - ALPHA)
S_swapped = (D**t - A**t) / (ALPHA - DELTA)
G = C_rec - E_phys
G_factorised = E0 * (1.0 - PHI) * DELTA * S
err_G = float(np.max(np.abs(G - G_factorised)))
err_S = float(np.max(np.abs(S - S_swapped)))
print(f"  max |G - E0*(1-phi)*delta*S(t)|           = {err_G:.3e}")
print(f"  max |S(t) - S(t) with the roots exchanged| = {err_S:.3e}")
check("the gap is a scalar amplitude times a root-symmetric shape",
      err_G < 1e-13 and err_S < 1e-15,
      witness=lambda: float(np.max(np.abs(G - E0 * (1.0 - PHI * 1.1) * DELTA * S))) < 1e-13)
print("  This is a Bateman function (Bateman 1910). The shape knows the two roots only")
print("  through their unordered pair; a parameter attached to a LABELLED root cannot")
print("  survive that. In pharmacokinetics the same structure is called flip-flop.")


hr("E6 - first edge: an open initial gap does not rescue identification")

G0 = 0.15
C_g0, _ = reported_series(ALPHA, DELTA, PHI, PERIODS, E0=E0, g0=G0)
PHI_MIRROR_G0 = (PHI * DELTA + G0 * (ALPHA - DELTA)) / ALPHA
C_g0_mirror, _ = reported_series(DELTA, ALPHA, PHI_MIRROR_G0, PERIODS, E0=E0, g0=G0)
err_g0 = float(np.max(np.abs(C_g0 - C_g0_mirror)))

# and the naive map, which is what a reader of the g0 = 0 theorem would reach for
C_g0_naive, _ = reported_series(DELTA, ALPHA, PHI_MIRROR, PERIODS, E0=E0, g0=G0)
err_g0_naive = float(np.max(np.abs(C_g0 - C_g0_naive)))

inv_1, inv_2 = (PHI - G0) * DELTA, (PHI_MIRROR_G0 - G0) * ALPHA
print(f"  initial gap g0 = {G0}")
print(f"  shifted map phi' = [phi*delta + g0*(alpha-delta)]/alpha = {PHI_MIRROR_G0:.10f}")
print(f"  max |C - C_mirror| with the shifted map   = {err_g0:.3e}")
print(f"  max |C - C_mirror| with the g0=0 map      = {err_g0_naive:.3e}  <-- the naive map fails")
print(f"  invariant (phi-g0)*delta = {inv_1:.12f}   (phi'-g0)*alpha = {inv_2:.12f}")
check("the mirror survives an open initial gap, with a shifted map and a shifted invariant",
      err_g0 < 1e-13 and err_g0_naive > 1e-4 and abs(inv_1 - inv_2) < 1e-15,
      witness=lambda: err_g0 < 1e-13 and err_g0_naive < 1e-13)


hr("E7 - second edge: with the physical scale unobserved, phi is not two-valued. It is free.")

# Observables: the unordered roots {A, D} and the two amplitudes k_A, k_D.  Four numbers.
# Parameters: alpha, delta, phi, E0, g0.  Five.  One dimension is free, and it is phi's.
x_true = (1.0 - PHI) * DELTA / (DELTA - ALPHA)
k_A_obs = E0 * (G0 + x_true)
k_D_obs = E0 * (1.0 - x_true)
print(f"  observed amplitudes: k_A = {k_A_obs:.10f}   k_D = {k_D_obs:.10f}")
print(f"  observed roots     : A  = {A:.6f}   D  = {D:.6f}   (unordered)")
print()

# Solve for the range of assumed E0 that keeps phi inside [0,1], rather than guessing a
# grid: phi(E0) = 1 - (1 - k_D/E0)*(delta-alpha)/delta, so phi = 1 at E0 = k_D and
# phi = 0 at E0 = k_D*(alpha-delta)/alpha.
E0_at_phi1 = k_D_obs
E0_at_phi0 = k_D_obs * (ALPHA - DELTA) / ALPHA
print(f"  phi = 0 at assumed E0 = {E0_at_phi0:.6f};  phi = 1 at assumed E0 = {E0_at_phi1:.6f}")
print(f"  a factor of {E0_at_phi1/E0_at_phi0:.2f} in the UNOBSERVED physical scale spans all of phi")
print()
print(f"  {'E0 assumed':>12}{'implied phi':>14}{'implied g0':>13}{'max |C - C_alt|':>19}")

feasible_phi, worst = [], 0.0
for E0_alt in np.linspace(E0_at_phi0, E0_at_phi1, 9):
    x_alt = 1.0 - k_D_obs / E0_alt
    phi_alt = 1.0 - x_alt * (DELTA - ALPHA) / DELTA
    g0_alt = k_A_obs / E0_alt - x_alt
    C_alt, _ = reported_series(ALPHA, DELTA, phi_alt, PERIODS, E0=E0_alt, g0=g0_alt)
    e = float(np.max(np.abs(C_g0 - C_alt)))
    ok = -1e-9 <= phi_alt <= 1.0 + 1e-9
    if ok:
        feasible_phi.append(phi_alt)
        worst = max(worst, e)
    print(f"  {E0_alt:>12.2f}{phi_alt:>14.6f}{g0_alt:>13.6f}{e:>19.3e}"
          f"{'' if ok else '   (phi outside [0,1])'}")

lo, hi = min(feasible_phi), max(feasible_phi)
print()
print(f"  admissible phi over this scan: [{lo:.6f}, {hi:.6f}]  -- every one of them exact")
print(f"  worst reproduction error among them: {worst:.3e}")
print("  Letting E0 range over (0, inf) sweeps phi across the whole unit interval: the")
print("  reported series is consistent with a firm that recognises everything at once and")
print("  with a firm that recognises nothing, and with every firm in between.")
check("a one-parameter family of (E0, phi, g0) reproduces the reported series exactly",
      worst < 1e-12 and (hi - lo) > 0.5,
      witness=lambda: bool(max(abs(p - PHI) for p in feasible_phi) < 1e-9))
print("  Witness asserts every member of the family has the true phi. If that held, the")
print("  family would be a relabelling of one point and there would be nothing to report.")


hr("E8 - the deferral ratio is not identified either, and it changes sign")

R = (1.0 - PHI) * DELTA / (ALPHA - DELTA)
tail = (C_rec - E_phys)[-1] / E_phys[-1]
R_mirror = (1.0 - PHI_MIRROR) * ALPHA / (DELTA - ALPHA)
print(f"  R = (1-phi)*delta/(alpha-delta)           = {R:.10f}")
print(f"  lim_t (C-E)/E from the simulation         = {tail:.10f}")
print(f"  R in the mirror world                     = {R_mirror:.10f}   <-- opposite sign")
check("R is the steady-state gap ratio, and the mirror reverses its sign",
      abs(R - tail) < 2e-4 and R > 0 > R_mirror,
      witness=lambda: abs(R - (1.0 - PHI * 1.2) * DELTA / (ALPHA - DELTA)) < 2e-4)
print("  R is built from E. No filing reports E. R is the model's deferral measure and a")
print("  reader cannot compute it; what a reader can compute is the pair of amplitudes,")
print("  and what those identify is phi*delta.")


hr("SUMMARY")
summary()
