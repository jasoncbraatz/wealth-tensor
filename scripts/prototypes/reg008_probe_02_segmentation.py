#!/usr/bin/env python3
"""REG-008 probe 3 - ARM-BLIND. Sentence segmentation feasibility + INTERNAL head."""
import gzip, json, re

D = json.loads(gzip.open("data/reg-007-passages.json.gz", "rt").read())
fy = []
for r in D["firm_years"]:
    r = dict(r)
    for k in ("arm", "G", "t_sum", "A", "universe", "sic"):
        r.pop(k, None)
    fy.append(r)

INTERNAL = ["recoverability of a significant asset group", "asset group",
            "carrying amount of its net assets", "composition of its net assets",
            "long-lived asset impairment", "tested for recoverability",
            "recognition of a goodwill impairment loss in the financial statements of a subsidiary",
            "held for sale", "disposal group"]
print("-- INTERNAL (f)-family, firm-years hit / %d --" % len(fy))
for k in INTERNAL:
    c = sum(1 for r in fy if any(k in p["text"].lower() for p in r["passages"]))
    print(f"  {c:5d}  {k}")

# ---------------- the registered segmenter, candidate form ----------------
ABBR = ("U.S.|U.K.|Inc.|Corp.|Co.|Ltd.|LLC.|L.P.|L.L.C.|No.|Nos.|St.|Mr.|Mrs.|Ms.|Dr.|"
        "Jr.|Sr.|vs.|etc.|e.g.|i.e.|Fig.|approx.|Sec.|Art.|Ch.|pp.|Ph.D.|A.M.|P.M.|"
        "Jan.|Feb.|Mar.|Apr.|Jun.|Jul.|Aug.|Sept.|Sep.|Oct.|Nov.|Dec.").split("|")
DOT = "\x00"

def segment(text: str) -> list[str]:
    t = text
    for a in ABBR:                                   # protect known abbreviations
        t = t.replace(a, a.replace(".", DOT))
    t = re.sub(r"(\d)\.(\d)", r"\1" + DOT + r"\2", t)          # decimals
    t = re.sub(r"\b([A-Z])\.(?=[A-Z]\.)", r"\1" + DOT, t)      # initialisms A.B.C.
    t = re.sub(r"\b([A-Z])\.(?=\s[A-Z][a-z])", r"\1" + DOT, t) # initial before name
    parts = re.split(r"(?<=[.!?])\s+(?=[\"'(\[]?[A-Z0-9$])", t)
    return [p.replace(DOT, ".").strip() for p in parts if p.strip()]

PH = tuple(D["phrases"])
n = with_ru = 0
lens = []
samples = []
for r in fy[:600]:
    for p in r["passages"]:
        for s in segment(p["text"]):
            sl = s.lower()
            if any(x in sl for x in PH):
                n += 1; lens.append(len(s))
                if "reporting unit" in sl:
                    with_ru += 1
                if len(samples) < 6 and 80 < len(s) < 400:
                    samples.append(s)
lens.sort()
print(f"\ntrigger-bearing SENTENCES (first 600 firm-years): {n}")
print(f"  median {lens[len(lens)//2]} chars · p95 {lens[int(.95*len(lens))]} · max {lens[-1]}")
print(f"  >600 chars (segmentation suspect): {sum(1 for x in lens if x>600)/len(lens):.3f}")
print(f"  sharing a sentence with 'reporting unit': {with_ru} = {with_ru/max(1,n):.3f}")
print("\n-- sample sentences --")
for s in samples:
    print("   *", s[:300])
