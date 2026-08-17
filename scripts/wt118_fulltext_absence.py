#!/usr/bin/env python3
"""wt118_fulltext_absence.py -- the ABSENCE half of the prior-art search.

WHY THIS EXISTS, AND WHY AN ABSTRACT SWEEP CANNOT REPLACE IT
-------------------------------------------------------------
docs/REFERENCE-POLICY.md sec.1, this project's own law:

    "an abstract can never establish that something is NOT in a paper. Every zero-hit
     table this project has published came from grep over an extracted full text, and
     that is the only thing that licenses one."

wt117b sweeps titles and abstracts across four indexes -- that is the DISCOVERY half,
and it can only ever license "nobody ADVERTISES this result".  To say "the closest
published works do not CONTAIN it" you have to open them.  This script does that:
downloads the open-access full text of the nearest neighbours, extracts it, and runs a
PRE-REGISTERED conjunction grep.

THE PREDICATES ARE DECLARED BEFORE THE RUN, WHICH IS THE WHOLE POINT
---------------------------------------------------------------------
-49's rule: "I searched and found nothing" is only a result if the search was wide
enough to have found something.  So each predicate below states, in the code, WHAT A
POSITIVE WOULD HAVE LOOKED LIKE.  A predicate that fires means the paper may contain
the result; a predicate that stays dark across a corpus that INCLUDES A FIELD SURVEY is
the only kind of absence this project accepts.

CALIBRATION IS BUILT IN, BOTH ENDS (REG-013 rule)
--------------------------------------------------
CEILING: SANITY predicates that MUST fire in every document (each paper certainly
         discusses "tax" and "wealth").  A document where the sanity predicate is dark
         did not extract -- its zeros on the real predicates are VOID, not evidence.
FLOOR:   an ABSURD predicate that must stay dark everywhere.

Corpus selection is itself a claim, so it is recorded: the set is "the works the three
project documents name, plus the field's own survey".  A SURVEY IS THE SHARPEST ABSENCE
TEST AVAILABLE -- covering the field is its entire job.

USAGE
    python3 wt118_fulltext_absence.py --workdir /tmp/wt118 --out /tmp/wt118-absence.json
"""

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import urllib.request

UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/124.0 Safari/537.36")

