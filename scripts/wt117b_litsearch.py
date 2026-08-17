#!/usr/bin/env python3
"""wt117b_litsearch.py -- the prior-art search instrument, v2.  READ THIS HEADER.

WHAT v1 (wt117_litsearch.py) GOT WRONG, RECORDED BECAUSE IT IS THE LESSON
-------------------------------------------------------------------------
v1's calibration limb was `apparatus_valid = (positive_control_screened_in > 0)`.
It returned TRUE on ONE screened-in hit across FOUR positive controls, while ten of
its API calls had errored out.  Three of four controls -- including one whose subject
(capital income tax and the Pareto tail of wealth) has a famous Econometrica paper
sitting on it -- returned nothing, and the gate said the apparatus was fine.

That is the WT-092 shape one storey up: a calibration limb that measures its own
bookkeeping instead of the world.  `> 0` over a SUM cannot distinguish "every control
fired" from "one fired and three silently failed".

v2 replaces it with two harder tests:

  TIER K -- KNOWN-ITEM RETRIEVAL.  Nine works this session can name in advance, that
            certainly exist, and that a competent search of this question would have
            to surface.  For each, the instrument searches its TITLE and checks whether
            the true work comes back.  A search apparatus that cannot retrieve a paper
            you KNOW is there has zeros that mean nothing.  This is the ceiling.
            Reported per item, not summed.

  TIER P -- topical positive controls, now scored PER QUERY.  apparatus_valid requires
            EVERY positive control to screen in at least one hit, and names any that
            did not.

  TIER N -- negative controls (the floor) unchanged in spirit: well-formed absurd
            conjunctions that must screen in zero.

Also new in v2: OpenAlex is the primary index (250M works, full metadata, no key, no
aggressive rate limit).  Semantic Scholar rate-limited v1 on 10 of 14 calls, and a
source that fails two thirds of the time is not a source, it is a coin.

SEARCH BY THE SHAPE OF THE EQUATION, NOT BY THE SUBJECT MATTER
--------------------------------------------------------------
(blackbook 2026-08-12, the Bateman priority search.)  The object is

    x' = A x + k      Kesten recursion, tail index a solving  E[A^a] = 1

    STOCK levy   A -> (1-t)A                  SCALES the multiplier
    FLOW  levy   A -> A - r*(A-1)^+           TRUNCATES the multiplier

Five vocabularies carry these same two operations: economics (wealth vs capital-income
tax), applied probability (random difference equations / perpetuities), statistical
physics (multiplicative processes with a wall), actuarial mathematics (proportional vs
stop-loss reinsurance on a heavy tail), and public finance (Domar-Musgrave loss offset).
TIER T asks in all five.

USAGE
    python3 wt117b_litsearch.py --out /tmp/wt117b-results.json --md /tmp/wt117b.md
"""

import argparse
import json
import re
import sys
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

MAILTO = "jasoncbraatz@gmail.com"
UA = "wealth-tensor-litsearch/2.0 (mailto:%s)" % MAILTO

