#!/usr/bin/env python3
"""WT-070 - Paper I at the P3 level: what the fold sees, and what only the allocation sees.

RETROFITTED 2026-08-11 to the severity discipline (see scripts/severity.py). Every check
below now ships a WITNESS: a world in which the check goes red, executed at check time.
A guard whose witness also passes is a PHANTOM TAG and kills the run.

This script is the worked example for that discipline. It is also the script that shipped
the defect: R3's "population-defined perturbation gives exactly 1" passed because the
perturbation was rank-preserving, not because the allocation was irrelevant. Under the
witness rule it would have died on the first run.

    ./.venv/bin/python scripts/wt070_p3_fold.py
"""

from __future__ import annotations

import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))
sys.path.insert(0, str(Path(__file__).resolve().parent))

from wealth_tensor.excess_demand import Market      # noqa: E402
from severity import check, DEFINITIONAL, summary   # noqa: E402

N, STOCK, N_ALLOC = 400, 150, 25
LAMBDA_SWEEP = (1.00, 1.05, 1.15, 1.30, 1.60, 2.00)
RESERVATION_PRICES = np.random.default_rng(7).lognormal(3.0, 0.6, N)


def allocations(m, stock, k=N_ALLOC):
    out = []
    for seed in range(k):
        rng = np.random.default_rng(seed)
        h = np.zeros(m.size, dtype=bool)
        h[rng.choice(m.size, size=stock, replace=False)] = True
        out.append(h)
    return out


def interior_grid(m, n_points=401, eps=1e-9):
    grid = np.linspace(float(m.min()), float(m.max()), n_points)[1:-1]
    keep = np.array([np.min(np.abs(m - p)) > eps for p in grid])
    return grid[keep], int((~keep).sum())


def schedule(fn, grid):
    return tuple(fn(float(p)) for p in grid)


def top_set(m, stock):
    t = np.zeros(m.size, dtype=bool)
    t[np.argsort(m)[::-1][:stock]] = True
    return t


def hr(t):
    print("\n" + "=" * 78 + f"\n{t}\n" + "=" * 78)


# ===========================================================================
# R1 - the fold identity
# ===========================================================================

def r1(m, stock, allocs, grid):
    hr("R1 - THE FOLD IDENTITY   z(p) = #{i : m_i > p} - S")

    demands, supplies, excesses = set(), set(), set()
    for h in allocs:
        mk = Market(m, stock, holders=h)
        demands.add(schedule(mk.demand_at, grid))
        supplies.add(schedule(mk.supply_at, grid))
        excesses.add(schedule(mk.excess_demand, grid))
    closed_form = tuple(int(np.sum(m > p)) - stock for p in grid)

    print(f"  distinct D {len(demands)}   distinct S {len(supplies)}   "
          f"distinct z {len(excesses)}   grid {len(grid)}\n")

    # WITNESS for the two "25" claims: a world where the 25 allocations are the SAME
    # allocation. If the count is still 25 there, the counter is not reading the
    # allocation at all.
    same = allocs[0]
    def w_same(fn):
        return lambda: len({schedule(getattr(Market(m, stock, holders=same), fn), grid)
                            for _ in range(N_ALLOC)}) == N_ALLOC

    check("25 distinct demand schedules", len(demands) == N_ALLOC,
          witness=w_same("demand_at"))
    check("25 distinct supply schedules", len(supplies) == N_ALLOC,
          witness=w_same("supply_at"))

    # WITNESS for invariance: a world with a transaction wedge, where the allocation is
    # KNOWN not to cancel. If z is still single-valued there, the check is blind.
    def z_wedge(h, p, t=1.0):
        return int(np.sum(~h & (m > p))) - int(np.sum(h & (m < p - t)))

    def w_wedge():
        return len({tuple(z_wedge(h, float(p)) for p in grid) for h in allocs}) == 1

    check("exactly 1 distinct excess-demand schedule", len(excesses) == 1,
          witness=w_wedge)
    check("z equals the closed form at every grid point", excesses == {closed_form},
          witness=lambda: {tuple(z_wedge(h, float(p)) for p in grid)
                           for h in allocs} == {closed_form})

    # The code mutant (WT-069) is itself the witness's mirror: it must break the identity.
    mutant = {tuple(int(np.sum(~h & (m > p))) - int(np.sum(h & (m > p))) for p in grid)
              for h in allocs}
    check("MUTANT (supply reads m>p): the identity dies as it must",
          len(mutant) == N_ALLOC,
          witness=lambda: len(excesses) == N_ALLOC)
    return closed_form


