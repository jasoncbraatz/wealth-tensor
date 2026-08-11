#!/usr/bin/env python3
"""WT-072 - the two claims the WT-065 defender made, checked before either is believed.

The defender killed the P3 framing and offered a replacement. Two of its load-bearing
claims are computations, so neither is taken on trust.

D1  THE A1 EXHIBIT WAS ALSO MEASURING A HYPERGEOMETRIC.  Uniform random allocations make
    the crossing height V = |H \\ T| a draw with mean S(N-S)/N and sd ~4.7. The reported
    range 85-103 is +/- 2 sd of a number the POPULATION fixes. The quantity the paper is
    about has therefore never actually been varied. Varying it means varying the COUPLING
    between valuations and holdings, not resampling uniform allocations.

D2  THE IDENTIFICATION THEOREM.  With a per-unit wedge t, the residual in excess demand is
    the sliding-window count W(p) = #{i in H : p-t <= m_i <= p}. The defender claims W
    determines the holders' valuation set EXACTLY for every t > 0, by a leftmost-jump
    induction, while at t = 0 every coupling gives the same schedule. If true, the
    identified set for the coupling is EVERYTHING at t = 0 and a SINGLETON at every t > 0.
    Identification is discontinuous at zero. That is a stronger and more interesting claim
    than the invariance it replaces, so it gets checked harder, not less.

    ./.venv/bin/python scripts/wt072_coupling.py
"""

from __future__ import annotations

import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

from wealth_tensor.excess_demand import Market  # noqa: E402

N, STOCK = 400, 150
RESERVATION_PRICES = np.random.default_rng(7).lognormal(3.0, 0.6, N)


def hr(t):
    print("\n" + "=" * 78 + f"\n{t}\n" + "=" * 78)


def check(label, ok):
    print(f"  {'PASS' if ok else 'FAIL':4}  {label}")
    if not ok:
        raise SystemExit(f"ASSERTION FAILED: {label}")


def top_set(m, stock):
    t = np.zeros(m.size, dtype=bool)
    t[np.argsort(m)[::-1][:stock]] = True
    return t


def couplings(m, stock):
    """Structured couplings of holdings to valuations. Named, not sampled."""
    order = np.argsort(m)[::-1]          # descending valuation
    out = {}

    def mk(idx):
        h = np.zeros(m.size, dtype=bool)
        h[idx] = True
        return h

    out["comonotone (H = top-S)"] = mk(order[:stock])
    out["antitone (H = bottom-S)"] = mk(order[-stock:])
    mid = (m.size - stock) // 2
    out["block (H = middle-S)"] = mk(order[mid:mid + stock])
    out["alternating (every ~2.67th)"] = mk(order[np.linspace(
        0, m.size - 1, stock).astype(int)])
    out["uniform random (seed 0)"] = mk(np.random.default_rng(0).choice(
        m.size, size=stock, replace=False))
    return out


# ===========================================================================
# D1 - vary the coupling, not the sample
# ===========================================================================

def d1_structured_couplings(m, stock):
    hr("D1 - THE CROSSING HEIGHT, OVER STRUCTURED COUPLINGS RATHER THAN SAMPLES")

    T = top_set(m, stock)
    hyper_mean = stock * (m.size - stock) / m.size
    hyper_sd = float(np.sqrt(stock * (stock / m.size) * (1 - stock / m.size)
                             * (m.size - stock) / (m.size - 1)))

    # the uniform-sample band, computed rather than asserted
    sample_v = []
    for seed in range(25):
        rng = np.random.default_rng(seed)
        h = np.zeros(m.size, dtype=bool)
        h[rng.choice(m.size, size=stock, replace=False)] = True
        sample_v.append(int(np.sum(h & ~T)))

    print(f"  hypergeometric mean S(N-S)/N                 {hyper_mean:.2f}")
    print(f"  hypergeometric sd                            {hyper_sd:.2f}")
    print(f"  25 uniform draws                             "
          f"min {min(sample_v)}  mean {np.mean(sample_v):.2f}  max {max(sample_v)}")
    print(f"  +/- 2 sd band around the mean                "
          f"[{hyper_mean - 2 * hyper_sd:.1f}, {hyper_mean + 2 * hyper_sd:.1f}]")

    check("every uniform draw falls inside the +/- 2.5 sd band, so the reported "
          "range was sampling noise around a population constant",
          all(abs(v - hyper_mean) < 2.5 * hyper_sd for v in sample_v))

    print("\n  coupling                        crossing height   clearing interval")
    heights, intervals = [], set()
    for name, h in couplings(m, stock).items():
        mk = Market(m, stock, holders=h)
        p = mk.clearing_price()
        height = mk.demand_at(p)
        lo, hi = mk.marginal_pair()
        intervals.add((lo, hi))
        heights.append(height)
        print(f"  {name:30s}  {height:9d}       [{lo:.4f}, {hi:.4f}]")

    print(f"\n  range over structured couplings              "
          f"{min(heights)} to {max(heights)}")
    print(f"  range over 25 uniform samples                "
          f"{min(sample_v)} to {max(sample_v)}")
    print(f"  distinct clearing intervals                  {len(intervals)}")

    check("structured couplings span a far wider range than uniform sampling",
          (max(heights) - min(heights)) > 5 * (max(sample_v) - min(sample_v)))
    check("and the clearing interval is IDENTICAL across all of them",
          len(intervals) == 1)
    return heights, sample_v