# ------------------------------------------------------------------ the corpus
# key, cite, url, why THIS work is in the corpus (i.e. why its silence would count)
CORPUS = [
    ("BBZ2011", "Benhabib, Bisin & Zhu (2011), Econometrica 79(1)",
     "https://www.nber.org/system/files/working_papers/w14730/w14730.pdf",
     "The single closest published work: a Kesten wealth model in which BOTH an estate "
     "tax (on the stock) and a capital income tax (on the flow) enter the tail index. "
     "If the truncation-vs-scaling contrast is published anywhere, it is here."),
    ("BB2018survey", "Benhabib & Bisin (2018), J. Economic Literature 56(4) "
     "(NBER w21924, 'Skewed Wealth Distributions')",
     "https://www.nber.org/system/files/working_papers/w21924/w21924.pdf",
     "THE FIELD'S OWN SURVEY. Covering this literature is its job. A survey that never "
     "states the contrast is the strongest single piece of absence evidence obtainable."),
    ("GKKOC2019", "Guvenen, Kambourov, Kuruscu, Ocampo & Chen (NBER w26284; QJE 2023)",
     "https://www.nber.org/system/files/working_papers/w26284/w26284.pdf",
     "The most-cited head-to-head of a STOCK tax against a FLOW tax under heterogeneous "
     "returns. Different mechanism (reallocation), same policy pair -- so if anyone "
     "priced the pair at equal revenue in tail terms, they had every reason to here."),
    ("BBZ2015", "Benhabib, Bisin & Zhu (2015), J. Economic Theory 159",
     "https://shenghaozhu.weebly.com/uploads/2/3/0/5/23050810/benhabibbisinzhu2015.pdf",
     "The JET companion, infinite-horizon; the other half of the BBZ tail-index result."),
    ("Nirei2009", "Nirei (2009), 'Pareto Distributions in Economic Growth Models'",
     "http://piketty.pse.ens.fr/files/Nirei2009.pdf",
     "Computes how a capital-income tax moves the Pareto exponent -- the mechanism "
     "closest to ours in the growth-model wing."),

    # ---- corpus WIDENING, added in the same session after the first five came back
    # with four dark predicates. Five documents is not wide enough to have found
    # something; these eight are the ones a referee would name.
    ("BastaniWald2023", "Bastani & Waldenstrom (2023), Oxford Rev. Econ. Policy 39(3), "
     "604-616, 'Taxing the wealthy: the choice between wealth and capital income "
     "taxation' (DiVA full text)",
     "https://www.ifn.se/media/gbdhz33h/wp1454.pdf",
     "A SURVEY OF EXACTLY THIS POLICY PAIR -- stock levy against flow levy. If the "
     "truncation-vs-scaling contrast were known to the public-finance literature, a "
     "2023 survey whose whole subject is the choice between them would say so."),
    ("BoarMidrigan2022", "Boar & Midrigan (NBER w27622; J. Monetary Economics 2022), "
     "'Efficient Redistribution'",
     "https://www.nber.org/system/files/working_papers/w27622/w27622.pdf",
     "Optimal choice among wealth, capital-income and income taxes with heterogeneous "
     "returns; the other modern head-to-head besides Guvenen et al."),
    ("Gabaix2009", "Gabaix (2009), 'Power Laws in Economics and Finance' (NBER w14299)",
     "https://www.nber.org/system/files/working_papers/w14299/w14299.pdf",
     "The canonical survey of the random-growth machinery itself. Its job is to know "
     "what operations on the multiplier are known to do to the exponent."),
    ("PikettySaez2013", "Piketty & Saez (NBER w17989; Econometrica 2013), 'A Theory of "
     "Optimal Inheritance Taxation'",
     "https://www.nber.org/system/files/working_papers/w17989/w17989.pdf",
     "An anchor of the optimal-taxation-with-Pareto-tails literature that REVIEW-004, "
     "ROADS-001 and HANDOFF-PROMPT all name as the place this result would live."),
    ("ScheuerSlemrod2021", "Scheuer & Slemrod (NBER w28150; JEP 2021), 'Taxing Our "
     "Wealth'",
     "https://www.nber.org/system/files/working_papers/w28150/w28150.pdf",
     "The other anchor: a JEP survey of wealth taxation written for exactly the "
     "question of what a wealth tax does that an income tax does not."),
    ("SaezZucman2019", "Saez & Zucman (2019), 'Progressive Wealth Taxation', BPEA",
     "https://gabriel-zucman.eu/files/SaezZucman2019BPEA.pdf",
     "The most-read modern argument that a wealth tax compresses the top of the "
     "distribution, with an explicit mechanical model of the top tail."),
    ("BeareToda2022", "Beare & Toda (2022), Econometrica 90(4), 'Determination of "
     "Pareto Exponents in Economic Models Driven by Markov Multiplicative Processes' "
     "(arXiv 1712.01431)",
     "https://arxiv.org/pdf/1712.01431",
     "THE PROBABILITY WING. Tests the claim's other half separately: is the MATHS of "
     "a truncated multiplier killing the power law published as maths, independent of "
     "any tax application? A different vocabulary, per the search-by-equation-shape "
     "rule (blackbook 2026-08-12)."),
    ("BenhabibBisinZhu2016JET", "Benhabib, Bisin & Luo / Toda wing -- Toda (2019), "
     "'Wealth distribution with random discount factors' (arXiv 1808.01142)",
     "https://arxiv.org/pdf/1808.01142",
     "Second probability-wing member; modern Kesten-in-economics with a different "
     "shock structure."),

    # ---- THE STATISTICAL-PHYSICS WING, and the predicate's own positive control.
    # None of REVIEW-004, ROADS-001 or HANDOFF-PROMPT names this literature: all
    # three said to look in "optimal-taxation-with-Pareto-tails". This is the
    # blackbook's search-by-the-shape-of-the-equation lesson (2026-08-12) firing
    # exactly as written -- a within-field search cannot find a result that lives in
    # another field's vocabulary.
    ("SornetteCont1997", "Sornette & Cont (1997), J. Physique I 7(3), 431-444, "
     "'Convergent multiplicative processes repelled from zero: power laws and "
     "truncated power laws' (arXiv cond-mat/9609074)",
     "https://arxiv.org/pdf/cond-mat/9609074",
     "PREDICATE POSITIVE CONTROL. Its title contains the operation and the outcome. "
     "If TRUNCATION_x_TAIL does not fire HERE, the predicate is broken and its "
     "darkness across the economics corpus proves nothing about the economics."),
    ("Sornette1998", "Sornette (1998), 'Multiplicative processes and power laws', "
     "Phys. Rev. E 57(4) (arXiv cond-mat/9708231)",
     "https://arxiv.org/pdf/cond-mat/9708231",
     "Second predicate control and a second reading of what bounding a multiplicative "
     "process does to its exponent."),
    ("ManrubiaZanette1999", "Manrubia & Zanette (1999), 'Stochastic multiplicative "
     "processes with reset events' (arXiv cond-mat/9902068)",
     "https://arxiv.org/pdf/cond-mat/9902068",
     "The reset/redistribution variant -- the closest physics analogue to a levy with "
     "a per-capita rebate."),
    ("BouchaudMezard2000", "Bouchaud & Mezard (2000), Physica A 282, 536-545, "
     "'Wealth condensation in a simple model of economy' (arXiv cond-mat/0002374)",
     "https://arxiv.org/pdf/cond-mat/0002374",
     "THE OTHER LITERATURE NOBODY NAMED. Multiplicative growth PLUS redistribution "
     "with the Pareto exponent in CLOSED FORM, alpha = 1 + J/D: redistribution rate "
     "over noise intensity. If a levy's effect on the tail runs through the DISPERSION "
     "of the multiplier rather than through revenue, this literature already writes "
     "that as an equation."),
    ("RandomGrowthRedist2026", "arXiv 2605.19464, 'Diffusing diffusivity selects "
     "Pareto tail exponent in random growth with redistribution'",
     "https://arxiv.org/pdf/2605.19464",
     "RECENCY CHECK. A 2026 paper on random growth WITH REDISTRIBUTION selecting the "
     "Pareto exponent -- the nearest thing to our object found anywhere, and recent "
     "enough that no survey would carry it yet."),
]

