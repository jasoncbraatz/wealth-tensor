#!/usr/bin/env python3
"""wt117_litsearch.py -- the truncation-vs-scaling prior-art search, as an INSTRUMENT.

WHY THIS IS A SCRIPT AND NOT A BROWSING SESSION
-----------------------------------------------
Card 1217547572131984 names the trap directly: "I searched and found nothing" is only a
result if the search was wide enough to have found something.  A browsing session cannot
be re-run, cannot be audited, and cannot say what its own floor and ceiling were.

So this runs a MATRIX of queries against three public bibliographic APIs and records
every hit.  Crucially the matrix carries CALIBRATION QUERIES at both ends of the scale
(the REG-013 rule, lesson 2026-08-16: a rate means nothing without both ends of its
scale measured IN THE SAME RUN):

  TIER P (positive control)  queries whose subject matter is UNQUESTIONABLY published.
                             If these return zero, the APPARATUS is broken and the run
                             is void -- a zero on the target proves nothing.
  TIER T (target)            the actual question, asked several ways.
  TIER N (negative control)  well-formed queries about a deliberately absurd conjunction.
                             If these return confident hits, the API is fuzzy-matching
                             and a nonzero on the target means less than it looks.

SEARCH BY THE SHAPE OF THE EQUATION, NOT THE SUBJECT MATTER
-----------------------------------------------------------
(blackbook lesson 2026-08-12, the Bateman/flip-flop priority search.)  A within-field
search cannot find a result that lives in another field's vocabulary.  The object here is

    x' = A x + k        (Kesten recursion)   with tail index a from  E[A^a] = 1

and the two operations under comparison are, in vocabulary-neutral terms:

    STOCK levy    A -> (1-t) A                    a SCALING of the multiplier
    FLOW  levy    A -> A - r*(A-1)^+              a TRUNCATION of the multiplier

The same pair of operations is studied under at least five vocabularies: economics
(wealth tax vs capital income tax), applied probability (perpetuities / random
difference equations), statistical physics (multiplicative processes with a wall),
actuarial maths (proportional vs stop-loss / excess-of-loss reinsurance), and finance
(Domar-Musgrave loss offset).  TIER T asks in all of them.

USAGE
    python3 wt117_litsearch.py --out /tmp/wt117-results.json [--md /tmp/wt117.md]

Run on darwin (network); the JSON is the artefact the scouting note is written FROM.
"""

import argparse
import json
import re
import sys
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

UA = "wealth-tensor-litsearch/1.0 (mailto:jasoncbraatz@gmail.com)"

# ---------------------------------------------------------------- query matrix

# tier, id, query string, note on what a POSITIVE would look like
QUERIES = [
    # ---- TIER P: positive controls. These MUST return hits or the run is void.
    ("P", "P1", "Kesten process stationary distribution Pareto tail wealth",
     "Kesten/Goldie applied to wealth must be a large literature (Benhabib-Bisin-Zhu, Gabaix, Toda)."),
    ("P", "P2", "capital income tax Pareto tail wealth distribution tail index",
     "Benhabib Bisin Zhu 2011 computes exactly this. Zero here = broken apparatus."),
    ("P", "P3", "wealth tax versus capital income tax inequality heterogeneous returns",
     "Guvenen et al 'Use it or lose it', Boar-Midrigan. Unquestionably published."),
    ("P", "P4", "random growth model top wealth inequality power law taxation",
     "Gabaix-Lasry-Lions-Moll, Jones. Unquestionably published."),

    # ---- TIER T: the target, asked in six vocabularies.
    ("T", "T1", "truncation of growth multiplier tail index wealth taxation",
     "A paper stating that truncating A destroys/steepens the power law under a tax."),
    ("T", "T2", "tax on realized capital gains reduces variance of returns Pareto exponent",
     "A paper linking gain-contingent taxation to Var[log A] and thence to alpha."),
    ("T", "T3", "stochastic growth rate truncated above multiplicative process no power law tail",
     "Applied-probability statement: ess-sup A < 1 kills the Kesten tail."),
    ("T", "T4", "random difference equation truncated multiplier tail index perpetuity taxation",
     "Perpetuity / random-difference-equation vocabulary for the same operation."),
    ("T", "T5", "proportional tax scales multiplicative growth rate progressive tax truncates tail index",
     "The scaling-vs-truncation contrast stated as such."),
    ("T", "T6", "equal revenue wealth tax capital income tax stationary Gini comparison random returns",
     "The matched-budget ranking-reversal result itself."),
    ("T", "T7", "Domar Musgrave loss offset government silent partner variance of return wealth inequality",
     "The 1944 mechanism (income tax cuts mean AND variance) carried to the tail index."),
    ("T", "T8", "stop loss reinsurance truncates heavy tail index proportional reinsurance preserves",
     "Actuarial vocabulary: proportional vs excess-of-loss on a heavy tail."),
    ("T", "T9", "taxation Pareto exponent wealth distribution E[A^alpha]=1 after tax return",
     "The characteristic equation stated with a tax inside it."),
    ("T", "T10", "wealth tax progressivity changes Pareto tail index random growth calibration",
     "Progressive wealth tax -> tail index. Saez-Zucman adjacent."),

    # ---- TIER N: negative controls. Well-formed, deliberately absurd conjunction.
    ("N", "N1", "Kesten process tail index of medieval falconry guild membership",
     "Must return ~nothing. Nonzero confident hits = the API fuzzy-matches."),
    ("N", "N2", "truncation of the growth multiplier in Antarctic lichen taxation policy",
     "Must return ~nothing."),
]

