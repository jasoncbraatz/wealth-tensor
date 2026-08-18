#!/usr/bin/env python3
"""WT-089 · REG-003 · the recognition rate α, and the off-diagonal.

Run exactly as registered in `docs/preregistration/REG-003-p3-recognition-rate-and-
off-diagonal.md`, committed and pushed before this file existed.

    python3 scripts/wt089_recognition_and_offdiagonal.py --events events.json \
        --riskset riskset.json

Nothing here decides anything. Every threshold, null, seed, unit conversion and
regime boundary comes from REG-003. The four α-regimes are exhaustive: there is no
outcome for which this script returns nothing, and no pair of outcomes it cannot
tell apart. That was the point of registering a ladder instead of a threshold.

NOTE ON ORDER (the trap `-14` paid two round trips for, twice): `severity.check()`
EXECUTES its witness immediately, so a witness touching a helper defined later in
the file raises NameError mid-run. Every helper below is defined ABOVE the first
check that uses it. All of §1.
"""
from __future__ import annotations

import argparse
import json
import math
import pathlib
import random
import statistics
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from severity import check, summary  # noqa: E402

SEED = 20260812                 # REG-003 §4.2
N_PERM = 10_000                 # REG-003 §4.2
POWER_TRIALS = 400              # REG-003 §4.4
TIER_NAMES = {0: "PP&E", 1: "finite-lived intangible",
              2: "indefinite-lived intangible", 3: "goodwill"}

# RESULT-002's table, for REG-003 §2's reconciliation. Typed from the committed file.
RESULT_002 = {
    "pilot": {"n": 244, "firms": 121, "tiers": {0: 21, 1: 34, 2: 34, 3: 155}},
    "replication": {"n": 444, "firms": 190, "tiers": {0: 34, 1: 102, 2: 46, 3: 262}},
}

# ======================================================================================
# §1 · EVERY HELPER, DEFINED BEFORE THE FIRST CHECK THAT TOUCHES ONE
# ======================================================================================


def geom_mle(lags: list[int], censored: list[bool]) -> tuple[float, float, int, int]:
    """Censored geometric MLE.  REG-003 §3.1 A1:  α̂ = d / (d + S).

    P(T = t) = α(1-α)^t on t = 0,1,2,...; a right-censored observation contributes
    (1-α)^c.  S is the exposure -- the sum of observed lags over ALL events, censored
    or not.  Returns (α̂, se, d, S).
    """
    d = sum(1 for c in censored if not c)
    S = sum(lags)
    if d == 0:
        return float("nan"), float("nan"), 0, S      # REG-003 §3.3: UNDEFINED, never a number
    a = d / (d + S)
    if a <= 0.0 or a >= 1.0:
        return a, float("nan"), d, S
    info = d / a**2 + S / (1.0 - a) ** 2
    return a, info ** -0.5, d, S


def annualise(a_q: float) -> float:
    """Quarterly hazard -> annual.  REG-003 §3.1, fixed there so it cannot be chosen later."""
    return 1.0 - (1.0 - a_q) ** 4


def regime(a_yr: float) -> tuple[str, str]:
    """REG-003 §3.2's exhaustive ladder. Every real number lands in exactly one cell."""
    if a_yr >= 0.33:
        return "R1", "entire disclosed rectangle inside the domain"
    if a_yr >= 0.19:
        return "R2", "at least half the rectangle admissible"
    if a_yr > 0.05:
        return "R3", "less than half admissible; the calibration is too low"
    return "R4", "the calibration stands; §4.4's domain sentence stands as written"


def dweibull_nll(q: float, k: float, lags: list[int], censored: list[bool]) -> float:
    """Nakagawa-Osaki discrete Weibull:  P(T > t) = q^((t+1)^k).  k = 1 is geometric."""
    if not (0.0 < q < 1.0) or k <= 0.0:
        return float("inf")
    nll = 0.0
    for t, c in zip(lags, censored):
        if c:
            nll -= (t ** k) * math.log(q) if t > 0 else 0.0        # P(T >= t) = q^(t^k)
        else:
            p = q ** (t ** k) - q ** ((t + 1) ** k)
            if p <= 0.0:
                return float("inf")
            nll -= math.log(p)
    return nll