# Corpus members whose job is to prove the PREDICATES work. A predicate that stays
# dark across the economics corpus is evidence of absence ONLY if it demonstrably
# fires on a document that certainly contains the thing it looks for.
PREDICATE_CONTROLS = {"SornetteCont1997": ["TRUNCATION_x_TAIL"],
                      "Sornette1998": ["TRUNCATION_x_TAIL"]}

# ------------------------------------------------------------------ predicates
# name, regex A, regex B, max chars apart, WHAT A POSITIVE WOULD HAVE LOOKED LIKE
# TAIL, v2. v1 read "tail index|tail exponent|Pareto exponent|Pareto tail|
# power[- ]law tail|tail parameter|..." -- every alternative containing the literal
# word "tail" or "Pareto". It therefore could not fire on the statistical-physics
# wing, which says "truncated power law" and "exponent mu" and almost never "tail".
# The predicate control caught this: TRUNCATION_x_TAIL stayed DARK on Sornette &
# Cont (1997), a paper whose TITLE is "power laws and truncated power laws".
# A predicate that cannot fire on the one document certain to contain the thing is
# not measuring absence, it is manufacturing it -- and eleven dark economics texts
# would have been written up as a clean result on the strength of it.
TAIL = (r"tail index|tail exponent|Pareto exponent|Pareto tail|power[- ]law tail|"
        r"tail parameter|thickness of the tail|fatness of the tail|"
        r"power[- ]law|Pareto|exponent (?:of the )?(?:distribution|power|mu|α|alpha)|"
        r"scaling exponent|critical exponent|heavy[- ]tail|fat[- ]tail|"
        r"regularly varying|tail (?:of the )?distribution")
