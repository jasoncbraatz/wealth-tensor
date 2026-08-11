#!/usr/bin/env python3
"""WT-070 - Paper I at the P3 level: what the fold sees, and what only the allocation sees.

Regenerates every number in Paper I v0.2 sections 3 and 4. Nothing in the paper is
hand-transcribed; this script is the source (WT-053).

THREE RESULTS, and they are different in kind.

R1  THE FOLD IDENTITY.  z(p) = #{i : m_i > p} - S at every non-reservation price. Restated
    from v0.1, unchanged, because it is the only claim v0.1's referee left standing.

R2  THE VOLUME THEOREM.  Wicksteed (1910, p. 498) asserts that the initial distribution of
    the stock "affects the amount of business done ... but it does not affect the price or
    the ultimate distribution," and never derives it. Here it is derived and measured:

        V(H) = |H \\ T|,  T = the S agents with the highest reservation prices.

    Volume is the size of the mismatch between who holds and who should hold. It is a
    function of the allocation ALONE given the population; z is a function of the
    population ALONE given the stock. They are exactly complementary, which is why one
    diagram cannot be read for both.

R3  THE COMPARATIVE-STATIC.  REVIEW-002's finding F1 is correct and is conceded: one
    schedule CAN be shifted with the other held pointwise fixed. This result uses that
    concession rather than denying it. To specify such a perturbation you must name the
    allocation - "raise NON-HOLDERS' valuations" is not one operation on a population, it
    is a family of operations indexed by H, and the members of that family disagree about
    the new price. A perturbation defined on the population alone does not.

Every asserted invariant below is mutation-guarded (WT-069): a deliberate corruption that
SHOULD break it is run, and the script fails loudly if the corruption does not break it.

    ./.venv/bin/python scripts/wt070_p3_fold.py
"""

from __future__ import annotations

import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

from wealth_tensor.excess_demand import Market  # noqa: E402

# ---------------------------------------------------------------------------
# Population. Identical to v0.1 so that every figure is comparable to the
# superseded draft and to REVIEW-002's counter-demonstrations.
# ---------------------------------------------------------------------------

N = 400
STOCK = 150
N_ALLOC = 25
LAMBDA_SWEEP = (1.00, 1.05, 1.15, 1.30, 1.60, 2.00)

RESERVATION_PRICES = np.random.default_rng(7).lognormal(mean=3.0, sigma=0.6, size=N)


def allocations(m, stock, k=N_ALLOC):
    """k distinct allocations of the same stock over the same population."""
    out = []
    for seed in range(k):
        rng = np.random.default_rng(seed)
        h = np.zeros(m.size, dtype=bool)
        h[rng.choice(m.size, size=stock, replace=False)] = True
        out.append(h)
    return out


def interior_grid(m, n_points=401, eps=1e-9):
    """Grid strictly inside the support, with reservation prices excluded.

    v0.1 credited the tie fix to this epsilon filter. REVIEW-002 established that the
    filter removes ZERO points and that the correction came entirely from dropping the
    two endpoints, which are data. Both are done here and the accounting is honest: the
    endpoint drop is what works, the epsilon filter is retained as a guard against a
    future population whose grid does land on a datum.
    """
    grid = np.linspace(float(m.min()), float(m.max()), n_points)[1:-1]
    keep = np.array([np.min(np.abs(m - p)) > eps for p in grid])
    return grid[keep], int((~keep).sum())


def schedule(fn, grid):
    return tuple(fn(float(p)) for p in grid)


def top_set(m, stock):
    """T: the `stock` agents with the highest reservation prices. A fold over units."""
    t = np.zeros(m.size, dtype=bool)
    t[np.argsort(m)[::-1][:stock]] = True
    return t


def hr(title):
    print()
    print("=" * 78)
    print(title)
    print("=" * 78)


def check(label, condition):
    print(f"  {'PASS' if condition else 'FAIL':4}  {label}")
    if not condition:
        raise SystemExit(f"ASSERTION FAILED: {label}")


# ===========================================================================
# R1 - the fold identity
# ===========================================================================

def r1_fold_identity(m, stock, allocs, grid):
    hr("R1 - THE FOLD IDENTITY   z(p) = #{i : m_i > p} - S")

    demands, supplies, excesses = set(), set(), set()
    for h in allocs:
        mk = Market(m, stock, holders=h)
        demands.add(schedule(mk.demand_at, grid))
        supplies.add(schedule(mk.supply_at, grid))
        excesses.add(schedule(mk.excess_demand, grid))

    closed_form = tuple(int(np.sum(m > p)) - stock for p in grid)

    print(f"  grid points (interior, ties excluded)        {len(grid)}")
    print(f"  allocations                                  {len(allocs)}")
    print(f"  distinct demand schedules D(p)               {len(demands)}")
    print(f"  distinct supply schedules S(p)               {len(supplies)}")
    print(f"  distinct excess-demand schedules z(p)        {len(excesses)}")

    check("25 distinct demand schedules", len(demands) == N_ALLOC)
    check("25 distinct supply schedules", len(supplies) == N_ALLOC)
    check("exactly 1 distinct excess-demand schedule", len(excesses) == 1)
    check("z equals the closed form at every grid point", excesses == {closed_form})

    # WT-069 mutation guard: break the partition argument by counting holders ABOVE p
    # in the supply term rather than below. The identity must die.
    mutant = set()
    for h in allocs:
        mutant.add(tuple(int(np.sum(~h & (m > p))) - int(np.sum(h & (m > p)))
                         for p in grid))
    check("MUTANT (supply reads m>p): identity dies as it must", len(mutant) == N_ALLOC)
    return closed_form


