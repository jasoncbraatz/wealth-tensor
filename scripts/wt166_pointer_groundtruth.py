#!/usr/bin/env python3
"""wt166 — THE LABELLED GROUND TRUTH, AND WHETHER ANY VERB-FREE TEST RECOVERS IT.

WHAT THIS ASKS
--------------
`REVIEW-028` established that the bare-pointer count `wt160` and `wt163` return is a
property of the VERB LIST: two independently-chosen a priori vocabularies returned the
same ten while a reading consulting no list returned fourteen. Its §6.4 then closed the
obvious repair — delete the verb list and flag every bare target — by measuring that
**341 of the corpus's 444 `<token> in <target>` constructions at `07cd47e` have a BARE
target**, most of them ordinary prose. Its §8 falsifier 5 named the one attack left:

    if a defensible sub-class of bare targets can be carved out STRUCTURALLY, without
    any verb list, the enumeration problem is soluble and this review's pessimism is
    wrong. That is the single most valuable attack available on this file.

Nobody had run it because nobody had the labels. `docs/pointer-groundtruth.tsv` is the
labels — all 341 rows READ and adjudicated by hand, no verb list consulted, because a
ground truth built with a word list cannot score a word list. This script recomputes the
341, refuses if the labels have drifted from the corpus by a single row, and SCORES
candidate verb-free structural tests against them, reporting precision AND recall.

WHAT "VERB-FREE" HAS TO MEAN, OR THE EXERCISE IS CIRCULAR
--------------------------------------------------------
Verb-free is not the same as vocabulary-free, and the difference is the whole finding.
A test that keys on CLOSED-CLASS function words — determiners, copulas, prepositions, a
fixed and finite set English is not adding to — carries no content vocabulary and is
vocabulary-free in the sense at issue. A test that keys on OPEN-CLASS content words —
verbs, nouns — is a word list wearing a different hat, and inherits every enumeration
problem REVIEW-028 documented. Two candidates below (T2, T5) are open-class and are
labelled LIST-BOUND. **T5 is expected to score best of the five and is disqualified in
advance for exactly this reason** — see REVIEW-029 §2.1, written before any score existed.

THE BAR, NAMED IN ADVANCE (REVIEW-029 §3, committed at 2515eaf before a single label existed)
--------------------------------------------------------------------------------------------
A test CLEARS iff precision >= 0.50 AND recall >= 0.80 over all 341 rows. The prediction
was that none would, that the mechanism is the ~4.4% base rate, and that the separating
feature is not in the target at all — it is in the verb.

PRE-REGISTERED CANDIDATES (T1..T5) versus EXPLORATORY (T6)
----------------------------------------------------------
T1..T5 and the best pairwise conjunction were named in REVIEW-029 §2.1 BEFORE the labels
existed. **T6 was invented AFTER reading the labels and is reported as EXPLORATORY.** It
cannot falsify the prediction — a test chosen by looking at the answers and then scored on
those same answers is fitting, not testing — and this script prints that caveat next to its
numbers rather than in a footnote. The held-out corpus that could test T6 honestly already
exists and is untouched: Papers I and II, out of `#scope` for seven passes running.

THE LABELS ARE PINNED TO `07cd47e` AND DO NOT MOVE WHEN THE MANUSCRIPTS ARE REPAIRED.
`wt164` repaired four of these rows at HEAD and `wt167` repairs a fifth; this script always
reads `07cd47e`, so a repair cannot silently invalidate the ground truth. F9 proves the
revision pin is live rather than decorative.

EXIT CODES:  0 = labels intact and scoring complete · 2 = key-set drift, or a
post-condition failed, or the instrument is broken.  There is no exit 1: this script
reports a measurement, it does not flag defects.
"""
from __future__ import annotations

import argparse
import importlib.util
import json
import os
import re
import subprocess
import sys

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GROUNDTRUTH = os.path.join(REPO_ROOT, "docs", "pointer-groundtruth.tsv")
REV = "07cd47e"

PAPERS = [
    ("III", "docs/papers/paper-III-dual-tensor/paper-III.md"),
    ("IV", "docs/papers/paper-IV-composition/paper-IV.md"),
]