TAXW = r"tax|taxation|levy|levies"

PREDICATES = [
    # --- CEILING, SPLIT IN TWO. v1 of this script used a single "SANITY_tail"
    # ceiling requiring the phrase "tail index|Pareto exponent|..." near
    # "wealth|income", and it VOIDED four documents that had extracted perfectly
    # (100k-286k characters) merely because they say "Pareto parameter" or
    # "Pareto distribution" instead. That ceiling was testing MY VOCABULARY, not the
    # extraction -- the same defect the instrument exists to catch, one storey up.
    # EXTRACTION and TOPIC are different questions and now get different limbs.
    ("SANITY_extracted", r"\bthe\b", r"\bof\b", 200,
     "EXTRACTION CEILING. Ordinary English function words. Dark = the PDF did not "
     "extract to text, and every other zero in this document is VOID."),
    ("SANITY_tax_wealth", r"\btax", r"\bwealth|\bcapital\b|\bincome\b", 400,
     "TOPIC CEILING. Confirms the document really is about taxing wealth/capital. "
     "Dark = the document is not a fair test of this question, not that it extracted "
     "badly."),
    ("SANITY_tail_vocab", TAIL + r"|Pareto", r"wealth|income|distribution", 800,
     "COVERAGE PROBE, deliberately NOT part of validity. Records whether the document "
     "speaks the tail-index dialect at all. A paper can be a fair test of an absence "
     "while using different words -- that is the whole reason to search by the shape "
     "of the equation rather than the subject matter."),

    ("TRUNCATION_x_TAIL", r"truncat|censor|capped|caps the|cap on|bounded above|"
     r"upper bound on the (?:return|growth|multiplier)", TAIL, 700,
     "POSITIVE = a sentence linking truncation/capping of the growth process to the "
     "tail index. THIS IS THE HEADLINE CLAIM. Any hit must be read at source."),
    ("SCALING_vs_TRUNCATION", r"scal(?:e|es|ing)|proportional(?:ly)? reduc|multiplicat"
     r"ive(?:ly)? reduc", r"truncat|censor|capped|cap the", 500,
     "POSITIVE = the two operations named in the same breath, which is the paper's "
     "organising contrast."),
    ("EQUAL_REVENUE_PAIR", r"equal revenue|same revenue|revenue[- ]neutral|equal[- ]"
     r"yield|matched revenue|identical revenue", r"wealth tax|capital income tax|"
     r"estate tax|tax on wealth|tax on capital income", 700,
     "POSITIVE = an explicit matched-budget comparison of a stock levy against a flow "
     "levy. This is the ranking-reversal result's own framing."),
    # NOTE: the first draft of this predicate used a bare `without loss|no loss` and
    # fired on TWO documents purely via the mathematician's idiom "without loss of
    # generality" -- Boar-Midrigan and Piketty-Saez both. A predicate that matches
    # boilerplate manufactures its own positives, which is worse than a dark one:
    # it makes a corpus look covered. Negative lookahead added, and the false
    # positives are recorded here rather than quietly deleted.
    ("NO_LOSS_OFFSET",
     r"loss[- ]offset|loss offset|(?:without|with no|no) loss(?!\s+(?:of|in)\s+"
     r"generality)|asymmetric(?:ally)? tax|tax(?:ed|es|ation)? only (?:on )?gains|"
     r"gains but not losses|(?:deduct|offset)\w* (?:of )?losses", TAXW, 500,
     "POSITIVE = the asymmetry that MAKES our flow levy a truncation rather than an "
     "affine contraction. Domar-Musgrave's territory."),
    ("VARIANCE_OF_RETURN_x_TAIL", r"variance of (?:the )?(?:log )?(?:rate of )?return|"
     r"dispersion of returns|volatility of returns|Var\s*\[?\s*log", TAIL, 700,
     "POSITIVE = a paper routing a tax's effect on the tail THROUGH the variance of "
     "the growth multiplier, which is our stated mechanism."),
    ("NO_POWER_LAW_AT_ALL", r"no (?:longer )?(?:a )?power[- ]law|power law (?:vanish|"
     r"disappear|break)|tail (?:vanish|disappear)|thin(?:ner)?[- ]tailed|"
     r"no Pareto tail|fails to (?:be|have a) (?:Pareto|power)", TAXW, 700,
     "POSITIVE = the strongest form of our claim: a tax strong enough to destroy the "
     "power law outright (our r=1 cap, ess-sup A = 0.9524)."),

    ("ABSURD_FLOOR", r"medieval falconry|Antarctic lichen|lighthouse keeper", r".", 400,
     "FLOOR. Must stay dark in every document. A hit means the matcher is broken."),
]


