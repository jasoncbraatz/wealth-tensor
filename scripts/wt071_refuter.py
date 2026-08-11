#!/usr/bin/env python3
"""WT-071 - the three checks the WT-065 refuter demanded, run before anything is claimed.

RETROFITTED 2026-08-11 (wealthTensor-09) to the severity discipline, scripts/severity.py.
Every check below now ships a WITNESS: a world in which the check goes red, executed at
check time. A guard whose witness also passes is a PHANTOM TAG and kills the run. Before
this retrofit the script used a bare check(label, condition) and was therefore capable of
the exact defect it was written to expose - which is the joke, and it is on us.

Building the witnesses also CORRECTED this script. See C2(a): the claim that the ratio is
"dominated by the noise in its own denominator" was too strong. Across N the denominator
swings 12.9x and the numerator swings 4.6x. The denominator moves more, and the numerator
moves too, and the conclusion - that the ratio is not an effect size - survives both.

The adversarial pass on WT-070 landed three hits. Each is a computation, so each is
settled by running it rather than by arguing about it.

C1  THE CROSSING HEIGHT IS THE VOLUME.  At a clearing price p* strictly inside the
    interval, {i : m_i > p*} is exactly T, so D(p*) = |T \\ H| and S(p*) = |H \\ T| = V.
    If true, the Marshallian cross does NOT display irrelevant information: its price
    coordinate reads the population and its quantity coordinate reads the allocation
    mismatch, which is the one quantity z cannot deliver. This INVERTS the framing
    WT-070 was written to support.

C2  THE 26x IS AN ARTEFACT OF N, AND THE CONTROL WAS MISSPECIFIED.  The baseline
    interval is a gap between consecutive order statistics, width O(1/N); the spread
    from a 20% shift is O(1). The ratio is therefore Theta(N) and is not an effect
    size. And "raise EVERYONE 20%" is rank-preserving by construction, so the 23-vs-1
    contrast may be rank-scrambling vs rank-preserving rather than allocation-indexed
    vs population-defined. The honest control is a random subset of the same size that
    never mentions H.

C3  THE INVARIANCE IS THE FRICTIONLESS LIMIT.  With a per-unit wedge t, a holder sells
    only if m_i < p - t. Then

        z(p) = #{i : m_i > p} - S + #{i in H : p - t <= m_i <= p}

    and the allocation no longer cancels. The residual is the locked-in holders. If the
    algebra is right, H is load-bearing everywhere except at t = 0.

    ./.venv/bin/python scripts/wt071_refuter.py
"""

from __future__ import annotations

import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))
sys.path.insert(0, str(Path(__file__).resolve().parent))

from wealth_tensor.excess_demand import Market      # noqa: E402
from severity import check, summary                 # noqa: E402

N, STOCK, N_ALLOC = 400, 150, 25
RESERVATION_PRICES = np.random.default_rng(7).lognormal(3.0, 0.6, N)


def allocations(m, stock, k=N_ALLOC, offset=0):
    out = []
    for seed in range(offset, offset + k):
        rng = np.random.default_rng(seed)
        h = np.zeros(m.size, dtype=bool)
        h[rng.choice(m.size, size=stock, replace=False)] = True
        out.append(h)
    return out


def top_set(m, stock, size=None):
    t = np.zeros(m.size, dtype=bool)
    t[np.argsort(m)[::-1][:(stock if size is None else size)]] = True
    return t


def bottom_set(m, stock):
    t = np.zeros(m.size, dtype=bool)
    t[np.argsort(m)[:stock]] = True
    return t


def hr(t):
    print("\n" + "=" * 78 + f"\n{t}\n" + "=" * 78)


# ===========================================================================
# C1 - the crossing height is the volume
# ===========================================================================

