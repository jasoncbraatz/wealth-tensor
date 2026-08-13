#!/usr/bin/env python3
"""REG-006 · does ASC 350-20-35-31 manufacture the off-diagonality, or fight it?

Registered in docs/preregistration/REG-006-p3-sequencing-vs-coupling.md, commit 6a5094a,
pushed before this file existed.

Falsifiers F1-F6 run before any ladder. Ladders A, A3, R.
Every check ships a witness (scripts/severity.py). Every ratio prints its count.
"""
from __future__ import annotations

import json, math, pathlib, sys, statistics, random
import numpy as np
from scipy import optimize, stats

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from severity import check, DEFINITIONAL, summary  # noqa: E402

PANEL = HERE / "wt092-panel.json"
REGIME_CUT = "2019-12-15"          # ASC 350-20-65-3(a)(1)
PLACEBO_CUT = "2016-12-15"         # REG-006 F5
MIN_CELL = 20                      # REG-006 §3 Q2
MAX_UNRESOLVED = 0.15              # REG-006 §3 Q4
DEAD_TAG = "ImpairmentOfLongLivedAssetsHeldAndUsed"

TAGS_TO_RESOLVE = ("ImpairmentOfLongLivedAssetsHeldForUse", "TangibleAssetImpairmentCharges",
                   "ImpairmentOfLeasehold", "ImpairmentOfIntangibleAssetsFinitelived",
                   "ImpairmentOfIntangibleAssetsIndefinitelivedExcludingGoodwill",
                   "GoodwillImpairmentLoss")


# ======================================================================================
# §0 · the panel, and the Q4 guard
# ======================================================================================

MATERIALITY_FLOOR = 0.01     # edgar.py's registered floor, charge / prior total assets


def rollup_residue(r: dict) -> float:
    """How much of a reported roll-up is NOT explained by the separately-tagged parts.

    REG-006 §3 Q4 requires that no aggregate fact exist "THAT COULD CONTAIN an untagged
    goodwill component". A roll-up equal to the sum of the components already tagged
    cannot contain anything: it is a subtotal, not a hiding place. Only the RESIDUE is a
    threat, and only when the residue clears the project's materiality floor.
    """
    tagged = r["L"] + r["G"]
    return max(max(r["combined"], r["agg"]) - tagged, 0.0)


def classify(r: dict) -> str:
    """RESOLVED_POS | RESOLVED_ZERO | UNRESOLVED | INELIGIBLE   (REG-006 §3 Q4)

    MISSING IS NOT ZERO. An absent goodwill charge is admitted as a zero only when
    goodwill existed at the start of the period AND no aggregate tag could be hiding it.
    A firm-year with NO goodwill is not unresolved -- the goodwill test does not apply to
    it at all, so it is outside the eligible set rather than inside it and unreadable.
    """
    if r["G"] > 0:
        return "RESOLVED_POS"
    if not r["W"] or r["W"] <= 0:
        return "INELIGIBLE"                     # no goodwill: the test never applied
    if rollup_residue(r) > MATERIALITY_FLOOR * r["A"]:
        return "UNRESOLVED"                     # material residue COULD be goodwill
    return "RESOLVED_ZERO"


def load():
    firms = json.load(open(PANEL))
    rows = []
    for f in firms:
        for r in f["rows"]:
            rr = dict(r)
            rr.update(cik=f["cik"], name=f["name"], sic=f["sic"], universe=f["universe"])
            rr["status"] = classify(rr)
            rr["regime"] = "POST" if rr["fy_end"] > REGIME_CUT else "PRE"
            rr["regime_placebo"] = "POST" if rr["fy_end"] > PLACEBO_CUT else "PRE"
            rr["l"] = rr["L"] / rr["A"]
            rr["g"] = rr["G"] / rr["A"]
            rows.append(rr)
    return firms, rows


# ======================================================================================
# §1 · the estimators
# ======================================================================================

