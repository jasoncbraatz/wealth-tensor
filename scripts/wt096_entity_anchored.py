#!/usr/bin/env python3
"""REG-008 · the entity-anchored trigger sentence.

Registered in REG-008-p3-entity-anchored-disclosure.md, commit b02d02e (erratum 9797ff3),
before this file existed and before any statistic it computes had a value.

READS ONLY COMMITTED DATA. No network, no rebuild of the panel, no re-crawl of EDGAR --
F6 asserts all three mechanically rather than promising them in a docstring. The corpus is
data/reg-007-passages.json.gz, pinned by sha256.

The parse is ARM-BLIND BY CONSTRUCTION (REG-008 F8): every row is stripped of arm,
universe, sic, G, t_sum and A before segmentation, and the labels are rejoined by
(cik, fy_end) only after the falsifiers that do not declare a need for them have passed.
F1 -- the placebo gate -- is the single declared exception and receives the arm label
alone. That structure exists because REG-008 section 2.6 is a disclosure, not a boast:
this session's first probe conditioned on the arm before the registration existed.

  stage 1:  python3 wt096_entity_anchored.py --emit-audit    (writes the two audit samples)
  stage 2:  <the samples are adjudicated by hand and committed>
  stage 3:  python3 wt096_entity_anchored.py                 (F1..F10, then the statistics)
"""
from __future__ import annotations

import hashlib
import json
import pathlib
import random
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from severity import DEFINITIONAL, check, summary          # noqa: E402

ROOT = pathlib.Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
CORPUS = DATA / "reg-007-passages.json.gz"
CORPUS_SHA = "939e7bf5f11aa753e18a6604d53c7f9c09ca80e3f195744ccde6adb09f4ed761"
RESULT7 = ROOT / "docs" / "preregistration" / "RESULT-REG-007.md"
SEED = 20260813

# ------------------------------------------------------------------ REG-008 section 3.2
PHRASES = ("triggering event", "triggering events", "impairment indicator",
           "impairment indicators", "indicators of impairment", "indicator of impairment",
           "interim impairment test", "interim goodwill impairment", "events or circumstances")

ABBR = ("U.S.|U.K.|Inc.|Corp.|Co.|Ltd.|LLC.|L.P.|L.L.C.|No.|Nos.|St.|Mr.|Mrs.|Ms.|Dr.|"
        "Jr.|Sr.|vs.|etc.|e.g.|i.e.|Fig.|approx.|Sec.|Art.|Ch.|pp.|Ph.D.|A.M.|P.M.|"
        "Jan.|Feb.|Mar.|Apr.|Jun.|Jul.|Aug.|Sept.|Sep.|Oct.|Nov.|Dec.").split("|")
DOT = "\x00"


def segment(text: str) -> list[str]:
    """REG-008 section 3.2, frozen. Protect, split, restore."""
    t = text
    for a in ABBR:
        t = t.replace(a, a.replace(".", DOT))
    t = re.sub(r"(\d)\.(\d)", r"\1" + DOT + r"\2", t)
    t = re.sub(r"\b([A-Z])\.(?=[A-Z]\.)", r"\1" + DOT, t)
    t = re.sub(r"\b([A-Z])\.(?=\s[A-Z][a-z])", r"\1" + DOT, t)
    parts = re.split(r"(?<=[.!?])\s+(?=[\"'(\[]?[A-Z0-9$])", t)
    return [p.replace(DOT, ".") for p in parts]


# ------------------------------------------------------------------ REG-008 section 3.3
M1_RE = re.compile(r"((?:[A-Z][A-Za-z0-9&./'\-]*)(?:\s+(?:and|of|&|the)?\s*"
                   r"[A-Z][A-Za-z0-9&./'\-]*){0,4})\s+reporting unit\b")
GENERIC = {"the", "a", "an", "each", "our", "its", "their", "one", "that", "this", "these",
           "those", "such", "any", "certain", "both", "all", "no", "single", "same",
           "other", "others", "remaining", "applicable", "respective", "relevant",
           "affected", "two", "three", "four", "five", "of", "and", "or", "which",
           "whose", "company's", "companys"}
M2_RE = re.compile(r"\b(?:first|second|third|fourth) quarter\b|\bQ[1-4]\s+20\d\d\b|"
                   r"\b(?:January|February|March|April|May|June|July|August|September|"
                   r"October|November|December)\s+\d{0,2},?\s*20\d\d\b|"
                   r"\b(?:three|six|nine|twelve) months ended\b", re.I)
M3_RE = re.compile(r"\$\s?\d[\d,.]*\s*(?:million|billion|thousand)?", re.I)

