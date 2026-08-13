#!/usr/bin/env python3
"""REG-006 ladder C: REG-003 §4's off-diagonal, re-derived under the CORRECTED tier-0 list.

Registered in REG-006 §4 C before this file existed: "Reported whatever it is."

Everything except TIER_TAGS[0] is edgar.py's registered code, unmodified: the same
extract_events, the same eligible-quarter risk set, the same 10,000 draws, the same seed.
One pass over companyfacts does both the events and the risk set -- wt089 paid for two.
"""
from __future__ import annotations

import json, pathlib, sys, time
from concurrent.futures import ThreadPoolExecutor

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import edgar as E                                     # noqa: E402

CORRECTED_T0 = ("ImpairmentOfLongLivedAssetsHeldForUse",
                "TangibleAssetImpairmentCharges",
                "ImpairmentOfLeasehold")
ORIGINAL_T0 = E.TIER_TAGS[0]

MODE = sys.argv[1] if len(sys.argv) > 1 else "corrected"
if MODE == "corrected":
    E.TIER_TAGS[0] = CORRECTED_T0
print(f"ladder C · tier 0 = {E.TIER_TAGS[0]}", flush=True)

uni = {int(k): v for k, v in json.loads((HERE / "universe.json").read_text()).items()}


def one(item):
    cik, (name, sic) = item
    try:
        raw = E._get(f"https://data.sec.gov/api/xbrl/companyfacts/CIK{int(cik):010d}.json")
        facts = json.loads(raw)
    except Exception:
        return None
    # BOTH tag lists in one pass. The crawl is the expensive part; extraction is free,
    # and running them side by side makes the comparison exact rather than across runs.
    res = {}
    for lab, t0 in (("original", ORIGINAL_T0), ("corrected", CORRECTED_T0)):
        E.TIER_TAGS[0] = t0
        drops = {b: 0 for b in E.DROP_BUCKETS}
        try:
            # the CALL SITE from wt089_harvest.py, copied rather than reconstructed:
            # the defaults are PRE-001's ("streak"), and the registered PRE-002/REG-003
            # sample is "peak". Reconstructing the call silently re-registers the study.
            res[lab] = (E.extract_events(facts, str(cik), name, drops,
                                         include_annual_attributed=True,
                                         onset_rule="peak", signal="revenue"), drops)
        except Exception:
            res[lab] = ([], drops)
    elig = []
    try:
        # verbatim wt089_riskset.eligible_quarters. peak_onset returns a TUPLE, so
        # `is not None` on the call itself is always true and inflates the risk set.
        rev, rtag, _ = E.duration_series(facts, E.REVENUE_TAGS)
        if rtag is not None and len(rev) >= E.MIN_HISTORY_QUARTERS:
            assets = E.instant_series(facts, E.ASSETS_TAG)
            if assets:
                for q in sorted(rev):
                    denom = next((assets[k] for k in range(q - 1, q - 6, -1)
                                  if k in assets), None)
                    if not denom or denom <= 0:
                        continue
                    onset, _c = E.peak_onset(rev, q)
                    if onset is None:
                        continue
                    elig.append(q)
    except Exception:
        pass
    uniname = "pilot" if E.PILOT_SIC[0] <= sic <= E.PILOT_SIC[1] else "replication"
    return uniname, str(cik), res, elig


if __name__ == "__main__":
    MODES = ("original", "corrected")
    out = {m: {"pilot": [], "replication": []} for m in MODES}
    dropsum = {m: {b: 0 for b in E.DROP_BUCKETS} for m in MODES}
    risk, n = {}, 0
    with ThreadPoolExecutor(max_workers=6) as ex:
        for r in ex.map(one, list(uni.items())):
            n += 1
            if r:
                u, cik, res, elig = r
                for m in MODES:
                    evs, dr = res[m]
                    if evs:
                        out[m][u].extend(evs)
                    for b, v in dr.items():
                        dropsum[m][b] += v
                if elig:
                    risk[cik] = elig
            if n % 200 == 0:
                print(f"  {n}/{len(uni)}  orig="
                      f"{sum(len(v) for v in out['original'].values())}  corr="
                      f"{sum(len(v) for v in out['corrected'].values())}", flush=True)

    json.dump(risk, open(HERE / "ladderC-riskset.json", "w"))
    import wt089_recognition_and_offdiagonal as W
    B = {}
    for m in MODES:
        json.dump({"universes": {u: {"events": ev, "n_events": len(ev)}
                                 for u, ev in out[m].items()}},
                  open(HERE / f"ladderC-events-{m}.json", "w"))
        print("\n" + "#" * 86)
        print(f"# TIER 0 = {m.upper()}   events "
              f"pilot={len(out[m]['pilot'])} replication={len(out[m]['replication'])}")
        print(f"# drops: " + "  ".join(f"{k}={v}" for k, v in dropsum[m].items() if v))
        print("#" * 86, flush=True)
        B[m] = W.instrument_b(dict(out[m]), risk)
    json.dump({"B": B, "drops": dropsum,
               "n_events": {m: {u: len(v) for u, v in out[m].items()} for m in MODES}},
              open(HERE / "ladderC-result.json", "w"), indent=1, default=str)
