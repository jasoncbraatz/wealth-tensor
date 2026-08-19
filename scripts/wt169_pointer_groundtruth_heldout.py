#!/usr/bin/env python3
"""wt169 — THE HELD-OUT TEST: does the document-noun pre-filter survive text it was not built against?

WHAT THIS ASKS
--------------
`REVIEW-029` scored six verb-free structural tests against 341 hand-labelled bare-target
rows in Papers III and IV. Nothing cleared the bar. But two of its numbers were measured
on the corpus they were built against:

  * **T5's recall of 1.0000.** The document-class-noun test flags 61 of the 341 and holds
    all fifteen POINTERs — a 5.6x reading reduction with zero misses. Its noun list
    `DOC_NOUNS` was written by the session that had just read all 341 labels.
  * **T6's failure** (0.0366 / 0.2000). T6 was invented AFTER those labels were read and
    scored on them. A test chosen by looking at the answers is fitting, not testing.

`REVIEW-029` §8 falsifiers 4 and 5 name running both on held-out text as the outstanding
work. **Papers I and II are that text**: untouched, in the repository, and no instrument
in this programme — not `N1`-`N6`, not `DOC_NOUNS`, not `CLAIM_NOUNS`, not `T6` — was
written against a sentence of them. `docs/pointer-groundtruth-I-II.tsv` is the held-out
truth set: 88 bare-target rows at `83db4d5`, all read in context, labelled by REVIEW-028
§3's rule, committed before this file existed.

THE RULE THAT MAKES THIS A TEST AND NOT A REPEAT
------------------------------------------------
**Every candidate function and every word list is IMPORTED FROM `wt166`, unmodified.**
Not one word of `DOC_NOUNS` or `CLAIM_NOUNS` is re-tuned — re-tuning them would make this
the same circular exercise one corpus over, which is the exact failure REVIEW-027 §5
named. `G8` enforces that mechanically: the sets are hashed and compared against digests
recorded here, so a future session that edits a noun list makes this script fail loudly
rather than quietly rescoring.

THE BARS
--------
Carried over from REVIEW-029 §3 unchanged, so the two measurements are commensurable:
CLEARS iff precision >= 0.50 AND recall >= 0.80; PARTIAL WIN iff precision >= 0.30 with
recall >= 0.90. REVIEW-030 §3 adds one this programme had never defined operationally:

    a candidate is a **USABLE PRE-FILTER** iff, on text it was not built against, it
    reaches recall == 1.0000 AND flags <= 25% of rows.

Recall must be *perfect*: a pre-filter exists so a human can decline to read the rows it
does not flag, and one miss means the human must read them all anyway to be sure.

POST-CONDITIONS ARE PREDICTIONS, AND THIS FILE WAS COMMITTED UNRUN
------------------------------------------------------------------
`G6`, `G7`, `G11`, `G12`, `G13` and `G14` assert things about a measurement that had not
been taken when they were written. That is deliberate (wealthTensor-89's lesson vii). If
one of them is wrong the repair is REVIEW-028 §7.2's: narrow it to the true fact, add a
post-condition pinning the surprise, and say so in the review — never relax the bar.

EXIT CODES:  0 = labels intact and scoring complete · 2 = key-set drift, a mutated word
list, or a failed post-condition.  There is no exit 1: this reports a measurement, it
does not flag defects.
"""
from __future__ import annotations

import argparse
import contextlib
import hashlib
import importlib.util
import json
import os
import sys

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GROUNDTRUTH = os.path.join(REPO_ROOT, "docs", "pointer-groundtruth-I-II.tsv")
REV = "83db4d5"

HELD_OUT_PAPERS = [
    ("I", "docs/papers/paper-I-price-formation/paper-I.md"),
    ("II", "docs/papers/paper-II-redistribution/paper-II.md"),
]