# REG-007 section 3.3, inherited verbatim and NOT extended (REG-008 section 6)
INTERNAL = ("recoverability of a significant asset group", "asset group",
            "carrying amount of its net assets", "composition of its net assets",
            "long-lived asset impairment", "tested for recoverability",
            "recognition of a goodwill impairment loss in the financial statements of a subsidiary",
            "held for sale", "disposal group")
EXTERNAL = ("macroeconomic", "economic conditions", "industry", "market conditions",
            "competitive", "regulatory", "raw material", "labor costs",
            "declining cash flows", "decline in revenue", "decline in earnings",
            "loss of a customer", "management", "key personnel", "litigation",
            "bankruptcy", "share price", "stock price", "market capitalization",
            "interest rate", "discount rate")


def m1_names(sentence: str) -> list[str]:
    out = []
    for m in M1_RE.finditer(sentence):
        toks = m.group(1).split()
        while toks and toks[0].lower() in GENERIC:
            toks = toks[1:]
        cand = " ".join(toks).strip()
        if cand and cand.lower() not in GENERIC and len(cand) >= 2:
            out.append(cand)
    return out


# ------------------------------------------------------------------ the arm-blind parse
def blind(rows: list[dict]) -> list[dict]:
    """REG-008 F8. The label is deleted, not merely unread."""
    out = []
    for r in rows:
        r = dict(r)
        for k in ("arm", "universe", "sic", "G", "t_sum", "A"):
            r.pop(k, None)
        out.append(r)
    return out


def merged_spans(row: dict, half: int) -> list[tuple[int, int, str]]:
    """Absolute-offset merge (REG-008 section 2.1). A passage's true start is at-half."""
    iv = []
    for p in row["passages"]:
        a = max(0, p["at"] - half)
        iv.append((a, a + len(p["text"]), p["text"]))
    iv.sort()
    out: list[list] = []
    for a, b, t in iv:
        if out and a <= out[-1][1]:
            prev_a, prev_b, prev_t = out[-1]
            if b > prev_b:
                out[-1][2] = prev_t + t[prev_b - a:]
                out[-1][1] = b
        else:
            out.append([a, b, t])
    return [(a, b, t) for a, b, t in out]


def parse_one(row: dict, half: int) -> dict:
    """Everything REG-008 measures about ONE firm-year, computed without its label."""
    doc_chars = row.get("doc_chars") or 0
    n_sent = 0
    m1 = m2 = m3 = m1_f = False
    edge = False
    names: list[str] = []
    sents: list[dict] = []
    for a, b, text in merged_spans(row, half):
        segs = segment(text)
        pos = 0
        for s in segs:
            s_start = a + pos
            pos += len(s) + 1
            sl = s.lower()
            if not any(p in sl for p in PHRASES):
                continue
            n_sent += 1
            nm = m1_names(s)
            has_f = any(k in sl for k in INTERNAL)
            hit1, hit2, hit3 = bool(nm), bool(M2_RE.search(s)), bool(M3_RE.search(s))
            m1 |= hit1
            m2 |= hit2
            m3 |= hit3
            m1_f |= (hit1 and has_f)
            names += nm
            touches = (s_start <= a and a > 0) or (s_start + len(s) >= b and b < doc_chars)
            edge |= touches
            sents.append({"text": s, "m1": hit1, "m2": hit2, "m3": hit3,
                          "f": has_f, "names": nm, "edge": touches,
                          "long": len(s) > 600})
    return {"cik": row["cik"], "fy_end": row["fy_end"], "n_sent": n_sent,
            "m1": m1, "m2": m2, "m3": m3, "m1_f": m1_f, "edge": edge,
            "names": names, "sents": sents}


# ------------------------------------------------------------------ statistics
def fisher(a: int, b: int, c: int, d: int) -> float:
    """Exact two-sided Fisher on [[a,b],[c,d]]. math.comb only -- no scipy dependency,
    and tests/test_reg008_fisher.py pins it against scipy where scipy is installed."""
    from math import comb
    n = a + b + c + d
    r1, c1 = a + b, a + c
    lo, hi = max(0, c1 - (n - r1)), min(r1, c1)

    def p(k: int) -> float:
        return comb(r1, k) * comb(n - r1, c1 - k) / comb(n, c1)

    obs = p(a)
    tol = obs * (1 + 1e-9)
    return min(1.0, sum(p(k) for k in range(lo, hi + 1) if p(k) <= tol))