# --- import wt160's criterion rather than re-implementing it -------------------------
# Same rule as wt163: "same criterion" must be PROVED by sharing the code, not asserted.
_spec = importlib.util.spec_from_file_location(
    "wt160", os.path.join(os.path.dirname(os.path.abspath(__file__)),
                          "wt160_bare_pointer_sweep.py"))
wt160 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(wt160)

# Every WORD token immediately preceding " in ". The corpus's own vocabulary, not anyone's
# guess at one — REVIEW-028 §3 step 1. The `(?<![\w-])` guard is wt160's, for the same
# reason: `\b` fires inside a hyphenated compound (`mis-specified in`).
TOKEN_RE = re.compile(r"(?<![\w-])([A-Za-z][\w'’-]*)\s+in\s+")

MARKUP = re.compile(r"[*_]{1,3}")

# --- CLOSED-CLASS function words: not a content vocabulary --------------------------
DEFINITE = {"the", "this", "that", "these", "those", "its", "their", "his", "her",
            "our", "your", "my"}
DETERMINERS = DEFINITE | {"a", "an", "some", "any", "each", "every", "no", "both"}
BE_FORMS = {"is", "are", "was", "were", "be", "been", "being", "am"}

# --- OPEN-CLASS lists: these make T2 and T5 LIST-BOUND, by construction --------------
CLAIM_NOUNS = {"claim", "claims", "result", "results", "finding", "findings", "analysis",
               "analyses", "conjecture", "conjectures", "prediction", "predictions",
               "reason", "reasons", "evidence", "control", "controls", "test", "tests",
               "measurement", "measurements", "statement", "entry", "entries", "work",
               "works", "figure", "figures", "number", "numbers", "value", "values"}
DOC_NOUNS = {"statement", "registration", "registrations", "title", "titles", "table",
             "tables", "log", "logs", "note", "notes", "repository", "paper", "papers",
             "appendix", "text", "record", "records", "run", "runs", "sweep", "sweeps",
             "directory", "file", "files", "section", "sections", "abstract", "list",
             "draft", "report", "reports", "document", "documents", "row", "rows",
             "session", "sessions", "commit", "commits", "figure", "figures"}


def _read(path: str, rev: str | None):
    if rev:
        return subprocess.check_output(["git", "show", f"{rev}:{path}"],
                                       cwd=REPO_ROOT).decode("utf-8")
    with open(os.path.join(REPO_ROOT, path), encoding="utf-8") as fh:
        return fh.read()


def _section_spans(flat: str):
    """Character spans of each `##`/`###` heading's section in the flattened text."""
    starts = [m.start() for m in re.finditer(r"(?:^| )#{2,3} ", flat)]
    if not starts:
        return [(0, len(flat))]
    bounds = starts + [len(flat)]
    return [(bounds[i], bounds[i + 1]) for i in range(len(starts))]


def enumerate_rows(rev: str | None = REV):
    """Every `<token> in <target>` construction; bare ones (N1..N6 silent) are the 341."""
    rows, considered = [], 0
    for label, path in PAPERS:
        text = _read(path, rev)
        flat, lines = wt160._flatten(text)
        spans = _section_spans(flat)
        for m in TOKEN_RE.finditer(flat):
            considered += 1
            target = wt160._target_window(flat, m.end())
            if wt160._is_named(target) is not None:
                continue
            # everything from the previous clause boundary up to the construction
            j = m.start()
            while j > 0 and flat[j - 1] not in ".;:!?" and m.start() - j < 160:
                j -= 1
            lead = flat[j:m.start()]
            pos = 0.0
            for a, b in spans:
                if a <= m.start() < b and b > a:
                    pos = (m.start() - a) / (b - a)
                    break
            rows.append({
                "file": label,
                "line": lines[m.start()] if m.start() < len(lines) else 0,
                "token": m.group(1),
                "target": target,
                "lead": lead.strip(),
                "section_pos": pos,
                "excerpt": flat[max(0, m.start() - 90):min(len(flat), m.end() + 120)].strip(),
            })
    return rows, considered


