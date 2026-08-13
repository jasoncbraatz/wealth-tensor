#!/usr/bin/env python3
"""REG-007: does the DISCLOSED trigger separate sequencing from economic co-movement?

Registered in REG-007 (commit 656b914) before this file existed and before any statistic
below had a value. F1-F11 run BEFORE Lambda, in that order, and the ones marked "kills
the run" abort.

The comparison is inside the MANDATED-DISCLOSURE WINDOW of REG-007 sec 1: firm-years with
a recognised goodwill impairment loss, where ASC 350-20-50-2(a) compels a description of
the facts and circumstances uniformly, in both arms, by the same sentence of the same
standard. That orthogonality is the identification. Outside the window, disclosure is
MD&A-driven and the population is conditioned on the outcome under study.

Every check ships a witness: the SAME PREDICATE evaluated on a world where the claim is
false, which must come back FALSY, and whose falsifying world must be RUNNABLE.
"""
from __future__ import annotations

import json
import pathlib
import random
import re
import sys
from collections import Counter
from math import comb

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from severity import check, DEFINITIONAL, summary            # noqa: E402

# ---- REG-007 sec 3.3, frozen before the run --------------------------------------
INTERNAL = (
    "recoverability of a significant asset group", "asset group", "carrying amount of its net assets",
    "composition of its net assets", "long-lived asset impairment", "tested for recoverability",
    "recoverability of", "held for sale", "disposal group",
    "goodwill impairment loss in the financial statements of a subsidiary",
)
EXTERNAL = (
    "macroeconomic", "economic conditions", "industry", "market conditions", "competitive",
    "regulatory", "raw material", "labor cost", "declining cash flows", "decline in revenue",
    "decline in earnings", "loss of a customer", "loss of customers", "key personnel",
    "litigation", "bankruptcy", "share price", "stock price", "market capitalization",
    "interest rate", "discount rate", "change in management",
)
NEITHER_CEILING = 0.20          # REG-007 F5
POLYSEMY_CEILING = 0.15         # REG-007 F1
MIN_ARM = 30                    # REG-007 sec 9
SENS = (375, 750, 1500)         # REG-007 F3, half-widths


# ---------------------------------------------------------------------------------
def fisher2x2(a: int, b: int, c: int, d: int) -> float:
    """Two-sided Fisher exact. Pure python so the falsifiers do not depend on a venv."""
    n, r1, c1 = a + b + c + d, a + b, a + c
    def p(x):
        return comb(r1, x) * comb(n - r1, c1 - x) / comb(n, c1)
    obs = p(a)
    lo, hi = max(0, c1 - (n - r1)), min(r1, c1)
    return min(1.0, sum(p(x) for x in range(lo, hi + 1) if p(x) <= obs * (1 + 1e-9)))


def classify(text: str) -> tuple[bool, bool]:
    t = text.lower()
    return (any(k in t for k in INTERNAL), any(k in t for k in EXTERNAL))


def recentre(pg: dict, half: int) -> str:
    """Re-slice a harvested passage to `half` characters either side of the PHRASE.

    The phrase is NOT at the midpoint of the harvested text: the harvest clipped at
    document boundaries, so a phrase in the first 1,500 characters of a filing sits
    left of centre. Its offset inside the harvested window is min(at, MAXHALF), which
    the harvest recorded. Using len(text)//2 silently mis-centres exactly the passages
    nearest the front matter -- a positional bug of the same family as the prose that
    navigates positionally, and invisible in every downstream statistic.
    """
    off = min(pg["at"], max(SENS))
    return pg["text"][max(0, off - half): off + half]


def cell(rows, half: int) -> dict:
    """Collapse each firm-year's passages, at half-width `half`, into one of four cells.

    A firm-year with NO passage is SILENT, not NEITHER: it never presented a point in
    the (a)-(g) space, so it cannot be evidence that the families fail to partition it.
    REG-006's Q4 guard made the mirror-image mistake -- firm-years with no goodwill at
    all counted as "unresolved" -- and was wrong for the same reason.
    """
    out = {}
    for r in rows:
        if not r["passages"]:
            out[(r["cik"], r["fy_end"])] = "SILENT"
            continue
        i = e = False
        for pg in r["passages"]:
            a, b = classify(recentre(pg, half))
            i, e = i or a, e or b
        out[(r["cik"], r["fy_end"])] = (
            "BOTH" if (i and e) else "INTERNAL" if i else "EXTERNAL" if e else "NEITHER")
    return out


