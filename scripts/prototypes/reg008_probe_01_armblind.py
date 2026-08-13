#!/usr/bin/env python3
"""REG-008 probe 2 - ARM-BLIND BY CONSTRUCTION. The arm key is deleted from every row
before anything is counted, so no quantity here can be conditioned on the comparison."""
import gzip, json, re, collections

D = json.loads(gzip.open("data/reg-007-passages.json.gz", "rt").read())
fy = []
for r in D["firm_years"]:
    r = dict(r)
    for k in ("arm", "G", "t_sum", "A", "universe", "sic"):
        r.pop(k, None)          # arm-blind AND universe-blind, enforced not promised
    fy.append(r)
print("arm-blind rows:", len(fy))

INTERNAL = ["recoverability of a significant asset group", "asset group",
            "carrying amount of its net assets", "composition of its net assets",
            "long-lived asset impairment", "tested for recoverability",
            "recognition of a goodwill impairment loss in the financial statements of a subsidiary",
            "held for sale", "disposal group"]
EXTERNAL = ["macroeconomic", "economic conditions", "industry", "market conditions",
            "competitive", "regulatory", "raw material", "labor costs",
            "declining cash flows", "decline in revenue", "decline in earnings",
            "loss of a customer", "management", "key personnel", "litigation",
            "bankruptcy", "share price", "stock price", "market capitalization",
            "interest rate", "discount rate"]

print("\n-- INTERNAL (f)-family keyword resolution, firm-years hit / %d --" % len(fy))
for k in INTERNAL:
    c = sum(1 for r in fy if any(k in p["text"].lower() for p in r["passages"]))
    print(f"  {c:5d}  {k}")
print("\n-- EXTERNAL, firm-years hit --")
for k in EXTERNAL:
    c = sum(1 for r in fy if any(k in p["text"].lower() for p in r["passages"]))
    print(f"  {c:5d}  {k}")

# candidate corrected/alternative (f) phrasings firms might actually use
print("\n-- candidate replacements for the two DEAD keywords --")
for k in ["composition or carrying amount", "net assets of the reporting unit",
          "carrying amount of the reporting unit", "significant asset group",
          "recoverability of", "tested for recoverability", "test for recoverability",
          "recoverability test", "more likely than not that", "held-for-sale",
          "sale of a business", "divestiture", "deconsolidat"]:
    c = sum(1 for r in fy if any(k in p["text"].lower() for p in r["passages"]))
    print(f"  {c:5d}  {k}")

# sentence-level: how often does a trigger phrase share a SENTENCE with 'reporting unit'?
ABBR = r"(?:U\.S|Inc|Corp|Co|Ltd|LLC|L\.P|No|Nos|St|Mr|Mrs|Ms|Dr|Jr|Sr|vs|etc|e\.g|i\.e|Fig|approx|Sec|Art|Ch|pp)"
SPLIT = re.compile(r"(?<![A-Z])(?<!" + ABBR + r")(?<!\s\d)(?<![\d,]\d)\.\s+(?=[A-Z(\"'$])")
PH = tuple(D["phrases"])
n_sent = with_ru = 0
lens = []
for r in fy[:600]:
    for p in r["passages"]:
        for s in SPLIT.split(p["text"]):
            sl = s.lower()
            if any(x in sl for x in PH):
                n_sent += 1; lens.append(len(s))
                if "reporting unit" in sl:
                    with_ru += 1
lens.sort()
print(f"\ntrigger-bearing SENTENCES (first 600 firm-years): {n_sent}")
print(f"  median length {lens[len(lens)//2]} chars, p95 {lens[int(.95*len(lens))]}, max {lens[-1]}")
print(f"  sharing a sentence with 'reporting unit': {with_ru} = {with_ru/max(1,n_sent):.3f}")
