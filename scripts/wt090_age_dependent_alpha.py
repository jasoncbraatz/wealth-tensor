#!/usr/bin/env python3
"""WT-090 · REG-004 · the deferral measure under an age-dependent recognition rate.

Run exactly as registered in `docs/preregistration/REG-004-p3-age-dependent-
recognition.md`, committed and pushed (5160f51) before this file existed.

    python3 scripts/wt090_age_dependent_alpha.py --events data/pre-002-events.json

Nothing here decides anything. Every ladder boundary, tolerance, sweep grid and
reported direction comes from REG-004. Ladders N, M, C, D, E and S are exhaustive.

THE CLAIM UNDER TEST (REG-004 §1). Let a gap cohort created at time s be recognised
at lag T >= 1 periods, so it sits in the gap at s+1 .. s+T. Then

    gap(t) = SUM_{a>=1} c_{t-a} * P(T >= a),      c_s = (1-phi) * delta * E(s)

and with E(t) = E0 * D^t, D = 1-delta, z = 1/D:

    R = gap/E = (1-phi) * delta * SUM_{a>=1} z^a P(T>=a)
              = (1-phi) * (Pi(z) - 1),            Pi(z) = E[z^T]

because SUM_{a>=1} z^a P(T>=a) = z(Pi(z)-1)/(z-1) and z-1 = delta/D.

UNITS. The lag is measured in QUARTERS and everything below is computed in quarters.
Section 4.4's ladder is stated in annual rates, so annual delta is converted by
delta_q = 1 - (1-delta_a)^(1/4) and quarterly crossings are converted back. The
period change is not free -- R is a ratio of two stocks and depends on the
discretisation -- so section 0 reports the size of that gap explicitly, before any
correction is quoted, so no reader mistakes a units artefact for a shape effect.

NOTE ON ORDER (the trap -14 paid two round trips for): severity.check() EXECUTES its
witness immediately, so every helper is defined ABOVE the first check that uses it.
"""
from __future__ import annotations

import argparse
import json
import math
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from severity import check, summary  # noqa: E402

# ---- everything below is fixed by REG-004; nothing is chosen at run time -------------
K_HAT = 1.21                    # RESULT-REG-003 §3, discrete Weibull profile MLE
Q_HAT = 0.9213424092985028      # RESULT-REG-003 §3
ALPHA_Q_HAT = 0.12272272272272272   # RESULT-REG-003 §2, censored geometric MLE, pooled
NEST_TOL = 1e-12                # REG-004 §2 F1, F4
SIM_TOL = 2e-4                  # REG-004 §2 F2 -- §4.3's published transient bound
SIM_PERIODS = 400               # §4.3's own horizon
TAIL_EPS = 1e-14                # remainder bound for every Pi() evaluation

# §4.4's tabulated ladder, annual rates, typed from the manuscript table.
TIERS = [
    {"name": "0 · property, plant and equipment", "phi": 0.80, "delta_a": 0.030},
    {"name": "1 · finite-lived intangibles",      "phi": 0.60, "delta_a": 0.020},
    {"name": "2 · indefinite-lived intangibles",  "phi": 0.40, "delta_a": 0.010},
    {"name": "3 · goodwill",                      "phi": 0.20, "delta_a": 0.002},
]
ALPHA_A_CAL = 0.05              # §4.4's calibration, for the discretisation check only
DELTA3_STAR_PUBLISHED = 0.00789  # §4.4's crossing, annual, under the constant hazard

# REG-004 §4 ladder M: the disclosed rectangle. ASC 360 / ASC 350-30-50 lives.
RECT_PPE_LIVES = (10.0, 40.0)
RECT_FLI_LIVES = (3.0, 20.0)


# ======================================================================================
# §0 · lag distributions.  Each exposes P(T >= a) for a >= 1 and a name.
# ======================================================================================
def q2a(delta_a: float) -> float:
    """Annual rate -> quarterly rate.  Survival composes; rates do not."""
    return 1.0 - (1.0 - delta_a) ** 0.25


def a2q(delta_q: float) -> float:
    return 1.0 - (1.0 - delta_q) ** 4