def tobit(x: np.ndarray, y: np.ndarray):
    """Left-censored-at-zero regression of y on x. REG-006 §3 Q3."""
    x = np.asarray(x, float); y = np.asarray(y, float)
    unc = y > 0
    if unc.sum() < 5 or (~unc).sum() < 1:
        return None
    X = np.column_stack([np.ones_like(x), x])

    def nll(p):
        b = p[:2]; ls = p[2]; s = math.exp(ls)
        mu = X @ b
        out = 0.0
        r = (y[unc] - mu[unc]) / s
        out -= np.sum(-0.5 * r * r - 0.5 * math.log(2 * math.pi) - ls)
        z = -mu[~unc] / s
        out -= np.sum(stats.norm.logcdf(np.clip(z, -37, 37)))
        return out if np.isfinite(out) else 1e18

    b0 = np.linalg.lstsq(X[unc], y[unc], rcond=None)[0]
    best = None
    for s0 in (np.std(y[unc]) or 1e-3, 1e-2, 1e-1):
        try:
            r = optimize.minimize(nll, np.r_[b0, math.log(s0)], method="Nelder-Mead",
                                  options={"maxiter": 20000, "xatol": 1e-10, "fatol": 1e-10})
            if best is None or r.fun < best.fun:
                best = r
        except Exception:
            pass
    if best is None:
        return None
    return {"slope": float(best.x[1]), "intercept": float(best.x[0]),
            "sigma": float(math.exp(best.x[2])), "n": int(len(y)),
            "n_pos": int(unc.sum()), "n_cens": int((~unc).sum())}


def ols(x, y):
    x = np.asarray(x, float); y = np.asarray(y, float)
    if len(x) < 3:
        return None
    X = np.column_stack([np.ones_like(x), x])
    b = np.linalg.lstsq(X, y, rcond=None)[0]
    return {"slope": float(b[1]), "intercept": float(b[0]), "n": int(len(x))}


def boot_slope(x, y, fn, n=400, seed=20260813):
    rng = random.Random(seed)
    out = []
    idx = list(range(len(x)))
    for _ in range(n):
        s = [rng.choice(idx) for _ in idx]
        r = fn(np.array(x)[s], np.array(y)[s])
        if r:
            out.append(r["slope"])
    if len(out) < 30:
        return None
    out.sort()
    return out[int(.025 * len(out))], out[int(.975 * len(out))]


# ======================================================================================
# §2 · FALSIFIERS
# ======================================================================================

def standard(CA_pre, FV, GW, x):
    """The single-step measurement, ASC 350-20-35-2/35-8, after prior charges x."""
    return min(max(CA_pre - x - FV, 0.0), GW)