# ---------------------------------------------------------------- API adapters


def _get(url, tries=4, sleep=3.0):
    last = None
    for i in range(tries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA,
                                                       "Accept": "application/json"})
            with urllib.request.urlopen(req, timeout=45) as r:
                return r.read()
        except Exception as e:          # noqa: BLE001 - we want the message, not the type
            last = e
            time.sleep(sleep * (i + 1))
    raise RuntimeError("GET failed after %d tries: %s :: %s" % (tries, url, last))


def search_semanticscholar(q, limit=15):
    url = ("https://api.semanticscholar.org/graph/v1/paper/search?query="
           + urllib.parse.quote(q)
           + "&limit=%d&fields=title,year,abstract,externalIds,citationCount,authors" % limit)
    d = json.loads(_get(url))
    out = []
    for p in d.get("data", []) or []:
        out.append({
            "title": p.get("title"),
            "year": p.get("year"),
            "citations": p.get("citationCount"),
            "authors": [a.get("name") for a in (p.get("authors") or [])][:4],
            "doi": (p.get("externalIds") or {}).get("DOI"),
            "arxiv": (p.get("externalIds") or {}).get("ArXiv"),
            "abstract": (p.get("abstract") or "")[:900],
        })
    return {"total": d.get("total"), "hits": out}


def search_arxiv(q, limit=15):
    url = ("http://export.arxiv.org/api/query?search_query=all:"
           + urllib.parse.quote('"%s"' % q if False else q)
           + "&start=0&max_results=%d" % limit)
    raw = _get(url)
    ns = {"a": "http://www.w3.org/2005/Atom",
          "o": "http://a9.com/-/spec/opensearch/1.1/"}
    root = ET.fromstring(raw)
    tot_el = root.find("o:totalResults", ns)
    out = []
    for e in root.findall("a:entry", ns):
        t = e.find("a:title", ns)
        s = e.find("a:summary", ns)
        pub = e.find("a:published", ns)
        idl = e.find("a:id", ns)
        out.append({
            "title": re.sub(r"\s+", " ", (t.text or "").strip()) if t is not None else None,
            "year": (pub.text or "")[:4] if pub is not None else None,
            "authors": [a.find("a:name", ns).text
                        for a in e.findall("a:author", ns)][:4],
            "arxiv": (idl.text or "").rsplit("/", 1)[-1] if idl is not None else None,
            "abstract": re.sub(r"\s+", " ", (s.text or "").strip())[:900] if s is not None else "",
        })
    return {"total": int(tot_el.text) if tot_el is not None else None, "hits": out}


def search_crossref(q, limit=15):
    url = ("https://api.crossref.org/works?query.bibliographic="
           + urllib.parse.quote(q)
           + "&rows=%d&select=title,author,issued,DOI,is-referenced-by-count,abstract" % limit)
    d = json.loads(_get(url))
    msg = d.get("message", {})
    out = []
    for it in msg.get("items", []) or []:
        ttl = (it.get("title") or [None])[0]
        issued = ((it.get("issued") or {}).get("date-parts") or [[None]])[0][0]
        ab = re.sub(r"<[^>]+>", " ", it.get("abstract") or "")
        out.append({
            "title": re.sub(r"\s+", " ", ttl) if ttl else None,
            "year": issued,
            "citations": it.get("is-referenced-by-count"),
            "authors": [" ".join(filter(None, [a.get("given"), a.get("family")]))
                        for a in (it.get("author") or [])][:4],
            "doi": it.get("DOI"),
            "abstract": re.sub(r"\s+", " ", ab)[:900],
        })
    return {"total": msg.get("total-results"), "hits": out}