# ===========================================================================
# D2 - does the wedge identify the coupling?
# ===========================================================================

def d2_identification(m, stock):
    hr("D2 - IDENTIFICATION.   does W(p) = #{i in H : p-t <= m_i <= p} pin down H?")

    def W(h, t, grid):
        return tuple(int(np.sum(h & (m >= p - t) & (m <= p))) for p in grid)

    grid = np.linspace(float(m.min()) - 3.5, float(m.max()) + 0.5, 3000)

    named = couplings(m, stock)
    rng = np.random.default_rng(99)
    pool = list(named.values())
    for _ in range(20):
        h = np.zeros(m.size, dtype=bool)
        h[rng.choice(m.size, size=stock, replace=False)] = True
        pool.append(h)

    print(f"  candidate holder sets                        {len(pool)}")
    print(f"  grid points                                  {len(grid)}")
    print("\n      t        distinct W profiles   distinct holder VALUATION sets")
    holder_sets = {tuple(np.sort(m[h])) for h in pool}
    for t in (0.0, 0.01, 0.10, 1.00):
        profiles = {W(h, t, grid) for h in pool}
        print(f"      {t:5.2f}    {len(profiles):15d}   {len(holder_sets):20d}")
        if t == 0.0:
            check("at t = 0 every coupling gives the SAME residual: "
                  "the coupling is completely unidentified",
                  len(profiles) == 1)
        else:
            check(f"at t = {t} the residual separates every distinct holder set: "
                  f"identification is exact",
                  len(profiles) == len(holder_sets))

    # The sharp version: two holder sets differing in ONE agent must be separated,
    # because that is the hardest case for the induction to survive.
    base = named["uniform random (seed 0)"].copy()
    inside = np.flatnonzero(base)
    outside = np.flatnonzero(~base)
    swapped = base.copy()
    swapped[inside[0]] = False
    swapped[outside[0]] = True

    print("\n  hardest case: two holder sets differing in exactly ONE agent")
    for t in (0.01, 0.10, 1.00):
        sep = W(base, t, grid) != W(swapped, t, grid)
        check(f"t = {t:4.2f}: a single-agent swap changes W", sep)

    # And the degradation the defender predicted: strength is O(t) as t -> 0.
    print("\n      t        L1 distance between the two W profiles (single swap)")
    for t in (0.001, 0.01, 0.10, 1.00, 3.00):
        a, b = np.array(W(base, t, grid)), np.array(W(swapped, t, grid))
        print(f"      {t:6.3f}   {int(np.abs(a - b).sum()):6d}")

    print("\n  VERDICT: the defender's identification claim holds numerically.")
    print("           Unidentified at t = 0, exactly identified at every t > 0,")
    print("           with separation degrading toward zero as t does.")


def main():
    m, stock = RESERVATION_PRICES, STOCK
    print(__doc__.split("\n")[0])
    d1_structured_couplings(m, stock)
    d2_identification(m, stock)
    hr("BOTH DEFENDER CLAIMS CHECKED")


if __name__ == "__main__":
    main()