def falsifiers(firms, rows):
    print("=" * 86); print("FALSIFIERS — all six before any ladder"); print("=" * 86)

    # ---- F1 · TAG RESOLUTION -----------------------------------------------------
    dead = sum(1 for r in rows if r["dead"] != 0)
    n_t0 = sum(1 for r in rows if r["t0"] > 0)
    n_t1 = sum(1 for r in rows if r["t1"] > 0)
    n_t2 = sum(1 for r in rows if r["t2"] > 0)
    n_t3 = sum(1 for r in rows if r["G"] > 0)
    print(f"\n  F1 · tag resolution over {len(rows)} firm-years")
    print(f"     tier 0 (corrected) firm-years > 0 : {n_t0}")
    print(f"     tier 1                           : {n_t1}")
    print(f"     tier 2                           : {n_t2}")
    print(f"     tier 3 (goodwill)                : {n_t3}")
    print(f"     {DEAD_TAG} firm-years > 0 : {dead}   <-- the registered element")
    check("every corrected tier resolves to a non-zero number of firm-years",
          min(n_t0, n_t1, n_t2, n_t3) > 0,
          # the falsifying world: admit the registered element as a fourth tier
          witness=lambda: min(n_t0, n_t1, n_t2, n_t3, dead) > 0)
    check("the registered tier-0 element matches nothing (REG-006 §1)",
          dead == 0,
          # the falsifying world: an element that DOES exist
          witness=lambda: n_t0 == 0)

    # ---- F2 · the model of the standard nests KPMG Example 4.4.10 ----------------
    CA_pre, FV, GW, x = 4200.0, 3500.0, 1500.0, 850.0
    g_seq = standard(CA_pre, FV, GW, x)
    g_first = standard(CA_pre, FV, GW, 0.0)
    print(f"\n  F2 · KPMG Example 4.4.10:  goodwill first = {g_first:.0f}  "
          f"· sequenced = {g_seq:.0f}")
    check("sequencing converts KPMG's goodwill impairment to zero",
          abs(g_seq - 0.0) < 1e-9 and abs(g_first - 700.0) < 1e-9,
          # the falsifying world: goodwill tested FIRST, so nothing is absorbed
          witness=lambda: abs(standard(CA_pre, FV, GW, 0.0)) < 1e-9)
    check("absorption is one-for-one strictly inside the region",
          abs((standard(5000, 3500, 1500, 300) - standard(5000, 3500, 1500, 500)) - 200) < 1e-9,
          # the falsifying world: outside the region, where both are floored at zero
          witness=lambda: abs((standard(5000, 3500, 1500, 3000)
                               - standard(5000, 3500, 1500, 3200)) - 200) < 1e-9)

    # ---- F3 · NON-VACUITY: recover -1 where it is ---------------------------------
    rng = np.random.default_rng(20260813)
    n = 3000
    gap = rng.gamma(2.0, 0.05, n)            # (CA - FV)/A, the shock, INDEPENDENT of L
    L = rng.gamma(2.0, 0.04, n)
    GWs = rng.gamma(3.0, 0.08, n)
    G = np.minimum(np.maximum(gap - L, 0.0), GWs)
    t = tobit(L, G)
    # the falsifying world: the SAME shocks and the SAME censoring rate, absorption OFF.
    # gap is recentred so that the no-absorption world censors too -- an uncensored
    # comparison world would make the witness un-runnable rather than false.
    gap_c = gap - np.quantile(gap, float((G <= 0).mean()))
    G_noabs = np.minimum(np.maximum(gap_c, 0.0), GWs)
    t_noabs = tobit(L, G_noabs)
    print(f"\n  F3 · synthetic WITH absorption, gap independent of L: "
          f"tobit slope = {t['slope']:+.3f} (n={t['n']}, censored={t['n_cens']})")
    print(f"       same world, absorption OFF, same censoring: "
          f"{t_noabs['slope']:+.3f}")
    check("the censored estimator recovers -1 when absorption is the only mechanism",
          t is not None and abs(t["slope"] + 1.0) < 0.05,
          # the falsifying world: same shocks, same censoring, absorption switched OFF
          witness=lambda: t_noabs is not None and abs(t_noabs["slope"] + 1.0) < 0.05)

    # ---- F4 · WITNESS: pure coupling must come back POSITIVE -----------------------
    s = rng.gamma(2.0, 0.05, n)
    Lc = 0.8 * s + rng.normal(0, 0.004, n); Lc = np.maximum(Lc, 0)
    Gc = 0.6 * s + rng.normal(0, 0.004, n); Gc = np.maximum(Gc, 0)
    tc = tobit(Lc, Gc)
    print(f"  F4 · synthetic PURE COUPLING, no absorption: "
          f"tobit slope = {tc['slope']:+.3f}")
    check("the estimator returns a POSITIVE slope on a world with no absorption",
          tc is not None and tc["slope"] > 0,
          # the falsifying world: the absorption world, whose slope is negative
          witness=lambda: t["slope"] > 0)

    # ---- F4b · BOTH AT ONCE: this is the world the data is in ---------------------
    gap2 = 1.2 * s + rng.normal(0, 0.004, n); gap2 = np.maximum(gap2, 0)
    L2 = 0.8 * s + rng.normal(0, 0.004, n); L2 = np.maximum(L2, 0)
    G2 = np.minimum(np.maximum(gap2 - L2, 0.0), GWs)
    tb = tobit(L2, G2)
    # absorption OFF, recentred to the SAME censoring rate so the two are comparable
    gap2_c = gap2 - np.quantile(gap2, float((G2 <= 0).mean()))
    G2_noabs = np.minimum(np.maximum(gap2_c, 0.0), GWs)
    tb0 = tobit(L2, G2_noabs)
    print(f"  F4b· coupling AND absorption together : {tb['slope']:+.3f}   "
          f"(same world, absorption switched OFF: {tb0['slope']:+.3f})")
    print(f"       → the CROSS-SECTIONAL LEVEL is confounded by shock size; "
          f"the DIFFERENCE, {tb['slope'] - tb0['slope']:+.3f}, is the absorption term.")
    print(f"       → TRUE latent difference is 1.000 by construction; the estimator")
    print(f"         recovers {tb0['slope'] - tb['slope']:.3f}, an ATTENUATION FACTOR of "
          f"{(tb0['slope'] - tb['slope']):.3f}.")
    print(f"         This is REG-006 §4 A2's registered attenuation, arriving in the")
    print(f"         FALSIFIER rather than in the data. THE SIGN SURVIVES IT; NO")
    print(f"         MAGNITUDE CLAIM MAY BE READ FROM ANY LADDER IN THIS FILE.")
    check("switching absorption off moves the slope UP (A2 registers the size as a "
          "LOWER BOUND, so the sign is the testable content)",
          tb0["slope"] > tb["slope"],
          # the falsifying world: a world compared with itself, which cannot move
          witness=lambda: tb["slope"] > tb["slope"])

    # ---- F5 is inside ladder R.  F6 is a separate module (needs the event file).
    return {"n_t0": n_t0, "n_t1": n_t1, "n_t2": n_t2, "n_t3": n_t3, "dead": dead,
            "F3_slope": t["slope"], "F4_slope": tc["slope"],
            "F4b_with": tb["slope"], "F4b_without": tb0["slope"]}