# ------------------------------------------------------------------ TIER K
# (author-ish, year, title-as-searched, why it is a fair known-item test)
KNOWN_ITEMS = [
    ("Benhabib, Bisin & Zhu", 2011,
     "The distribution of wealth and fiscal policy in economies with finitely lived agents",
     "Econometrica. Derives the Pareto tail of wealth and how capital-income and estate "
     "taxes move it. If the apparatus misses this, its zeros are worthless."),
    ("Kesten", 1973,
     "Random difference equations and renewal theory for products of random matrices",
     "The theorem the whole question rests on."),
    ("Goldie", 1991,
     "Implicit renewal theory and tails of solutions of random equations",
     "The E[A^alpha]=1 characterisation in its standard form."),
    ("Gabaix", 2009, "Power laws in economics and finance",
     "The canonical survey; any competent index has it."),
    ("Gabaix, Lasry, Lions & Moll", 2016,
     "The dynamics of inequality", "Econometrica; random growth and the top tail."),
    ("Guvenen, Kambourov, Kuruscu, Ocampo & Chen", 2023,
     "Use it or lose it: efficiency gains from wealth taxation",
     "The closest published STOCK-vs-FLOW tax comparison under heterogeneous returns."),
    ("Piketty & Saez", 2013, "A theory of optimal inheritance taxation",
     "Anchor of the optimal-taxation-with-Pareto-tails literature the docs name."),
    ("Saez & Stantcheva", 2018, "A simpler theory of optimal capital taxation",
     "Same literature, the other anchor."),
    ("Nirei & Aoki", 2016,
     "Pareto distribution of income in neoclassical growth models",
     "Explicitly computes how a capital-income tax moves the Pareto exponent."),
    ("Toda", 2019, "Wealth distribution with random discount factors",
     "Modern Kesten-in-economics; tests coverage of the probability-flavoured wing."),
    ("Benhabib, Bisin & Zhu", 2015,
     "The wealth distribution in Bewley economies with capital income risk",
     "JET companion to the 2011 paper."),
    ("Beare & Toda", 2022,
     "Determination of Pareto exponents in economic models driven by Markov multiplicative processes",
     "The most general modern statement of the tail-index machinery."),
]

# ------------------------------------------------------------------ TIER P / T / N
QUERIES = [
    # ---- TIER P: topical positive controls, scored PER QUERY.
    ("P", "P1", "Kesten process wealth distribution Pareto tail",
     "Kesten-in-economics is a large literature; a zero here is an apparatus failure."),
    ("P", "P2", "capital income taxation Pareto tail wealth distribution",
     "Benhabib-Bisin-Zhu sits exactly here."),
    ("P", "P3", "wealth tax capital income tax heterogeneous returns inequality",
     "Guvenen et al., Boar-Midrigan, Kina-Slavik-Yazici."),
    ("P", "P4", "random growth model top wealth inequality power law",
     "Gabaix-Lasry-Lions-Moll, Jones, Nirei."),
    ("P", "P5", "taxation Pareto exponent income distribution",
     "Nirei-Aoki; the exponent-moves-with-the-tax result."),

    # ---- TIER T: the target, in five vocabularies.
    ("T", "T1", "truncated growth multiplier tail index taxation wealth",
     "A paper saying a tax that truncates A steepens or destroys the power law."),
    ("T", "T2", "capital gains tax reduces variance of returns wealth inequality tail",
     "Gain-contingent tax -> Var[log A] -> alpha."),
    ("T", "T3", "multiplicative process bounded growth rate loses power law tail",
     "Applied probability: ess-sup A < 1 kills the Kesten tail."),
    ("T", "T4", "random difference equation truncated multiplier tail behaviour",
     "Perpetuity vocabulary for the same operation."),
    ("T", "T5", "proportional taxation scales growth rate progressive taxation truncates tail",
     "The scaling-versus-truncation contrast stated as such."),
    ("T", "T6", "equal revenue comparison wealth tax capital income tax stationary inequality",
     "The matched-budget ranking reversal itself."),
    ("T", "T7", "Domar Musgrave loss offset risk taking taxation variance of return",
     "The 1944 mechanism carried to the tail index."),
    ("T", "T8", "stop loss reinsurance heavy tail index proportional reinsurance",
     "Actuarial vocabulary: excess-of-loss truncates, quota-share scales."),
    ("T", "T9", "tail index after tax return characteristic equation wealth accumulation",
     "The characteristic equation with a tax inside it."),
    ("T", "T10", "progressive wealth taxation Pareto tail index random returns",
     "Saez-Zucman adjacent; progressivity -> tail index."),
    ("T", "T11", "taxation of stochastic returns changes shape of growth rate distribution",
     "Vocabulary-neutral phrasing of the whole thesis."),
    ("T", "T12", "wealth tax versus capital gains tax tail of wealth distribution random growth",
     "The plainest possible phrasing of the target."),

    # ---- TIER N: the floor.
    ("N", "N1", "Kesten process tail index medieval falconry guild membership",
     "Must screen in zero."),
    ("N", "N2", "truncated growth multiplier Antarctic lichen taxation policy",
     "Must screen in zero."),
    ("N", "N3", "Pareto tail exponent of nineteenth century lighthouse keeper salaries reinsurance",
     "Must screen in zero."),
]