def key(row) -> tuple:
    return (row["file"], int(row["line"]), row["token"], row["target"])


# --- the candidate verb-free structural tests ---------------------------------------

def _words(target: str):
    return MARKUP.sub("", target).strip().split()


def t1_definite_head(row) -> bool:
    """T1 · the target begins with a definite determiner. CLOSED-CLASS."""
    w = _words(row["target"])
    return bool(w) and w[0].lower().strip("*_(“\"'") in DEFINITE


def t2_claim_subject(row) -> bool:
    """T2 · the clause's subject is a claim/result noun. OPEN-CLASS — LIST-BOUND."""
    lead = MARKUP.sub("", row["lead"]).lower()
    return any(re.search(rf"(?<![\w-]){re.escape(n)}(?![\w-])", lead) for n in CLAIM_NOUNS)


def t3_det_abstract_shape(row) -> bool:
    """T3 · short determiner-headed target, no digit, no percentage. CLOSED-CLASS."""
    w = _words(row["target"])
    if not (1 <= len(w) <= 4):
        return False
    if w[0].lower().strip("*_(“\"'") not in DETERMINERS:
        return False
    return not any(ch.isdigit() or ch == "%" for ch in row["target"])


def t4_section_position(row) -> bool:
    """T4 · the construction sits in the final third of its section. CLOSED-CLASS (none)."""
    return row["section_pos"] >= 2.0 / 3.0


def t5_document_head_noun(row) -> bool:
    """T5 · the target contains a document-class noun. OPEN-CLASS — LIST-BOUND.

    Pre-disqualified in REVIEW-029 §2.1, before any score existed: it is verb-free and it
    is not vocabulary-free. If it wins it wins by moving the word list from the verb to
    the noun, which relocates the enumeration problem rather than solving it.
    """
    w = [x.lower().strip("*_.,;:()“”\"'") for x in _words(row["target"])]
    return any(x in DOC_NOUNS for x in w)


def t6_copular_frame(row) -> bool:
    """T6 · EXPLORATORY, invented AFTER the labels were read. CLOSED-CLASS.

    A form of `be` within the three tokens before the construction — the copular or
    passive frame `X is/are <token> in Y`. This CANNOT falsify REVIEW-029 §3's prediction:
    it was chosen by looking at the answers. Papers I and II are the held-out corpus.
    """
    lead = MARKUP.sub("", row["lead"]).lower().split()
    return any(w.strip(".,;:()“”\"'") in BE_FORMS for w in lead[-3:])


CANDIDATES = [
    ("T1", "definite head", "CLOSED-CLASS", "pre-registered", t1_definite_head),
    ("T2", "claim-subject", "OPEN-CLASS (LIST-BOUND)", "pre-registered", t2_claim_subject),
    ("T3", "determiner + abstract-noun shape", "CLOSED-CLASS", "pre-registered", t3_det_abstract_shape),
    ("T4", "section position (final third)", "CLOSED-CLASS", "pre-registered", t4_section_position),
    ("T5", "document-class head noun", "OPEN-CLASS (LIST-BOUND)", "pre-registered (disqualified in advance)", t5_document_head_noun),
    ("T6", "copular/passive frame", "CLOSED-CLASS", "EXPLORATORY — post-hoc, cannot falsify", t6_copular_frame),
]

PRECISION_BAR = 0.50
RECALL_BAR = 0.80


def score(rows, positives: set, fn) -> dict:
    tp = fp = fn_ = 0
    for r in rows:
        flagged, real = fn(r), key(r) in positives
        if flagged and real:
            tp += 1
        elif flagged:
            fp += 1
        elif real:
            fn_ += 1
    prec = tp / (tp + fp) if (tp + fp) else 0.0
    rec = tp / (tp + fn_) if (tp + fn_) else 0.0
    return {"flagged": tp + fp, "tp": tp, "fp": fp, "fn": fn_,
            "precision": prec, "recall": rec,
            "clears": prec >= PRECISION_BAR and rec >= RECALL_BAR}