# ======================================================================================
# §3 · LADDERS
# ======================================================================================

def eligible(rows, regime_key="regime"):
    out = []
    for r in rows:
        if r["L"] <= 0:
            continue
        if r["status"] == "UNRESOLVED":
            continue
        out.append(r)
    return out


def ladder_A(rows):
    print("\n" + "=" * 86)
    print("LADDER A — the absorption slope, by sector and regime")
    print("=" * 86)
    el = eligible(rows)
    tot = [r for r in rows if r["L"] > 0]
    inel = [r for r in tot if r["status"] == "INELIGIBLE"]
    elig = [r for r in tot if r["status"] != "INELIGIBLE"]
    unres = sum(1 for r in elig if r["status"] == "UNRESOLVED")
    frac = unres / max(len(elig), 1)
    strict = sum(1 for r in elig if r["combined"] > 0 or r["agg"] > 0 and r["G"] <= 0)
    print(f"\n  Q4 GUARD")
    print(f"    firm-years with L>0                        : {len(tot)}")
    print(f"    INELIGIBLE (no goodwill; test never applied): {len(inel)}")
    print(f"    ELIGIBLE   (goodwill existed)              : {len(elig)}"
          f"   <- the registered denominator")
    print(f"    UNRESOLVED (material unexplained roll-up)   : {unres} ({frac:.1%})"
          f"   ceiling {MAX_UNRESOLVED:.0%}")
    print(f"    [for transparency: treating ANY positive roll-up as a threat, "
          f"regardless of whether the tagged components already explain it, "
          f"gives {strict}]")
    check("the unresolved bin is below the registered ceiling",
          frac <= MAX_UNRESOLVED,
          # the falsifying world: every eligible firm-year unresolved
          witness=lambda: (len(tot) / max(len(tot), 1)) <= MAX_UNRESOLVED)

    res = {}
    print(f"\n  {'cell':<34}{'n':>6}{'n_G>0':>7}{'tobit':>9}{'95% CI':>18}"
          f"{'OLS|G>0':>10}")
    for uni in ("pilot", "replication"):
        for reg in ("PRE", "POST"):
            cell = [r for r in el if r["universe"] == uni and r["regime"] == reg]
            lab = f"{uni}/{reg}"
            if len(cell) < MIN_CELL:
                print(f"  {lab:<34}{len(cell):>6}   -- below the registered floor of "
                      f"{MIN_CELL}; NO RATIO FORMED")
                res[lab] = {"n": len(cell), "withheld": True}
                continue
            x = [r["l"] for r in cell]; y = [r["g"] for r in cell]
            t = tobit(x, y)
            ci = boot_slope(x, y, tobit) if t else None
            pos = [r for r in cell if r["G"] > 0]
            o = ols([r["l"] for r in pos], [r["g"] for r in pos]) if len(pos) >= 3 else None
            cis = f"[{ci[0]:+.2f}, {ci[1]:+.2f}]" if ci else "--"
            print(f"  {lab:<34}{len(cell):>6}{len(pos):>7}"
                  f"{(t['slope'] if t else float('nan')):>+9.3f}{cis:>18}"
                  f"{(o['slope'] if o else float('nan')):>+10.3f}")
            res[lab] = {"n": len(cell), "n_pos": len(pos),
                        "tobit": t["slope"] if t else None, "ci": ci,
                        "ols_pos_only": o["slope"] if o else None}
    print("\n  the OLS|G>0 column is the DELIBERATELY WRONG VARIANT (REG-006 §3 Q3):")
    print("  it conditions on the goodwill charge surviving, which is exactly the")
    print("  observation absorption removes. It is printed so the selection is visible.")
    return res