def fit_q_given_k(k: float, lags, censored, lo=1e-6, hi=1 - 1e-9) -> tuple[float, float]:
    """Golden-section on q for fixed k. Deterministic; no scipy, so the run is reproducible."""
    gr = (math.sqrt(5.0) - 1.0) / 2.0
    a, b = lo, hi
    c, d = b - gr * (b - a), a + gr * (b - a)
    fc, fd = dweibull_nll(c, k, lags, censored), dweibull_nll(d, k, lags, censored)
    for _ in range(200):
        if fc < fd:
            b, d, fd = d, c, fc
            c = b - gr * (b - a)
            fc = dweibull_nll(c, k, lags, censored)
        else:
            a, c, fc = c, d, fd
            d = a + gr * (b - a)
            fd = dweibull_nll(d, k, lags, censored)
        if abs(b - a) < 1e-10:
            break
    q = (a + b) / 2.0
    return q, dweibull_nll(q, k, lags, censored)


def fit_dweibull(lags, censored, kgrid=None) -> dict:
    """Profile over k. Returns k̂, q̂ and the 95% profile-likelihood interval on k."""
    kgrid = kgrid or [0.20 + 0.005 * i for i in range(0, 561)]      # 0.20 .. 3.00
    prof = [(k,) + fit_q_given_k(k, lags, censored) for k in kgrid]
    kbest, qbest, nbest = min(prof, key=lambda r: r[2])
    inside = [k for k, _q, n in prof if 2.0 * (n - nbest) <= 3.841]
    return {"k": kbest, "q": qbest, "nll": nbest,
            "k_ci": [min(inside), max(inside)] if inside else [float("nan")] * 2,
            "k_ci_excludes_1": bool(inside) and not (min(inside) <= 1.0 <= max(inside))}


def np_hazard(lags, censored, tmax: int = 20) -> list[dict]:
    """Non-parametric discrete hazard h_t = d_t / n_t, reported beside the fitted one."""
    out = []
    for t in range(tmax):
        at_risk = sum(1 for L, c in zip(lags, censored) if L > t or (L == t and not c))
        deaths = sum(1 for L, c in zip(lags, censored) if L == t and not c)
        out.append({"t": t, "n_risk": at_risk, "d": deaths,
                    "h": (deaths / at_risk) if at_risk else float("nan")})
    return out


def fq_tiers(events: list[dict]) -> dict[tuple[str, int], set]:
    """(cik, charge quarter) -> set of distinct tiers. REG-003 §4.1's unit."""
    fq: dict[tuple[str, int], set] = {}
    for e in events:
        fq.setdefault((e["cik"], e["q_star"]), set()).add(e["tier"])
    return fq


def co_stats(fq: dict) -> tuple[int, dict]:
    """N_co and the six off-diagonal cells. COUNTS, never shares (REG-003 §4.1)."""
    n_co = sum(1 for s in fq.values() if len(s) >= 2)
    M = {p: 0 for p in ((0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3))}
    for s in fq.values():
        for p in M:
            if p[0] in s and p[1] in s:
                M[p] += 1
    return n_co, M


def marginals(events: list[dict]) -> dict[str, dict[int, int]]:
    """n(f,t): distinct quarters in which firm f records a tier-t event."""
    m: dict[str, dict[int, set]] = {}
    for e in events:
        m.setdefault(e["cik"], {}).setdefault(e["tier"], set()).add(e["q_star"])
    return {f: {t: len(qs) for t, qs in d.items()} for f, d in m.items()}