class Lag:
    """A recognition-lag distribution.  sur(a) = P(T >= a), a >= 1."""

    def __init__(self, name: str, sur, support_min: int, ratio=None):
        self.name, self._sur, self.support_min = name, sur, support_min
        # P(T>=a+1)/P(T>=a), supplied in a form that does NOT underflow.  Evaluating it
        # as sur(a+1)/sur(a) is wrong for a reason that is silent: the survival function
        # underflows to 0.0 while the TERM z^a * S(a) is still large, and a loop that
        # reads that as "the tail is exhausted" returns a finite number for a divergent
        # sum.  Caught by tests/test_deferral_transform.py, not by any run of §5.
        self._ratio = ratio or (lambda a: (self._sur(a + 1) / self._sur(a))
                                if self._sur(a) > 0.0 else 0.0)

    def sur(self, a: int) -> float:
        return self._sur(a)

    def ratio(self, a: int) -> float:
        return self._ratio(a)

    def pi(self, z: float, eps: float = TAIL_EPS) -> float:
        """E[z^T] = 1 + (z-1) * SUM_{a>=1} z^(a-1) P(T>=a).

        Summed to a PROVEN remainder bound (REG-004 §4 ladder D asks for a bound and
        not a truncation): the terms are t_a = z^(a-1) P(T>=a), and once the observed
        ratio t_{a+1}/t_a has been below some rho < 1 for the whole tail AND the
        survival ratio P(T>=a+1)/P(T>=a) is non-increasing in a (true for every
        distribution here: IFR by construction, or geometric with a constant ratio),
        the remainder is bounded by t_a * rho / (1 - rho).
        """
        if z <= 0:
            raise ValueError("z must be positive")
        # Terms are accumulated MULTIPLICATIVELY, t_{a+1} = t_a * z * S(a+1)/S(a),
        # never as z**(a-1) * S(a): the two factors overflow long before their product
        # does, and near the geometric's own radius the sum needs tens of thousands of
        # terms.  Caught by tests/test_deferral_transform.py at 0.99 * alpha.
        total, a, prev = 0.0, 1, None
        t = self.sur(1)
        while True:
            total += t
            r = self.ratio(a)
            if r == 0.0:
                break                      # genuine exhaustion: finite support
            if prev is not None and t < prev:
                rho = t / prev
                if rho < 1.0 and t * rho / (1.0 - rho) < eps * max(total, 1.0):
                    break
            if t > 1e290 and (prev is None or t >= prev):
                # Not a proof of divergence -- an IFR lag's terms can peak above 1e230
                # and still turn over -- but past this point the partial sum cannot be
                # carried in double precision, so refusing is the honest return either
                # way.  The threshold sits two orders below overflow so the refusal is
                # reached before inf silently poisons the sum.
                raise RuntimeError(f"{self.name}: Pi(z={z}) exceeds double precision"
                                   f" while still rising -- D3")
            if a > 200_000:
                raise RuntimeError(f"{self.name}: Pi(z={z}) did not converge -- D3")
            prev = t
            t = t * z * r
            a += 1
        return 1.0 + (z - 1.0) * total

    def mean(self) -> float:
        return self.pi_derivative_at_1()

    def pi_derivative_at_1(self) -> float:
        """E[T] = SUM_{a>=1} P(T>=a).  Diverges only for a lag with no mean."""
        total, a, = 0.0, 1
        while True:
            s = self.sur(a)
            total += s
            if s < 1e-15 or a > 200_000:
                break
            a += 1
        return total

    def conditioned(self) -> "Lag":
        """Condition on T >= 1.  REG-004 §3, question three, failure one."""
        p_ge_1 = self.sur(1)
        return Lag(self.name + " | T>=1", lambda a: self.sur(a) / p_ge_1, 1,
                   ratio=self.ratio)      # conditioning is a constant rescale for a>=1


def geometric(alpha: float) -> Lag:
    """T ~ Geom on {1,2,...}: P(T >= a) = (1-alpha)^(a-1).  E[T] = 1/alpha."""
    return Lag(f"geometric(alpha={alpha:.6f})", lambda a: (1.0 - alpha) ** (a - 1), 1,
               ratio=lambda a: 1.0 - alpha)


def geometric_as_registered(alpha: float) -> Lag:
    """REG-003's registered support {0,1,2,...}: P(T >= a) = (1-alpha)^a."""
    return Lag(f"geometric-on-0(alpha={alpha:.6f})", lambda a: (1.0 - alpha) ** a, 0)


def dweibull(q: float, k: float) -> Lag:
    """Nakagawa-Osaki, exactly wt089's convention: P(T >= t) = q^(t^k)."""
    return Lag(f"discrete Weibull(q={q:.6f}, k={k:.3f})",
               lambda a: q ** (a ** k), 0,
               ratio=lambda a: q ** ((a + 1) ** k - a ** k))