# --- import wt166 whole: its enumerator, its candidates, its word lists, its scorer ---
_spec = importlib.util.spec_from_file_location(
    "wt166", os.path.join(os.path.dirname(os.path.abspath(__file__)),
                          "wt166_pointer_groundtruth.py"))
wt166 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(wt166)

# Digests of wt166's word lists as they stood when this file was written, sorted and
# joined with '|'. G8 compares against these: a re-tuned list fails the run.
WORDLIST_DIGESTS = {
    "CLAIM_NOUNS": "67d2c39795f72b83a0dff456059cbbdcd4093aaf24dd5ca4212806edcf804677",
    "DOC_NOUNS":   "c8455f33c422c4f9781c3aede56307aca6bf37923047c09a83b07e4927e01fd2",
    "DEFINITE":    "437efdb8197338188eab42f7ea69690c19fb4eb342271dd143b73a2a862283d7",
    "DETERMINERS": "54097d5ea131014a297ebfc749d0e80230cfd0c19d15d829ecd0709904449a89",
    "BE_FORMS":    "fe0100ddae4e2f99cb20b6f65eb67a778aa8d008f16df3de41cbb5b515303ee2",
}

# REVIEW-029 §5's published numbers for the SAME six tests on the corpus they were built
# against, quoted here only to print the two columns side by side. wt166 is re-run below
# to recompute them rather than trusting these; G13 compares the recomputation, not these.
III_IV_PUBLISHED = {"T5_recall": 1.0000, "T5_precision": 0.2459, "T5_flagged": 61,
                    "bare": 341, "pointers": 15}

PRECISION_BAR = wt166.PRECISION_BAR      # 0.50, imported not restated
RECALL_BAR = wt166.RECALL_BAR            # 0.80
PARTIAL_PRECISION_BAR = 0.30
PARTIAL_RECALL_BAR = 0.90
PREFILTER_FLAG_FRACTION = 0.25


@contextlib.contextmanager
def _papers(papers):
    """Point wt166's enumerator at a different corpus, then put it back.

    G9 proves the restore actually happens: after this script has scored the held-out
    corpus, wt166's own 341-row enumeration at 07cd47e must still reproduce exactly.
    """
    saved = wt166.PAPERS
    wt166.PAPERS = papers
    try:
        yield
    finally:
        wt166.PAPERS = saved


def enumerate_held_out(rev: str | None = REV):
    with _papers(HELD_OUT_PAPERS):
        return wt166.enumerate_rows(rev)


def load_labels(path: str = GROUNDTRUTH):
    rows, header = [], None
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            if line.startswith("#") or not line.strip():
                continue
            parts = line.rstrip("\n").split("\t")
            if header is None:
                header = parts
                continue
            rows.append(dict(zip(header, parts)))
    return rows


def _digest(names) -> str:
    return hashlib.sha256("|".join(sorted(names)).encode()).hexdigest()


def prefilter_verdict(s, n_rows) -> bool:
    return s["recall"] >= 1.0 and s["flagged"] <= PREFILTER_FLAG_FRACTION * n_rows


# --- post-conditions ------------------------------------------------------------------
# POSITIVE = the instrument must fire.  NEGATIVE = the instrument must stay silent.