# ===========================================================================
# R2 - the volume theorem
# ===========================================================================

def r2(m, stock, allocs):
    hr("R2 - THE VOLUME THEOREM   V(H) = |H \\ T|,  T = the top-S valuers")

    T = top_set(m, stock)
    measured = [Market(m, stock, holders=h).volume() for h in allocs]
    predicted = [int(np.sum(h & ~T)) for h in allocs]

    T_bad = np.zeros(m.size, dtype=bool)
    T_bad[np.argsort(m)[:stock]] = True

    check("V(H) = |H \\ T| for all 25 allocations", measured == predicted,
          witness=lambda: measured == [int(np.sum(h & ~T_bad)) for h in allocs])

    h_eff = T.copy()
    bottom = np.zeros(m.size, dtype=bool)
    bottom[np.argsort(m)[:stock]] = True

    v_min = Market(m, stock, holders=h_eff).volume()
    v_max = Market(m, stock, holders=bottom).volume()
    hyper = stock * (m.size - stock) / m.size

    print(f"  sampled  min {min(measured)}  mean {np.mean(measured):.2f}  "
          f"max {max(measured)}")
    print(f"  hypergeometric mean S(N-S)/N   {hyper:.2f}")
    print(f"  V at H = T  {v_min}      V at H = bottom-S  {v_max}"
          f"      max possible {min(stock, m.size - stock)}\n")

    check("V = 0 when holders are already the top-S valuers", v_min == 0,
          witness=lambda: Market(m, stock, holders=bottom).volume() == 0)
    check("V is maximal when holders are the bottom-S valuers",
          v_max == min(stock, m.size - stock),
          witness=lambda: Market(m, stock, holders=h_eff).volume()
          == min(stock, m.size - stock))

    # THE CHECK THAT SHOULD HAVE EXISTED FROM THE START. The sampled mean sitting near
    # the hypergeometric mean is not evidence that anything was measured - it is what
    # uniform resampling MUST produce. The witness is a world of structured couplings,
    # where the mean is nowhere near it. If the structured world ALSO lands on the
    # hypergeometric mean, this quantity is not reading the coupling at all.
    structured = [Market(m, stock, holders=h).volume() for h in (h_eff, bottom)]
    check("the sampled mean sits within 5 of the hypergeometric mean - "
          "i.e. UNIFORM SAMPLING MEASURED NOTHING",
          abs(np.mean(measured) - hyper) < 5.0,
          witness=lambda: abs(np.mean(structured) - hyper) < 5.0)

    check("clearing interval identical at both volume extremes",
          Market(m, stock, holders=h_eff).marginal_pair()
          == Market(m, stock, holders=bottom).marginal_pair(),
          witness=lambda: Market(m * 1.2, stock, holders=h_eff).marginal_pair()
          == Market(m, stock, holders=bottom).marginal_pair())
    return measured


# ===========================================================================
# R3 - the comparative static. THE SECTION THAT SHIPPED THE DEFECT.
# ===========================================================================