def null_draw(marg: dict, risk: dict, rng: random.Random) -> dict:
    """One draw of REG-003 §4.2's null: each tier's quarters redrawn independently
    from that firm's eligible-quarter set, marginals held exactly."""
    fq: dict[tuple[str, int], set] = {}
    for f, tiers in marg.items():
        Q = risk.get(f) or []
        for t, n in tiers.items():
            if n > len(Q):                    # risk set smaller than observed: keep observed n
                picks = Q
            else:
                picks = rng.sample(Q, n) if Q else []
            for q in picks:
                fq.setdefault((f, q), set()).add(t)
    return fq


def two_sided_p(observed: float, draws: list[float]) -> float:
    """Empirical two-sided p. REG-003 §4.3 is two-sided on purpose: a one-sided test
    cannot separate independence from ANTI-co-occurrence."""
    n = len(draws)
    hi = sum(1 for d in draws if d >= observed)
    lo = sum(1 for d in draws if d <= observed)
    return min(1.0, 2.0 * min(hi + 1, lo + 1) / (n + 1))


def holm(pairs: list[tuple]) -> list[tuple]:
    """Holm across the six pairwise cells (REG-003 §4.3, secondary and labelled so)."""
    s = sorted(pairs, key=lambda r: r[1])
    m = len(s)
    out, run = [], 0.0
    for i, (lab, p) in enumerate(s):
        run = max(run, min(1.0, (m - i) * p))
        out.append((lab, p, run))
    return out


def boot_ci_clustered(vals_by_firm: dict, stat, n_boot: int = 2000,
                      seed: int = SEED) -> tuple[float, float]:
    """Firm-clustered bootstrap. Events within a firm are not independent (§9's own
    second limitation), so the resample is over FIRMS."""
    rng = random.Random(seed)
    firms = list(vals_by_firm)
    if not firms:
        return float("nan"), float("nan")
    out = []
    for _ in range(n_boot):
        pool = []
        for _ in range(len(firms)):
            pool.extend(vals_by_firm[rng.choice(firms)])
        if pool:
            out.append(stat(pool))
    out.sort()
    if not out:
        return float("nan"), float("nan")
    return out[int(0.025 * len(out))], out[int(0.975 * len(out))]


def inject_cooccurrence(events: list[dict], pi: float, rng: random.Random) -> list[dict]:
    """REG-003 §4.4's power injection: with probability pi, MOVE a tier's quarter onto
    another tier's quarter in the same firm. A move preserves n(f,t) exactly, so the
    null distribution is unchanged and one null serves every power trial."""
    by_firm: dict[str, list[dict]] = {}
    for e in events:
        by_firm.setdefault(e["cik"], []).append(dict(e))
    out = []
    for f, evs in by_firm.items():
        qs_by_tier: dict[int, set] = {}
        for e in evs:
            qs_by_tier.setdefault(e["tier"], set()).add(e["q_star"])
        for e in evs:
            if rng.random() < pi:
                targets = [q for t, qs in qs_by_tier.items() if t != e["tier"]
                           for q in qs if q not in qs_by_tier.get(e["tier"], set())]
                if targets:
                    old = e["q_star"]
                    new = rng.choice(targets)
                    qs_by_tier[e["tier"]].discard(old)
                    qs_by_tier[e["tier"]].add(new)
                    e["q_star"] = new
            out.append(e)
    return out


def _inject_by_adding(events: list[dict], rng: random.Random) -> list[dict]:
    """The WRONG injection, kept because it is the witness for the right one.

    Adding a co-occurring event instead of moving one raises n(f,t), which changes
    the null distribution — so a power figure computed against a null built from the
    *observed* marginals would be measuring the wrong null. Never called in a result;
    exists so that `inject_cooccurrence`'s marginal-preservation can go red.
    """
    out = [dict(e) for e in events]
    for e in list(out):
        for f in [e]:
            partner = next((x for x in out if x["cik"] == f["cik"]
                            and x["tier"] != f["tier"]), None)
            if partner is not None:
                out.append({**f, "q_star": partner["q_star"]})
                return out
    return out