# ===========================================================================
# R2 - the volume theorem
# ===========================================================================

def r2_volume_theorem(m, stock, allocs):
    hr("R2 - THE VOLUME THEOREM   V(H) = |H \\ T|,  T = the top-S valuers")

    T = top_set(m, stock)
    measured, predicted = [], []
    for h in allocs:
        mk = Market(m, stock, holders=h)
        measured.append(mk.volume())
        predicted.append(int(np.sum(h & ~T)))

    check("V(H) = |H \\ T| for all 25 allocations", measured == predicted)

    # The two extremes, constructed rather than sampled.
    h_efficient = T.copy()
    v_min = Market(m, stock, holders=h_efficient).volume()

    bottom = np.argsort(m)[:stock]          # the stock lowest valuers
    h_worst = np.zeros(m.size, dtype=bool)
    h_worst[bottom] = True
    v_max = Market(m, stock, holders=h_worst).volume()

    hyper_mean = stock * (m.size - stock) / m.size

    print(f"  volume across the 25 sampled allocations     "
          f"min {min(measured)}  mean {np.mean(measured):.2f}  max {max(measured)}")
    print(f"  hypergeometric mean S(N-S)/N                 {hyper_mean:.2f}")
    print(f"  V at the EFFICIENT allocation H = T          {v_min}")
    print(f"  V at the WORST allocation H = bottom S       {v_max}")
    print(f"  theoretical maximum min(S, N-S)              {min(stock, m.size - stock)}")

    check("V = 0 when the holders are already the top-S valuers", v_min == 0)
    check("V is maximal when holders are the bottom-S valuers",
          v_max == min(stock, m.size - stock))
    check("the sampled mean sits within 5 of the hypergeometric mean",
          abs(np.mean(measured) - hyper_mean) < 5.0)

    # The corollary, stated as the two numbers that make it: same population, same stock,
    # excess demand pointwise identical, volume anywhere in [0, 150].
    mk_e = Market(m, stock, holders=h_efficient)
    mk_w = Market(m, stock, holders=h_worst)
    same_price = mk_e.marginal_pair() == mk_w.marginal_pair()
    check("clearing interval identical at both volume extremes", same_price)

    # WT-069 mutation guard: T built from the LOWEST valuers instead of the highest.
    # V = |H \ T| must stop matching.
    T_bad = np.zeros(m.size, dtype=bool)
    T_bad[np.argsort(m)[:stock]] = True
    bad = [int(np.sum(h & ~T_bad)) for h in allocs]
    check("MUTANT (T = bottom-S): the volume identity dies as it must",
          bad != measured)

    return measured, v_min, v_max, hyper_mean


# ===========================================================================
# R3 - the comparative static
# ===========================================================================

