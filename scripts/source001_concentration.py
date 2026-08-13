#!/usr/bin/env python3
"""SOURCE-001 section 6 step 2, finished: the dominant-asset concentration count
over the WHOLE registered panel rather than the 80-firm sample.

NOT A REGISTRATION AND NOT A RESULT. This is a source probe: it reports a count
against a denominator so that a power calculation for REG-009 has one. It computes
no estimate, fits nothing, and makes no claim about phi, sigma or delta.

WHY THIS FILE EXISTS AT ALL, when section 4a's probe was thrown away.
The thrown-away probe was written twice, and the first version divided each class's
most recent 10-K value by the most recent Assets, fetched independently. For a firm
that stops reporting different concepts in different years that divides one balance
sheet by another; it returned class shares of 93.4, 25.8 and 8.26 of total assets.
Those announced themselves, being impossible. A contaminated 0.62 would not have.
So the period-matching rule and the refusal are IN THIS FILE, as code, and the file
is committed rather than thrown away -- that is the whole difference between a
lesson and a control.

TWO MODES, and --sample is not optional in spirit:
  --sample   reproduce section 4a's deterministic 80-firm numbers (11 / 9 / 6 / 3
             at 0.50 / 0.60 / 0.70 / 0.80, on 74 matchable firms). This is the
             method check. A full-panel number produced by a method that cannot
             reproduce the published one is a different measurement wearing its name.
  --full     all 1,602 firms.

Read-only against data.sec.gov. Caches nothing to disk (darwin's disk runs hot).

RUN THIS FROM THE CLOUD, NOT DARWIN. --full is ~4,300 data.sec.gov calls and it
is what got darwin IP-flagged in wealthTensor-24. A container has a disposable
address and darwin does not; source001_lifetime_by_fyend.py carries the same
warning, and this file -- the one that earned it -- did not until -26.
"""
from __future__ import annotations

import argparse
import json
import pathlib
import sys
import threading
import time
import urllib.error
import urllib.request
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor

HERE = pathlib.Path(__file__).resolve().parent
PANEL = HERE.parent / "data" / "reg-006-wt092-panel.json"
UA = {"User-Agent": "jason c braatz jasoncbraatz@gmail.com"}

# The asset classes a dominant-asset restriction could select on. Face-financial
# concepts only, deliberately: section 3 measured that footnote concepts are tagged
# by almost nobody, so a class defined by a footnote tag would be a class of zero.
CLASSES = {
    "ppe": ("PropertyPlantAndEquipmentNet",),
    "goodwill": ("Goodwill",),
    "intangibles": ("IntangibleAssetsNetExcludingGoodwill",
                    "FiniteLivedIntangibleAssetsNet"),
}
ASSETS = "Assets"
THRESHOLDS = (0.50, 0.60, 0.70, 0.80)

# A share above this is arithmetically impossible for a face-financial class net of
# depreciation and is treated as evidence the two numbers came off different balance
# sheets. It is a REFUSAL, not a clip: the firm is excluded and named on stderr.
IMPOSSIBLE = 1.05

# Pacing. The 80-firm sample passed at 4 workers sharing an unlocked timestamp;
# the 1,602-firm run died on HTTP 429 after ~500 firms. An unsynchronised gap check
# is not a rate limit -- N threads all read the same stale timestamp and fire at
# once -- so the interval is held under a lock, and 429 gets its own long backoff.
_gate = threading.Lock()
_last = [0.0]
MIN_GAP = 0.15          # ~6.7 req/s, comfortably under SEC's 10/s courtesy limit


def _pace() -> None:
    with _gate:
        gap = time.time() - _last[0]
        if gap < MIN_GAP:
            time.sleep(MIN_GAP - gap)
        _last[0] = time.time()


def _get_json(url: str, retries: int = 6):
    """One data.sec.gov call.

    Returns None on 404 -- a concept the filer has never tagged is the expected
    case here, not an error. 429 is a THROTTLE, not a failure: back off long and
    keep the whole pool waiting, because a retry that races the other threads just
    earns another 429.
    """
    for i in range(retries):
        try:
            _pace()
            req = urllib.request.Request(url, headers=UA)
            with urllib.request.urlopen(req, timeout=60) as fh:
                return json.loads(fh.read())
        except urllib.error.HTTPError as e:
            if e.code == 404:
                return None
            if e.code == 429:
                wait = float(e.headers.get("Retry-After") or 0) or (5.0 * (i + 1))
                print(f"!! 429 -- holding the pool {wait:.0f}s", file=sys.stderr,
                      flush=True)
                with _gate:            # stall every worker, not just this one
                    time.sleep(wait)
                    _last[0] = time.time()
                continue
            if i == retries - 1:
                raise
            time.sleep(1.0 + 1.5 * i)
        except Exception:
            if i == retries - 1:
                raise
            time.sleep(1.0 + 1.5 * i)
    return None