def load_labels():
    rows = []
    with open(GROUNDTRUTH, encoding="utf-8") as fh:
        header = None
        for line in fh:
            if line.startswith("#") or not line.strip():
                continue
            parts = line.rstrip("\n").split("\t")
            if header is None:
                header = parts
                continue
            rows.append(dict(zip(header, parts)))
    return rows


def label_variants(labels):
    """PRIMARY (as written) · STRICT (FIRM pointers only) · LOOSE (+ every SOFT NOT-POINTER)."""
    def k(r):
        return (r["file"], int(r["line"]), r["token"], r["target"])
    primary = {k(r) for r in labels if r["label"] == "POINTER"}
    strict = {k(r) for r in labels if r["label"] == "POINTER" and r["confidence"] == "FIRM"}
    loose = primary | {k(r) for r in labels
                       if r["label"] == "NOT-POINTER" and r["confidence"] == "SOFT"}
    return {"PRIMARY": primary, "STRICT": strict, "LOOSE": loose}


# --- post-conditions -----------------------------------------------------------------
# POSITIVE = the instrument must fire.  NEGATIVE = the instrument must stay silent.

REVIEW028_FOURTEEN = {
    ("III", 11, "named", "the data-availability statement"),
    ("III", 1001, "states", "the table where it belongs"),
    ("III", 1551, "given", "the two rows above"),
    ("III", 1608, "given", "the companion papers of this programme"),
    ("III", 2372, "named", "its own title"),
    ("III", 2400, "named", "its own title"),
    ("III", 2529, "named", "the title"),
    ("IV", 11, "named", "the data-availability statement"),
    ("IV", 397, "named", "the registration"),
    ("IV", 444, "stated", "the registration before the numbers existed"),
    ("III", 625, "visible", "the parameter sweep"),
    ("III", 1216, "declared", "the registration before the pilot was run"),
    ("III", 2055, "printed", "the same logs"),
    ("IV", 725, "verified", "the sessions that introduced them to Papers II or III"),
}

# wt163's six disclosed false positives, as they appear inside the 341.
EXCLUSION_TARGETS = ["place by a test suite", "**100%**", "all nine is the sign"]


def _postconditions(rows, labels, variants, results):
    checks = []

    def add(cid, kind, desc, fn):
        checks.append((cid, kind, desc, fn))

    recomputed = {key(r) for r in rows}
    labelled = {(r["file"], int(r["line"]), r["token"], r["target"]) for r in labels}

    add("F1", "POSITIVE", "the TSV's key set is EXACTLY the recomputed key set",
        lambda: (recomputed == labelled,
                 f"{len(recomputed)} recomputed, {len(labelled)} labelled, "
                 f"{len(recomputed ^ labelled)} symmetric difference"))

    add("F2", "POSITIVE", "REVIEW-028 §3/§6.4's published counts reproduce (444/341/282/59)",
        lambda: ((len(rows) == 341
                  and sum(1 for r in rows if r["file"] == "III") == 282
                  and sum(1 for r in rows if r["file"] == "IV") == 59),
                 f"{len(rows)} bare; III {sum(1 for r in rows if r['file']=='III')}, "
                 f"IV {sum(1 for r in rows if r['file']=='IV')}"))

    add("F3", "POSITIVE", "every one of wt160's ten flags at 07cd47e is labelled POINTER",
        lambda: _f3(variants))

    add("F4", "POSITIVE", "exactly one POINTER row is outside REVIEW-028's fourteen, and it is "
                          "III 1261 «are in the run logs»",
        lambda: _f4(variants))

    add("F5", "NEGATIVE", "none of wt163's disclosed false positives is labelled POINTER",
        lambda: _f5(labels))

    add("F6", "NEGATIVE", "no PRE-REGISTERED candidate clears precision>=0.50 AND recall>=0.80 "
                          "under the PRIMARY labels",
        lambda: _f6(results))

    add("F7", "NEGATIVE", "T4 (section position) does not reach twice the base rate in precision",
        lambda: _f7(results, variants))

    add("F8", "POSITIVE", "PRIMARY and STRICT agree: no pre-registered candidate clears under "
                          "either — the verdict does not turn on the four SOFT pointers",
        lambda: _f8(results))

    add("F14", "POSITIVE", "under LOOSE exactly one pre-registered candidate clears, and it is "
                           "T5 — the LIST-BOUND one disqualified in advance. F8's FIRST form "
                           "asserted all three variants agree and was WRONG (REVIEW-029 §7)",
        lambda: _f14(results))

    add("F15", "NEGATIVE", "LOOSE is not an independent test of T5: the SOFT NOT-POINTER rows it "
                           "promotes are overwhelmingly document-noun rows, which is what T5 "
                           "selects on",
        lambda: _f15(rows, labels, variants))

    add("F9", "NEGATIVE", "the revision pin is LIVE: recomputing at HEAD does NOT give the "
                          "07cd47e key set (wt164 and wt167 repaired five of these rows)",
        _f9)

    add("F10", "POSITIVE", "the key (file, line, token, target) is unique across all 341 rows",
        lambda: (len(labelled) == len(labels) == 341,
                 f"{len(labels)} rows, {len(labelled)} distinct keys"))

    add("F11", "NEGATIVE", "the drift guard is not vacuous: a fabricated row makes F1 fail",
        lambda: (recomputed != (labelled | {("III", 99999, "fabricated", "a row")}),
                 "one invented key breaks equality"))

    add("F12", "POSITIVE", "the labels are 15 POINTER — 11 FIRM, 4 SOFT — and 36 SOFT NOT-POINTER",
        lambda: _f12(labels))

    add("F13", "NEGATIVE", "T1 does not reach the precision bar, as REVIEW-029 §3 predicted "
                           "specifically (high recall, abject precision)",
        lambda: _f13(results))

    return checks


