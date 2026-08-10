"""Regenerate every number Paper I publishes, from the committed modules.

Paper I -- "Price formation without independent curves" -- rests on two modules that
ADR-001 allocates to it as one paper: excess_demand.py and cournot.py. This script is the
single regeneration command required by docs/papers/PREPRINT-CHECKLIST.md §A, and it
exists because Paper I's headline figures were hand-transcribed into the ledger on
2026-08-04 and pinned by no test since. WT-027 is the precedent: hand-transcribed numbers
from an exploratory run did not regenerate from the committed module.

Ledger entries covered: WT-001, WT-005, WT-018, WT-019, WT-020, WT-021.

Run:  ./.venv/bin/python scripts/wt018_report.py
"""

import sys
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "src"))

import numpy as np

from wealth_tensor.excess_demand import Market
from wealth_tensor import cournot as cn

# --- Configuration, identical to tests/test_excess_demand.py so the paper, the tests and
# --- this script all describe one experiment rather than three similar ones.
RNG_POP = np.random.default_rng(7)
M = RNG_POP.lognormal(3.0, 0.6, 400)
S = 150
K = 25
LAMBDAS = [1.0, 1.05, 1.15, 1.3, 1.6, 2.0]
ENDOWMENT_SEED = 1

A, B = 100.0, 1.0
CORNER_COSTS = [8.0, 9.0, 10.0, 11.0, 30.0]


def rule(title):
    print()
    print("=" * 78)
    print(title)
    print("=" * 78)


def allocations(k=K):
    return [Market(M, S, rng=np.random.default_rng(i)) for i in range(k)]


# ---------------------------------------------------------------- §A  the population
rule("A · POPULATION  (WT-018)")
print(f"  agents N                    {M.size}")
print(f"  reservation prices          lognormal(mu=3.0, sigma=0.6), numpy default_rng(7)")
print(f"  stock S                     {S}")
print(f"  allocations drawn           {K}, numpy default_rng(0..{K - 1})")
print(f"  min / median / max m        {M.min():.4f} / {np.median(M):.4f} / {M.max():.4f}")

mks = allocations()

# ------------------------------------------------- §B  the invariance, and its complement
rule("B · THE CURVES ARE NOT INDEPENDENT  (WT-018)")

pairs = {tuple(np.round(mk.marginal_pair(), 12)) for mk in mks}

# An interior grid that avoids the data points. Grid endpoints that coincide with an m_i
# make the strict inequalities in demand_at/supply_at disagree about a single agent, which
# is a tie convention rather than an economic effect; it would otherwise show up as extra
# distinct schedules and be mistaken for one.
GRID = np.linspace(M.min(), M.max(), 401)[1:-1]
GRID = np.array([p for p in GRID if np.min(np.abs(M - p)) > 1e-9])

demand_curves = {tuple(mk.demand_at(float(p)) for p in GRID) for mk in mks}
supply_curves = {tuple(mk.supply_at(float(p)) for p in GRID) for mk in mks}
excess_curves = {tuple(mk.excess_demand(float(p)) for p in GRID) for mk in mks}
identity = tuple(int(np.sum(M > p)) - S for p in GRID)

lo, hi = mks[0].marginal_pair()
print(f"  interior grid points, ties excluded               {len(GRID)}")
print(f"  distinct clearing intervals over {K} allocations   {len(pairs)}")
print(f"  distinct DEMAND schedules                        {len(demand_curves)}")
print(f"  distinct SUPPLY schedules                         {len(supply_curves)}")
print(f"  distinct EXCESS-DEMAND schedules                   {len(excess_curves)}")
print(f"  excess demand == count(m_i > p) - S, identically  "
      f"{all(c == identity for c in excess_curves)}")
print()
print("  The allocation cancels from the DIFFERENCE of the two schedules, at every")
print("  price, not merely at the crossing. D and S are two decompositions of a single")
print("  function of c(m) and S, and the decomposition carries no economic content.")
print()
print(f"  the one clearing interval  (marginal pair)        [{lo:.6f}, {hi:.6f}]")
print(f"    lo = (S+1)-th highest reservation price         {np.sort(M)[::-1][S]:.6f}")
print(f"    hi =  S-th    highest reservation price         {np.sort(M)[::-1][S - 1]:.6f}")
print(f"  interval width                                    {hi - lo:.6f}")
print(f"  midpoint (the reported clearing price)            {(lo + hi) / 2:.6f}")