def fmt_p(p: float) -> str:
    return f"{p:.4f}" if p >= 1e-4 else "<0.0001"


# ======================================================================================
# §2 · THE HELPERS ARE PROVEN BEFORE THEY CARRY A RESULT
# ======================================================================================

def prove_helpers() -> None:
    rng = random.Random(1)

    def synth(alpha: float, n: int = 4000, cap: int = 20):
        lags, cens = [], []
        for _ in range(n):
            t = 0
            while rng.random() > alpha and t < cap:
                t += 1
            lags.append(t)
            cens.append(t >= cap)
        return lags, cens

    L2, C2 = synth(0.20)
    L5, C5 = synth(0.50)
    a2 = geom_mle(L2, C2)[0]
    check("the censored geometric MLE recovers a rate it was not told",
          abs(a2 - 0.20) < 0.02,
          witness=lambda: abs(geom_mle(L5, C5)[0] - 0.20) < 0.02)

    check("censored observations contribute exposure, so ignoring them raises the rate",
          geom_mle([1, 2, 3, 20], [False, False, False, True])[0]
          < geom_mle([1, 2, 3], [False, False, False])[0],
          witness=lambda: geom_mle([1, 2, 3], [False, False, False])[0]
          < geom_mle([1, 2, 3], [False, False, False])[0])

    check("annualisation strictly raises a positive quarterly hazard",
          annualise(0.13) > 0.13,
          witness=lambda: annualise(0.0) > 0.0)

    check("the four α-regimes are exhaustive and ordered",
          [regime(x)[0] for x in (0.9, 0.33, 0.25, 0.19, 0.10, 0.05, 0.0)]
          == ["R1", "R1", "R2", "R2", "R3", "R4", "R4"],
          witness=lambda: [regime(x)[0] for x in (0.9, 0.0)] == ["R4", "R1"])

    fit1 = fit_dweibull(L2, C2, kgrid=[1.0])
    check("the discrete Weibull nests the geometric at k = 1",
          abs((1.0 - fit1["q"]) - a2) < 0.01,
          witness=lambda: abs((1.0 - fit_q_given_k(2.0, L2, C2)[0]) - a2) < 0.01)

    ev_flat = [{"cik": "A", "q_star": 10, "tier": 0}, {"cik": "A", "q_star": 12, "tier": 3},
               {"cik": "B", "q_star": 8, "tier": 1}, {"cik": "B", "q_star": 9, "tier": 3}]
    ev_stack = [{"cik": "A", "q_star": 10, "tier": 0}, {"cik": "A", "q_star": 10, "tier": 3},
                {"cik": "B", "q_star": 8, "tier": 1}, {"cik": "B", "q_star": 8, "tier": 3}]
    check("N_co counts stacked firm-quarters and not spread ones",
          co_stats(fq_tiers(ev_stack))[0] == 2 and co_stats(fq_tiers(ev_flat))[0] == 0,
          witness=lambda: co_stats(fq_tiers(ev_flat))[0] == 2)

    marg = marginals(ev_stack)
    risk = {"A": list(range(5, 25)), "B": list(range(5, 25))}
    draw = null_draw(marg, risk, random.Random(7))
    drawn = {}
    for (f, _q), ts in draw.items():
        for t in ts:
            drawn[(f, t)] = drawn.get((f, t), 0) + 1
    check("the null preserves every per-firm, per-tier marginal exactly",
          all(drawn.get((f, t), 0) == n for f, d in marg.items() for t, n in d.items()),
          witness=lambda: all(drawn.get((f, t), 0) == n + 1
                              for f, d in marg.items() for t, n in d.items()))

    # The witness here must be a world where marginals genuinely CHANGE. ev_flat and
    # ev_stack have identical marginals -- they differ only in which quarters the events
    # sit on, which is the whole point of the null -- so comparing against ev_stack was a
    # phantom tag, and the harness caught it in 0.16s before it carried a power figure.
    inj = inject_cooccurrence(ev_flat, 1.0, random.Random(3))
    mi = marginals(inj)
    bad = marginals(_inject_by_adding(ev_flat, random.Random(3)))
    check("the power injection MOVES rather than adds, so the null is unchanged by it",
          mi == marginals(ev_flat),
          witness=lambda: bad == marginals(ev_flat))
    check("moving preserves the event count; the adding witness really does differ",
          len(inj) == len(ev_flat) and bad != marginals(ev_flat),
          witness=lambda: len(_inject_by_adding(ev_flat, random.Random(3))) == len(ev_flat))

    check("a fully censored cell returns UNDEFINED rather than a number",
          math.isnan(geom_mle([20, 20], [True, True])[0]),
          witness=lambda: math.isnan(geom_mle([2, 3], [False, False])[0]))