def _postconditions(rows, labels, variants, results, pairs, iiiv):
    checks = []

    def add(cid, kind, desc, fn):
        checks.append((cid, kind, desc, fn))

    recomputed = {wt166.key(r) for r in rows}
    labelled = {(r["file"], int(r["line"]), r["token"], r["target"]) for r in labels}

    add("G1", "POSITIVE", "the TSV's key set is EXACTLY the recomputed key set",
        lambda: (recomputed == labelled,
                 f"{len(recomputed)} recomputed, {len(labelled)} labelled, "
                 f"{len(recomputed ^ labelled)} symmetric difference"))

    add("G2", "POSITIVE", "the held-out corpus is 125 constructions / 88 bare / 44 in I / 44 in II",
        lambda: ((len(rows) == 88
                  and sum(1 for r in rows if r["file"] == "I") == 44
                  and sum(1 for r in rows if r["file"] == "II") == 44),
                 f"{len(rows)} bare; I {sum(1 for r in rows if r['file']=='I')}, "
                 f"II {sum(1 for r in rows if r['file']=='II')}"))

    add("G3", "POSITIVE", "the labels are 7 POINTER — 4 FIRM, 3 SOFT — and 9 SOFT NOT-POINTER",
        lambda: _g3(labels))

    add("G4", "POSITIVE", "the key (file, line, token, target) is unique across all 88 rows",
        lambda: (len(labelled) == len(labels) == 88,
                 f"{len(labels)} rows, {len(labelled)} distinct keys"))

    add("G5", "NEGATIVE", "the drift guard is not vacuous: a fabricated row makes G1 fail",
        lambda: (recomputed != (labelled | {("I", 99999, "fabricated", "a row")}),
                 "one invented key breaks equality"))

    add("G8", "POSITIVE", "wt166's word lists are UNMODIFIED — DOC_NOUNS and CLAIM_NOUNS were "
                          "not re-tuned for this corpus",
        _g8)

    add("G6", "NEGATIVE", "T5 does NOT reach recall 1.0000 on held-out text — the number "
                          "REVIEW-029 §6.1 warned would not survive",
        lambda: _g6(results))

    add("G13", "POSITIVE", "T5's recall is STRICTLY LOWER here than on the corpus its noun list "
                           "was written against, recomputed rather than quoted",
        lambda: _g13(results, iiiv))

    add("G7", "NEGATIVE", "no pre-registered candidate (T1..T5) clears precision>=0.50 AND "
                          "recall>=0.80 under the PRIMARY labels",
        lambda: _g7(results))

    add("G11", "NEGATIVE", "no pre-registered candidate reaches the PARTIAL-WIN bar either "
                           "(precision>=0.30 with recall>=0.90)",
        lambda: _g11(results))

    add("G14", "NEGATIVE", "no candidate — pre-registered or exploratory — is a USABLE PRE-FILTER "
                           "on held-out text (recall 1.0000 with <=25% of rows flagged)",
        lambda: _g14(results, rows))

    add("G12", "POSITIVE", "the mechanism, as a number: exactly ONE of the 7 POINTERs has a "
                           "DOC_NOUNS word in its target, and it is the data-availability "
                           "statement — the one construction Paper III also carries",
        lambda: _g12(rows, variants))

    add("G15", "NEGATIVE", "the truth set is not a restatement of the thing being tested: T5's "
                           "flag set is NOT the POINTER set",
        lambda: _g15(rows, variants))

    add("G16", "POSITIVE", "T6 is being scored, for the first time, on text it was not invented "
                           "against — and it still fails",
        lambda: _g16(results))

    add("G17", "POSITIVE", "the base rate here is between 2% and 9%, so this class is a property "
                           "of how these manuscripts are written and not of Paper III's length",
        lambda: _g17(rows, variants))

    add("G9", "POSITIVE", "wt166 is left UNMUTATED: its own 341-row enumeration at 07cd47e still "
                          "reproduces after this script has re-pointed and restored PAPERS",
        _g9)

    add("G10", "POSITIVE", "the best pairwise conjunction was computed and reported whether or "
                           "not it helps (REVIEW-029 §3's standing commitment)",
        lambda: (len(pairs) >= 1,
                 f"best pair {pairs[0]['pair']} prec {pairs[0]['score']['precision']:.4f} "
                 f"recall {pairs[0]['score']['recall']:.4f}" if pairs else "none computed"))

    return checks