def r3(m, stock, allocs, grid):
    hr("R3 - THE COMPARATIVE STATIC   (and the phantom tag that lived here)")

    base = Market(m, stock, holders=allocs[0])
    h0 = allocs[0]
    m_up = m.copy(); m_up[~h0] *= 1.20
    pert = Market(m_up, stock, holders=h0)

    check("F1 CONCEDED: supply unchanged at every grid point",
          schedule(base.supply_at, grid) == schedule(pert.supply_at, grid),
          witness=lambda: schedule(base.supply_at, grid)
          == schedule(Market(m * 1.20, stock, holders=h0).supply_at, grid))
    check("F1 CONCEDED: demand moved",
          schedule(base.demand_at, grid) != schedule(pert.demand_at, grid),
          witness=lambda: schedule(base.demand_at, grid)
          != schedule(Market(m, stock, holders=h0).demand_at, grid))

    check("the new interval is recovered from the perturbed POPULATION alone",
          (float(np.sort(m_up)[::-1][stock]), float(np.sort(m_up)[::-1][stock - 1]))
          == pert.marginal_pair(),
          witness=lambda: (float(np.sort(m)[::-1][stock]),
                           float(np.sort(m)[::-1][stock - 1])) == pert.marginal_pair())

    indexed = {Market(_h_up(m, h), stock, holders=h).marginal_pair() for h in allocs}
    everyone = {Market(m * 1.20, stock, holders=h).marginal_pair() for h in allocs}

    # A random subset of the SAME SIZE, which never mentions the allocation. This is the
    # witness that kills the original claim - and it is also the control the session
    # should have run in the first place.
    n_out = m.size - stock
    def random_subset_fans_out():
        got = set()
        for i, _ in enumerate(allocs):
            rng = np.random.default_rng(1000 + i)
            pick = np.zeros(m.size, dtype=bool)
            pick[rng.choice(m.size, size=n_out, replace=False)] = True
            b = m.copy(); b[pick] *= 1.20
            got.add((float(np.sort(b)[::-1][stock]), float(np.sort(b)[::-1][stock - 1])))
        return len(got) == 1          # if this is TRUE the original claim was real

    print(f"  'raise NON-HOLDERS 20%'  distinct intervals  {len(indexed)}")
    print(f"  'raise EVERYONE 20%'     distinct intervals  {len(everyone)}\n")

    check("the allocation-indexed perturbation fans out", len(indexed) > 1,
          witness=lambda: len(everyone) > 1)

    # THE PHANTOM TAG, PRESERVED AND NOW LABELLED. The original wrote:
    #     check("the population-defined perturbation gives exactly 1", len(everyone)==1)
    # It passed. It could not have failed: multiplying every valuation by a constant is
    # RANK-PRESERVING, so the marginal pair is forced to be a single scaled interval by
    # monotonicity, whatever the allocation does. The witness below is a genuinely
    # population-defined perturbation that is NOT rank-preserving - a random subset,
    # never naming H - and it fans out too. So the 23-vs-1 contrast was
    # rank-scrambling versus rank-preserving, and NOT allocation versus population.
    check("HISTORICAL PHANTOM TAG: 'the population-defined perturbation gives "
          "exactly 1' - passed, and could not have failed",
          len(everyone) == 1,
          witness=random_subset_fans_out)

    return len(indexed), len(everyone)


def _h_up(m, h):
    out = m.copy(); out[~h] *= 1.20
    return out


# ===========================================================================
# R4 - the endowment transform, reported with its defect visible
# ===========================================================================

def r4(m, stock, allocs, grid):
    hr("R4 - THE ENDOWMENT TRANSFORM   reported WITH the defect REVIEW-002 found")

    print("  lambda   volume: min   mean    max     distinct z")
    rows = []
    for lam in LAMBDA_SWEEP:
        vols, zs = [], set()
        for h in allocs:
            mh = Market(m, stock, holders=h).with_endowment_effect(lam)
            vols.append(mh.volume())
            zs.add(schedule(mh.excess_demand, grid))
        rows.append((lam, min(vols), float(np.mean(vols)), max(vols), len(zs)))
        print(f"  {lam:5.2f}        {min(vols):4d}  {np.mean(vols):6.2f}   "
              f"{max(vols):4d}     {len(zs):3d}")
    print()

    check("at lambda = 1 the invariance holds", rows[0][4] == 1,
          witness=lambda: rows[-1][4] == 1)
    check("at every lambda > 1 the invariance BREAKS, as F2 established",
          all(r[4] == N_ALLOC for r in rows[1:]),
          witness=lambda: rows[0][4] == N_ALLOC)
    check("at lambda = 1 volume nonetheless varies across allocations",
          rows[0][3] - rows[0][1] > 0,
          witness=DEFINITIONAL(
              "the falsifying world is a population whose top-S and bottom-(N-S) "
              "valuations are not distinct, which the continuous lognormal draw "
              "excludes with probability one; no admissible world here falsifies it"))
    check("mean volume falls monotonically over the sweep",
          all(rows[i][2] >= rows[i + 1][2] for i in range(len(rows) - 1)),
          witness=lambda: all(rows[i][2] <= rows[i + 1][2]
                              for i in range(len(rows) - 1)))
    return rows


def main():
    m, stock = RESERVATION_PRICES, STOCK
    allocs = allocations(m, stock)
    grid, dropped = interior_grid(m)
    print(__doc__.split("\n")[0])
    print(f"\n  N = {m.size}   S = {stock}   allocations = {len(allocs)}   "
          f"grid = {len(grid)}   eps-filtered = {dropped}")
    r1(m, stock, allocs, grid)
    r2(m, stock, allocs)
    r3(m, stock, allocs, grid)
    r4(m, stock, allocs, grid)
    summary("WT-070 SEVERITY")


if __name__ == "__main__":
    main()