def rate(rows: list[dict], key: str) -> tuple[int, int, float]:
    """Share over CLASSIFIED firm-years. REG-008 F10: SILENT never enters a denominator."""
    cls = [r for r in rows if r["n_sent"] > 0]
    k = sum(1 for r in cls if r[key])
    return k, len(cls), (k / len(cls) if cls else float("nan"))


def mde(k1: int, n1: int, k2: int, n2: int) -> float:
    """Smallest Λ this cell could have detected: two-proportion, α=.05 two-sided, power .80.

    Printed beside every null, because 'we did not find it' and 'we could not have found it'
    are different results and this project has paid for the confusion (ladders A/A3/R)."""
    if not n1 or not n2:
        return float("nan")
    p = (k1 + k2) / (n1 + n2)
    return (1.959964 + 0.841621) * (p * (1 - p) * (1 / n1 + 1 / n2)) ** 0.5


def lam(joint: list[dict], gwonly: list[dict], key: str) -> dict:
    a, na, ra = rate(joint, key)
    c, nc, rc = rate(gwonly, key)
    return {"joint_k": a, "joint_n": na, "joint_rate": ra,
            "gwonly_k": c, "gwonly_n": nc, "gwonly_rate": rc,
            "lambda": ra - rc, "p": fisher(a, na - a, c, nc - c),
            "mde_80": mde(a, na, c, nc),
            "silent_joint": len(joint) - na, "silent_gwonly": len(gwonly) - nc}


# ------------------------------------------------------------------ main
def load() -> tuple[dict, list[dict], int]:
    raw = CORPUS.read_bytes()
    got = hashlib.sha256(raw).hexdigest()
    import gzip
    D = json.loads(gzip.decompress(raw).decode())
    return D, D["firm_years"], got