# ======================================================================================
# §3 · RECONCILIATION  (REG-003 §2, branch chosen by a count no statistic touches)
# ======================================================================================

def reconcile(payload: dict) -> str:
    print("\n" + "=" * 86)
    print("§2 · RECONCILIATION AGAINST RESULT-002 — the branch, before any statistic")
    print("=" * 86)
    total_new = total_old = 0
    worst_tier = 0.0
    for lab in ("pilot", "replication"):
        u = payload["universes"][lab]
        ev = u["events"]
        old = RESULT_002[lab]
        firms = len({e["cik"] for e in ev})
        cens = sum(1 for e in ev if e["censored"]) / len(ev) if ev else float("nan")
        print(f"\n  {lab}: SIC {u['sic'][0]}-{u['sic'][1]} · "
              f"{u['n_registrants']} registrants · {u['n_firms_fetched']} fetched")
        print(f"    {'':<34}{'RESULT-002':>12}{'rebuilt':>12}{'Δ%':>10}")
        print(f"    {'events':<34}{old['n']:>12}{len(ev):>12}"
              f"{100*(len(ev)-old['n'])/old['n']:>+9.1f}%")
        print(f"    {'firms':<34}{old['firms']:>12}{firms:>12}"
              f"{100*(firms-old['firms'])/old['firms']:>+9.1f}%")
        for t in (0, 1, 2, 3):
            n = sum(1 for e in ev if e["tier"] == t)
            o = old["tiers"][t]
            worst_tier = max(worst_tier, abs(n - o) / o)
            print(f"    {'tier ' + str(t) + ' · ' + TIER_NAMES[t]:<34}{o:>12}{n:>12}"
                  f"{100*(n-o)/o:>+9.1f}%")
        print(f"    {'censored share':<34}{'':>12}{cens:>11.1%}")
        total_new += len(ev)
        total_old += old["n"]
    agree = 1.0 - abs(total_new - total_old) / total_old
    print(f"\n  TOTAL  RESULT-002 {total_old} · rebuilt {total_new} "
          f"· agreement {agree:.1%} · worst tier drift {worst_tier:.1%}")
    if total_new < 200:
        branch = "NOT RUN"
    elif agree >= 0.95 and worst_tier <= 0.20:
        branch = "REGISTERED SAMPLE"
    else:
        branch = "NEW SAMPLE (2026-08 pull)"
    print(f"  REG-003 §2 BRANCH: {branch}")
    if branch == "NEW SAMPLE (2026-08 pull)":
        print("    → every result below is a 2026-08 pull, NOT 'the 688 events'.")
    return branch


# ======================================================================================
# §4 · INSTRUMENT A — the recognition rate
# ======================================================================================