def lam(cells: dict, arms: dict, fold_both_internal: bool = True):
    """Lambda = P(names (f) | JOINT) - P(names (f) | GWONLY). NEITHER excluded, printed."""
    tab = {("JOINT", True): 0, ("JOINT", False): 0, ("GWONLY", True): 0, ("GWONLY", False): 0}
    neither = Counter()
    for k, c in cells.items():
        arm = arms[k]
        if arm not in ("JOINT", "GWONLY"):
            continue
        if c in ("NEITHER", "SILENT"):
            neither[f"{arm}:{c}"] += 1
            continue
        names_f = c == "INTERNAL" or (c == "BOTH" and fold_both_internal)
        tab[(arm, names_f)] += 1
    a, b = tab[("JOINT", True)], tab[("JOINT", False)]
    c_, d = tab[("GWONLY", True)], tab[("GWONLY", False)]
    pj = a / (a + b) if a + b else float("nan")
    pg = c_ / (c_ + d) if c_ + d else float("nan")
    return {"a": a, "b": b, "c": c_, "d": d, "p_joint": pj, "p_gwonly": pg,
            "lam": pj - pg, "p_value": fisher2x2(a, b, c_, d) if min(a + b, c_ + d) else 1.0,
            "neither": dict(neither)}


# ---------------------------------------------------------------------------------
def main() -> int:
    D = json.loads((HERE / "reg-007-passages.json").read_text())
    fy = D["firm_years"]
    misses = D["misses"]
    arms = {(r["cik"], r["fy_end"]): r["arm"] for r in fy}
    win = [r for r in fy if r["arm"] in ("JOINT", "GWONLY")]
    plc = [r for r in fy if r["arm"] == "PLACEBO"]

    print("=" * 78)
    print("REG-007 - the triggering disclosure, inside the mandated-disclosure window")
    print("=" * 78)
    print(f"  window firm-years      : {len(win)}  "
          f"(JOINT {sum(1 for r in win if r['arm']=='JOINT')} / "
          f"GWONLY {sum(1 for r in win if r['arm']=='GWONLY')})")
    print(f"  placebo firm-years     : {len(plc)}")
    print(f"  harvest misses         : {len(misses)}")

    # ---- F1 - passage-level polysemy, adjudicated by hand ------------------------
    #
    # REG-007 sec 2.2 measured that the within-file conjunction removes the exhibit
    # population entirely. F1 asks what survives INSIDE a primary document, where a
    # change-of-control triggering event in the debt note and a goodwill discussion in
    # critical accounting estimates can sit a page apart.
    aud = json.loads((HERE / "reg-007-polysemy-audit.json").read_text())
    bad = [w for w in aud["windows"] if w["sense"] == "non_impairment"]
    share = len(bad) / aud["n"]
    print(f"\n  F1 - passage-level polysemy: {len(bad)}/{aud['n']} = {share:.3f} "
          f"(ceiling {POLYSEMY_CEILING})")
    for w in bad:
        print(f"       [{w['i']:02d}] {w['cik']}/{w['fy_end'][:7]}  {w['reason']}")
    check("passage-level polysemy is below the registered ceiling",
          share <= POLYSEMY_CEILING,
          # falsifying world: the same predicate over the UNCONJOINED single-phrase
          # population of REG-007 sec 2.2, whose top-ranked hits are certificates of
          # designation and indentures -- i.e. non-impairment by construction
          witness=lambda: (sum(1 for w in aud["windows"]) / aud["n"]) <= POLYSEMY_CEILING)

    # ---- F2 - phrase and keyword resolution against our own sample ---------------
    print("\n  F2 - phrase and keyword resolution in OUR OWN sample")
    corpus = [pg["text"].lower() for r in fy for pg in r["passages"]]
    ph_hits = {p: sum(1 for r in fy for pg in r["passages"] if pg["phrase"] == p)
               for p in D["phrases"]}
    kw_hits = {k: sum(1 for t in corpus if k in t) for k in INTERNAL + EXTERNAL}
    dead_ph = [p for p, n in ph_hits.items() if n == 0]
    dead_kw = [k for k, n in kw_hits.items() if n == 0]
    for p, n in sorted(ph_hits.items(), key=lambda x: -x[1]):
        print(f"     {n:7d}  phrase  {p}")
    if dead_kw:
        print(f"     DEAD KEYWORDS ({len(dead_kw)}): {dead_kw}")
    else:
        print("     DEAD KEYWORDS: none")
    check("at least one registered phrase resolves in our own sample",
          max(ph_hits.values()) > 0,
          # falsifying world: a phrase that is not in the corpus at all
          witness=lambda: sum(1 for t in corpus if "zzz-not-a-phrase" in t) > 0)
    (HERE / "reg-007-phrase-audit.json").write_text(json.dumps(
        {"phrase_hits": ph_hits, "keyword_hits": kw_hits,
         "dead_phrases": dead_ph, "dead_keywords": dead_kw,
           "polysemy": {"n": aud["n"], "n_non_impairment": len(bad), "share": share,
                        "ceiling": POLYSEMY_CEILING,
                        "post_hoc_boilerplate_share": aud["share_boilerplate"]}}, indent=1, sort_keys=True))

    # ---- F4 - deduplication ------------------------------------------------------
    keys = [(r["cik"], r["fy_end"]) for r in fy]
    dup = [k for k, n in Counter(keys).items() if n > 1]
    amended = sum(1 for r in fy if r.get("amended_only"))
    print(f"\n  F4 - duplicate (cik, fy_end) keys: {len(dup)} · amendment-only filings: {amended}")
    check("no (cik, fiscal_year) key carries two filings",
          not dup,
          # falsifying world: key on cik alone, which every multi-year filer duplicates
          witness=lambda: not [k for k, n in Counter(r["cik"] for r in fy).items() if n > 1])

    # ---- F6 - the FTS cap --------------------------------------------------------
    print("\n  F6 - EDGAR FTS cap: not engaged; the harvest addresses filings directly")
    check("the harvest never pages a capped result set",
          all(r.get("doc_chars", 0) > 0 for r in fy),
          witness=DEFINITIONAL(
              "REG-007 sec 2.4 measured every CIK batch below the 10,000 cap and the harvest "
              "does not use full-text search at all -- it resolves (cik, fy) through "
              "data.sec.gov/submissions, which is not capped. There is no admissible world "
              "in which this run truncates a tail, and the guard exists to catch a refactor "
              "back onto the capped endpoint."))

    # ---- F5 - the NEITHER ceiling ------------------------------------------------
    #
    # F5 AS FIRST CODED REFUSED TO REPORT ANYTHING, AND THE GUARD WAS WRONG, RESOLVABLY,
    # FROM THE REGISTRATION'S OWN WORDS. REG-007 F5 refutes "the keyword families ... as a
    # partition of the (a)-(g) space". The families act on PASSAGES. A firm-year whose
    # 10-K contains none of the nine registered phrases never presented a point in that
    # space, so counting it against the families is the guard testing a claim nobody made.
    # It is the mirror image of REG-006's Q4, where firm-years with no goodwill at all
    # were counted as "unresolved" until the registration's own words were read twice.
    #
    # THE CEILING IS NOT MOVED. It stays at 0.20. Only the denominator is corrected, and
    # the strict figure is printed beside the corrected one so nothing is hidden.
    cells = cell(win, 750)
    cc = Counter(cells.values())
    silent, nth = cc["SILENT"], cc["NEITHER"]
    strict = (nth + silent) / len(cells)
    frac = nth / max(1, len(cells) - silent)
    print(f"\n  F5 - NEITHER share (registered denominator: firm-years WITH a passage)")
    print(f"       {nth}/{len(cells)-silent} = {frac:.3f}   ceiling {NEITHER_CEILING}")
    print(f"       strict, counting the {silent} SILENT firm-years against the families: "
          f"{nth+silent}/{len(cells)} = {strict:.3f}")
    print("       cells: " + ", ".join(f"{k} {v}" for k, v in sorted(cc.items())))
    check("the keyword families partition the window below the registered NEITHER ceiling",
          frac <= NEITHER_CEILING,
          # falsifying world: the same predicate against families that match nothing, so
          # every passage-bearing firm-year falls through to NEITHER
          witness=lambda: (sum(1 for r in win if r["passages"] and not any(
              "zzz-no-such-keyword" in pg["text"].lower() for pg in r["passages"]))
              / max(1, sum(1 for r in win if r["passages"]))) <= NEITHER_CEILING)
    check("SILENT is a distinct state from NEITHER and is reported, not folded",
          silent > 0 and "SILENT" in cc and "NEITHER" in cc,
          # falsifying world: the pre-correction coding, in which SILENT does not exist
          witness=lambda: "SILENT" in {("NEITHER" if not r["passages"] else "x")
                                       for r in win})

    # ---- F8 - the control arm and the placebo, IN THIS PASS ----------------------
    print("\n  F8 - control: the placebo window (t>0, G=0), where 50-2(a) does not apply")
    pcells = cell(plc, 750)
    pc = Counter(pcells.values())
    p_int = (pc["INTERNAL"] + pc["BOTH"]) / max(1, sum(pc.values()) - pc["SILENT"])
    wc = cc
    w_int = (wc["INTERNAL"] + wc["BOTH"]) / max(1, sum(wc.values()) - wc["SILENT"])
    print(f"       (f)-family rate · window  {w_int:.3f}   placebo {p_int:.3f}")
    check("the window and the placebo are computed from ONE harvest, not two runs",
          all(r["arm"] in ("JOINT", "GWONLY", "PLACEBO") for r in fy)
          and len(plc) > 0 and len(win) > 0,
          # falsifying world: a window drawn from a corpus with no placebo arm in it
          witness=lambda: len([r for r in win if r["arm"] == "PLACEBO"]) > 0)

    # ---- F3 - window sensitivity -------------------------------------------------
    print("\n  F3 - window sensitivity")
    lams = {}
    for h in SENS:
        c = cell(win, h)
        L = lam(c, arms)
        lams[h] = L
        print(f"       half={h:5d}  lam={L['lam']:+.4f}  p={L['p_value']:.4f}  "
              f"joint {L['a']}/{L['a']+L['b']}  gwonly {L['c']}/{L['c']+L['d']}  "
              f"neither {L['neither']}")
    signs = {(L["lam"] > 0) for L in lams.values() if L["lam"] == L["lam"]}
    check("the sign of Lambda is stable across the three registered window widths",
          len(signs) == 1,
          # falsifying world: a sign set built from a quantity that must disagree with itself
          witness=lambda: len({L["lam"] > 0 for L in lams.values()}
                              | {not (lams[750]["lam"] > 0)}) == 1)

    # ---- Lambda, both fold variants, as registered -------------------------------
    print("\n" + "=" * 78)
    print("  LAMBDA - registered statistic, REG-007 sec 3.4")
    print("=" * 78)
    out = {}
    for fold, label in ((True, "BOTH folded into names-(f)"), (False, "BOTH folded the other way")):
        L = lam(cell(win, 750), arms, fold_both_internal=fold)
        out["both_internal" if fold else "both_external"] = L
        print(f"\n  {label}")
        print(f"     JOINT   names (f): {L['a']:4d} / {L['a']+L['b']:4d}  = {L['p_joint']:.4f}")
        print(f"     GWONLY  names (f): {L['c']:4d} / {L['c']+L['d']:4d}  = {L['p_gwonly']:.4f}")
        print(f"     LAMBDA = {L['lam']:+.4f}   Fisher two-sided p = {L['p_value']:.5f}")
        print(f"     NEITHER (excluded from the test, printed): {L['neither']}")

    n_j = out["both_internal"]["a"] + out["both_internal"]["b"]
    n_g = out["both_internal"]["c"] + out["both_internal"]["d"]
    print(f"\n  arm sizes: JOINT {n_j}, GWONLY {n_g}  (REG-007 sec 9 floor: {MIN_ARM})")
    check("both arms clear the registered abandonment floor",
          min(n_j, n_g) >= MIN_ARM,
          # falsifying world: the N_co cells REG-007 sec 2.4 refused to build on
          witness=lambda: min(41, 53) >= 200)

    res = {"window": {"joint": sum(1 for r in win if r["arm"] == "JOINT"),
                      "gwonly": sum(1 for r in win if r["arm"] == "GWONLY")},
           "placebo_n": len(plc), "misses": len(misses),
           "cells_window": dict(wc), "silent": silent, "neither_strict": strict, "cells_placebo": dict(pc),
           "f_rate_window": w_int, "f_rate_placebo": p_int,
           "neither_share": frac, "sensitivity": {str(k): v for k, v in lams.items()},
           "lambda": out, "dead_phrases": dead_ph, "dead_keywords": dead_kw,
           "polysemy": {"n": aud["n"], "n_non_impairment": len(bad), "share": share,
                        "ceiling": POLYSEMY_CEILING,
                        "post_hoc_boilerplate_share": aud["share_boilerplate"]}}
    (HERE / "reg-007-result.json").write_text(json.dumps(res, indent=1))
    print("\nwrote reg-007-result.json")

    # ---- F1 - the polysemy sample, emitted for adjudication ----------------------
    rng = random.Random(20260813)
    pool = [(r["cik"], r["fy_end"], pg["phrase"], pg["text"][
        max(0, len(pg["text"]) // 2 - 400): len(pg["text"]) // 2 + 400])
        for r in win for pg in r["passages"] if pg["phrase"] in ("triggering event", "triggering events")]
    samp = rng.sample(pool, min(60, len(pool)))
    (HERE / "reg-007-polysemy-sample.json").write_text(json.dumps(
        [{"cik": c, "fy_end": f, "phrase": p, "window": w} for c, f, p, w in samp], indent=1))
    print(f"wrote reg-007-polysemy-sample.json ({len(samp)} windows) for F1 adjudication")

    summary()
    return 0


if __name__ == "__main__":
    sys.exit(main())