def _f3(variants):
    text = _read(PAPERS[0][1], REV)
    flags = wt160.sweep_text(text, PAPERS[0][1])[0]
    text4 = _read(PAPERS[1][1], REV)
    flags += wt160.sweep_text(text4, PAPERS[1][1])[0]
    keys = {("III" if "paper-III" in f["file"] else "IV", f["line"], f["verb"], f["target"])
            for f in flags}
    missing = keys - variants["PRIMARY"]
    return not missing, f"{len(flags)} wt160 flags at {REV}; {len(missing)} not labelled POINTER"


def _f4(variants):
    extra = variants["PRIMARY"] - REVIEW028_FOURTEEN
    want = {("III", 1261, "are", "the run logs")}
    return extra == want, f"outside the fourteen: {sorted(extra)}"


def _f5(labels):
    hits = [r for r in labels
            if any(t in r["target"] for t in EXCLUSION_TARGETS) and r["label"] == "POINTER"]
    seen = [r for r in labels if any(t in r["target"] for t in EXCLUSION_TARGETS)]
    return not hits, f"{len(seen)} exclusion row(s) present, {len(hits)} labelled POINTER"


def _f6(results):
    bad = [r for r in results["PRIMARY"]
           if r["prereg"] and r["score"]["clears"]]
    return not bad, f"{len(bad)} pre-registered candidate(s) clear the bar"


def _f7(results, variants):
    base = len(variants["PRIMARY"]) / 341
    t4 = next(r for r in results["PRIMARY"] if r["id"] == "T4")
    return t4["score"]["precision"] < 2 * base, \
        f"T4 precision {t4['score']['precision']:.4f} against a base rate of {base:.4f}"


def _f8(results):
    verdicts = {v: sorted(r["id"] for r in results[v] if r["prereg"] and r["score"]["clears"])
                for v in ("PRIMARY", "STRICT", "LOOSE")}
    return verdicts["PRIMARY"] == verdicts["STRICT"] == [], f"{verdicts}"


def _f14(results):
    """The surprise, pinned. Under LOOSE the verdict FLIPS, and only for T5.

    F8's first form asserted PRIMARY, STRICT and LOOSE all agree. They do not. That
    assertion was a prediction about the measurement, the measurement refuted it, and the
    honest repair is to pin what was measured rather than to relax the bar or drop the
    variant — REVIEW-028 §7.2's rule, which cost that session three post-conditions.
    """
    cleared = sorted(r["id"] for r in results["LOOSE"] if r["prereg"] and r["score"]["clears"])
    t5 = next(r for r in results["LOOSE"] if r["id"] == "T5")
    return cleared == ["T5"], (f"LOOSE clears {cleared}; T5 precision "
                               f"{t5['score']['precision']:.4f}, recall {t5['score']['recall']:.4f}")