def instrument_a(events_by_universe: dict) -> dict:
    print("\n" + "=" * 86)
    print("§3 · INSTRUMENT A — THE RECOGNITION RATE α")
    print("=" * 86)
    pooled = [e for ev in events_by_universe.values() for e in ev]
    out = {}

    def one(label: str, ev: list[dict]) -> dict:
        lags = [e["lag"] for e in ev]
        cens = [bool(e["censored"]) for e in ev]
        a, se, d, S = geom_mle(lags, cens)
        if math.isnan(a):
            print(f"  {label:<46}  UNDEFINED (d = 0)")
            return {"label": label, "n": len(ev), "undefined": True}
        ay = annualise(a)
        lo, hi = annualise(max(a - 1.96 * se, 0.0)), annualise(min(a + 1.96 * se, 1.0))
        r, meaning = regime(ay)
        print(f"  {label:<46}  n={len(ev):>4} d={d:>4}  α̂_q={a:.4f}±{se:.4f}"
              f"   α̂_yr={ay:.4f} [{lo:.4f}, {hi:.4f}]   {r}")
        return {"label": label, "n": len(ev), "d": d, "S": S, "alpha_q": a, "se_q": se,
                "alpha_yr": ay, "ci_yr": [lo, hi], "regime": r, "meaning": meaning}

    print("\n  A1 · censored geometric MLE  (REG-003 §3.1)")
    for lab, ev in events_by_universe.items():
        out[lab] = one(lab, ev)
    out["pooled"] = one("POOLED (both universes)", pooled)

    print("\n  A3 · the sensitivities PRE-002 registered, run again unchanged")
    sens = {
        "annual-attributed charges excluded":
            [e for e in pooled if not e.get("annual_attributed")],
        "right-censored events excluded": [e for e in pooled if not e["censored"]],
        "one event per firm (largest charge)": list(
            {e["cik"]: e for e in sorted(pooled, key=lambda x: x["severity"])}.values()),
    }
    out["sensitivities"] = {k: one("  · " + k, v) for k, v in sens.items()}

    print("\n  A2 · the SHAPE, fitted and not assumed  (WT-080)")
    lags = [e["lag"] for e in pooled]
    cens = [bool(e["censored"]) for e in pooled]
    fit = fit_dweibull(lags, cens)
    print(f"    discrete Weibull  k̂ = {fit['k']:.3f}  "
          f"95% profile CI [{fit['k_ci'][0]:.3f}, {fit['k_ci'][1]:.3f}]  "
          f"q̂ = {fit['q']:.4f}")
    print(f"    constant hazard (k = 1) is "
          f"{'REJECTED — α is not a scalar over this window' if fit['k_ci_excludes_1'] else 'NOT rejected'}")
    out["weibull"] = fit

    print("\n    non-parametric hazard by quarter (h_t = d_t / n_t):")
    hz = np_hazard(lags, cens)
    out["hazard"] = hz
    print("      " + "  ".join(f"t{h['t']}={h['h']:.3f}" for h in hz[:10]))
    print("      " + "  ".join(f"t{h['t']}={h['h']:.3f}" for h in hz[10:]))

    p = out["pooled"]
    print(f"\n  REG-003 §3.2 VERDICT: α̂_yr = {p['alpha_yr']:.4f} → "
          f"{p['regime']} — {p['meaning']}")
    if p["regime"] in ("R1", "R2"):
        print("  REG-003 §3.3 REQUIRES THIS SENTENCE HERE, NOT IN A LIMITATIONS SECTION:")
        print("    Both known biases — conditioning on a charge occurring, and PRE-002's")
        print("    revenue-peak onset — push α̂ UP. This estimate is exactly what two")
        print("    upward biases would manufacture, and is weak evidence for its regime.")
    else:
        print("  REG-003 §3.3: both known biases push α̂ UP, and it landed here anyway.")
        print("    The two biases were working against this finding; it survives them.")
    return out


# ======================================================================================
# §5 · INSTRUMENT B — the off-diagonal
# ======================================================================================

