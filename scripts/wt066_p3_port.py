#!/usr/bin/env python3
"""WT-066 -- the instrument registered by REG-001. Does the fold survive a layer change?

Regenerates every number this project may publish about the P3 second-layer port.
WT-053: every published number comes from a committed script that has been run.

    ./.venv/bin/python scripts/wt066_p3_port.py

Registered in advance (REG-001 §4):
  H1  static net pressure is invariant to the booked set                 -- expected PASS, trivial
  H2a event TIMING is invariant under endogenous aggregate-coupled labelling -- expected PASS
  H2b event MAGNITUDE is NOT invariant                                   -- expected PASS (varies)
  H3  if H1 fails, the port is invalid and the re-scope is unexercised   -- falsifier

H1 alone is registered as INSUFFICIENT. Read REG-001 §4 before quoting any number here.

THREE THINGS THIS SCRIPT DOES BECAUSE THE FIRST VERSION OF IT WAS WRONG
----------------------------------------------------------------------
The first run of this instrument reported ``H2a PASS`` from a regime in which **zero
recognition events fired**. Timing was invariant because there was no timing. That is the
same defect as the ``4/21 < 4/11 < 4/7 < 4/3`` guard REVIEW-002 replaced -- an assertion
incapable of failing -- committed in the session that quoted it as a lesson. So:

1. **A regime with no events is reported VACUOUS, never PASS.** The verdict is withheld,
   not inferred from an empty set.
2. **The test runs across a SWEEP of regimes**, and each row prints its peak pending
   share, so the reader can see which rows are in the switch-off regime and which are in
   the accumulating one. A single parameter point would be a result about a parameter.
3. **A negative control runs alongside**, in which the recognition order reads item
   *indices* rather than item *thresholds* -- labels instead of units. The invariance MUST
   break there. If the negative control passes, this instrument cannot detect failure and
   its verdicts are worthless; that case is reported as INSTRUMENT INVALID.
"""

import pathlib
import sys

import numpy as np

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "src"))

from wealth_tensor.recognition_fold import RecognitionLedger  # noqa: E402

N_ITEMS = 400
N_RECOGNISED = 150
N_LABELLINGS = 25
SEED = 20260811

# (scrutiny steps, recognition rate). Chosen to span the switch-off regime (recognition
# keeps pace, nothing accumulates, no events) through the accumulating regime. The peak
# pending share printed for each row is what tells the two apart, and it is reported
# rather than asserted.
REGIMES = ((120, 0.25), (120, 0.05), (60, 0.10), (40, 0.25), (20, 0.10), (12, 0.05))


def population(seed=SEED):
    rng = np.random.default_rng(seed)
    tau = rng.lognormal(mean=3.0, sigma=0.45, size=N_ITEMS)
    v = rng.lognormal(mean=1.0, sigma=0.8, size=N_ITEMS)
    return tau, v, rng


def interior_grid(tau, k=399):
    """Grid strictly inside the threshold range, with the endpoints dropped.

    The endpoints are data points -- they ARE thresholds -- and including them is what
    put four spurious clearing intervals into Paper I's first draft. Dropped, not
    filtered: REVIEW-002 established that the 1e-9 filter Paper I credited removes zero
    points and that dropping the endpoints is what actually did the work.
    """
    lo, hi = float(tau.min()), float(tau.max())
    return np.linspace(lo, hi, k + 2)[1:-1]


def sweep_row(tau, v, labellings, steps, alpha, tie_break, mag_trigger=True):
    scrutiny = np.linspace(float(tau.min()) * 0.6, float(tau.max()) * 1.05, steps)
    timings, magnitudes, counts, peaks, n_events = set(), set(), set(), [], set()
    for b in labellings:
        led = RecognitionLedger(tau, v, booked=b, recognition_rate=alpha,
                                crisis_threshold=0.25)
        out = led.run(scrutiny, magnitude_trigger=mag_trigger, tie_break=tie_break)
        timings.add(out["event_periods"])
        magnitudes.add(out["event_magnitudes"])
        counts.add(out["event_counts"])
        peaks.append(out["peak_pending_share"])
        n_events.add(len(out["events"]))
    return {"timings": len(timings), "magnitudes": len(magnitudes),
            "counts": len(counts), "peak": max(peaks),
            "events": sorted(n_events), "fired": max(n_events) > 0}