SOURCES = [("semanticscholar", search_semanticscholar),
           ("arxiv", search_arxiv),
           ("crossref", search_crossref)]

# ---------------------------------------------------------------- relevance screen

# A hit is SCREENED-IN only if its title+abstract mention BOTH a tail/power-law concept
# AND a tax/levy concept AND a multiplicative-process concept. This is deliberately
# mechanical: the screen is re-runnable and its misses are inspectable, whereas
# "it looked relevant to me" is not.
RE_TAIL = re.compile(r"\b(pareto|tail index|tail exponent|power[- ]law|heavy[- ]tail|"
                     r"tail behaviou?r|extreme value|regularly varying)\b", re.I)
RE_TAX = re.compile(r"\b(tax|taxation|levy|levies|tariff|redistribut|reinsuranc|"
                    r"loss offset|transfer)\w*\b", re.I)
RE_MULT = re.compile(r"\b(kesten|multiplicative|random growth|stochastic growth|"
                     r"random difference equation|perpetuit|geometric brownian|"
                     r"idiosyncratic return|random return|growth multiplier|"
                     r"proportional random)\w*\b", re.I)
RE_TRUNC = re.compile(r"\b(truncat|cap(?:ped|ping)?|censor|bound(?:ed)? above|"
                      r"upper bound|clip|ceiling)\w*\b", re.I)


def screen(hit):
    txt = " ".join(filter(None, [hit.get("title") or "", hit.get("abstract") or ""]))
    return {
        "tail": bool(RE_TAIL.search(txt)),
        "tax": bool(RE_TAX.search(txt)),
        "mult": bool(RE_MULT.search(txt)),
        "trunc": bool(RE_TRUNC.search(txt)),
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True)
    ap.add_argument("--md")
    ap.add_argument("--limit", type=int, default=15)
    a = ap.parse_args()

    results = []
    for tier, qid, q, note in QUERIES:
        for sname, fn in SOURCES:
            try:
                r = fn(q, a.limit)
                err = None
            except Exception as e:                      # noqa: BLE001
                r, err = {"total": None, "hits": []}, str(e)
            for h in r["hits"]:
                h["screen"] = screen(h)
            n_screened = sum(1 for h in r["hits"]
                             if h["screen"]["tail"] and h["screen"]["tax"]
                             and h["screen"]["mult"])
            results.append({"tier": tier, "qid": qid, "query": q, "positive_looks_like": note,
                            "source": sname, "total": r["total"],
                            "returned": len(r["hits"]), "screened_in": n_screened,
                            "error": err, "hits": r["hits"]})
            print("[%s %s] %-16s total=%s returned=%d screened_in=%d %s"
                  % (tier, qid, sname, r["total"], len(r["hits"]), n_screened,
                     ("ERR " + err[:60]) if err else ""), flush=True)
            time.sleep(1.5)

    # ---- CALIBRATION VERDICT: the run is only interpretable if both ends measured.
    p_screened = sum(x["screened_in"] for x in results if x["tier"] == "P")
    n_screened = sum(x["screened_in"] for x in results if x["tier"] == "N")
    t_screened = sum(x["screened_in"] for x in results if x["tier"] == "T")
    errors = sum(1 for x in results if x["error"])
    calib = {
        "positive_control_screened_in": p_screened,
        "negative_control_screened_in": n_screened,
        "target_screened_in": t_screened,
        "api_errors": errors,
        "apparatus_valid": p_screened > 0,
        "note": ("A zero on TIER T is interpretable ONLY if "
                 "positive_control_screened_in > 0. Otherwise the run is VOID."),
    }
    payload = {"calibration": calib, "results": results}
    with open(a.out, "w") as f:
        json.dump(payload, f, indent=1)
    print("\nCALIBRATION: %s" % json.dumps(calib, indent=1))
    print("wrote %s" % a.out)

    if a.md:
        with open(a.md, "w") as f:
            f.write("| tier | qid | source | total | returned | screened-in |\n")
            f.write("|---|---|---|---|---|---|\n")
            for x in results:
                f.write("| %s | %s | %s | %s | %d | %d |\n"
                        % (x["tier"], x["qid"], x["source"], x["total"],
                           x["returned"], x["screened_in"]))
        print("wrote %s" % a.md)
    return 0 if calib["apparatus_valid"] else 2


if __name__ == "__main__":
    sys.exit(main())
