#!/usr/bin/env python3
"""REG-008 feasibility probes. Reads the COMMITTED REG-007 corpus, computes no statistic
that any REG-008 prediction depends on. Declared in REG-008 section 2."""
import gzip, json, re, collections, random, sys

D = json.loads(gzip.open("data/reg-007-passages.json.gz", "rt").read())
print("schema:", D["schema"], "| half_widths:", D["half_widths"])
fy = D["firm_years"]
print("firm_years:", len(fy), "| misses:", len(D["misses"]))
arms = collections.Counter(r["arm"] for r in fy)
print("arms:", dict(arms))
print("passages:", sum(len(r["passages"]) for r in fy))

# ---- 1. window geometry: absolute offsets are recoverable, so overlaps are mergeable ----
HALF = max(D["half_widths"])
tot_p = tot_span = 0
overl = 0
per_fy_spans = []
for r in fy:
    iv = []
    for p in r["passages"]:
        a = max(0, p["at"] - HALF)
        b = a + len(p["text"])
        assert p["text"] , "empty"
        iv.append((a, b))
    iv.sort()
    merged = []
    for a, b in iv:
        if merged and a <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], b); overl += 1
        else:
            merged.append([a, b])
    tot_p += len(iv); tot_span += len(merged)
    per_fy_spans.append(len(merged))
print(f"passages {tot_p} -> merged spans {tot_span} ({overl} overlaps absorbed)")
print("spans per firm-year: median", sorted(per_fy_spans)[len(per_fy_spans)//2],
      "max", max(per_fy_spans))

# ---- 2. sentence-boundary truncation at the window edge ----
END = re.compile(r"[.!?]")
trunc = ok = 0
for r in fy[:400]:
    for p in r["passages"]:
        t = p["text"]
        i = t.lower().find(p["phrase"])
        if i < 0:
            continue
        left = t[:i]; right = t[i:]
        has_l = bool(END.search(left)) or p["at"] - HALF <= 0
        has_r = bool(END.search(right))
        (ok if (has_l and has_r) else trunc).__class__  # noop
        if has_l and has_r: ok += 1
        else: trunc += 1
print(f"phrase occurrences with sentence boundaries on BOTH sides inside the window: "
      f"{ok}/{ok+trunc} = {ok/(ok+trunc):.4f}  (truncated {trunc})")

# ---- 3. 'reporting unit' presence and named-unit candidates ----
RU = re.compile(r"reporting units?", re.I)
GENERIC = {"the","a","an","each","our","its","their","one","that","this","these","those",
           "such","any","certain","both","all","no","single","same","other","others",
           "remaining","applicable","respective","relevant","affected","two","three",
           "four","five","of","and","or","its","which","whose","company's","companys"}
NAMED = re.compile(r"((?:[A-Z][A-Za-z0-9&./'\-]*)(?:\s+(?:and|of|&|the)?\s*[A-Z][A-Za-z0-9&./'\-]*){0,4})\s+reporting unit\b")
QUOTED = re.compile(r"[\"“]([^\"”]{2,60})[\"”]\s+reporting unit\b", re.I)

n_ru = 0
names = collections.Counter()
fy_with_named = 0
for r in fy:
    blob = " ".join(p["text"] for p in r["passages"])
    if RU.search(blob):
        n_ru += 1
    got = False
    for m in NAMED.finditer(blob):
        cand = m.group(1).strip()
        toks = cand.split()
        while toks and toks[0].lower() in GENERIC:
            toks = toks[1:]
        if not toks:
            continue
        cand = " ".join(toks)
        if cand.lower() in GENERIC or len(cand) < 2:
            continue
        names[cand] += 1; got = True
    if got:
        fy_with_named += 1
print(f"firm-years whose passages mention 'reporting unit': {n_ru}/{len(fy)}")
print(f"firm-years with >=1 NAMED-unit candidate: {fy_with_named}/{len(fy)}")
print("top 30 candidate names:", names.most_common(30))
print("distinct candidates:", len(names))

# by arm
byarm = collections.Counter(); tot = collections.Counter()
for r in fy:
    blob = " ".join(p["text"] for p in r["passages"])
    tot[r["arm"]] += 1
    for m in NAMED.finditer(blob):
        cand = " ".join(t for t in m.group(1).split() if t.lower() not in GENERIC)
        if cand:
            byarm[r["arm"]] += 1
            break
print("named-unit rate by arm:", {k: f"{byarm[k]}/{tot[k]}={byarm[k]/tot[k]:.3f}" for k in tot})

# ---- 4. the two DEAD keywords, corrected wording ----
for s in ["composition of its net assets",
          "composition or carrying amount of its net assets",
          "carrying amount of its net assets",
          "goodwill impairment loss in the financial statements of a subsidiary",
          "impairment loss recognized in the financial statements of a subsidiary",
          "financial statements of a subsidiary",
          "recoverability of a significant asset group"]:
    c = sum(1 for r in fy if any(s in p["text"].lower() for p in r["passages"]))
    print(f"  [{s!r}] firm-years: {c}")

# ---- 5. dated / amount markers ----
DATE = re.compile(r"\b(?:first|second|third|fourth) quarter\b|\bQ[1-4]\s+20\d\d\b|"
                  r"\b(?:January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2}?,?\s*20\d\d\b|"
                  r"\b(?:three|six|nine|twelve) months ended\b", re.I)
AMT = re.compile(r"\$\s?\d[\d,.]*\s*(?:million|billion|thousand)?", re.I)
d = a = 0
for r in fy:
    blob = " ".join(p["text"] for p in r["passages"])
    d += bool(DATE.search(blob)); a += bool(AMT.search(blob))
print(f"firm-years with a DATE marker anywhere in passages: {d}/{len(fy)}")
print(f"firm-years with an AMOUNT marker anywhere in passages: {a}/{len(fy)}")