def empirical(lags, censored, tmax: int = 20) -> Lag:
    """Kaplan-Meier discrete survival on the observed window, mass beyond tmax DROPPED.

    REG-004 §3, question three, failure two: z^a with z>1 weights exactly the tail
    this truncates, so the resulting Pi is a STRICT LOWER BOUND on the true one and
    the bias grows with delta.  Reported as a bound, never as the point estimate.
    """
    sur = {0: 1.0}
    s = 1.0
    for t in range(0, tmax + 1):
        at_risk = sum(1 for L, c in zip(lags, censored) if L >= t)
        died = sum(1 for L, c in zip(lags, censored) if L == t and not c)
        if at_risk > 0:
            s *= (1.0 - died / at_risk)
        sur[t + 1] = s
    return Lag(f"empirical KM (truncated at {tmax}q, LOWER BOUND)",
               lambda a: sur.get(a, 0.0), 1)


# ======================================================================================
# §0b · the registered closed form, the naive substitution, and alpha_eff
# ======================================================================================
def R_registered(lag: Lag, delta_q: float, phi: float) -> float:
    """REG-004 §1:  R = (1-phi) * (Pi(1/(1-delta)) - 1)."""
    return (1.0 - phi) * (lag.pi(1.0 / (1.0 - delta_q)) - 1.0)


def R_naive(alpha_q: float, delta_q: float, phi: float) -> float:
    """The published closed form with alpha <- 1/E[T].  Undefined at delta >= alpha."""
    if delta_q >= alpha_q:
        return math.inf
    return (1.0 - phi) * delta_q / (alpha_q - delta_q)


def alpha_eff(lag: Lag, delta_q: float) -> float:
    """delta * Pi / (Pi - 1).  A FUNCTION of delta, never a parameter (REG-004 §3)."""
    pi = lag.pi(1.0 / (1.0 - delta_q))
    return delta_q * pi / (pi - 1.0)


def simulate_R(lag: Lag, delta_q: float, phi: float, periods: int = SIM_PERIODS) -> float:
    """Age-structured simulation.  No closed form anywhere in this loop (F2).

    Cohorts are carried by age; each period every cohort of age a is multiplied by the
    survival ratio P(T>=a+1)/P(T>=a), i.e. it faces its own age-specific hazard.
    """
    E0, D = 1.0, 1.0 - delta_q
    cohorts: list[float] = []          # cohorts[i] = amount now of age i+1
    E = E0
    for _ in range(periods):
        aged = []
        for i, amt in enumerate(cohorts):
            a = i + 1
            s_a, s_a1 = lag.sur(a), lag.sur(a + 1)
            aged.append(amt * (s_a1 / s_a) if s_a > 0 else 0.0)
        born = (1.0 - phi) * delta_q * E * lag.sur(1)   # survives to age 1 w.p. P(T>=1)
        cohorts = [born] + aged
        E *= D
    return sum(cohorts) / E


def solve_delta_star(lag: Lag, target_pi: float) -> float:
    """delta solving Pi(1/(1-delta)) = target.  Pi is increasing in delta; bisect."""
    def pi_or_inf(d: float) -> float:
        """Divergence IS the answer at delta >= alpha for a geometric lag, not an error."""
        try:
            return lag.pi(1.0 / (1.0 - d))
        except (OverflowError, RuntimeError):
            return math.inf

    lo, hi = 1e-12, 0.999
    if pi_or_inf(lo) > target_pi:
        return 0.0
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if pi_or_inf(mid) < target_pi:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def kendall_tau(xs) -> float:
    n, conc, disc = len(xs), 0, 0
    for i in range(n):
        for j in range(i + 1, n):
            if xs[i] < xs[j]:
                conc += 1
            elif xs[i] > xs[j]:
                disc += 1
    return (conc - disc) / (n * (n - 1) / 2)