def _get(url, tries=5, base_sleep=4.0):
    last = None
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA,
                                                       "Accept": "application/json"})
            with urllib.request.urlopen(req, timeout=60) as r:
                return r.read()
        except Exception as e:                          # noqa: BLE001
            last = e
            time.sleep(base_sleep * (2 ** i))
    raise RuntimeError("GET failed after %d tries: %s" % (tries, last))


def _norm(t):
    return re.sub(r"[^a-z0-9 ]", " ", (t or "").lower())


def search_openalex(q, limit=25):
    url = ("https://api.openalex.org/works?search=" + urllib.parse.quote(q)
           + "&per-page=%d&mailto=%s" % (limit, MAILTO))
    d = json.loads(_get(url))
    out = []
    for w in d.get("results", []) or []:
        inv = w.get("abstract_inverted_index") or {}
        ab = ""
        if inv:
            pos = {}
            for word, idxs in inv.items():
                for i in idxs:
                    pos[i] = word
            ab = " ".join(pos[k] for k in sorted(pos))[:1200]
        out.append({
            "title": w.get("title"),
            "year": w.get("publication_year"),
            "citations": w.get("cited_by_count"),
            "authors": [a["author"]["display_name"]
                        for a in (w.get("authorships") or [])][:4],
            "doi": w.get("doi"),
            "id": w.get("id"),
            "abstract": ab,
        })
    return {"total": (d.get("meta") or {}).get("count"), "hits": out}


def search_semanticscholar(q, limit=20):
    url = ("https://api.semanticscholar.org/graph/v1/paper/search?query="
           + urllib.parse.quote(q)
           + "&limit=%d&fields=title,year,abstract,externalIds,citationCount,authors" % limit)
    d = json.loads(_get(url))
    out = []
    for p in d.get("data", []) or []:
        out.append({"title": p.get("title"), "year": p.get("year"),
                    "citations": p.get("citationCount"),
                    "authors": [a.get("name") for a in (p.get("authors") or [])][:4],
                    "doi": (p.get("externalIds") or {}).get("DOI"),
                    "abstract": (p.get("abstract") or "")[:1200]})
    return {"total": d.get("total"), "hits": out}


def search_arxiv(q, limit=20):
    url = ("http://export.arxiv.org/api/query?search_query=all:"
           + urllib.parse.quote(q) + "&start=0&max_results=%d" % limit)
    root = ET.fromstring(_get(url))
    ns = {"a": "http://www.w3.org/2005/Atom", "o": "http://a9.com/-/spec/opensearch/1.1/"}
    tot = root.find("o:totalResults", ns)
    out = []
    for e in root.findall("a:entry", ns):
        t, s, pub, idl = (e.find("a:title", ns), e.find("a:summary", ns),
                          e.find("a:published", ns), e.find("a:id", ns))
        out.append({"title": re.sub(r"\s+", " ", (t.text or "").strip()) if t is not None else None,
                    "year": (pub.text or "")[:4] if pub is not None else None,
                    "authors": [x.find("a:name", ns).text for x in e.findall("a:author", ns)][:4],
                    "arxiv": (idl.text or "").rsplit("/", 1)[-1] if idl is not None else None,
                    "abstract": re.sub(r"\s+", " ", (s.text or "").strip())[:1200] if s is not None else ""})
    return {"total": int(tot.text) if tot is not None else None, "hits": out}