# --------------------------------------------------------- §C  excess demand steps +1/0/-1
rule("C · EXCESS DEMAND STEPS +1 -> 0 -> -1 ACROSS THE PAIR  (WT-018)")
steps = {(mk.excess_demand(lo - 1e-9), mk.excess_demand((lo + hi) / 2), mk.excess_demand(hi + 1e-9))
         for mk in mks}
print(f"  distinct (z(lo-), z(mid), z(hi+)) triples over {K} allocations   {len(steps)}")
print(f"  the triple                                                      {sorted(steps)[0]}")

# ------------------------------------------------------ §D  reduction to Marshallian cross
rule("D · REDUCTION TO THE MARSHALLIAN CROSS  (WT-019)")
crosses = np.array([mk.marshallian_cross() for mk in mks])
inside = [(lo <= c <= hi + 1e-9) for c in crosses]
print(f"  allocations tested                              {K}")
print(f"  crosses landing inside the clearing interval    {sum(inside)} / {K}")
print(f"  cross min / max across allocations              {crosses.min():.6f} / {crosses.max():.6f}")
print(f"  distinct cross values                           {len(set(np.round(crosses, 12)))}")
print(f"  interval                                        [{lo:.6f}, {hi:.6f}]")

# ----------------------------------------------------------- §E  the anti-SMD monotonicity
rule("E · EXCESS DEMAND IS MONOTONE HERE -- THIS IS NOT AN SMD RESULT  (WT-020)")
mk3 = Market(M, S, rng=np.random.default_rng(3))
zs = [mk3.excess_demand(float(p)) for p in np.linspace(M.min(), M.max(), 500)]
violations = sum(1 for a, b in zip(zs, zs[1:]) if a < b)
print(f"  grid points                                     500")
print(f"  monotonicity violations                         {violations}")
print(f"  z at grid min / max                             {zs[0]} / {zs[-1]}")
print(f"  sign changes                                    {sum(1 for a, b in zip(zs, zs[1:]) if (a > 0) != (b > 0))}")
print("  NOTE: single-crossing and monotone. SMD arbitrary-shape needs >=2 goods and")
print("        income effects. This module does NOT demonstrate SMD pathology.")

# ------------------------------------------------------------- §F  the endowment effect
rule("F · ENDOWMENT EFFECT: VOLUME FALLS AS A CONSEQUENCE, NOT A FIT  (WT-021)")
mk_e = Market(M, S, rng=np.random.default_rng(ENDOWMENT_SEED))
vols = [mk_e.with_endowment_effect(l).volume() for l in LAMBDAS]
print(f"  allocation seed                                 default_rng({ENDOWMENT_SEED})")
print(f"  {'lambda':>8s}  {'volume':>7s}  {'change':>7s}")
prev = None
for l, v in zip(LAMBDAS, vols):
    d = "" if prev is None else f"{v - prev:+d}"
    print(f"  {l:8.2f}  {v:7d}  {d:>7s}")
    prev = v
print()
print(f"  volume series                                   {' -> '.join(str(v) for v in vols)}")
print(f"  monotone non-increasing                         {all(a >= b for a, b in zip(vols, vols[1:]))}")
print(f"  total decline                                   {vols[0]} -> {vols[-1]}  "
      f"({100 * (vols[0] - vols[-1]) / vols[0]:.1f}% of baseline)")

# ------------------------------------------------------------- §G  Cournot: the corner
rule("G · THE CORNER SOLUTION IS THE MARGINAL PAIR  (WT-001)")
r = cn.solve_cournot(A, B, CORNER_COSTS)
print(f"  inverse demand                                  p = {A:.0f} - {B:.0f}Q")
print(f"  marginal costs                                  {CORNER_COSTS}")
print(f"  excluded firms (0-indexed)                      {r['excluded']}")
print(f"  {'firm':>5s}  {'MC':>6s}  {'q':>8s}  {'profit':>10s}  {'share':>7s}")
for i, c in enumerate(CORNER_COSTS):
    print(f"  {i:5d}  {c:6.1f}  {r['q'][i]:8.3f}  {r['profit'][i]:10.3f}  {r['share'][i]:7.4f}")