def instrument_b(events_by_universe: dict, risk: dict) -> dict:
    print("\n" + "=" * 86)
    print("§4 · INSTRUMENT B — THE OFF-DIAGONAL")
    print("=" * 86)
    out = {}
    multi_firms = 0
    for ev in events_by_universe.values():
        m = marginals(ev)
        multi_firms += sum(1 for d in m.values() if len(d) >= 2)
    print(f"\n  PRECONDITION (REG-003 §4.4): {multi_firms} firms record two or more "
          f"distinct tiers")
    if multi_firms < 20:
        print("    → INCONCLUSIVE — NO POWER. Reported as such, never as 'independence holds'.")
        return {"precondition": "FAILED", "multi_tier_firms": multi_firms}
    print("    → met (≥ 20). The null has something to reject.")
    out["multi_tier_firms"] = multi_firms

    for lab, ev in events_by_universe.items():
        marg = marginals(ev)
        obs_fq = fq_tiers(ev)
        n_obs, M_obs = co_stats(obs_fq)
        rng = random.Random(SEED)
        draws, Md = [], {p: [] for p in M_obs}
        for _ in range(N_PERM):
            fq = null_draw(marg, risk, rng)
            n, M = co_stats(fq)
            draws.append(n)
            for p in M_obs:
                Md[p].append(M[p])
        draws_s = sorted(draws)
        lo, hi = draws_s[int(0.025 * N_PERM)], draws_s[int(0.975 * N_PERM)]
        mean = statistics.fmean(draws)
        p_two = two_sided_p(n_obs, draws)
        direction = ("ABOVE" if n_obs > hi else "BELOW" if n_obs < lo else "INSIDE")
        print(f"\n  {lab}: {len(obs_fq)} firm-quarters · "
              f"N_co observed = {n_obs}")
        print(f"    null mean {mean:.1f} · central 95% [{lo}, {hi}] · "
              f"two-sided p = {fmt_p(p_two)} · {direction}")
        if mean > 0:
            print(f"    observed / expected = {n_obs / mean:.2f}×")

        cells = []
        for pr in sorted(M_obs):
            em = statistics.fmean(Md[pr])
            cells.append((f"{TIER_NAMES[pr[0]]} × {TIER_NAMES[pr[1]]}",
                          two_sided_p(M_obs[pr], Md[pr]), M_obs[pr], em))
        adj = holm([(c[0], c[1]) for c in cells])
        byname = {c[0]: c for c in cells}
        print(f"    secondary — the six off-diagonal cells (Holm-corrected, DESCRIPTIVE):")
        print(f"      {'pair':<52}{'obs':>5}{'exp':>8}{'o/e':>7}{'p_holm':>9}")
        for name, _p, ph in adj:
            _n, _pp, o, e = byname[name]
            print(f"      {name:<52}{o:>5}{e:>8.1f}"
                  f"{(o/e if e else float('nan')):>7.2f}{ph:>9.4f}")
        out[lab] = {"n_fq": len(obs_fq), "n_co": n_obs, "null_mean": mean,
                    "ci": [lo, hi], "p_two_sided": p_two, "direction": direction,
                    "cells": [{"pair": c[0], "p": c[1], "obs": c[2], "exp": c[3]}
                              for c in cells],
                    "holm": [{"pair": a, "p": b, "p_holm": c} for a, b, c in adj]}

        print(f"    POWER (REG-003 §4.4 — reported whether or not the primary rejects).")
        print("      The injection MOVES quarters within a firm, so marginals and therefore")
        print("      the null distribution are unchanged; one null serves every trial.")
        prng = random.Random(SEED + 1)
        pw = {}
        for pi in (0.05, 0.10, 0.20, 0.40):
            hits = 0
            for _ in range(POWER_TRIALS):
                inj = inject_cooccurrence(ev, pi, prng)
                if co_stats(fq_tiers(inj))[0] > hi:
                    hits += 1
            pw[pi] = hits / POWER_TRIALS
            print(f"      π = {pi:.2f} → power {pw[pi]:.2f}")
        out[lab]["power"] = pw
        if direction == "INSIDE" and pw[0.20] < 0.80:
            print("      → NOT DETECTED AT THIS POWER. The paper says that, not 'independent'.")

    dirs = [out[l]["direction"] for l in events_by_universe if l in out]
    if len(set(dirs)) > 1 and "INSIDE" not in dirs:
        print("\n  REG-003 §4.3: the two universes DISAGREE IN DIRECTION. "
              "Reported as a failure to replicate; neither direction claimed.")
    out["verdict"] = dirs
    return out