def search_crossref(q, limit=20):
    url = ("https://api.crossref.org/works?query.bibliographic=" + urllib.parse.quote(q)
           + "&rows=%d&mailto=%s"
             "&select=title,author,issued,DOI,is-referenced-by-count,abstract" % (limit, MAILTO))
    msg = json.loads(_get(url)).get("message", {})
    out = []
    for it in msg.get("items", []) or []:
        ttl = (it.get("title") or [None])[0]
        yr = ((it.get("issued") or {}).get("date-parts") or [[None]])[0][0]
        ab = re.sub(r"<[^>]+>", " ", it.get("abstract") or "")
        out.append({"title": re.sub(r"\s+", " ", ttl) if ttl else None, "year": yr,
                    "citations": it.get("is-referenced-by-count"),
                    "authors": [" ".join(filter(None, [a.get("given"), a.get("family")]))
                                for a in (it.get("author") or [])][:4],
                    "doi": it.get("DOI"), "abstract": re.sub(r"\s+", " ", ab)[:1200]})
    return {"total": msg.get("total-results"), "hits": out}


SOURCES = [("openalex", search_openalex),
           ("semanticscholar", search_semanticscholar),
           ("arxiv", search_arxiv),
           ("crossref", search_crossref)]

RE_TAIL = re.compile(r"\b(pareto|tail index|tail exponent|power[- ]law|heavy[- ]tail|"
                     r"tail behaviou?r|regularly varying|top tail|fat[- ]tail)\w*\b", re.I)
RE_TAX = re.compile(r"\b(tax|taxation|taxes|levy|levies|redistribut|reinsuranc|"
                    r"loss offset|transfer|subsid)\w*\b", re.I)
RE_MULT = re.compile(r"\b(kesten|multiplicative|random growth|stochastic growth|"
                     r"random difference equation|perpetuit|geometric brownian|"
                     r"idiosyncratic return|random return|growth multiplier|"
                     r"stochastic return|rate of return heterogeneity)\w*\b", re.I)
RE_TRUNC = re.compile(r"\b(truncat|censor|bounded above|upper bound|clip|cap\b|capped|"
                      r"ceiling|stop[- ]loss|excess of loss)\w*\b", re.I)


def screen(hit):
    txt = " ".join(filter(None, [hit.get("title") or "", hit.get("abstract") or ""]))
    return {"tail": bool(RE_TAIL.search(txt)), "tax": bool(RE_TAX.search(txt)),
            "mult": bool(RE_MULT.search(txt)), "trunc": bool(RE_TRUNC.search(txt))}


def is_core(h):
    s = h["screen"]
    return s["tail"] and s["tax"] and s["mult"]