def facts_by_period(cik: int, concept: str) -> dict[str, float]:
    """end-date -> USD value, from 10-K instants only.

    Where a period end carries several values (an original and its restatements)
    the LATEST-FILED one wins, deterministically. The return is indexed by period
    end because that index is the entire point of this file.
    """
    url = (f"https://data.sec.gov/api/xbrl/companyconcept/"
           f"CIK{cik:010d}/us-gaap/{concept}.json")
    doc = _get_json(url)
    if not doc:
        return {}
    best: dict[str, tuple[str, float]] = {}
    for unit, rows in (doc.get("units") or {}).items():
        if unit != "USD":
            continue
        for r in rows:
            if r.get("form") != "10-K":
                continue
            end, val, filed = r.get("end"), r.get("val"), r.get("filed") or ""
            if end is None or val is None:
                continue
            if end not in best or filed > best[end][0]:
                best[end] = (filed, float(val))
    return {end: v for end, (_f, v) in best.items()}


def firm_shares(cik: int) -> dict | None:
    """Every class share for one firm, ON ONE BALANCE SHEET.

    The matched period is the LATEST period end at which total assets and at least
    one class are both reported. Taking each concept's own latest value instead is
    the defect this file exists to refuse.
    """
    assets = facts_by_period(cik, ASSETS)
    if not assets:
        return None
    got: dict[str, dict[str, float]] = {}
    for cls, tags in CLASSES.items():
        merged: dict[str, float] = {}
        for tag in tags:
            for end, val in facts_by_period(cik, tag).items():
                merged.setdefault(end, val)
        if merged:
            got[cls] = merged
    if not got:
        return None
    common = [e for e in assets
              if any(e in m for m in got.values()) and assets[e] > 0]
    if not common:
        return None
    end = max(common)
    total = assets[end]
    shares = {cls: m[end] / total for cls, m in got.items() if end in m}
    return {"cik": cik, "end": end, "assets": total, "shares": shares}


def sample_ciks(panel: list, per_universe: int = 40) -> list[int]:
    """Section 3's rule, restated: every k-th CIK ascending, per universe."""
    out: list[int] = []
    by_u: dict[str, list[int]] = defaultdict(list)
    for f in panel:
        by_u[f.get("universe") or "?"].append(int(f["cik"]))
    for u in sorted(by_u):
        ciks = sorted(by_u[u])
        k = max(1, len(ciks) // per_universe)
        out.extend(ciks[i * k] for i in range(per_universe) if i * k < len(ciks))
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--sample", action="store_true",
                   help="section 4a's deterministic 80 firms (the method check)")
    g.add_argument("--full", action="store_true", help="all 1,602 firms")
    ap.add_argument("--out", default="", help="write the per-firm record here")
    ap.add_argument("--workers", type=int, default=4)
    args = ap.parse_args()

    panel = json.loads(PANEL.read_text())
    ciks = sample_ciks(panel) if args.sample else sorted({int(f["cik"]) for f in panel})
    print(f"# universe: {len(ciks)} firms ({'sample' if args.sample else 'full panel'})",
          flush=True)

    def safe(cik: int):
        """One firm's failure is one firm's failure. It is counted, not fatal."""
        try:
            return firm_shares(cik)
        except Exception as e:  # noqa: BLE001
            print(f"!! ERROR cik={cik}: {e}", file=sys.stderr, flush=True)
            return "error"

    rows, refused, unmatched, errored = [], [], [], []
    done = 0
    with ThreadPoolExecutor(max_workers=args.workers) as ex:
        for cik, res in zip(ciks, ex.map(safe, ciks)):
            done += 1
            if done % 100 == 0:
                print(f"#   {done}/{len(ciks)}", file=sys.stderr, flush=True)
                if args.out:
                    pathlib.Path(args.out + ".partial").write_text(
                        json.dumps({"done": done, "firms": rows}))
            if res == "error":
                errored.append(cik)
                continue
            if res is None:
                unmatched.append(cik)
                continue
            bad = {c: s for c, s in res["shares"].items() if s > IMPOSSIBLE}
            if bad:
                refused.append({"cik": cik, "end": res["end"], "shares": bad})
                print(f"!! REFUSED cik={cik} end={res['end']} impossible={bad}",
                      file=sys.stderr, flush=True)
                continue
            rows.append(res)

    n = len(rows)
    print(f"\nmatchable firms: {n} of {len(ciks)}"
          f"  (unmatchable {len(unmatched)}, refused {len(refused)},"
          f" errored {len(errored)})")
    print(f"\n{'threshold':>10} {'firms':>6} {'share':>7}   composition")
    for t in THRESHOLDS:
        hit = [r for r in rows if max(r["shares"].values(), default=0.0) >= t]
        comp: dict[str, int] = defaultdict(int)
        for r in hit:
            comp[max(r["shares"], key=r["shares"].get)] += 1
        pretty = ", ".join(f"{k} {v}" for k, v in sorted(comp.items()))
        print(f"{t:>10.2f} {len(hit):>6} {len(hit)/n if n else 0:>7.3f}   {pretty}")

    if args.out:
        pathlib.Path(args.out).write_text(json.dumps(
            {"n_universe": len(ciks), "n_matchable": n,
             "unmatchable": unmatched, "refused": refused, "errored": errored,
             "thresholds": {f"{t:.2f}": len([r for r in rows
                                             if max(r['shares'].values(), default=0) >= t])
                            for t in THRESHOLDS},
             "firms": rows}, indent=1))
        print(f"\nwrote {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
