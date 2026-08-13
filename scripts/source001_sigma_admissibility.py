#!/usr/bin/env python3
"""SOURCE-001 section 6 step 5's PRECONDITION: the other two counts, and reachability.

NOT A REGISTRATION AND NOT A RESULT. This is a source probe. It reports counts
against denominators so REG-009 can state a scope it can defend. It computes no
estimate, fits nothing, and makes no claim about phi, sigma or delta.

WHY THIS FILE EXISTS.
SOURCE-001 section 2 rejects equity return volatility on THREE independent counts,
"any one of which is fatal":

  (1) it is LEVERED, so it moves with capital structure, which is not in the model;
  (2) it AGGREGATES every asset the firm holds;
  (3) it prices GROWTH OPTIONS that correspond to no recognised asset at all.

Section 4's third candidate family -- the single-dominant-asset restriction -- is
aimed squarely at count (2), and sections 4a and 4b priced how hard it bites there:
99 firms of 1,444 at a 0.70 threshold. Section 6 step 3 then promotes that to
"equity-return volatility for PP&E-dominant firms only, where the restriction is
what makes it admissible under section 2 rather than a proxy in violation of it."

That sentence is one count doing three counts' work. A restaurant chain that is 75
per cent PP&E on the balance sheet is still levered and still holds growth options;
concentration of ASSETS is silent about both. Section 2 said any one count is fatal,
so a restriction that clears exactly one leaves two standing. Running the volatility
probe on the strength of that sentence would commit the WT-038 type error this
document was written to prevent -- with the restriction serving as the alibi.

"levered" and "growth options" appear exactly once each in this repository: in the
sentence that declares them fatal. Nothing between there and section 6 step 3 revisits
them. That is what this probe is for.

WHAT IT MEASURES, and what it deliberately does not.
  count 2  the class share -- carried through from source001_concentration, unchanged.
  count 1  book equity / assets, PERIOD-MATCHED to the same balance sheet the class
           share came off. At book, and only at book: E/A is the deleveraging factor
           E/(D+E) under the accounting identity, and it is the honest cheap version
           of the quantity that turns an equity vol into an asset vol.
  count 3  NOT MEASURED, and the reason is recorded rather than elided. Growth options
           need MARKET equity, and no market-data source is reachable from the
           container this ran in. That is a fact about this instrument, not about the
           firms -- section 3's error, and the one this document keeps meeting.
  reach    can the price series be got at all? Two INDEPENDENT instruments, because
           one instrument agreeing with itself is one instrument: (a) presence in the
           SEC's company_tickers.json, which lists CURRENT registrants only, and
           (b) the panel's own last balance-sheet year, which never touches that file.
  distress is the dominance STRUCTURAL or terminal? A firm in wind-down writes off
           goodwill and sells inventory, and what is left is property -- so distress
           mechanically concentrates a balance sheet. The class share is recomputed at
           every period end the filer reports, and the share LAG_YEARS before the last
           one is reported beside it. A dominance that exists only on the final balance
           sheet is an artifact of dying, and an equity series for such a firm prices
           distress rather than news about an asset.

GUARDS CARRIED AS CODE, following this document's own precedent that the mistake and
its refusal ship together:
  * period matching, inherited from source001_concentration and not re-derived;
  * IMPOSSIBLE refuses a book equity share above 1.05 of assets -- two balance sheets
    divided by each other, loudly, which is section 4a's defect class;
  * THIN refuses any bucket under 30 firms rather than reporting a rate for it
    (section 3b's rule; at a 0.70 threshold the goodwill arm has 18 and IS refused);
  * every between-bucket gap prints a two-proportion z, so a difference has to earn
    the word (section 3b's rule).

Read-only against data.sec.gov. Run from the CLOUD, never darwin -- wealthTensor-24
got darwin IP-flagged doing exactly this.
"""
from __future__ import annotations

import argparse
import json
import math
import pathlib
import statistics
import sys
import threading
import time
import urllib.error
import urllib.request
from collections import Counter, defaultdict
from concurrent.futures import ThreadPoolExecutor

HERE = pathlib.Path(__file__).resolve().parent
DATA = HERE.parent / "data"
CONC = DATA / "source-001-concentration-full.json"
UA = {"User-Agent": "jason c braatz jasoncbraatz@gmail.com"}