def _g3(labels):
    p = [r for r in labels if r["label"] == "POINTER"]
    firm = [r for r in p if r["confidence"] == "FIRM"]
    softnp = [r for r in labels if r["label"] == "NOT-POINTER" and r["confidence"] == "SOFT"]
    ok = len(p) == 7 and len(firm) == 4 and len(softnp) == 9
    return ok, (f"{len(p)} POINTER ({len(firm)} FIRM, {len(p)-len(firm)} SOFT), "
                f"{len(softnp)} SOFT NOT-POINTER")


def _g8():
    bad = []
    for name, want in WORDLIST_DIGESTS.items():
        got = _digest(getattr(wt166, name))
        if got != want:
            bad.append(f"{name} {got[:12]} != {want[:12]}")
    return not bad, ("all five lists match their recorded digests" if not bad
                     else "; ".join(bad))


def _g6(results):
    t5 = next(r for r in results["PRIMARY"] if r["id"] == "T5")
    return t5["score"]["recall"] < 1.0, \
        (f"T5 recall {t5['score']['recall']:.4f} on held-out text "
         f"(precision {t5['score']['precision']:.4f}, flagged {t5['score']['flagged']})")


def _g13(results, iiiv):
    here = next(r for r in results["PRIMARY"] if r["id"] == "T5")["score"]["recall"]
    there = next(r for r in iiiv["PRIMARY"] if r["id"] == "T5")["score"]["recall"]
    return here < there, (f"T5 recall {here:.4f} on Papers I+II against {there:.4f} recomputed "
                          f"on Papers III+IV")


def _g7(results):
    bad = [r["id"] for r in results["PRIMARY"] if r["prereg"] and r["score"]["clears"]]
    return not bad, f"{len(bad)} pre-registered candidate(s) clear the bar: {bad}"


def _partial(s):
    return s["precision"] >= PARTIAL_PRECISION_BAR and s["recall"] >= PARTIAL_RECALL_BAR


def _g11(results):
    bad = [r["id"] for r in results["PRIMARY"] if r["prereg"] and _partial(r["score"])]
    return not bad, f"{len(bad)} pre-registered candidate(s) reach the partial-win bar: {bad}"


def _g14(results, rows):
    bad = [r["id"] for r in results["PRIMARY"] if prefilter_verdict(r["score"], len(rows))]
    return not bad, f"{len(bad)} usable pre-filter(s): {bad}"


def _g12(rows, variants):
    pos = [r for r in rows if wt166.key(r) in variants["PRIMARY"]]
    hits = [r for r in pos if wt166.t5_document_head_noun(r)]
    ok = len(hits) == 1 and "data-availability statement" in hits[0]["target"]
    return ok, (f"{len(hits)} of {len(pos)} POINTERs carry a DOC_NOUNS word: "
                f"{[h['target'] for h in hits]}")


def _g15(rows, variants):
    flagged = {wt166.key(r) for r in rows if wt166.t5_document_head_noun(r)}
    return flagged != variants["PRIMARY"], \
        (f"T5 flags {len(flagged)} rows, the truth set holds {len(variants['PRIMARY'])}; "
         f"{len(flagged ^ variants['PRIMARY'])} rows differ")


def _g16(results):
    t6 = next(r for r in results["PRIMARY"] if r["id"] == "T6")
    return not t6["score"]["clears"], \
        (f"T6 precision {t6['score']['precision']:.4f}, recall {t6['score']['recall']:.4f} "
         f"— first honest test")


def _g17(rows, variants):
    base = len(variants["PRIMARY"]) / len(rows)
    return 0.02 <= base <= 0.09, f"base rate {base:.4f} ({len(variants['PRIMARY'])}/{len(rows)})"


def _g9():
    try:
        rows, considered = wt166.enumerate_rows(wt166.REV)
    except Exception as exc:                                     # noqa: BLE001
        return False, f"raised {exc!r}"
    ok = (considered == 444 and len(rows) == 341
          and wt166.PAPERS[0][0] == "III" and wt166.PAPERS[1][0] == "IV")
    return ok, (f"wt166 still gives {considered} constructions / {len(rows)} bare at "
                f"{wt166.REV}; PAPERS = {[p[0] for p in wt166.PAPERS]}")