def fetch(url, dest):
    if os.path.exists(dest) and os.path.getsize(dest) > 20000:
        return "cached"
    req = urllib.request.Request(url, headers={"User-Agent": UA,
                                               "Accept": "application/pdf,*/*"})
    with urllib.request.urlopen(req, timeout=120) as r, open(dest, "wb") as f:
        shutil.copyfileobj(r, f)
    return "downloaded"


def extract(pdf, txt):
    if shutil.which("pdftotext"):
        subprocess.run(["pdftotext", "-q", pdf, txt], check=False)
        if os.path.exists(txt) and os.path.getsize(txt) > 2000:
            return "pdftotext"
    try:
        from pypdf import PdfReader
    except ImportError:
        try:
            from PyPDF2 import PdfReader                      # type: ignore
        except ImportError:
            return None
    try:
        rd = PdfReader(pdf)
        with open(txt, "w") as f:
            for pg in rd.pages:
                f.write(pg.extract_text() or "")
                f.write("\n")
        return "pypdf" if os.path.getsize(txt) > 2000 else None
    except Exception:                                          # noqa: BLE001
        return None


def conj(text, ra, rb, span):
    """Return up to 4 windows where ra and rb co-occur within `span` characters."""
    hits = []
    A = [m.start() for m in re.finditer(ra, text, re.I)]
    if not A:
        return hits
    B = [m.start() for m in re.finditer(rb, text, re.I)]
    if not B:
        return hits
    for a in A:
        for b in B:
            if abs(a - b) <= span:
                lo, hi = max(0, min(a, b) - 160), min(len(text), max(a, b) + 240)
                hits.append(re.sub(r"\s+", " ", text[lo:hi]))
                break
        if len(hits) >= 4:
            break
    return hits


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--workdir", default="/tmp/wt118")
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    os.makedirs(a.workdir, exist_ok=True)

    docs = []
    for key, cite, url, why in CORPUS:
        pdf = os.path.join(a.workdir, key + ".pdf")
        txt = os.path.join(a.workdir, key + ".txt")
        rec = {"key": key, "cite": cite, "url": url, "why_in_corpus": why}
        try:
            rec["fetch"] = fetch(url, pdf)
            rec["bytes_pdf"] = os.path.getsize(pdf)
        except Exception as e:                                 # noqa: BLE001
            rec["fetch"] = "FAILED: " + str(e)[:140]
            rec["extract"] = None
            rec["predicates"] = {}
            docs.append(rec)
            print("[%-12s] FETCH FAILED %s" % (key, str(e)[:70]), flush=True)
            continue
        rec["extract"] = extract(pdf, txt)
        if not rec["extract"]:
            rec["predicates"] = {}
            docs.append(rec)
            print("[%-12s] EXTRACT FAILED" % key, flush=True)
            continue
        text = open(txt, errors="ignore").read()
        rec["chars"] = len(text)
        preds = {}
        for name, ra, rb, span, positive_is in PREDICATES:
            w = conj(text, ra, rb, span)
            preds[name] = {"fired": bool(w), "n_windows": len(w),
                           "positive_would_look_like": positive_is,
                           "windows": w[:3]}
        rec["predicates"] = preds
        # Validity = the text EXTRACTED and the document is ON TOPIC and the absurd
        # floor stayed dark. Tail-index VOCABULARY is recorded but does NOT gate.
        # 6000, not 20000: v1's floor voided Sornette (1998) at 10,359 chars and
        # Manrubia & Zanette at 17,416 -- both are Physical Review LETTERS, which are
        # four pages by design. A length floor calibrated on 40-page economics working
        # papers silently discards an entire literature for being concise.
        rec["extracted_ok"] = preds["SANITY_extracted"]["fired"] and rec["chars"] > 6000
        rec["on_topic"] = preds["SANITY_tax_wealth"]["fired"]
        rec["speaks_tail_dialect"] = preds["SANITY_tail_vocab"]["fired"]
        rec["document_valid"] = (rec["extracted_ok"] and rec["on_topic"]
                                 and not preds["ABSURD_FLOOR"]["fired"])
        docs.append(rec)
        fired = [n for n, v in preds.items()
                 if v["fired"] and not n.startswith(("SANITY", "ABSURD"))]
        print("[%-22s] %-9s chars=%-7d extracted=%s ontopic=%s tail-dialect=%s fired=%s"
              % (key, rec["extract"], rec["chars"], rec["extracted_ok"],
                 rec["on_topic"], rec["speaks_tail_dialect"],
                 ",".join(fired) or "NONE"), flush=True)

    valid = [d for d in docs if d.get("document_valid")]
    real = [n for n, *_ in PREDICATES if not n.startswith(("SANITY", "ABSURD"))]
    summary = {
        "corpus_size": len(CORPUS),
        "documents_extracted_and_valid": len(valid),
        "valid_document_keys": [d["key"] for d in valid],
        "documents_void": [d["key"] for d in docs if not d.get("document_valid")],
        "void_reasons": {d["key"]: {"fetch": d.get("fetch"),
                                    "extract": d.get("extract"),
                                    "chars": d.get("chars"),
                                    "extracted_ok": d.get("extracted_ok"),
                                    "on_topic": d.get("on_topic")}
                         for d in docs if not d.get("document_valid")},
        "valid_docs_not_speaking_tail_dialect":
            [d["key"] for d in valid if not d.get("speaks_tail_dialect")],
        # Did each predicate control actually fire the predicate it exists to prove?
        "predicate_controls": {
            k: {p: bool(next((d for d in docs if d["key"] == k), {})
                        .get("predicates", {}).get(p, {}).get("fired"))
                for p in ps}
            for k, ps in PREDICATE_CONTROLS.items()},
        "predicates_proven_capable_of_firing":
            sorted({p for k, ps in PREDICATE_CONTROLS.items() for p in ps
                    if next((d for d in docs if d["key"] == k), {})
                    .get("predicates", {}).get(p, {}).get("fired")}),
        "predicate_fire_counts_over_valid_docs":
            {n: sum(1 for d in valid if d["predicates"][n]["fired"]) for n in real},
        "predicates_dark_across_entire_valid_corpus":
            [n for n in real if not any(d["predicates"][n]["fired"] for d in valid)],
        "note": ("A dark predicate is evidence of absence ONLY over documents_valid; a "
                 "document whose SANITY ceilings did not fire contributes NOTHING. "
                 "Windows that DID fire must be read at source before any claim -- a "
                 "regex hit is a lead, not a finding (REFERENCE-POLICY sec.2)."),
    }
    json.dump({"summary": summary, "documents": docs}, open(a.out, "w"), indent=1)
    print("\nSUMMARY:\n" + json.dumps(summary, indent=1))
    print("\nwrote %s" % a.out)
    return 0


if __name__ == "__main__":
    sys.exit(main())