def main():
    tau, v, rng = population()
    grid = interior_grid(tau)
    labellings = []
    for _ in range(N_LABELLINGS):
        b = np.zeros(N_ITEMS, dtype=bool)
        b[rng.choice(N_ITEMS, size=N_RECOGNISED, replace=False)] = True
        labellings.append(b)

    print("=" * 79)
    print("WT-066 - P3 SECOND-LAYER PORT - instrument for REG-001")
    print("=" * 79)
    print(f"items {N_ITEMS} - recognised {N_RECOGNISED} - labellings {N_LABELLINGS} "
          f"- grid {grid.size} interior points - seed {SEED}")
    print(f"grid points coinciding with a threshold: "
          f"{int(np.sum(np.isin(grid, tau)))}  (must be 0)")

    # ---------------- H1 -- the static identity ----------------
    print("\n--- H1  static net pressure  (REGISTERED AS INSUFFICIENT ON ITS OWN) ---")
    pend_s, rev_s, net_s = set(), set(), set()
    mismatches = 0
    for b in labellings:
        pend = tuple(RecognitionLedger.pending_at(tau, b, s) for s in grid)
        rev = tuple(RecognitionLedger.reversible_at(tau, b, s) for s in grid)
        net = tuple(p - r for p, r in zip(pend, rev))
        struct = tuple(RecognitionLedger.structural_pressure(tau, N_RECOGNISED, s)
                       for s in grid)
        mismatches += sum(a != c for a, c in zip(net, struct))
        pend_s.add(pend); rev_s.add(rev); net_s.add(net)

    print(f"distinct PENDING schedules      : {len(pend_s)}")
    print(f"distinct REVERSIBLE schedules   : {len(rev_s)}")
    print(f"distinct NET PRESSURE schedules : {len(net_s)}")
    print(f"points where net != #(tau<s) - R: {mismatches}")
    h1 = len(net_s) == 1 and mismatches == 0 and len(pend_s) > 1 and len(rev_s) > 1
    print(f"H1: {'PASS' if h1 else 'FAIL'}")
    if not h1:
        print("\nH3 FIRES: port invalid at the first step. Report as unexercised generality.")
        return 1

    # ---------------- negative control: can this instrument fail at all? -------------
    print("\n--- NEGATIVE CONTROL  (recognition order reads INDICES, not thresholds) ---")
    print("     If the invariance survives this, the instrument cannot detect failure.")
    print(f"{'steps':>6} {'alpha':>6} {'peak share':>11} {'events':>10} "
          f"{'timings':>8} {'magnitudes':>11}")
    control_broke = False
    for steps, alpha in REGIMES:
        r = sweep_row(tau, v, labellings, steps, alpha, "index")
        note = "" if r["fired"] else "  (vacuous - no events)"
        print(f"{steps:>6} {alpha:>6.2f} {r['peak']:>11.3f} {str(r['events']):>10} "
              f"{r['timings']:>8} {r['magnitudes']:>11}{note}")
        if r["fired"] and (r["timings"] > 1 or r["magnitudes"] > 1):
            control_broke = True
    print(f"negative control breaks the invariance: {control_broke}")
    if not control_broke:
        print("\nINSTRUMENT INVALID: the control that must fail did not. No verdict is")
        print("reported below, because a test that cannot fail has not been passed.")
        return 1

    # ---------------- H2 -- endogenous, aggregate-coupled ----------------
    print("\n--- H2  endogenous + aggregate-coupled, magnitude-triggered as lag.py ---")
    print(f"{'steps':>6} {'alpha':>6} {'peak share':>11} {'events':>10} "
          f"{'timings':>8} {'magnitudes':>11}  verdict")
    live, h2a_ok, h2b_ok = 0, True, False
    for steps, alpha in REGIMES:
        r = sweep_row(tau, v, labellings, steps, alpha, "threshold")
        if not r["fired"]:
            verdict = "VACUOUS (switch-off regime, no events)"
        else:
            live += 1
            verdict = f"H2a {'PASS' if r['timings'] == 1 else 'FAIL'}"
            if r["timings"] != 1:
                h2a_ok = False
            if r["magnitudes"] > 1:
                h2b_ok = True
        print(f"{steps:>6} {alpha:>6.2f} {r['peak']:>11.3f} {str(r['events']):>10} "
              f"{r['timings']:>8} {r['magnitudes']:>11}  {verdict}")

    print(f"\nlive (non-vacuous) regimes: {live} of {len(REGIMES)}")
    if live == 0:
        print("H2: VACUOUS across every regime. NO VERDICT. Not a pass.")
        return 1
    print(f"H2a  event timing invariant to the booked set      : "
          f"{'PASS' if h2a_ok else 'FAIL'}")
    print(f"H2b  event magnitude varies with the booked set    : "
          f"{'PASS' if h2b_ok else 'FAIL - magnitude also invariant'}")

    # -------- the discriminating run: is it the TRIGGER that carries the labels? --------
    print("\n--- ISOLATION  same dynamics, COUNT-triggered instead of magnitude-triggered ---")
    print("     The count is a fold over units; the magnitude is a fold over units AND")
    print("     labels. If timing is invariant here and not above, the trigger is the")
    print("     channel through which the labelling re-enters. That is the whole finding.")
    print(f"{'steps':>6} {'alpha':>6} {'events':>10} {'timings':>8} {'magnitudes':>11}")
    cnt_live, cnt_timing_ok = 0, True
    for steps, alpha in REGIMES:
        r = sweep_row(tau, v, labellings, steps, alpha, "threshold", mag_trigger=False)
        note = "" if r["fired"] else "  (vacuous)"
        print(f"{steps:>6} {alpha:>6.2f} {str(r['events']):>10} {r['timings']:>8} "
              f"{r['magnitudes']:>11}{note}")
        if r["fired"]:
            cnt_live += 1
            if r["timings"] != 1:
                cnt_timing_ok = False
    if cnt_live:
        print(f"count-triggered timing invariant across {cnt_live} live regimes: "
              f"{'YES' if cnt_timing_ok else 'NO'}")
    else:
        print("count-triggered: VACUOUS across every regime. No verdict.")

    print("\n" + "=" * 79)
    print("REG-001 §7: a pass licenses exactly one sentence -- the fold-invariance")
    print("survives a change of layer. It licenses no claim about the world, and no")
    print("claim of novelty in the price layer, which is Wicksteed's.")
    print("=" * 79)
    return 0


if __name__ == "__main__":
    sys.exit(main())