def _f15(rows, labels, variants):
    """Why T5's LOOSE win deflates, stated as a number rather than as a rhetorical move."""
    soft_np = {(r["file"], int(r["line"]), r["token"], r["target"])
               for r in labels if r["label"] == "NOT-POINTER" and r["confidence"] == "SOFT"}
    hit = sum(1 for r in rows if key(r) in soft_np and t5_document_head_noun(r))
    return hit >= 0.75 * len(soft_np), (f"T5 flags {hit} of the {len(soft_np)} SOFT NOT-POINTER "
                                        f"rows LOOSE promotes to positives "
                                        f"({hit/len(soft_np):.0%}) — near-circular")


def _f9():
    try:
        head_rows, _ = enumerate_rows(rev="HEAD")
    except Exception as exc:                                     # noqa: BLE001
        return False, f"raised {exc!r}"
    rev_rows, _ = enumerate_rows(rev=REV)
    same = {key(r) for r in head_rows} == {key(r) for r in rev_rows}
    return not same, (f"HEAD {len(head_rows)} bare rows against {REV}'s {len(rev_rows)}; "
                      f"key sets {'IDENTICAL — the pin is dead' if same else 'differ, as they must'}")


def _f12(labels):
    p = [r for r in labels if r["label"] == "POINTER"]
    firm = [r for r in p if r["confidence"] == "FIRM"]
    softnp = [r for r in labels if r["label"] == "NOT-POINTER" and r["confidence"] == "SOFT"]
    ok = len(p) == 15 and len(firm) == 11 and len(softnp) == 36
    return ok, f"{len(p)} POINTER ({len(firm)} FIRM, {len(p)-len(firm)} SOFT), {len(softnp)} SOFT NOT-POINTER"


def _f13(results):
    t1 = next(r for r in results["PRIMARY"] if r["id"] == "T1")
    return t1["score"]["precision"] < PRECISION_BAR, \
        f"T1 precision {t1['score']['precision']:.4f}, recall {t1['score']['recall']:.4f}"


def run_postconditions(rows, labels, variants, results, verbose=True):
    ok_all, out = True, []
    for cid, kind, desc, fn in _postconditions(rows, labels, variants, results):
        try:
            ok, detail = fn()
        except Exception as exc:                                 # noqa: BLE001
            ok, detail = False, f"raised {exc!r}"
        ok_all &= ok
        out.append({"id": cid, "kind": kind, "desc": desc, "ok": ok, "detail": detail})
        if verbose:
            print(f"  [{'ok  ' if ok else 'FAIL'}] {cid} {kind:8s} {desc} — {detail}")
    return ok_all, out