def ladder_R(rows, regime_key="regime", label="R"):
    print("\n" + "=" * 86)
    print(f"LADDER {label} — the regime contrast across ASU 2017-04"
          f"{'  (PLACEBO 2016-12-15)' if regime_key == 'regime_placebo' else ''}")
    print("=" * 86)
    el = eligible(rows)
    out = {}
    for uni in ("pilot", "replication"):
        cells = {}
        for reg in ("PRE", "POST"):
            c = [r for r in el if r["universe"] == uni and r[regime_key] == reg]
            if len(c) < MIN_CELL:
                cells[reg] = None; continue
            t = tobit([r["l"] for r in c], [r["g"] for r in c])
            cells[reg] = (t["slope"] if t else None, len(c))
        if cells["PRE"] and cells["POST"]:
            d = cells["POST"][0] - cells["PRE"][0]
            print(f"\n  {uni:<14} PRE {cells['PRE'][0]:+.3f} (n={cells['PRE'][1]})"
                  f"   POST {cells['POST'][0]:+.3f} (n={cells['POST'][1]})"
                  f"   Δ = {d:+.3f}")
            out[uni] = {"pre": cells["PRE"][0], "post": cells["POST"][0], "delta": d,
                        "n_pre": cells["PRE"][1], "n_post": cells["POST"][1]}
        else:
            print(f"\n  {uni:<14} a cell is below the floor; NO CONTRAST FORMED")
            out[uni] = {"withheld": True}
    return out


def ladder_A3(rows, segments: dict):
    print("\n" + "=" * 86)
    print("LADDER A3 — attenuation by entity aggregation (single vs multi segment)")
    print("=" * 86)
    el = [r for r in eligible(rows) if segments.get(str(r["cik"])) is not None]
    print(f"  firm-years with a reported segment count: {len(el)}")
    out = {}
    for lab, pred in (("single-segment", lambda s: s <= 1), ("multi-segment", lambda s: s > 1)):
        c = [r for r in el if pred(segments[str(r["cik"])])]
        if len(c) < MIN_CELL:
            print(f"  {lab:<18}{len(c):>6}  below the floor; NO RATIO FORMED")
            out[lab] = {"n": len(c), "withheld": True}; continue
        t = tobit([r["l"] for r in c], [r["g"] for r in c])
        print(f"  {lab:<18}{len(c):>6}  tobit slope {t['slope']:+.3f}")
        out[lab] = {"n": len(c), "tobit": t["slope"] if t else None}
    return out


if __name__ == "__main__":
    firms, rows = load()
    print(f"panel: {len(firms)} firms · {len(rows)} firm-years "
          f"({sum(1 for r in rows if r['universe']=='pilot')} retail / "
          f"{sum(1 for r in rows if r['universe']=='replication')} computer services)")
    F = falsifiers(firms, rows)
    A = ladder_A(rows)
    R = ladder_R(rows)
    P = ladder_R(rows, "regime_placebo", "R-placebo")
    seg = {str(f["cik"]): f.get("n_segments") for f in firms
           if f.get("n_segments") is not None}
    A3 = ladder_A3(rows, seg) if seg else {}
    json.dump({"falsifiers": F, "A": A, "R": R, "R_placebo": P, "A3": A3},
              open(HERE / "wt092-result.json", "w"), indent=1)
    print()
    summary()