# ======================================================================================
def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--events", default="data/pre-002-events.json")
    ap.add_argument("--json-out", default=None)
    args = ap.parse_args()

    blob = json.loads(pathlib.Path(args.events).read_text())
    lags, cens = [], []
    for uni in blob["universes"].values():
        for e in uni["events"]:
            lags.append(int(e["lag"]))
            cens.append(bool(e["censored"]))
    out: dict = {"n_events": len(lags)}

    DW = dweibull(Q_HAT, K_HAT)
    DW1 = DW.conditioned()
    EMP = empirical(lags, cens)
    mean_dw = DW.mean()
    GEO_SAME_MEAN = geometric(1.0 / mean_dw)

    print(f"\nWT-090 · REG-004 · the deferral measure under an age-dependent hazard")
    print(f"  events {len(lags)}  ·  min observed lag {min(lags)}q  ·  "
          f"max {max(lags)}q  ·  censored {sum(cens)}")
    print(f"  fitted discrete Weibull  q = {Q_HAT:.6f}  k = {K_HAT}  "
          f"E[T] = {mean_dw:.4f}q")
    print(f"  P(T=0) under the fit = {1.0 - DW.sur(1):.4f}  "
          f"-- mass at a lag the instrument cannot produce (REG-004 §3)")
    out["mean_lag_dw"] = mean_dw
    out["p_T0_dw"] = 1.0 - DW.sur(1)
    out["min_observed_lag"] = min(lags)

    # ---------------------------------------------------------------- §0 · units first
    print("\n§0 · THE DISCRETISATION, STATED BEFORE ANY CORRECTION IS QUOTED")
    disc = []
    for t in TIERS:
        d_a, phi = t["delta_a"], t["phi"]
        r_annual = (1 - phi) * d_a / (ALPHA_A_CAL - d_a)
        r_quarter = R_naive(q2a(ALPHA_A_CAL), q2a(d_a), phi)
        disc.append(abs(r_quarter - r_annual) / r_annual)
        print(f"  {t['name']:<36} R annual {r_annual:.4f}   "
              f"R quarterly {r_quarter:.4f}   gap {disc[-1]*100:5.2f}%")
    out["discretisation_max_pct"] = max(disc) * 100
    print(f"  worst period-change gap {max(disc)*100:.2f}% -- every correction below "
          f"is computed in quarters ON BOTH SIDES, so it is a shape effect and not this.")

    check("the geometric benchmark is not rigged: it has the fitted lag's own mean",
          abs(GEO_SAME_MEAN.mean() - mean_dw) < 1e-9,
          witness=lambda: abs(geometric(0.5).mean() - mean_dw) < 1e-9)

    check("the instrument's own support bound holds: no event has a lag of zero",
          min(lags) >= 1,
          witness=lambda: min(lags + [0]) >= 1)

    # -------------------------------------------------------------- §1 · F1 · nesting
    print("\n§1 · FALSIFIER F1 · the registered form must NEST the published one")
    worst_nest = 0.0
    for t in TIERS:
        for a_a in (0.05, 0.20, 0.408):
            d_q, a_q = q2a(t["delta_a"]), q2a(a_a)
            if d_q >= a_q:
                continue
            reg = R_registered(geometric(a_q), d_q, t["phi"])
            pub = R_naive(a_q, d_q, t["phi"])
            worst_nest = max(worst_nest, abs(reg - pub) / abs(pub))
    print(f"  worst relative departure over the ladder x three rates: {worst_nest:.3e}")
    out["F1_worst"] = worst_nest
    check("F1 · at a geometric lag the registered form reproduces (1-phi)d/(a-d)",
          worst_nest < NEST_TOL,
          witness=lambda: abs(R_registered(dweibull(Q_HAT, 1.6), q2a(0.03), 0.8)
                              - R_naive(1.0 / dweibull(Q_HAT, 1.6).mean(),
                                        q2a(0.03), 0.8))
          / R_naive(1.0 / dweibull(Q_HAT, 1.6).mean(), q2a(0.03), 0.8) < NEST_TOL)

    # ----------------------------------------------------------- §2 · F2/F3 · the sim
    print("\n§2 · FALSIFIER F2 · an age-structured simulation, no closed form in the loop")
    sim_rows, worst_sim, worst_naive_sim = [], 0.0, 0.0
    for t in TIERS:
        d_q, phi = q2a(t["delta_a"]), t["phi"]
        s = simulate_R(DW, d_q, phi)
        r = R_registered(DW, d_q, phi)
        n = R_naive(1.0 / mean_dw, d_q, phi)
        e_r = abs(s - r) / abs(r)
        e_n = abs(s - n) / abs(s) if math.isfinite(n) else math.inf
        worst_sim, worst_naive_sim = max(worst_sim, e_r), max(worst_naive_sim, e_n)
        sim_rows.append({"tier": t["name"], "sim": s, "registered": r,
                         "naive": n, "err_registered": e_r, "err_naive": e_n})
        print(f"  {t['name']:<36} sim {s:.6f}  registered {r:.6f}  "
              f"err {e_r:.2e}   |   naive {n:.6f}  err {e_n:.2e}")
    out["F2_worst"] = worst_sim
    out["F3_naive_worst"] = worst_naive_sim
    check("F2 · the simulation reproduces the registered closed form to §4.3's bound",
          worst_sim < SIM_TOL,
          witness=lambda: abs(simulate_R(DW, q2a(0.03), 0.8)
                              - R_registered(DW, q2a(0.03), 0.5))
          / R_registered(DW, q2a(0.03), 0.5) < SIM_TOL)
    def _geom_world_err() -> float:
        g = geometric(ALPHA_Q_HAT)
        d, p = q2a(0.010), 0.4
        return abs(simulate_R(g, d, p) - R_naive(ALPHA_Q_HAT, d, p)) / simulate_R(g, d, p)

    check("F3 · the same simulation REJECTS the naive substitution somewhere",
          worst_naive_sim > SIM_TOL,
          witness=lambda: _geom_world_err() > SIM_TOL)

    # ------------------------------------------------------------- §3 · F4 · phi scale
    print("\n§3 · FALSIFIER F4 · phi is a pure scale under age-dependence")
    d_q = q2a(0.030)
    r0 = R_registered(DW, d_q, 0.0)
    worst_phi = max(abs(R_registered(DW, d_q, p) / r0 - (1.0 - p))
                    for p in [i / 10 for i in range(11)])
    print(f"  worst |R(phi)/R(0) - (1-phi)| over phi in 0.0..1.0 : {worst_phi:.3e}")
    out["F4_worst"] = worst_phi
    check("F4 · R(phi)/R(0) = (1-phi) exactly, so §4.2's proportionality is untouched",
          worst_phi < NEST_TOL,
          witness=lambda: abs(R_registered(DW, d_q, 0.3) / r0
                              - (1.0 - 0.5)) < NEST_TOL)

    # --------------------------------------------------------------- §4 · ladder N/M/E
    print("\n§4 · LADDER N · the SIGN, against a geometric with the SAME MEAN")
    n_rows, all_below, any_below = [], True, False
    for t in TIERS:
        d_q, phi = q2a(t["delta_a"]), t["phi"]
        r_dw = R_registered(DW, d_q, phi)
        r_dw1 = R_registered(DW1, d_q, phi)
        r_ge = R_registered(geometric(1.0 / DW.mean()), d_q, phi)
        r_ge1 = R_registered(geometric(1.0 / DW1.mean()), d_q, phi)
        r_em = R_registered(EMP, d_q, phi)
        below = (r_dw < r_ge) and (r_dw1 < r_ge1)
        all_below &= below
        any_below |= below
        n_rows.append({"tier": t["name"], "R_dweibull": r_dw, "R_dweibull_T1": r_dw1,
                       "R_geom_same_mean": r_ge, "R_geom_same_mean_T1": r_ge1,
                       "R_empirical_lower_bound": r_em,
                       "ratio": r_dw / r_ge})
        print(f"  {t['name']:<36} DW {r_dw:.5f}  DW|T>=1 {r_dw1:.5f}  "
              f"geom(=mean) {r_ge:.5f}/{r_ge1:.5f}  "
              f"ratio {r_dw/r_ge:.4f}/{r_dw1/r_ge1:.4f}  emp>= {r_em:.5f}")
    ladder_N = "N1" if all_below else ("N3" if not any_below else "N2")
    out["ladder_N"], out["N_rows"] = ladder_N, n_rows
    print(f"  -> LADDER N = {ladder_N}"
          f"  ({'below at every swept delta' if ladder_N=='N1' else 'mixed / above'})")

    check("the T>=1 conditioning moves R UP, as REG-004 §3 registered in advance",
          all(r["R_dweibull_T1"] > r["R_dweibull"] for r in n_rows),
          witness=lambda: all(R_registered(DW, q2a(t["delta_a"]), t["phi"])
                              > R_registered(DW1, q2a(t["delta_a"]), t["phi"])
                              for t in TIERS))
    check("the truncated empirical transform is a LOWER bound, as registered",
          all(r["R_empirical_lower_bound"] <= r["R_dweibull_T1"] + 1e-12
              for r in n_rows),
          witness=lambda: all(r["R_dweibull_T1"] <= r["R_empirical_lower_bound"] + 1e-12
                              for r in n_rows))

    print("\n§4b · LADDER M · the MAGNITUDE, on the tabulated ladder §4.3 reports")
    m_ladder_rows, worst_m = [], 0.0
    for t in TIERS:
        d_q, phi = q2a(t["delta_a"]), t["phi"]
        r_dw = R_registered(DW1, d_q, phi)
        r_nv = R_naive(1.0 / DW1.mean(), d_q, phi)
        rel = abs(r_nv - r_dw) / r_dw
        worst_m = max(worst_m, rel)
        m_ladder_rows.append({"tier": t["name"], "registered": r_dw,
                              "naive": r_nv, "rel": rel})
        print(f"  {t['name']:<36} registered {r_dw:.5f}  naive {r_nv:.5f}  "
              f"naive overstates by {rel*100:6.2f}%")
    ladder_M = ("M1" if worst_m < 0.01 else "M2" if worst_m < 0.10
                else "M3" if worst_m < 0.50 else "M4")
    out["ladder_M_tabulated"], out["M_rows"] = ladder_M, m_ladder_rows
    out["M_worst_tabulated_pct"] = worst_m * 100
    print(f"  -> LADDER M (tabulated ladder) = {ladder_M}, worst {worst_m*100:.2f}%")

    print("\n§4c · LADDER M on the DISCLOSED RECTANGLE, which is where disclosure lives")
    alpha_nv = 1.0 / DW1.mean()
    d_break_a = a2q(alpha_nv)
    rect_lo = min(1.0 / RECT_PPE_LIVES[1], 1.0 / RECT_FLI_LIVES[1])
    rect_hi = max(1.0 / RECT_PPE_LIVES[0], 1.0 / RECT_FLI_LIVES[0])
    print(f"  disclosed decay rates span delta_a in [{rect_lo:.4f}, {rect_hi:.4f}] "
          f"(lives {1/rect_hi:.1f}..{1/rect_lo:.1f} years)")
    print(f"  the naive form's pole sits at delta_a = {d_break_a:.4f} "
          f"(life {1/d_break_a:.2f}y), OUTSIDE the rectangle, so the rectangle-wide")
    print(f"  maximum is a bounded number and not an artefact of approaching a pole.")
    grid = [rect_lo + (rect_hi - rect_lo) * i / 200 for i in range(201)]
    rect_rows = []
    for d_a in grid:
        d_q = q2a(d_a)
        r_dw = R_registered(DW1, d_q, 0.5)
        r_nv = R_naive(alpha_nv, d_q, 0.5)
        rect_rows.append((d_a, r_dw, r_nv, abs(r_nv - r_dw) / r_dw))
    worst_rect = max(r[3] for r in rect_rows)
    at = max(rect_rows, key=lambda r: r[3])
    ladder_M_rect = ("M1" if worst_rect < 0.01 else "M2" if worst_rect < 0.10
                     else "M3" if worst_rect < 0.50 else "M4")
    for d_a in (0.025, 0.05, 0.10, 0.20, 0.3333):
        d_q = q2a(d_a)
        r_dw, r_nv = R_registered(DW1, d_q, 0.5), R_naive(alpha_nv, d_q, 0.5)
        print(f"  life {1/d_a:5.1f}y  delta_a {d_a:.4f}   registered {r_dw:.5f}   "
              f"naive {r_nv:.5f}   naive overstates by {100*(r_nv-r_dw)/r_dw:7.2f}%")
    print(f"  -> LADDER M (disclosed rectangle) = {ladder_M_rect}, worst "
          f"{worst_rect*100:.2f}% at delta_a = {at[0]:.4f} (life {1/at[0]:.1f}y)")
    out["ladder_M_rectangle"] = ladder_M_rect
    out["M_worst_rect_pct"] = worst_rect * 100
    out["M_worst_rect_delta_a"] = at[0]
    out["naive_pole_delta_a"] = d_break_a
    out["rect_delta_a"] = [rect_lo, rect_hi]
    check("the naive pole lies outside the rectangle, so ladder M is not a pole artefact",
          d_break_a > rect_hi,
          witness=lambda: a2q(q2a(ALPHA_A_CAL)) > rect_hi)

    print("\n§4d · LADDER E · is alpha_eff flat enough to be a constant?")
    ae_lo = alpha_eff(DW1, q2a(rect_lo))
    ae_hi = alpha_eff(DW1, q2a(rect_hi))
    print(f"  read over the DISCLOSED RECTANGLE, as REG-004 §4 ladder E registers it:")
    for d_a in (rect_lo, 0.05, 0.10, 0.20, rect_hi):
        print(f"    life {1/d_a:5.1f}y  delta_a {d_a:.4f}  alpha_eff "
              f"{alpha_eff(DW1, q2a(d_a)):.6f}/q = {a2q(alpha_eff(DW1, q2a(d_a))):.4f}/yr")
    print(f"  and over §4.4's tabulated ladder, for comparison:")
    for t in TIERS:
        ae = alpha_eff(DW1, q2a(t["delta_a"]))
        print(f"  {t['name']:<36} alpha_eff {ae:.6f}/q = {a2q(ae):.4f}/yr")
    ratio_e = ae_hi / ae_lo
    ladder_E = "E1" if ratio_e < 1.05 else "E2" if ratio_e <= 1.50 else "E3"
    out["ladder_E"], out["E_ratio"] = ladder_E, ratio_e
    out["alpha_eff_yr_range"] = [a2q(ae_lo), a2q(ae_hi)]
    print(f"  -> LADDER E = {ladder_E}, top/bottom ratio {ratio_e:.4f}; "
          f"alpha_eff runs {a2q(ae_lo):.4f} .. {a2q(ae_hi):.4f} per year "
          f"against the measured alpha-hat {a2q(ALPHA_Q_HAT):.4f}")
    check("alpha_eff is a FUNCTION of delta and not a parameter (REG-004 §3)",
          ratio_e > 1.0 + 1e-9,
          witness=lambda: alpha_eff(geometric(ALPHA_Q_HAT), q2a(0.030))
          / alpha_eff(geometric(ALPHA_Q_HAT), q2a(0.002)) > 1.0 + 1e-9)

    # ------------------------------------------------------------------ §5 · ladder D
    print("\n§5 · LADDER D · the existence condition")
    d_ok = True
    for d_a in [0.002, 0.01, 0.03, 0.10, 0.20, 0.3333, 0.50, 0.80]:
        try:
            v = DW1.pi(1.0 / (1.0 - q2a(d_a)))
            print(f"  delta_a {d_a:<7.4f} -> Pi = {v:.6f}   (finite)")
        except RuntimeError as exc:
            d_ok = False
            print(f"  delta_a {d_a:<7.4f} -> {exc}")
    ladder_D = "D1" if d_ok else "D3"
    out["ladder_D"] = ladder_D
    print(f"  -> LADDER D = {ladder_D}")
    print(f"  the geometric's radius of convergence is 1/(1-alpha), so it caps delta at "
          f"alpha; the fitted Weibull's survival q^(a^k) with k>1 beats every z^a, so "
          f"its generating function is entire and the condition has no analogue.")
    check("D · the constant-hazard condition alpha>delta genuinely binds the geometric",
          math.isinf(R_naive(ALPHA_Q_HAT, q2a(0.60), 0.5)),
          witness=lambda: math.isinf(R_naive(ALPHA_Q_HAT, q2a(0.3333), 0.5)))
    def _finite_R(lag, d_a) -> bool:
        try:
            v = R_registered(lag, q2a(d_a), 0.5)
        except (RuntimeError, OverflowError):
            return False
        return math.isfinite(v)

    check("D · and the registered form is finite at the very delta that kills it",
          _finite_R(DW1, 0.60),
          witness=lambda: _finite_R(geometric(ALPHA_Q_HAT), 0.60))

    # ------------------------------------------------------------------ §6 · ladder C
    print("\n§6 · LADDER C · does §4.4's tabulated reversal survive the shape correction?")
    c_out = {}
    for label, lag in (("constant hazard (published)", geometric(ALPHA_Q_HAT)),
                       ("measured shape (DW | T>=1)", DW1)):
        Rs = [R_registered(lag, q2a(t["delta_a"]), t["phi"]) for t in TIERS]
        tau = kendall_tau(Rs)
        R2 = Rs[2]
        K = R2 / (1.0 - TIERS[3]["phi"])
        d3q = solve_delta_star(lag, 1.0 + K)
        d3a = a2q(d3q)
        c_out[label] = {"R": Rs, "tau": tau, "K": K, "delta3_star_a": d3a,
                        "margin_vs_tabulated": d3a / TIERS[3]["delta_a"]}
        print(f"  {label:<28} tau {tau:+.2f}   K {K:.5f}   "
              f"delta3* = {d3a:.5f}/yr (life {1/d3a:.1f}y)   "
              f"tabulated goodwill 0.00200 sits {d3a/0.002:.2f}x below it")
        print(f"      R by tier: " + "  ".join(f"{r:.5f}" for r in Rs))
    d3a_meas = c_out["measured shape (DW | T>=1)"]["delta3_star_a"]
    tau_meas = c_out["measured shape (DW | T>=1)"]["tau"]
    ladder_C = ("C3" if d3a_meas <= TIERS[3]["delta_a"]
                else "C1" if abs(tau_meas + 1.0) < 1e-9 else "C2")
    out["ladder_C"], out["C_detail"] = ladder_C, c_out
    print(f"  published crossing (annual, constant hazard, §4.4) = "
          f"{DELTA3_STAR_PUBLISHED}")
    print(f"  -> LADDER C = {ladder_C}")
    check("C · the crossing solver reproduces §4.4's published 0.00789 at alpha=0.05",
          abs(a2q(solve_delta_star(geometric(q2a(ALPHA_A_CAL)),
                                   1.0 + (R_registered(geometric(q2a(ALPHA_A_CAL)),
                                                       q2a(TIERS[2]["delta_a"]),
                                                       TIERS[2]["phi"])
                                          / (1.0 - TIERS[3]["phi"]))))
              - DELTA3_STAR_PUBLISHED) < 5e-4,
          witness=lambda: abs(a2q(solve_delta_star(geometric(q2a(ALPHA_A_CAL)), 2.0))
                              - DELTA3_STAR_PUBLISHED) < 5e-4)

    # ------------------------------------------------------------------ §7 · ladder S
    print("\n§7 · LADDER S · was §4.2's two-root exchange leaning on the constant hazard?")
    d_q, phi = q2a(TIERS[0]["delta_a"]), TIERS[0]["phi"]
    ae = alpha_eff(DW1, d_q)

    def series_age(lag: Lag, delta: float, ph: float, n: int = 120) -> list[float]:
        """Reported book value C(t) = E(t) + gap(t), age-structured, no closed form."""
        E, cohorts, out_ = 1.0, [], []
        for _ in range(n):
            aged = []
            for i, amt in enumerate(cohorts):
                a = i + 1
                s_a, s_a1 = lag.sur(a), lag.sur(a + 1)
                aged.append(amt * (s_a1 / s_a) if s_a > 0 else 0.0)
            born = (1.0 - ph) * delta * E * lag.sur(1)
            cohorts = [born] + aged
            E *= (1.0 - delta)
            out_.append(E + sum(cohorts))
        return out_

    def rel_dev(x, y):
        return max(abs(a - b) / max(abs(a), 1e-300) for a, b in zip(x, y))

    base = series_age(DW1, d_q, phi)
    same_world_geom = series_age(geometric(ae), d_q, phi)       # the witness / baseline
    mirror = series_age(geometric(d_q), ae, phi * d_q / ae)     # the registered swap
    d0, d1 = rel_dev(base, same_world_geom), rel_dev(base, mirror)
    print(f"  baseline · age-dependent vs its OWN constant-hazard match at alpha_eff: "
          f"{d0:.4e}")
    print(f"  the registered swap (alpha_eff,delta,phi) -> (delta,alpha_eff,phi d/a): "
          f"{d1:.4e}")
    print(f"  ratio {d1/d0 if d0>0 else float('inf'):.3f}  "
          f"-- the swap adds this much on top of the shape approximation")
    ladder_S = ("S1" if d1 < 1e-12 else "S2" if d1 <= 3.0 * d0 else "S3")
    out["ladder_S"], out["S_d0"], out["S_d1"] = ladder_S, d0, d1
    print(f"  -> LADDER S = {ladder_S}")
    check("S · the baseline is not vacuous: a constant-hazard world DOES mirror exactly",
          rel_dev(series_age(geometric(ae), d_q, phi),
                  series_age(geometric(d_q), ae, phi * d_q / ae)) < 1e-9,
          witness=lambda: rel_dev(series_age(geometric(ae), d_q, phi),
                                  series_age(geometric(d_q), ae, phi)) < 1e-9)

    print()
    if args.json_out:
        pathlib.Path(args.json_out).write_text(json.dumps(out, indent=2))
    summary()          # raises SystemExit(1) itself if anything failed or was vacuous
    return 0


if __name__ == "__main__":
    sys.exit(main())