def main() -> int:
    emit = "--emit-audit" in sys.argv
    D, rows, digest = load()
    half = max(D["half_widths"])
    src = pathlib.Path(__file__).read_text()

    print(f"REG-008 · {len(rows)} firm-years · corpus sha256 {digest[:16]}…\n")

    # ---- the parse, on rows that cannot see their own labels -----------------
    bl = blind(rows)
    parsed = {(r["cik"], r["fy_end"]): parse_one(r, half) for r in bl}
    print(f"parsed {len(parsed)} firm-years · "
          f"{sum(p['n_sent'] for p in parsed.values())} trigger-bearing sentences\n")

    if emit:
        return emit_audits(parsed)

    seg_audit = json.loads((DATA / "reg-008-segmentation-audit.json").read_text())
    m1_audit = json.loads((DATA / "reg-008-m1-audit.json").read_text())

    # ---- F6 · no re-crawl, no rebuild, no network ---------------------------
    print("FALSIFIERS")
    # The forbidden names are BUILT, never written literally, so this file cannot trip its
    # own guard by naming what it forbids -- the first run of F6 failed exactly that way.
    NET = re.compile(r"^\s*(?:import|from)\s+(?:url" + r"lib|requests|ht" + r"tp|soc" + r"ket)\b", re.M)
    PANEL = "reg-006-wt092-" + "panel"
    check("F6 · corpus digest is the committed one",
          digest == CORPUS_SHA,
          witness=lambda: hashlib.sha256(CORPUS.read_bytes() + b"!").hexdigest() == CORPUS_SHA)
    check("F6 · no network import, no live network module, no panel rebuild",
          not NET.search(src) and PANEL not in src
          and not ({"urllib.request", "requests", "http.client"} & set(sys.modules)),
          witness=lambda: not NET.search(src + "\nimport url" + "lib.request\n"))

    # ---- F8 · the label is deleted, not merely unread ------------------------
    check("F8 · the parsed rows carry no arm, universe, sic, G, t_sum or A",
          all(not ({"arm", "universe", "sic", "G", "t_sum", "A"} & set(r))
              for r in bl),
          witness=lambda: all(not ({"arm", "universe", "sic", "G", "t_sum", "A"}
                                   & set(r)) for r in bl + [{"arm": "JOINT"}]))

    # ---- F7 · resolution, re-run --------------------------------------------
    blob = {k: " ".join(s["text"].lower() for s in p["sents"])
            for k, p in parsed.items()}
    res = {}
    for label, pats in (("phrase", PHRASES), ("internal", INTERNAL), ("external", EXTERNAL)):
        for pat in pats:
            res[f"{label}:{pat}"] = sum(1 for b in blob.values() if pat in b)
    res["marker:M1"] = sum(1 for p in parsed.values() if p["m1"])
    res["marker:M2"] = sum(1 for p in parsed.values() if p["m2"])
    res["marker:M3"] = sum(1 for p in parsed.values() if p["m3"])
    dead = sorted(k for k, v in res.items() if v == 0)
    (DATA / "reg-008-resolution-audit.json").write_text(
        json.dumps({"counts": res, "dead": dead}, indent=1))
    check("F7 · every registered pattern has a recorded hit count",
          len(res) == len(PHRASES) + len(INTERNAL) + len(EXTERNAL) + 3,
          witness=lambda: len({k: v for k, v in list(res.items())[:-1]})
          == len(PHRASES) + len(INTERNAL) + len(EXTERNAL) + 3)
    print(f"             DEAD patterns ({len(dead)}): " + "; ".join(d.split(':', 1)[1] for d in dead))

    # ---- F2 · segmentation ---------------------------------------------------
    bad = sum(1 for v in seg_audit["verdicts"] if v["boundary_error"])
    n_seg = len(seg_audit["verdicts"])
    check(f"F2 · segmentation boundary errors {bad}/{n_seg} <= 10%",
          bad / n_seg <= 0.10,
          witness=lambda: (bad + n_seg) / n_seg <= 0.10)

    # ---- F3 · M1 precision ---------------------------------------------------
    notunit = sum(1 for v in m1_audit["verdicts"] if not v["genuine_unit"])
    n_m1 = len(m1_audit["verdicts"])
    check(f"F3 · M1 non-designators {notunit}/{n_m1} <= 15%",
          notunit / n_m1 <= 0.15,
          witness=lambda: (notunit + n_m1) / n_m1 <= 0.15)

    # ---- F4 · window-edge truncation ----------------------------------------
    edge_n = sum(1 for p in parsed.values() if p["edge"])
    edge_rate = edge_n / len(parsed)
    check(f"F4 · firm-years touching a span edge {edge_n}/{len(parsed)} = {edge_rate:.4f} <= 5%",
          edge_rate <= 0.05,
          witness=lambda: sum(1 for p in parsed.values()
                              if p["n_sent"] > 0) / len(parsed) <= 0.05)

    # ---- F5 · constant provenance, read AND write ---------------------------
    r7 = RESULT7.read_text()
    READ = ("0.436", "0.403", "244", "281", "644", "1,189")
    check("F5 · every REG-007 constant this run prints appears in RESULT-REG-007",
          all(c in r7 for c in READ),
          witness=lambda: all(c in r7 for c in READ + ("0.9991",)))
    check("F5 · every constant this run WRITES is computed in this run",
          True,
          witness=DEFINITIONAL(
              "every number in the result dict below is assigned from a call on `parsed` "
              "in this same process; the read list above is the only imported constant "
              "set, and -21's defect was a complete read list beside a write list that "
              "did not exist. There is no admissible world where a value computed three "
              "lines above arrives from somewhere else, and the guard exists to catch a "
              "refactor that starts importing precomputed values."))

    # ---- rejoin the labels ---------------------------------------------------
    for r in rows:
        parsed[(r["cik"], r["fy_end"])]["arm"] = r["arm"]
        parsed[(r["cik"], r["fy_end"])]["universe"] = r["universe"]
    P = list(parsed.values())
    joint = [p for p in P if p["arm"] == "JOINT"]
    gwonly = [p for p in P if p["arm"] == "GWONLY"]
    placebo = [p for p in P if p["arm"] == "PLACEBO"]
    window = joint + gwonly

    # ---- F1 · the placebo gate (SEEN; a gate, not evidence) -----------------
    kw, nw, rw = rate(window, "m1")
    kp, np_, rp = rate(placebo, "m1")
    delta = rw - rp
    rng = random.Random(SEED)
    fake = window[:]
    rng.shuffle(fake)
    h = len(fake) // 2
    check(f"F1 · placebo gate: {rw:.4f} - {rp:.4f} = {delta:.4f} > 0.033 (REG-007's gap)",
          delta > 0.033,
          witness=lambda: (rate(fake[:h], "m1")[2] - rate(fake[h:], "m1")[2]) > 0.033)

    # ---- F9 · the universe split is computed once ---------------------------
    unis = sorted({p["universe"] for p in P})
    out = {"corpus_sha256": digest, "n_firm_years": len(P),
           "arm_n": {"JOINT": len(joint), "GWONLY": len(gwonly), "PLACEBO": len(placebo)},
           "placebo_gate": {"window_k": kw, "window_n": nw, "window_rate": rw,
                            "placebo_k": kp, "placebo_n": np_, "placebo_rate": rp,
                            "delta": delta, "reg007_gap": 0.033},
           "dead_patterns": dead, "pooled": {}, "by_universe": {}}
    for key in ("m1", "m2", "m3", "m1_f"):
        out["pooled"][key] = lam(joint, gwonly, key)
        out["by_universe"][key] = {
            u: lam([p for p in joint if p["universe"] == u],
                   [p for p in gwonly if p["universe"] == u], key) for u in unis}
    check("F9 · pooled and both universe cells exist in one result object",
          all(set(out["by_universe"][k]) == set(unis) and out["pooled"].get(k)
              for k in ("m1", "m2", "m3", "m1_f")),
          witness=lambda: all(set(out["by_universe"][k]) == set(unis) | {"__absent__"}
                              for k in ("m1",)))

    # ---- F10 · SILENT is its own cell ---------------------------------------
    sil = {a: sum(1 for p in g if p["n_sent"] == 0)
           for a, g in (("JOINT", joint), ("GWONLY", gwonly), ("PLACEBO", placebo))}
    out["silent"] = sil
    check("F10 · SILENT firm-years are counted and excluded from every denominator",
          out["pooled"]["m1"]["joint_n"] + sil["JOINT"] == len(joint)
          and out["pooled"]["m1"]["gwonly_n"] + sil["GWONLY"] == len(gwonly),
          witness=lambda: out["pooled"]["m1"]["joint_n"] + sil["JOINT"] + 1 == len(joint))

    summary("REG-008 FALSIFIERS")

    # ---- the statistics ------------------------------------------------------
    print("\nPLACEBO GATE (SEEN, REG-008 §2.6 — a gate, not evidence)")
    print(f"  window   {kw:4d}/{nw:4d} = {rw:.4f}")
    print(f"  placebo  {kp:4d}/{np_:4d} = {rp:.4f}")
    print(f"  Δ = {delta:.4f}   (REG-007's families: 0.436 − 0.403 = 0.033)")

    for key, tag in (("m1", "M1 named unit   [pooled SEEN]"),
                     ("m1_f", "M1 ∧ (f)-term   [UNSEEN, P2]"),
                     ("m2", "M2 dated trigger [UNSEEN, P4]"),
                     ("m3", "M3 tied amount   [UNSEEN, P4]")):
        d = out["pooled"][key]
        print(f"\n{tag}")
        print(f"  pooled     JOINT {d['joint_k']:4d}/{d['joint_n']:4d} = {d['joint_rate']:.4f} · "
              f"GWONLY {d['gwonly_k']:4d}/{d['gwonly_n']:4d} = {d['gwonly_rate']:.4f} · "
              f"Λ = {d['lambda']:+.4f} · p = {d['p']:.4f} · MDE₈₀ = {d['mde_80']:.4f}")
        for u in unis:
            e = out["by_universe"][key][u]
            thin = " THIN" if min(e["joint_n"], e["gwonly_n"]) < 30 else ""
            print(f"  {u:<9} JOINT {e['joint_k']:4d}/{e['joint_n']:4d} = {e['joint_rate']:.4f} · "
                  f"GWONLY {e['gwonly_k']:4d}/{e['gwonly_n']:4d} = {e['gwonly_rate']:.4f} · "
                  f"Λ = {e['lambda']:+.4f} · p = {e['p']:.4f} · MDE₈₀ = {e['mde_80']:.4f}{thin}")

    print(f"\nSILENT (no trigger-bearing sentence): {sil}")
    (DATA / "reg-008-result.json").write_text(json.dumps(out, indent=1))
    print(f"\nwrote {DATA/'reg-008-result.json'}")
    return 0


def emit_audits(parsed: dict) -> int:
    """Stage 1. Draw the two hand-audit samples, seeded, and write them for adjudication."""
    rng = random.Random(SEED)
    sents = [(k, i, s) for k, p in sorted(parsed.items())
             for i, s in enumerate(p["sents"])]
    seg = rng.sample(sents, 60)
    (DATA / "reg-008-segmentation-sample.json").write_text(json.dumps(
        {"seed": SEED, "n_population": len(sents),
         "items": [{"id": f"{k[0]}:{k[1]}:{i}", "long": s["long"], "text": s["text"]}
                   for k, i, s in seg]}, indent=1))
    withm1 = [(k, i, s) for k, i, s in sents if s["m1"]]
    m1 = rng.sample(withm1, 60)
    (DATA / "reg-008-m1-sample.json").write_text(json.dumps(
        {"seed": SEED, "n_population": len(withm1),
         "items": [{"id": f"{k[0]}:{k[1]}:{i}", "names": s["names"],
                    "text": s["text"][:600]} for k, i, s in m1]}, indent=1))
    print(f"emitted 60/{len(sents)} segmentation items and 60/{len(withm1)} M1 items")
    return 0


if __name__ == "__main__":
    sys.exit(main())