CLASSES = {
    "ppe": ("PropertyPlantAndEquipmentNet",),
    "goodwill": ("Goodwill",),
    "intangibles": ("IntangibleAssetsNetExcludingGoodwill",
                    "FiniteLivedIntangibleAssetsNet"),
}
ASSETS = "Assets"
EQUITY = ("StockholdersEquity",
          "StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest")
LIABILITIES = "Liabilities"

IMPOSSIBLE = 1.05        # book equity share above this: two balance sheets, refused
THIN = 30                # section 3b's rule: no rate reported for a bucket under this
LAG_YEARS = 3            # how far back the structural-vs-distress comparison reaches

# The refusal this probe adds, and the reason it is a refusal and not a footnote.
# A class share is a RATIO, and a ratio is silent about its denominator's size. The
# cheapest way for one asset class to be 80 per cent of a balance sheet is for there
# to be almost no balance sheet: this panel's 0.70-dominant set contains a filer with
# total assets of $388, of which $283 is property, and it passes every guard sections
# 4a and 4b carry. Nothing in either section reports a size. So the floors are swept
# rather than assumed -- the count is reported AT EACH, because which floor to use is
# REG-009's choice to defend and this document's job is only to price it.
MATERIALITY_FLOORS = (0.0, 1e6, 1e7, 1e8)

_gate = threading.Lock()
_last = [0.0]
MIN_GAP = 0.15


def _pace() -> None:
    with _gate:
        gap = time.time() - _last[0]
        if gap < MIN_GAP:
            time.sleep(MIN_GAP - gap)
        _last[0] = time.time()


def _get_json(url: str, retries: int = 6):
    """One data.sec.gov call. 404 is the expected case for an untagged concept."""
    for i in range(retries):
        try:
            _pace()
            req = urllib.request.Request(url, headers=UA)
            with urllib.request.urlopen(req, timeout=60) as fh:
                return json.loads(fh.read())
        except urllib.error.HTTPError as e:
            if e.code == 404:
                return None
            if e.code == 429:
                wait = float(e.headers.get("Retry-After") or 0) or (5.0 * (i + 1))
                print(f"!! 429 -- holding the pool {wait:.0f}s", file=sys.stderr,
                      flush=True)
                with _gate:
                    time.sleep(wait)
                    _last[0] = time.time()
                continue
            if i == retries - 1:
                raise
            time.sleep(1.0 + 1.5 * i)
        except Exception:
            if i == retries - 1:
                raise
            time.sleep(1.0 + 1.5 * i)
    return None


def facts_by_period(cik: int, concept: str) -> dict[str, float]:
    """end-date -> USD value from 10-K instants; latest-filed wins, deterministically.

    Byte-identical in behaviour to source001_concentration.facts_by_period. Copied
    rather than imported so this probe reproduces that file's numbers under its own
    roof; the reproduction is asserted in tests, which is what makes the copy safe.
    """
    url = (f"https://data.sec.gov/api/xbrl/companyconcept/"
           f"CIK{cik:010d}/us-gaap/{concept}.json")
    doc = _get_json(url)
    if not doc:
        return {}
    best: dict[str, tuple[str, float]] = {}
    for unit, rows in (doc.get("units") or {}).items():
        if unit != "USD":
            continue
        for r in rows:
            if r.get("form") != "10-K":
                continue
            end, val, filed = r.get("end"), r.get("val"), r.get("filed") or ""
            if end is None or val is None:
                continue
            if end not in best or filed > best[end][0]:
                best[end] = (filed, float(val))
    return {end: v for end, (_f, v) in best.items()}


def two_proportion_z(k1: int, n1: int, k2: int, n2: int) -> float | None:
    """Section 3b's rule: a gap between buckets has to earn the word 'difference'."""
    if n1 == 0 or n2 == 0:
        return None
    p1, p2 = k1 / n1, k2 / n2
    p = (k1 + k2) / (n1 + n2)
    se = math.sqrt(p * (1 - p) * (1 / n1 + 1 / n2))
    if se == 0:
        return None
    return (p1 - p2) / se