def c1_crossing_is_volume(m, stock, allocs):
    hr("C1 - IS THE CROSSING HEIGHT THE VOLUME?   D(p*) = S(p*) = |H \\ T| ?")

    T = top_set(m, stock)
    # WITNESS MATERIAL. Two worlds in which the identities below are FALSE:
    #   T_bad  - the bottom-S valuers, a same-size set that is not the efficient one,
    #            so |T_bad \ H| is not the crossing height;
    #   T_big  - a set of a DIFFERENT size, which breaks the two-sided cardinality
    #            balance that makes |H \ T| = |T \ H| hold.
    T_bad = bottom_set(m, stock)
    T_big = top_set(m, stock, size=stock + 10)
    p_lo = float(m.min())          # far below the interval: D = N-S, S = 0

    markets = [Market(m, stock, holders=h) for h in allocs]
    rows = []
    for mk, h in zip(markets, allocs):
        p = mk.clearing_price()
        rows.append((mk.demand_at(p), mk.supply_at(p),
                     int(np.sum(h & ~T)), int(np.sum(T & ~h)), mk.volume()))

    check("D(p*) = S(p*) at the clearing price, every allocation",
          all(r[0] == r[1] for r in rows),
          witness=lambda: all(mk.demand_at(p_lo) == mk.supply_at(p_lo)
                              for mk in markets))
    check("D(p*) = |T \\ H|, every allocation", all(r[0] == r[3] for r in rows),
          witness=lambda: all(r[0] == int(np.sum(T_bad & ~h))
                              for r, h in zip(rows, allocs)))
    check("S(p*) = |H \\ T| = V, every allocation",
          all(r[1] == r[2] == r[4] for r in rows),
          witness=lambda: all(r[1] == int(np.sum(h & ~T_bad)) == r[4]
                              for r, h in zip(rows, allocs)))
    check("|H \\ T| = |T \\ H|, every allocation", all(r[2] == r[3] for r in rows),
          witness=lambda: all(int(np.sum(h & ~T_big)) == int(np.sum(T_big & ~h))
                              for h in allocs))

    print(f"  crossing height across 25 allocations        "
          f"min {min(r[0] for r in rows)}  max {max(r[0] for r in rows)}")
    print("  VERDICT: the refuter is RIGHT. The quantity coordinate of the")
    print("           Marshallian cross IS the allocation mismatch. The diagram")
    print("           is not displaying irrelevant information; it is displaying")
    print("           exactly the information z cannot carry.")
    return rows


# ===========================================================================
# C2 - the spread, its N-dependence, and the honest control
# ===========================================================================

def c2_spread_and_control():
    hr("C2 - IS THE 26x AN ARTEFACT OF N, AND WAS THE CONTROL MISSPECIFIED?")

    print("  (a) N-dependence of the ratio")
    print("      N      interval width   spread    ratio     pop sd   distinct p*")
    ratios, gaps, spreads, sds, distincts = [], [], [], [], []
    for n in (400, 1000, 4000, 10000):
        s = int(round(n * 150 / 400))
        mm = np.random.default_rng(7).lognormal(3.0, 0.6, n)
        allocs = allocations(mm, s)
        desc = np.sort(mm)[::-1]
        width = float(desc[s - 1] - desc[s])
        prices = []
        for h in allocs:
            p = mm.copy()
            p[~h] *= 1.20
            d = np.sort(p)[::-1]
            prices.append((float(d[s]) + float(d[s - 1])) / 2.0)
        spread = max(prices) - min(prices)
        ratios.append(spread / width)
        gaps.append(width)
        spreads.append(spread)
        sds.append(float(np.std(mm)))
        distincts.append(len(set(prices)))
        print(f"      {n:6d}   {width:.6f}        {spread:.4f}    "
              f"{spread / width:8.1f}x  {sds[-1]:7.2f}   {distincts[-1]:6d}")

    def swing(v):
        return max(v) / min(v)

    # The refuter predicted the ratio would grow like Theta(N). It does not: it is
    # 26x, 8x, 113x, 47x. He was RIGHT that the ratio is not an effect size and WRONG
    # about why. The denominator is the gap between two consecutive order statistics -
    # a single draw with enormous relative variance.
    #
    # CORRECTED 2026-08-11 while building the witnesses. The earlier note here said the
    # ratio was "dominated by the noise in its own denominator." Measured: the gap swings
    # 12.9x across N and the spread swings 4.6x. The denominator moves MORE; it does not
    # move alone. Both statements below are now checked separately, because bundling them
    # into one assertion is how a check ends up untestable.
    print(f"\n      ratio across N: min {min(ratios):.1f}x  max {max(ratios):.1f}x  "
          f"({swing(ratios):.1f}-fold swing, non-monotone in N)")
    print(f"      component swings across N:  gap {swing(gaps):.1f}x   "
          f"spread {swing(spreads):.1f}x   population sd {swing(sds):.2f}x   "
          f"distinct p* {swing(distincts):.2f}x")

    # WITNESS: a quantity measured in the SAME experiment that is N-stable - the number
    # of distinct clearing prices across the 25 allocations. If even that swung fourfold,
    # the check would be detecting the sweep and not the statistic.
    check("the ratio is unstable across N by more than fourfold, so it is not an "
          "effect size", swing(ratios) > 4.0,
          witness=lambda: swing(distincts) > 4.0)

    # WITNESS: the population standard deviation - a denominator the population fixes -
    # is N-stable. That is what makes the order-statistic gap the culprit rather than
    # the sweep.
    check("and the denominator is the unstable part: a single order-statistic gap "
          "swings fourfold-plus across N where a population-scale denominator does not",
          swing(gaps) > 4.0,
          witness=lambda: swing(sds) > 4.0)

    print("\n  (b) the honest control - a random subset of the SAME SIZE, never naming H")
    m, stock = RESERVATION_PRICES, STOCK
    allocs = allocations(m, stock)
    n_nonholders = m.size - stock

    indexed, random_subset, everyone = [], [], []
    for i, h in enumerate(allocs):
        a = m.copy(); a[~h] *= 1.20
        indexed.append(float(np.mean(np.sort(a)[::-1][stock - 1:stock + 1])))

        rng = np.random.default_rng(1000 + i)
        pick = np.zeros(m.size, dtype=bool)
        pick[rng.choice(m.size, size=n_nonholders, replace=False)] = True
        b = m.copy(); b[pick] *= 1.20
        random_subset.append(float(np.mean(np.sort(b)[::-1][stock - 1:stock + 1])))

        c = m * 1.20
        everyone.append(float(np.mean(np.sort(c)[::-1][stock - 1:stock + 1])))

    def rng_of(v):
        return max(v) - min(v)

    print(f"      'raise NON-HOLDERS 20%'  (indexed by H)     "
          f"spread {rng_of(indexed):.4f}  distinct {len(set(indexed))}")
    print(f"      'raise a RANDOM 250 by 20%' (never names H) "
          f"spread {rng_of(random_subset):.4f}  distinct {len(set(random_subset))}")
    print(f"      'raise EVERYONE 20%'     (rank-preserving)  "
          f"spread {rng_of(everyone):.4f}  distinct {len(set(everyone))}")

    comparable = abs(rng_of(indexed) - rng_of(random_subset)) < 0.5 * rng_of(indexed)
    print("\n  VERDICT: the refuter is RIGHT on both counts."
          if comparable else "\n  VERDICT: the control DOES separate them.")
    # WITNESS: the rank-preserving perturbation. "Raise EVERYONE 20%" cannot fan out,
    # by monotonicity, so it is the world in which a fanning-out check goes red. This is
    # the -08 phantom tag pointed the other way: the control that could not vary is the
    # proof that the control which did vary was measuring something.
    check("the random-subset control fans out too, so the 23-vs-1 contrast was "
          "rank-scrambling vs rank-preserving and NOT H vs population",
          len(set(random_subset)) > 1,
          witness=lambda: len(set(everyone)) > 1)
    return ratios, rng_of(indexed), rng_of(random_subset), rng_of(everyone)