print()
print(f"  aggregate Q                                     {r['Q']:.4f}")
print(f"  price p                                         {r['p']:.4f}")
print(f"  excluded firm's MC                              {CORNER_COSTS[-1]:.1f}")
print(f"  p < MC of excluded firm (self-consistent)       {r['p'] < CORNER_COSTS[-1]}")
print(f"  HHI                                             {r['hhi']:.4f}")
try:
    cn.closed_form(A, B, CORNER_COSTS)
    print("  closed_form accepted the corner case            UNEXPECTED")
except ValueError as e:
    print(f"  closed_form refuses it                          ValueError: "
          f"{str(e).splitlines()[0][:52]}...")

# --------------------------------------------------- §H  Cournot: tatonnement instability
rule("H · TATONNEMENT INSTABILITY, GAIN (n-1)/2  (WT-005)")
print(f"  {'n':>3s}  {'undamped gain (n-1)/2':>22s}  {'undamped, 5000 iters':>22s}")
for n in [2, 3, 4, 6, 10, 20]:
    c = np.full(n, 10.0)
    try:
        out = cn.tatonnement(A, B, c, damping=1.0, max_iter=5000)
        undamped = f"converged in {out['iterations']}"
    except RuntimeError:
        undamped = "did NOT converge"
    print(f"  {n:3d}  {(n - 1) / 2:22.1f}  {undamped:>22s}")
print()
print("  The gain crosses 1 between n=2 and n=3, which is exactly where undamped")
print("  simultaneous adjustment stops converging. Output is floored at zero, so the")
print("  failure is bounded oscillation rather than divergence.")

rule("H2 · THE DAMPING THAT RESCUES IT SHRINKS LIKE 4/n  (WT-005, extended)")
print("  Damped map q <- q + d(BR(q) - q) has linearised gain |1 - d(n+1)/2|,")
print("  so it is stable iff  d < 4/(n+1).  Measured on a 0.02 grid:")
print(f"  {'n':>4s}  {'4/(n+1)':>9s}  {'largest d converging':>21s}  "
      f"{'smallest d failing':>19s}  {'bracket':>8s}")
STEP = 0.02
for n in [2, 3, 4, 6, 10, 20]:
    c = np.full(n, 10.0)
    ok, bad = [], []
    for d in np.round(np.arange(STEP, 1.41, STEP), 3):
        try:
            cn.tatonnement(A, B, c, damping=float(d), max_iter=20000)
            ok.append(float(d))
        except RuntimeError:
            bad.append(float(d))
    thr = 4.0 / (n + 1)
    lo_d, hi_d = max(ok), (min(bad) if bad else float("nan"))
    print(f"  {n:4d}  {thr:9.4f}  {lo_d:21.2f}  {hi_d:19.2f}  "
          f"{'yes' if lo_d <= thr <= hi_d else 'NO':>8s}")
print()
print("  The threshold is not a constant. The inertia required to rescue Cournot's own")
print("  adjustment process VANISHES like 4/n, so each firm must slow down in proportion")
print("  to the number of rivals it has. Rescuing the dynamic therefore requires every")
print("  firm to know n and to condition its own sluggishness on it -- which is more")
print("  information than the static expectation the dynamic is built on grants them.")
print("  The repair needs precisely what the model denies.")

# ------------------------------------------------------------ §I  Cournot: the identities
rule("I · IDENTITIES AND LIMITS, CHECKED NOT ASSUMED  (WT-001)")
print("  Lerner identity  (p - MC_i)/p == s_i/|eps|   -- max abs residual")
for c in ([10.0, 10.0], [5.0, 12.0, 20.0], [1.0, 2.0, 3.0, 4.0]):
    res = cn.lerner_residual(cn.closed_form(A, B, c))
    print(f"    c={str(c):24s}  {np.abs(res).max():.3e}")
print()
print("  Cournot limit theorem  p -> MC  (symmetric, MC = 10)")
for n in [2, 10, 100, 1000]:
    p = cn.closed_form(A, B, np.full(n, 10.0))["p"]
    print(f"    n={n:5d}   p = {p:8.4f}   p - MC = {p - 10.0:8.4f}")
print()
print("  HHI == 1/n exactly (symmetric)")
for n in [1, 2, 4, 8]:
    print(f"    n={n:2d}   HHI = {cn.closed_form(A, B, np.full(n, 10.0))['hhi']:.6f}   "
          f"1/n = {1.0 / n:.6f}")

rule("END")
print("  Every figure above is produced by the committed modules under the seeds named")
print("  in §A. Nothing here is transcribed.")
print()