def title_match(want, got):
    """Token-overlap match; a known item counts as retrieved at >=0.70 overlap."""
    a, b = set(_norm(want).split()), set(_norm(got or "").split())
    if not a:
        return 0.0
    return len(a & b) / len(a)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True)
    ap.add_argument("--md")
    a = ap.parse_args()

    # ---------------- TIER K: known-item retrieval (the real ceiling)
    known = []
    for who, yr, title, why in KNOWN_ITEMS:
        rec = {"who": who, "year": yr, "title": title, "why": why, "found_in": {}}
        for sname, fn in SOURCES[:2]:                    # openalex + s2 are enough
            try:
                r = fn(title, 10)
                best, bt = 0.0, None
                for h in r["hits"]:
                    m = title_match(title, h.get("title"))
                    if m > best:
                        best, bt = m, h
                rec["found_in"][sname] = {"best_overlap": round(best, 3),
                                          "best_title": (bt or {}).get("title"),
                                          "year": (bt or {}).get("year"),
                                          "doi": (bt or {}).get("doi"),
                                          "retrieved": best >= 0.70}
            except Exception as e:                       # noqa: BLE001
                rec["found_in"][sname] = {"error": str(e)[:120], "retrieved": False}
            time.sleep(1.2)
        rec["retrieved_anywhere"] = any(v.get("retrieved") for v in rec["found_in"].values())
        known.append(rec)
        print("[K] %-28s %s  retrieved=%s" % (who, yr, rec["retrieved_anywhere"]), flush=True)

    # ---------------- TIER P / T / N
    results = []
    for tier, qid, q, note in QUERIES:
        for sname, fn in SOURCES:
            try:
                r, err = fn(q), None
            except Exception as e:                       # noqa: BLE001
                r, err = {"total": None, "hits": []}, str(e)[:160]
            for h in r["hits"]:
                h["screen"] = screen(h)
            core = [h for h in r["hits"] if is_core(h)]
            results.append({"tier": tier, "qid": qid, "query": q,
                            "positive_looks_like": note, "source": sname,
                            "total": r["total"], "returned": len(r["hits"]),
                            "screened_in": len(core), "error": err, "hits": r["hits"]})
            print("[%s %s] %-15s total=%-9s ret=%-3d core=%d %s"
                  % (tier, qid, sname, r["total"], len(r["hits"]), len(core),
                     ("ERR " + err[:50]) if err else ""), flush=True)
            time.sleep(1.2)

    # ---------------- calibration, PER CONTROL, not summed
    per_p = {}
    for qid in sorted({x["qid"] for x in results if x["tier"] == "P"}):
        per_p[qid] = sum(x["screened_in"] for x in results
                         if x["qid"] == qid and x["tier"] == "P")
    per_n = {}
    for qid in sorted({x["qid"] for x in results if x["tier"] == "N"}):
        per_n[qid] = sum(x["screened_in"] for x in results
                         if x["qid"] == qid and x["tier"] == "N")

    k_missed = [k["who"] + " " + str(k["year"]) for k in known if not k["retrieved_anywhere"]]
    p_failed = [q for q, n in per_p.items() if n == 0]
    n_leaked = [q for q, n in per_n.items() if n > 0]

    calib = {
        "known_items_total": len(known),
        "known_items_retrieved": len(known) - len(k_missed),
        "known_items_missed": k_missed,
        "positive_controls_per_query": per_p,
        "positive_controls_that_returned_nothing": p_failed,
        "negative_controls_per_query": per_n,
        "negative_controls_that_leaked": n_leaked,
        "api_errors": sum(1 for x in results if x["error"]),
        # v2's gate: EVERY positive control must fire AND >=80% of known items retrieved.
        "apparatus_valid": (not p_failed) and (len(k_missed) <= 0.2 * len(known)),
        "note": ("v1's gate was sum(P)>0 and passed on 1 hit with 3 silent control "
                 "failures. v2 requires EVERY positive control to fire and >=80% of "
                 "named known items to be retrievable. A TIER T zero is a MEASUREMENT "
                 "only under apparatus_valid=true; otherwise the run is VOID."),
    }

    # target inventory: every distinct core hit across TIER T, dedup by title
    seen, target_hits = set(), []
    for x in results:
        if x["tier"] != "T":
            continue
        for h in x["hits"]:
            if not is_core(h):
                continue
            key = _norm(h.get("title"))[:90]
            if key in seen:
                continue
            seen.add(key)
            target_hits.append({"qid": x["qid"], "source": x["source"], **{
                k: h.get(k) for k in ("title", "year", "authors", "doi", "arxiv",
                                      "citations", "abstract", "screen")}})
    target_hits.sort(key=lambda h: (not h["screen"]["trunc"], -(h.get("citations") or 0)))

    payload = {"calibration": calib, "known_items": known,
               "target_core_hits": target_hits, "results": results}
    with open(a.out, "w") as f:
        json.dump(payload, f, indent=1)

    print("\nCALIBRATION:\n" + json.dumps(calib, indent=1))
    print("\nDISTINCT CORE HITS ACROSS TIER T: %d" % len(target_hits))
    for h in target_hits[:40]:
        print("  [%s/%s] %s (%s) trunc=%s cites=%s"
              % (h["qid"], h["source"], (h["title"] or "")[:95], h["year"],
                 h["screen"]["trunc"], h.get("citations")))
    print("\nwrote %s" % a.out)

    if a.md:
        with open(a.md, "w") as f:
            f.write("| tier | qid | source | total | returned | core |\n|---|---|---|---|---|---|\n")
            for x in results:
                f.write("| %s | %s | %s | %s | %d | %d |\n" % (x["tier"], x["qid"],
                        x["source"], x["total"], x["returned"], x["screened_in"]))
    return 0 if calib["apparatus_valid"] else 2


if __name__ == "__main__":
    sys.exit(main())