def score_corpus(rows, variants):
    out = {}
    for name, positives in variants.items():
        out[name] = [
            {"id": cid, "desc": desc, "klass": klass, "status": status,
             "prereg": status.startswith("pre-registered"),
             "score": wt166.score(rows, positives, fn)}
            for cid, desc, klass, status, fn in wt166.CANDIDATES
        ]
    return out


def best_pairs(rows, positives):
    prereg = [(c[0], c[4]) for c in wt166.CANDIDATES if c[3].startswith("pre-registered")]
    pairs = []
    for i in range(len(prereg)):
        for j in range(i + 1, len(prereg)):
            (ai, fa), (bi, fb) = prereg[i], prereg[j]
            s = wt166.score(rows, positives, lambda r, fa=fa, fb=fb: fa(r) and fb(r))
            pairs.append({"pair": f"{ai}+{bi}", "score": s})
    pairs.sort(key=lambda p: (p["score"]["precision"], p["score"]["recall"]), reverse=True)
    return pairs


def main(argv=None):
    ap = argparse.ArgumentParser(description="wt169 — score wt166's candidate tests against the "
                                             "HELD-OUT labelled ground truth (Papers I and II)")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--skip-postconditions", action="store_true")
    args = ap.parse_args(argv)

    try:
        rows, considered = enumerate_held_out(REV)
    except Exception as exc:                                     # noqa: BLE001
        print(f"wt169: cannot enumerate at {REV}: {exc}", file=sys.stderr)
        return 2

    labels = load_labels()
    labelled = {(r["file"], int(r["line"]), r["token"], r["target"]) for r in labels}
    recomputed = {wt166.key(r) for r in rows}

    if recomputed != labelled:
        only_corpus = sorted(recomputed - labelled)
        only_file = sorted(labelled - recomputed)
        print("wt169: REFUSING — docs/pointer-groundtruth-I-II.tsv has drifted from the corpus.",
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

    variants = wt166.label_variants(labels)
    results = score_corpus(rows, variants)
    pairs = best_pairs(rows, variants["PRIMARY"])

    # the SAME six tests recomputed on Papers III and IV, so the comparison is measured here
    # rather than quoted from a review.
    iiiv_rows, iiiv_considered = wt166.enumerate_rows(wt166.REV)
    iiiv_variants = wt166.label_variants(wt166.load_labels())
    iiiv = score_corpus(iiiv_rows, iiiv_variants)

    post_ok, post = (True, [])
    if not args.skip_postconditions:
        if not args.json:
            print("=== wt169 post-conditions ===")
        ok_all, out = True, []
        for cid, kind, desc, fn in _postconditions(rows, labels, variants, results, pairs, iiiv):
            try:
                ok, detail = fn()
            except Exception as exc:                             # noqa: BLE001
                ok, detail = False, f"raised {exc!r}"
            ok_all &= ok
            out.append({"id": cid, "kind": kind, "desc": desc, "ok": ok, "detail": detail})
            if not args.json:
                print(f"  [{'ok  ' if ok else 'FAIL'}] {cid} {kind:8s} {desc} — {detail}")
        post_ok, post = ok_all, out

    payload = {
        "rev": REV, "considered": considered, "bare": len(rows),
        "labels": {k: len(v) for k, v in variants.items()},
        "bar": {"precision": PRECISION_BAR, "recall": RECALL_BAR,
                "partial_precision": PARTIAL_PRECISION_BAR,
                "partial_recall": PARTIAL_RECALL_BAR,
                "prefilter_flag_fraction": PREFILTER_FLAG_FRACTION},
        "results": results, "best_pairs": pairs[:5],
        "control_III_IV": {"rev": wt166.REV, "considered": iiiv_considered,
                           "bare": len(iiiv_rows),
                           "labels": {k: len(v) for k, v in iiiv_variants.items()},
                           "results": iiiv},
        "published_III_IV": III_IV_PUBLISHED,
        "postconditions_ok": post_ok, "postconditions": post,
    }

    if args.json:
        print(json.dumps(payload, indent=2, ensure_ascii=False))
    else:
        print()
        print(f"=== the HELD-OUT corpus at {REV} (Papers I and II) ===")
        print(f"  {considered} «<token> in <target>» constructions, {len(rows)} with a BARE "
              f"target (N1..N6 silent)")
        print(f"  labels: PRIMARY {len(variants['PRIMARY'])} pointers "
              f"({len(variants['PRIMARY'])/len(rows):.2%} base rate) · "
              f"STRICT {len(variants['STRICT'])} · LOOSE {len(variants['LOOSE'])}")
        print(f"  bars: CLEARS at precision >= {PRECISION_BAR:.2f} AND recall >= {RECALL_BAR:.2f} · "
              f"PARTIAL WIN at {PARTIAL_PRECISION_BAR:.2f}/{PARTIAL_RECALL_BAR:.2f} · "
              f"USABLE PRE-FILTER at recall 1.0000 with <= {PREFILTER_FLAG_FRACTION:.0%} flagged")
        for name in ("PRIMARY", "STRICT", "LOOSE"):
            print(f"\n=== scored against {name} labels "
                  f"({len(variants[name])} pointers of {len(rows)}) ===")
            print(f"  {'':4s} {'test':34s} {'flagged':>7s} {'TP':>4s} {'FP':>4s} {'FN':>4s} "
                  f"{'prec':>7s} {'recall':>7s}  verdict")
            for r in results[name]:
                s = r["score"]
                pf = "  PRE-FILTER" if prefilter_verdict(s, len(rows)) else ""
                print(f"  {r['id']:4s} {r['desc']:34s} {s['flagged']:7d} {s['tp']:4d} "
                      f"{s['fp']:4d} {s['fn']:4d} {s['precision']:7.4f} {s['recall']:7.4f}  "
                      f"{'CLEARS' if s['clears'] else 'fails'}{pf}"
                      f"{'' if r['prereg'] else '   [was EXPLORATORY on III+IV; HELD-OUT here]'}")
        print("\n=== best pairwise conjunctions of the pre-registered five (PRIMARY) ===")
        for p in pairs[:5]:
            s = p["score"]
            print(f"  {p['pair']:9s} flagged {s['flagged']:4d}  prec {s['precision']:7.4f}  "
                  f"recall {s['recall']:7.4f}  {'CLEARS' if s['clears'] else 'fails'}")
        print(f"\n=== THE COMPARISON — same six tests, both corpora, both recomputed here ===")
        print(f"  {'':4s} {'':34s} {'III+IV prec':>12s} {'recall':>8s} | "
              f"{'I+II prec':>10s} {'recall':>8s}")
        for a, b in zip(iiiv["PRIMARY"], results["PRIMARY"]):
            print(f"  {a['id']:4s} {a['desc']:34s} {a['score']['precision']:12.4f} "
                  f"{a['score']['recall']:8.4f} | {b['score']['precision']:10.4f} "
                  f"{b['score']['recall']:8.4f}")
        t5h = next(r for r in results["PRIMARY"] if r["id"] == "T5")["score"]
        t5c = next(r for r in iiiv["PRIMARY"] if r["id"] == "T5")["score"]
        print(f"\nVERDICT: T5's recall goes {t5c['recall']:.4f} -> {t5h['recall']:.4f} on text its "
              f"noun list was not written against.")
        print("         The document-noun pre-filter is "
              + ("USABLE" if prefilter_verdict(t5h, len(rows)) else "NOT usable")
              + " on held-out text by REVIEW-030 §3's definition.")

    if not post_ok:
        print("wt169: POST-CONDITIONS FAILED — the instrument is not trustworthy.", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