def main(argv=None):
    ap = argparse.ArgumentParser(description="wt166 — score verb-free structural tests against "
                                             "the labelled bare-pointer ground truth")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--skip-postconditions", action="store_true")
    args = ap.parse_args(argv)

    try:
        rows, considered = enumerate_rows(REV)
    except Exception as exc:                                     # noqa: BLE001
        print(f"wt166: cannot enumerate at {REV}: {exc}", file=sys.stderr)
        return 2

    labels = load_labels()
    labelled = {(r["file"], int(r["line"]), r["token"], r["target"]) for r in labels}
    recomputed = {key(r) for r in rows}

    if recomputed != labelled:
        only_corpus = sorted(recomputed - labelled)
        only_file = sorted(labelled - recomputed)
        print("wt166: REFUSING — docs/pointer-groundtruth.tsv has drifted from the corpus.",
              file=sys.stderr)
        print(f"  {len(only_corpus)} construction(s) in the corpus with no label:", file=sys.stderr)
        for k in only_corpus[:20]:
            print(f"    + {k}", file=sys.stderr)
        print(f"  {len(only_file)} label(s) with no construction:", file=sys.stderr)
        for k in only_file[:20]:
            print(f"    - {k}", file=sys.stderr)
        print("  Labels cannot drift from the corpus. Re-read the affected rows and re-label; "
              "do not edit this guard.", file=sys.stderr)
        return 2

    variants = label_variants(labels)
    results = {}
    for name, positives in variants.items():
        results[name] = [
            {"id": cid, "desc": desc, "klass": klass, "status": status,
             "prereg": status.startswith("pre-registered"),
             "score": score(rows, positives, fn)}
            for cid, desc, klass, status, fn in CANDIDATES
        ]

    # the best pairwise conjunction over the PRE-REGISTERED five — committed in advance
    prereg = [(c[0], c[4]) for c in CANDIDATES if c[3].startswith("pre-registered")]
    pairs = []
    for i in range(len(prereg)):
        for j in range(i + 1, len(prereg)):
            (ai, fa), (bi, fb) = prereg[i], prereg[j]
            s = score(rows, variants["PRIMARY"], lambda r, fa=fa, fb=fb: fa(r) and fb(r))
            pairs.append({"pair": f"{ai}+{bi}", "score": s})
    pairs.sort(key=lambda p: (p["score"]["precision"], p["score"]["recall"]), reverse=True)

    post_ok, post = (True, [])
    if not args.skip_postconditions:
        if not args.json:
            print("=== wt166 post-conditions ===")
        post_ok, post = run_postconditions(rows, labels, variants, results,
                                           verbose=not args.json)

    payload = {
        "rev": REV, "considered": considered, "bare": len(rows),
        "labels": {k: len(v) for k, v in variants.items()},
        "bar": {"precision": PRECISION_BAR, "recall": RECALL_BAR},
        "results": results, "best_pairs": pairs[:5],
        "postconditions_ok": post_ok, "postconditions": post,
    }

    if args.json:
        print(json.dumps(payload, indent=2, ensure_ascii=False))
    else:
        print()
        print(f"=== the corpus at {REV} ===")
        print(f"  {considered} «<token> in <target>» constructions, {len(rows)} with a BARE "
              f"target (N1..N6 silent)")
        print(f"  labels: PRIMARY {len(variants['PRIMARY'])} pointers "
              f"({len(variants['PRIMARY'])/len(rows):.2%} base rate) · "
              f"STRICT {len(variants['STRICT'])} · LOOSE {len(variants['LOOSE'])}")
        print(f"  the bar, named in advance: precision >= {PRECISION_BAR:.2f} "
              f"AND recall >= {RECALL_BAR:.2f}")
        for name in ("PRIMARY", "STRICT", "LOOSE"):
            print(f"\n=== scored against {name} labels "
                  f"({len(variants[name])} pointers of {len(rows)}) ===")
            print(f"  {'':4s} {'test':34s} {'flagged':>7s} {'TP':>4s} {'FP':>4s} {'FN':>4s} "
                  f"{'prec':>7s} {'recall':>7s}  verdict")
            for r in results[name]:
                s = r["score"]
                print(f"  {r['id']:4s} {r['desc']:34s} {s['flagged']:7d} {s['tp']:4d} "
                      f"{s['fp']:4d} {s['fn']:4d} {s['precision']:7.4f} {s['recall']:7.4f}  "
                      f"{'CLEARS' if s['clears'] else 'fails'}"
                      f"{'' if r['prereg'] else '   [EXPLORATORY — post-hoc, cannot falsify]'}")
        print("\n=== best pairwise conjunctions of the pre-registered five (PRIMARY) ===")
        for p in pairs[:5]:
            s = p["score"]
            print(f"  {p['pair']:9s} flagged {s['flagged']:4d}  prec {s['precision']:7.4f}  "
                  f"recall {s['recall']:7.4f}  {'CLEARS' if s['clears'] else 'fails'}")
        cleared = [r["id"] for r in results["PRIMARY"] if r["prereg"] and r["score"]["clears"]]
        print(f"\nVERDICT: {len(cleared)} of 5 pre-registered verb-free structural tests clear "
              f"the bar" + (f" — {cleared}" if cleared else " — none."))

    if not post_ok:
        print("wt166: POST-CONDITIONS FAILED — the instrument is not trustworthy.", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
