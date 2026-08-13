"""Guard audit: does the registered tier-0 tag list see the long-lived-asset
impairments that exist in the registered sample's own firms?

Counts FACTS, not events. Registers nothing. Derives no statistic that any
RESULT file publishes. This is at-bat 3's question asked of at-bat 1's tier.
"""
import json, urllib.request, sys, time
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor

H = {"User-Agent": "jason c braatz jasoncbraatz@gmail.com"}

REGISTERED_T0 = ("ImpairmentOfLongLivedAssetsHeldAndUsed",
                 "TangibleAssetImpairmentCharges",
                 "ImpairmentOfLeasehold")
CANDIDATE     = "ImpairmentOfLongLivedAssetsHeldForUse"
OTHERS        = ("GoodwillImpairmentLoss",
                 "ImpairmentOfIntangibleAssetsFinitelived",
                 "ImpairmentOfIntangibleAssetsIndefinitelivedExcludingGoodwill",
                 "AssetImpairmentCharges",
                 "ImpairmentOfLongLivedAssetsToBeDisposedOf",
                 "GoodwillAndIntangibleAssetImpairment")
ALL = REGISTERED_T0 + (CANDIDATE,) + OTHERS

def facts(cik):
    u = f"https://data.sec.gov/api/xbrl/companyfacts/CIK{int(cik):010d}.json"
    for attempt in range(3):
        try:
            r = urllib.request.Request(u, headers=H)
            return json.loads(urllib.request.urlopen(r, timeout=60).read())
        except Exception as e:
            if "404" in str(e): return None
            time.sleep(1.5 * (attempt + 1))
    return None

def count(cik):
    f = facts(cik)
    if not f: return cik, None
    gaap = f.get("facts", {}).get("us-gaap", {})
    out = {}
    for t in ALL:
        node = gaap.get(t)
        if not node: out[t] = 0; continue
        n = 0
        for unit, rows in node.get("units", {}).items():
            for r in rows:
                fy = r.get("fy")
                if fy and 2013 <= int(fy) <= 2024: n += 1
        out[t] = n
    return cik, out

if __name__ == "__main__":
    d = json.load(open("/tmp/events.json"))
    ciks, uni = [], {}
    for uname, u in d["universes"].items():
        for e in u["events"]:
            c = int(e["cik"])
            if c not in uni: uni[c] = uname; ciks.append(c)
    print(f"firms with events in registered sample: {len(ciks)}", flush=True)
    res = {}
    with ThreadPoolExecutor(max_workers=6) as ex:
        for i, (c, o) in enumerate(ex.map(count, ciks)):
            if o: res[c] = o
            if (i+1) % 40 == 0: print(f"  {i+1}/{len(ciks)}", flush=True)
    json.dump({str(k): v for k, v in res.items()}, open("/home/claude/wt/tagcounts.json","w"))

    print(f"\nfirms resolved: {len(res)}")
    print(f"\n{'tag':62s} {'facts':>8s} {'firms>0':>8s}")
    for t in ALL:
        tot = sum(v[t] for v in res.values()); fr = sum(1 for v in res.values() if v[t] > 0)
        mark = "  <-- REGISTERED tier 0" if t in REGISTERED_T0 else ("  <-- CANDIDATE" if t == CANDIDATE else "")
        print(f"{t:62s} {tot:8d} {fr:8d}{mark}")

    reg_firms = {c for c,v in res.items() if any(v[t] > 0 for t in REGISTERED_T0)}
    cand_firms = {c for c,v in res.items() if v[CANDIDATE] > 0}
    print(f"\nfirms seen by REGISTERED tier-0 list : {len(reg_firms)}")
    print(f"firms seen by CANDIDATE tag alone    : {len(cand_firms)}")
    print(f"firms the candidate ADDS (unseen)    : {len(cand_firms - reg_firms)}")
    print(f"firms only the registered list sees  : {len(reg_firms - cand_firms)}")
    print(f"union                                : {len(reg_firms | cand_firms)}")