def firm_probe(cik: int, dominant: str) -> dict:
    """Counts 1 and 2 for one firm, plus the concentration trajectory.

    The matched period is the one source001_concentration already chose: the LATEST
    end at which total assets and at least one class are both reported. It is
    recomputed here rather than trusted, so a disagreement with the stored record is
    visible instead of silent.
    """
    assets = facts_by_period(cik, ASSETS)
    out: dict = {"cik": cik, "dominant": dominant}
    if not assets:
        out["status"] = "no-assets"
        return out

    cls_facts: dict[str, float] = {}
    for tag in CLASSES[dominant]:
        for end, val in facts_by_period(cik, tag).items():
            cls_facts.setdefault(end, val)
    if not cls_facts:
        out["status"] = "no-class"
        return out

    common = [e for e in assets if e in cls_facts and assets[e] > 0]
    if not common:
        out["status"] = "unmatchable"
        return out
    end = max(common)
    out["end"] = end
    out["assets"] = assets[end]
    out["share"] = cls_facts[end] / assets[end]

    # --- the trajectory: is the dominance structural, or is it terminal? ---
    series = {e: cls_facts[e] / assets[e] for e in common}
    out["share_series"] = {e: round(v, 4) for e, v in sorted(series.items())}
    cutoff = f"{int(end[:4]) - LAG_YEARS}-{end[5:]}"
    earlier = [e for e in common if e <= cutoff]
    if earlier:
        ref = max(earlier)
        out["share_lag"] = series[ref]
        out["share_lag_end"] = ref
    else:
        out["share_lag"] = None
        out["share_lag_end"] = None
        out["lag_absent_reason"] = ("filer reports no matched balance sheet "
                                    f"{LAG_YEARS}+ years before {end}")

    # --- count 1: book equity / assets, on THAT balance sheet ---
    eq: dict[str, float] = {}
    for tag in EQUITY:
        for e, v in facts_by_period(cik, tag).items():
            eq.setdefault(e, v)
    equity = eq.get(end)
    if equity is None:
        liab = facts_by_period(cik, LIABILITIES).get(end)
        if liab is not None:
            equity = assets[end] - liab
            out["equity_source"] = "assets-minus-liabilities"
    else:
        out["equity_source"] = "stockholders-equity"

    if equity is None:
        out["status"] = "no-equity"
        out["ea"] = None
        return out

    ea = equity / assets[end]
    if ea > IMPOSSIBLE:
        out["status"] = "refused-impossible-equity"
        out["ea"] = ea
        return out

    out["ea"] = ea
    out["status"] = "ok"
    return out


def pct(k: int, n: int) -> str:
    return f"{k}/{n} = {k/n:.3f}" if n else f"{k}/{n} = --"


def floor_label(f: float) -> str:
    if f <= 0:
        return "none"
    if f >= 1e9:
        return f"${f/1e9:g}B"
    return f"${f/1e6:g}M"