# ===========================================================================
# C3 - the wedge. does the allocation stop cancelling?
# ===========================================================================

def c3_wedge(m, stock, allocs):
    hr("C3 - THE WEDGE.   holder sells iff m_i < p - t.   does H come back?")

    def z_wedge(mm, h, p, t):
        return int(np.sum(~h & (mm > p))) - int(np.sum(h & (mm < p - t)))

    grid = np.linspace(float(m.min()), float(m.max()), 401)[1:-1]

    print("      t        distinct z schedules   distinct clearing prices")
    out = []
    for t in (0.0, 0.05, 0.25, 1.00, 3.00):
        zs, ps = set(), set()
        for h in allocs:
            sched = tuple(z_wedge(m, h, float(p), t) for p in grid)
            zs.add(sched)
            cross = next((float(p) for p in grid if z_wedge(m, h, float(p), t) <= 0),
                         float(grid[-1]))
            ps.add(round(cross, 6))
        out.append((t, len(zs), len(ps)))
        print(f"      {t:5.2f}    {len(zs):10d}           {len(ps):10d}")

    # The two checks are each other's witness, which is the cleanest form the discipline
    # takes: the claim is a DISCONTINUITY, so each side is the falsifying world for the
    # other. If the wedge made no difference, both witnesses would pass and both checks
    # would die together.
    check("at t = 0 the allocation cancels", out[0][1] == 1,
          witness=lambda: out[1][1] == 1)
    check("at every t > 0 the allocation does NOT cancel",
          all(r[1] > 1 for r in out[1:]),
          witness=lambda: out[0][1] > 1)

    # the residual term, measured: locked-in holders at the frictionless clearing price
    T = top_set(m, stock)
    p0 = float(np.mean(np.sort(m)[::-1][stock - 1:stock + 1]))
    print("\n      locked-in holders  #{i in H : p-t <= m_i <= p}  at the t=0 price")
    print("      t        min   mean    max     (of S = 150 holders)")
    for t in (0.05, 0.25, 1.00, 3.00):
        band = [int(np.sum(h & (m >= p0 - t) & (m <= p0))) for h in allocs]
        print(f"      {t:5.2f}    {min(band):3d}  {np.mean(band):6.2f}   {max(band):3d}")

    print("\n  VERDICT: the refuter is RIGHT. The identity is the frictionless limit.")
    print("           At any positive wedge the allocation is load-bearing, and the")
    print("           residual is the locked-in holders - the object the capital-gains")
    print("           and stamp-duty lock-in literatures exist to measure.")
    return out


def main():
    m, stock = RESERVATION_PRICES, STOCK
    allocs = allocations(m, stock)
    print(__doc__.split("\n")[0])
    c1_crossing_is_volume(m, stock, allocs)
    c2_spread_and_control()
    c3_wedge(m, stock, allocs)
    hr("ALL THREE REFUTER CHECKS RAN. See verdicts above.")
    summary("WT-071 SEVERITY")


if __name__ == "__main__":
    main()