# ======================================================================================
# §6 · COMPANION C — descriptive, no falsifier, no claim
# ======================================================================================

def companion_c(events_by_universe: dict) -> dict:
    print("\n" + "=" * 86)
    print("§5 · COMPANION C — severity dispersion by class  (DESCRIPTIVE; REG-003 §5)")
    print("=" * 86)
    print("  Registered with no falsifier and no threshold. Nothing here may be cited as")
    print("  support for §4.7. Returns volatility and disclosed lives are NOT in this")
    print("  sample; a proxy sharing σ's name and not its meaning is the WT-038 error.")
    pooled = [e for ev in events_by_universe.values() for e in ev]
    out = {}
    print(f"\n  {'class':<34}{'n':>5}{'median':>10}{'IQR':>18}{'sd log s':>10}{'95% CI (firm-clustered)':>28}")
    for t in (0, 1, 2, 3):
        sev = [e["severity"] for e in pooled if e["tier"] == t]
        if len(sev) < 2:
            continue
        by_firm: dict[str, list[float]] = {}
        for e in pooled:
            if e["tier"] == t:
                by_firm.setdefault(e["cik"], []).append(math.log(e["severity"]))
        sd = statistics.pstdev([math.log(s) for s in sev])
        lo, hi = boot_ci_clustered(by_firm, lambda p: statistics.pstdev(p))
        q = sorted(sev)
        iqr = (q[len(q) // 4], q[(3 * len(q)) // 4])
        print(f"  {TIER_NAMES[t]:<34}{len(sev):>5}{statistics.median(sev):>10.4f}"
              f"{f'{iqr[0]:.4f}-{iqr[1]:.4f}':>18}{sd:>10.3f}"
              f"{f'[{lo:.3f}, {hi:.3f}]':>28}")
        out[TIER_NAMES[t]] = {"n": len(sev), "median": statistics.median(sev),
                              "iqr": list(iqr), "sd_log": sd, "sd_log_ci": [lo, hi]}
    return out


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--events", default="data/pre-002-events.json")
    ap.add_argument("--riskset", default="data/pre-002-riskset.json")
    ap.add_argument("--out", default="data/reg-003-run.json")
    args = ap.parse_args()

    print("WT-089 · REG-003 · the recognition rate and the off-diagonal")
    print("Registration committed and pushed before this file existed (WT-052).\n")
    print("§1 · PROVING THE HELPERS BEFORE THEY CARRY A RESULT")
    prove_helpers()

    payload = json.loads(pathlib.Path(args.events).read_text())
    risk = {k: v for k, v in json.loads(pathlib.Path(args.riskset).read_text()).items()}
    branch = reconcile(payload)
    if branch == "NOT RUN":
        print("\n  REG-003 §2: rebuild unusable (n < 200). Both instruments NOT RUN.")
        summary("WT-089")
        return

    ebu = {lab: u["events"] for lab, u in payload["universes"].items()}
    res = {"branch": branch,
           "A": instrument_a(ebu),
           "B": instrument_b(ebu, risk),
           "C": companion_c(ebu)}
    pathlib.Path(args.out).write_text(json.dumps(res, indent=1, default=str))
    print(f"\n  written: {args.out}")
    summary("WT-089")


if __name__ == "__main__":
    main()