def r3_comparative_static(m, stock, allocs, grid):
    hr("R3 - THE COMPARATIVE STATIC   which perturbations are population-defined")

    base = Market(m, stock, holders=allocs[0])
    base_lo, base_hi = base.marginal_pair()

    # --- REVIEW-002's F1 counter-demonstration, reproduced and CONCEDED. ------------
    h0 = allocs[0]
    m_up = m.copy()
    m_up[~h0] *= 1.20
    pert = Market(m_up, stock, holders=h0)

    supply_same = schedule(base.supply_at, grid) == schedule(pert.supply_at, grid)
    demand_moved = schedule(base.demand_at, grid) != schedule(pert.demand_at, grid)
    check("F1 CONCEDED: supply unchanged at every grid point", supply_same)
    check("F1 CONCEDED: demand moved", demand_moved)

    p_lo, p_hi = pert.marginal_pair()
    print(f"  baseline clearing interval                   "
          f"[{base_lo:.6f}, {base_hi:.6f}]")
    print(f"  after raising NON-HOLDERS 20% (allocation 0) "
          f"[{p_lo:.6f}, {p_hi:.6f}]")

    # --- and now the point. The effect is computed from the fold alone. -------------
    fold_lo, fold_hi = float(np.sort(m_up)[::-1][stock]), float(np.sort(m_up)[::-1][stock - 1])
    check("the new interval is recovered from the perturbed POPULATION alone, "
          "with no reference to H", (fold_lo, fold_hi) == (p_lo, p_hi))

    # --- the family disagrees ------------------------------------------------------
    indexed_prices, indexed_intervals = [], set()
    for h in allocs:
        mm = m.copy()
        mm[~h] *= 1.20
        mk = Market(mm, stock, holders=h)
        indexed_intervals.add(mk.marginal_pair())
        indexed_prices.append(mk.clearing_price())

    population_intervals = set()
    for h in allocs:
        mm = m * 1.20                      # defined on the population, not on H
        mk = Market(mm, stock, holders=h)
        population_intervals.add(mk.marginal_pair())

    # The COUNT is the wrong statistic and saying so is the point (L32). Two of the 25
    # allocations happen to share a marginal pair, so the count is 23 rather than 25 -
    # a coincidence of two order statistics, not a structural fact. The SPREAD is the
    # structural quantity: how far apart the answers are, measured in units of the width
    # of the interval the answer is supposed to lie inside.
    base_width = base_hi - base_lo
    spread = max(indexed_prices) - min(indexed_prices)

    print()
    print("  'raise NON-HOLDERS' valuations 20%' - specified using H")
    print(f"    distinct clearing intervals over 25 allocations   "
          f"{len(indexed_intervals)}  (of {N_ALLOC}; two pairs coincide)")
    print(f"    clearing price ranges                             "
          f"{min(indexed_prices):.4f} to {max(indexed_prices):.4f}")
    print(f"    spread                                            "
          f"{spread:.4f}")
    print(f"    baseline interval width                           "
          f"{base_width:.6f}")
    print(f"    spread as a multiple of that width                "
          f"{spread / base_width:.1f}x")
    print("  'raise EVERYONE'S valuations 20%' - defined on the population")
    print(f"    distinct clearing intervals over 25 allocations   "
          f"{len(population_intervals)}")
    print(f"    spread                                            0.0000")

    check("the allocation-indexed perturbation fans out",
          len(indexed_intervals) > 1)
    check("it fans out by more than ten interval widths",
          spread / base_width > 10.0)
    check("the population-defined perturbation gives exactly 1",
          len(population_intervals) == 1)

    # WT-069 mutation guard: if the "population-defined" branch secretly read H it would
    # also fan out. Assert that swapping it for an H-reading transform breaks the 1.
    sneaky = set()
    for h in allocs:
        mm = m.copy()
        mm[h] *= 1.20
        sneaky.add(Market(mm, stock, holders=h).marginal_pair())
    check(f"MUTANT (population branch made H-reading): the 1 fans out "
          f"to {len(sneaky)}", len(sneaky) > 1)

    return {
        "base_interval": (base_lo, base_hi),
        "perturbed_interval": (p_lo, p_hi),
        "indexed_distinct": len(indexed_intervals),
        "indexed_spread": spread,
        "base_width": base_width,
        "spread_in_widths": spread / base_width,
        "population_distinct": len(population_intervals),
    }


# ===========================================================================
# R4 - the endowment transform, reported with its defect visible
# ===========================================================================

def r4_endowment_transform(m, stock, allocs, grid):
    hr("R4 - THE ENDOWMENT TRANSFORM   reported WITH the defect REVIEW-002 found")

    # REVIEW-002 finding A3: v0.1 reported a single volume column and never named the
    # allocation seed. R2 says why that is not a reporting slip but a category error -
    # volume is a function of the allocation BY THEOREM, so a volume table without an
    # allocation is not underspecified, it is a family reported as a number. Reported
    # here as the family it is.
    print("  lambda   volume: min   mean    max     distinct z across 25 allocations")
    rows = []
    for lam in LAMBDA_SWEEP:
        vols, zs = [], set()
        for h in allocs:
            mh = Market(m, stock, holders=h).with_endowment_effect(lam)
            vols.append(mh.volume())
            zs.add(schedule(mh.excess_demand, grid))
        rows.append((lam, min(vols), float(np.mean(vols)), max(vols), len(zs)))
        print(f"  {lam:5.2f}        {min(vols):4d}  {np.mean(vols):6.2f}   {max(vols):4d}"
              f"     {len(zs):3d}")

    spread_at_baseline = rows[0][3] - rows[0][1]
    print(f"\n  at lambda = 1 the volume SPREAD across allocations is "
          f"{spread_at_baseline} units, while z is pointwise identical")

    check("at lambda = 1 the invariance holds",
          rows[0][4] == 1)
    check("at lambda = 1 volume nonetheless varies across allocations",
          spread_at_baseline > 0)
    check("at every lambda > 1 the invariance BREAKS, as F2 established",
          all(r[4] == N_ALLOC for r in rows[1:]))
    check("mean volume falls monotonically over the sweep",
          all(rows[i][2] >= rows[i + 1][2] for i in range(len(rows) - 1)))
    return rows


def main():
    m, stock = RESERVATION_PRICES, STOCK
    allocs = allocations(m, stock)
    grid, dropped = interior_grid(m)

    print(__doc__.split("\n")[0])
    print(f"\n  N = {m.size}   S = {stock}   allocations = {len(allocs)}")
    print(f"  reservation prices ~ lognormal(3.0, 0.6), default_rng(7)")
    print(f"  interior grid points = {len(grid)}   "
          f"removed by the epsilon filter = {dropped}")

    r1_fold_identity(m, stock, allocs, grid)
    r2_volume_theorem(m, stock, allocs)
    r3_comparative_static(m, stock, allocs, grid)
    r4_endowment_transform(m, stock, allocs, grid)

    hr("ALL CHECKS PASSED")


if __name__ == "__main__":
    main()