def report(conc: dict, rows: list, reach_a: dict | None, reach_b: dict,
           threshold: float) -> None:
    """Everything printed, from the per-firm records alone.

    Separated from the fetch so the whole report regenerates offline from the
    committed artifact -- which is what lets a test assert the document against it
    without 400 SEC calls. Section 3a committed a per-record file precisely so its
    table would be auditable, and then nothing audited it for a session; the split
    here is that lesson wearing a seatbelt.
    """
    by_cls: dict[str, list] = defaultdict(list)
    for r in rows:
        by_cls[r["dominant"]].append(r)
    ok = [r for r in rows if r.get("status") == "ok"]

    print("\n" + "=" * 78)
    print("COUNT 2 (aggregation) -- the count the restriction was built for")
    print("=" * 78)
    for cls in ("ppe", "goodwill", "intangibles"):
        sub = by_cls.get(cls, [])
        sh = [r["share"] for r in sub if r.get("share") is not None]
        if not sh:
            continue
        thin = "  [THIN -- rate refused]" if len(sub) < THIN else ""
        print(f"  {cls:<12} n={len(sub):<3} median class share "
              f"{statistics.median(sh):.3f}{thin}")

    print("\n" + "=" * 78)
    print("MATERIALITY -- the refusal sections 4a and 4b do not carry")
    print("  A class share is a ratio and a ratio is silent about its denominator.")
    print("  The count is reported at each floor because the floor is REG-009's")
    print("  choice to defend; this probe's job is only to price it.")
    print("=" * 78)
    print(f"  {'floor':<8} {'firms':>5}   {'composition':<34} "
          f"{'median assets':>14}  {'current reg.':>12}")
    for f in MATERIALITY_FLOORS:
        sub = [r for r in ok if r["assets"] >= f]
        if not sub:
            continue
        comp = Counter(r["dominant"] for r in sub)
        med = statistics.median([r["assets"] for r in sub])
        line = (f"  {floor_label(f):<8} {len(sub):>5}   "
                f"{', '.join(f'{k} {comp[k]}' for k in ('ppe','goodwill','intangibles')):<34} "
                f"{'$'+format(med/1e6, '.3g')+'M':>14}")
        if reach_a is not None:
            k = sum(1 for r in sub if reach_a.get(r["cik"]))
            line += f"  {pct(k, len(sub)):>12}"
        if len(sub) < THIN:
            line += "  [THIN]"
        print(line)

    base = conc["firms"]
    for f in (1e6, 1e7):
        kd = sum(1 for r in ok if r["assets"] < f)
        nd = len(ok)
        comp_pop = [x for x in base
                    if max(x["shares"].values(), default=0.0) < threshold]
        kc = sum(1 for x in comp_pop if x["assets"] < f)
        z = two_proportion_z(kd, nd, kc, len(comp_pop))
        print(f"\n  under {floor_label(f)}: dominant-{threshold:.2f} {pct(kd, nd)}"
              f"   vs complement {pct(kc, len(comp_pop))}"
              + (f"   z = {z:+.2f}" if z is not None else ""))

    print("\n  and the trade the threshold actually makes:")
    print(f"  {'threshold':>10} {'firms':>6} {'median assets':>15} {'under $1M':>14}")
    for t in (0.50, 0.60, 0.70, 0.80):
        sub = [x for x in base if max(x["shares"].values(), default=0.0) >= t]
        med = statistics.median([x["assets"] for x in sub])
        k = sum(1 for x in sub if x["assets"] < 1e6)
        print(f"  {t:>10.2f} {len(sub):>6} {'$'+format(med/1e6, '.3g')+'M':>15} "
              f"{pct(k, len(sub)):>14}")

    print("\n" + "=" * 78)
    print("COUNT 1 (leverage) -- book equity / assets, ON THE SAME BALANCE SHEET")
    print("  E/A is the deleveraging factor E/(D+E). sigma_asset ~ sigma_equity * E/A,")
    print("  so a firm at E/A = 0.25 has an equity vol about FOUR TIMES its asset vol.")
    print("  Reported at floor 0 AND at $10M: at floor 0 the median is dominated by")
    print("  book-insolvent shells, which is a true number about a population that")
    print("  cannot carry the design.")
    print("=" * 78)
    for f in (0.0, 1e7):
        print(f"\n  --- materiality floor {floor_label(f)} ---")
        lev = {}
        for cls in ("ppe", "goodwill", "intangibles"):
            sub = [r for r in by_cls.get(cls, [])
                   if r.get("status") == "ok" and r["assets"] >= f]
            ea = sorted(r["ea"] for r in sub)
            if not ea:
                continue
            n = len(ea)
            lo = sum(1 for v in ea if v < 0.50)
            lev[cls] = (lo, n)
            thin = "  [THIN -- rate refused]" if n < THIN else ""
            print(f"  {cls:<12} n={n:<3} median E/A {statistics.median(ea):>7.3f}  "
                  f"IQR [{ea[n//4]:>7.3f}, {ea[(3*n)//4]:>6.3f}]  "
                  f"E/A < 0.50: {pct(lo, n)}{thin}")
        allsub = sorted(r["ea"] for r in ok if r["assets"] >= f)
        if allsub:
            n = len(allsub)
            print(f"  {'ALL':<12} n={n:<3} median E/A {statistics.median(allsub):>7.3f}"
                  f"   implied sigma_equity/sigma_asset ~ "
                  f"{1/statistics.median(allsub):.1f}x"
                  if statistics.median(allsub) > 0 else
                  f"  {'ALL':<12} n={n:<3} median E/A "
                  f"{statistics.median(allsub):>7.3f}   (book-insolvent median)")
        if "ppe" in lev and "intangibles" in lev:
            z = two_proportion_z(*lev["ppe"], *lev["intangibles"])
            if z is not None:
                # A z BETWEEN two THIN buckets is still the right statistic -- it
                # accounts for n -- but the rates it compares were refused above,
                # so it is labelled rather than printed bare. Suppressing it would
                # hide information; printing it unlabelled would launder a refusal.
                thin = "  [both buckets THIN -- the RATES above are refused; " \
                       "this z is the comparison, not a licence to quote them]" \
                    if min(lev["ppe"][1], lev["intangibles"][1]) < THIN else ""
                print(f"  ppe vs intangibles, share below E/A 0.50: "
                      f"z = {z:+.2f}{thin}")


    print("\n" + "=" * 78)
    print("COUNT 3 (growth options) -- NOT MEASURED")
    print("=" * 78)
    print("  Growth options need MARKET equity; no market-data source was reachable")
    print("  from the container this ran in. That is a statement about the")
    print("  INSTRUMENT and not about the firms -- section 3's error, refused here")
    print("  by naming it rather than by reporting a zero. What would close it:")
    print("  market cap at each matched period end, hence market-to-book, from a")
    print("  delisted-inclusive price source.")

    print("\n" + "=" * 78)
    print("STRUCTURAL OR TERMINAL -- the class share LAG_YEARS before the last one")
    print(f"  (LAG_YEARS = {LAG_YEARS}. A dominance present only on the final balance")
    print("   sheet is an artifact of dying; an equity series for such a firm prices")
    print("   distress rather than news about the asset.)")
    print("=" * 78)
    for cls in ("ppe", "goodwill", "intangibles"):
        sub = by_cls.get(cls, [])
        with_lag = [r for r in sub if r.get("share_lag") is not None]
        if not with_lag:
            print(f"  {cls:<12} n={len(sub):<3} no firm has a matched balance sheet "
                  f"{LAG_YEARS}+ years earlier")
            continue
        already = sum(1 for r in with_lag if r["share_lag"] >= threshold)
        deltas = sorted(r["share"] - r["share_lag"] for r in with_lag)
        thin = "  [THIN -- rate refused]" if len(with_lag) < THIN else ""
        print(f"  {cls:<12} n={len(sub):<3} lag observable for {len(with_lag)}; "
              f"already dominant {LAG_YEARS}y earlier: {pct(already, len(with_lag))}"
              f"  median rise {statistics.median(deltas):+.3f}{thin}")
    print("  NOTE: the lag is unobservable for the majority precisely BECAUSE these")
    print("  firms are short-lived filers -- so this bucket is itself selected, and")
    print("  the rates above describe the firms that lived long enough to be asked.")

    print("\n" + "=" * 78)
    print("REACH -- can the price series be got at all? TWO INDEPENDENT INSTRUMENTS")
    print("  (a) presence in the SEC's CURRENT-registrant file, and (b) the panel's")
    print("  own last balance-sheet year, which never touches that file. (a) alone")
    print("  is a lower bound and CANNOT establish that no price series exists.")
    print("=" * 78)
    for cls in ("ppe", "goodwill", "intangibles"):
        sub = by_cls.get(cls, [])
        if not sub:
            continue
        yrs = sorted(reach_b[r["cik"]] for r in sub)
        line = (f"  {cls:<12} n={len(sub):<3} "
                f"(b) median last fy_end {statistics.median(yrs):.0f}, "
                f"<=2019: {pct(sum(1 for y in yrs if y <= 2019), len(yrs))}")
        if reach_a is not None:
            k = sum(1 for r in sub if reach_a.get(r["cik"]))
            line += f"   (a) current registrant: {pct(k, len(sub))}"
        if len(sub) < THIN:
            line += "  [THIN]"
        print(line)
    if reach_a is not None:
        for lo, hi, lab in ((0, 2019, "<=2019"), (2020, 2022, "2020-2022"),
                            (2023, 9999, ">=2023")):
            sub = [r for r in rows if lo <= reach_b[r["cik"]] <= hi]
            k = sum(1 for r in sub if reach_a.get(r["cik"]))
            print(f"    cross-check, last fy_end {lab:<10} {pct(k, len(sub))}")
        p = by_cls.get("ppe", [])
        i = by_cls.get("intangibles", [])
        z = two_proportion_z(sum(1 for r in p if reach_a.get(r["cik"])), len(p),
                             sum(1 for r in i if reach_a.get(r["cik"])), len(i))
        if z is not None:
            print(f"\n  ppe vs intangibles, current-registrant rate: z = {z:+.2f}")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--threshold", type=float, default=0.70)
    ap.add_argument("--conc", default=str(CONC))
    ap.add_argument("--tickers", default="", help="SEC company_tickers.json (offline)")
    ap.add_argument("--from-json", default="",
                    help="regenerate the report from a previous --out artifact, "
                         "offline. The artifact is the evidence; this proves it.")
    ap.add_argument("--out", default="")
    ap.add_argument("--workers", type=int, default=4)
    args = ap.parse_args()

    conc = json.loads(pathlib.Path(args.conc).read_text())
    firms = conc["firms"]

    if args.from_json:
        art = json.loads(pathlib.Path(args.from_json).read_text())
        rows = art["firms"]
        reach_a = ({int(k): v for k, v in art["reach_current_registrant"].items()}
                   if art.get("reach_current_registrant") else None)
        reach_b = {int(k): v for k, v in art["reach_last_fy_end"].items()}
        print(f"# regenerated OFFLINE from {args.from_json}: "
              f"{art['n_dominant']} firms at >= {art['threshold']:.2f}")
        report(conc, rows, reach_a, reach_b, art["threshold"])
        return 0

    hit = [f for f in firms
           if max(f["shares"].values(), default=0.0) >= args.threshold]
    dom = {f["cik"]: max(f["shares"], key=f["shares"].get) for f in hit}
    print(f"# dominant-asset firms at >= {args.threshold:.2f}: {len(hit)} "
          f"of {conc['n_matchable']} matchable panel firms", flush=True)

    reach_a = None
    if args.tickers:
        tk = json.loads(pathlib.Path(args.tickers).read_text())
        listed = {int(v["cik_str"]) for v in tk.values()}
        reach_a = {f["cik"]: (f["cik"] in listed) for f in hit}
        print(f"# company_tickers.json: {len(listed)} distinct CIKs (CURRENT "
              f"registrants only -- a delisted filer is absent BY CONSTRUCTION)")
        print(f"# panel base rate: "
              f"{pct(sum(1 for f in firms if f['cik'] in listed), len(firms))}")
    reach_b = {f["cik"]: int(f["end"][:4]) for f in hit}

    def safe(f):
        try:
            return firm_probe(f["cik"], dom[f["cik"]])
        except Exception as e:  # noqa: BLE001
            print(f"!! ERROR cik={f['cik']}: {e}", file=sys.stderr, flush=True)
            return {"cik": f["cik"], "dominant": dom[f["cik"]], "status": "error"}

    rows = []
    with ThreadPoolExecutor(max_workers=args.workers) as ex:
        for i, res in enumerate(ex.map(safe, hit), 1):
            rows.append(res)
            if i % 25 == 0:
                print(f"#   {i}/{len(hit)}", file=sys.stderr, flush=True)

    report(conc, rows, reach_a, reach_b, args.threshold)

    if args.out:
        pathlib.Path(args.out).write_text(json.dumps({
            "threshold": args.threshold,
            "lag_years": LAG_YEARS,
            "thin": THIN,
            "impossible": IMPOSSIBLE,
            "materiality_floors": list(MATERIALITY_FLOORS),
            "n_dominant": len(hit),
            "n_matchable_panel": conc["n_matchable"],
            "count3_measured": False,
            "count3_reason": "no market-data source reachable from this container; "
                             "growth options need market equity",
            "reach_current_registrant": ({str(k): v for k, v in reach_a.items()}
                                         if reach_a else None),
            "reach_last_fy_end": {str(k): v for k, v in reach_b.items()},
            "firms": rows,
        }, indent=1))
        print(f"\nwrote {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
