"""The severe test: does recognition lag scale with GAAP-assigned unobservability?

`lag.py` models the reporting layer as a filter with an observable share phi, and its sharpest
claim is that recognition lag scales with **(1 - phi)**. That is a claim about the world, and
until it is run against the world it is an accounting scheme rather than a theory (WT-043).

This module supplies phi from a source that is not us. US GAAP sorts long-lived assets into
classes that differ in exactly the relevant way -- whether value change reaches the statements
through a *schedule* or only through a *discrete judgement*:

    tier 0  PP&E                         ASC 360      depreciated every period
    tier 1  finite-lived intangibles     ASC 350-30   amortised every period
    tier 2  indefinite-lived intangibles ASC 350-30   annual test only
    tier 3  goodwill                     ASC 350-20   annual test only

Tiers 0 and 1 have a continuous channel. Tiers 2 and 3 have none. That is a phi gradient in the
plain sense of `lag.py`, written into the standards decades before this framework existed.

The prediction, the universe, the tags, the materiality floor, the onset rule, the test
statistic and the falsification condition are all fixed by
`docs/preregistration/PRE-001-wt026-observability-lag.md`, committed before any lag was computed.
Read it before changing anything here: this file is the pre-registration's executable half, and a
constant edited here is a pre-registration silently amended.

Everything below the fetch layer is pure and is tested on synthetic fixtures, so the logic can be
checked without an EDGAR round trip.
"""

from __future__ import annotations

import datetime as _dt
import json
import math
import os
import time
import urllib.request
from collections import defaultdict

# --------------------------------------------------------------------------------------
# PRE-001 constants. These ARE the pre-registration. Changing one is an amendment.
# --------------------------------------------------------------------------------------

TIER_TAGS: dict[int, tuple[str, ...]] = {
    0: ("ImpairmentOfLongLivedAssetsHeldAndUsed",
        "TangibleAssetImpairmentCharges",
        "ImpairmentOfLeasehold"),
    1: ("ImpairmentOfIntangibleAssetsFinitelived",),
    2: ("ImpairmentOfIntangibleAssetsIndefinitelivedExcludingGoodwill",),
    3: ("GoodwillImpairmentLoss",),
}

#: Tagged as a combined goodwill-and-intangible charge. PRE-001 s5.2 assigns it to tier 3 only
#: when no separate tier-1/2 charge is reported in the same quarter, because otherwise it is a
#: roll-up that would double-count.
COMBINED_TAG = "GoodwillAndIntangibleAssetImpairment"

TIER_NAMES = {0: "PP&E", 1: "finite-lived intangible",
              2: "indefinite-lived intangible", 3: "goodwill"}

REVENUE_TAGS = ("RevenueFromContractWithCustomerExcludingAssessedTax",
                "Revenues",
                "SalesRevenueNet",
                "RevenueFromContractWithCustomerIncludingAssessedTax")

ASSETS_TAG = "Assets"

MATERIALITY_FLOOR = 0.01     # charge / prior total assets
MIN_RUN = 2                  # consecutive YoY-declining quarters required
MAX_LOOKBACK = 20            # quarters; a run reaching this is right-censored
MIN_HISTORY_QUARTERS = 12

PILOT_SIC = (5200, 5999)          # retail trade
REPLICATION_SIC = (7370, 7379)    # computer and data processing services

DROP_BUCKETS = ("no_sic", "sic_out_of_range", "no_revenue_tag", "insufficient_history",
                "below_materiality", "no_assets_denominator", "no_deterioration_run",
                "right_censored", "ambiguous_tier", "duplicate_restated_fact")


# --------------------------------------------------------------------------------------
# Quarter arithmetic
#
# Quarters are indexed off the CALENDAR quarter a period ends in, not off the filer's fiscal
# labels. A January-year-end retailer and a December-year-end one then sit on the same axis, and
# YoY is always exactly -4 regardless of whose calendar it is. The `fy`/`fp` fields in
# companyfacts describe the FILING, not the fact, and using them here would silently misalign
# every off-calendar filer -- which in retail is most of them.
# --------------------------------------------------------------------------------------

def qindex(d: _dt.date) -> int:
    """Integer quarter index from a period-end date. Monotone, so q - 4 is one year back."""
    return d.year * 4 + (d.month - 1) // 3


def qlabel(q: int) -> str:
    return f"{q // 4}Q{q % 4 + 1}"


def _d(s: str) -> _dt.date:
    return _dt.date.fromisoformat(s)


# --------------------------------------------------------------------------------------
# companyfacts -> series
# --------------------------------------------------------------------------------------

def _collect(facts: dict, tags, unit: str = "USD") -> tuple[list[dict], int]:
    """All USD facts for the first tag present, latest-filed wins on a repeated period.

    EDGAR restates. The same (start, end) pair appears once per filing that reported it, and the
    values differ after a restatement. Taking the latest `filed` means the analysis sees the
    numbers as the registrant last stood behind them. The count of superseded facts is returned
    so it can be reported in the drop accounting rather than vanishing.
    """
    us = facts.get("facts", {}).get("us-gaap", {})
    rows, superseded = {}, 0
    for tag in tags:
        node = us.get(tag)
        if not node:
            continue
        for f in node.get("units", {}).get(unit, []):
            if "end" not in f or f.get("val") is None:
                continue
            key = (f.get("start"), f["end"])
            prior = rows.get(key)
            if prior is None:
                rows[key] = dict(f, tag=tag)
            else:
                superseded += 1
                if str(f.get("filed", "")) > str(prior.get("filed", "")):
                    rows[key] = dict(f, tag=tag)
        if rows:
            break   # fallback order: the first tag that yields anything is the firm's tag
    return list(rows.values()), superseded


def duration_series(facts: dict, tags) -> tuple[dict[int, float], str | None, int]:
    """Quarterly flow series keyed by quarter index.

    Two sources, in this order of preference:

    1. a fact whose period is one quarter long, used directly;
    2. a *difference of cumulatives* -- companyfacts carries year-to-date facts (H1, 9M, FY) that
       share a fiscal-year start date, so differencing consecutive ones recovers the quarter.

    (2) is not a nicety. For most registrants **Q4 is never tagged as a quarter at all** -- the
    10-K reports the year, and Q4 exists only as FY minus the first three. A pipeline that reads
    only one-quarter facts is blind to Q4, and Q4 is when the annual impairment tests of ASC
    350-20/30 are performed. Missing it would have deleted most of tiers 2 and 3, which is the
    half of the ladder the prediction is about.
    """
    rows, superseded = _collect(facts, tags)
    if not rows:
        return {}, None, superseded
    tag = rows[0]["tag"]

    direct: dict[int, float] = {}
    by_start: dict[str, list[dict]] = defaultdict(list)
    for f in rows:
        if not f.get("start"):
            continue
        s, e = _d(f["start"]), _d(f["end"])
        days = (e - s).days
        if 80 <= days <= 100:
            direct[qindex(e)] = float(f["val"])
        if days <= 400:
            # A one-quarter fact belongs in the cumulative chain too: for a calendar-year filer
            # Q1 IS the first year-to-date figure, and leaving it out breaks the Q2 difference.
            by_start[f["start"]].append({"end": e, "val": float(f["val"]), "days": days})

    derived: dict[int, float] = {}
    for _s, group in by_start.items():
        group.sort(key=lambda g: g["end"])
        prev = None
        for g in group:
            if prev is not None and 80 <= (g["end"] - prev["end"]).days <= 100:
                derived[qindex(g["end"])] = g["val"] - prev["val"]
            prev = g
        # The first cumulative in a fiscal year IS its first quarter when it spans ~90 days.
        first = group[0]
        if 80 <= first["days"] <= 100:
            derived.setdefault(qindex(first["end"]), first["val"])

    out = dict(derived)
    out.update(direct)          # a directly tagged quarter always wins over a difference
    return out, tag, superseded


def instant_series(facts: dict, tag: str) -> dict[int, float]:
    """Balance-sheet stock series keyed by the quarter it was measured at."""
    rows, _ = _collect(facts, (tag,))
    out: dict[int, float] = {}
    for f in rows:
        if f.get("start"):
            continue
        out[qindex(_d(f["end"]))] = float(f["val"])
    return out


def annual_only_charges(facts: dict, tags) -> dict[int, float]:
    """Charges reported ONLY as an annual figure, attributed to the fiscal fourth quarter.

    Kept separate from `duration_series` on purpose. Attributing a year's charge to its final
    quarter can only ever *lengthen* measured lag, and a bias that runs in the hypothesis's
    favour has to be visible, switchable and reported -- never folded into the main path where it
    would look like data. `scripts/wt026_severe_test.py` runs the test with and without these and
    publishes both.
    """
    rows, _ = _collect(facts, tags)
    quarterly, annual = set(), {}
    for f in rows:
        if not f.get("start"):
            continue
        s, e = _d(f["start"]), _d(f["end"])
        days = (e - s).days
        if 80 <= days <= 100:
            quarterly.add(qindex(e))
        elif 350 <= days <= 380 and float(f["val"]) != 0.0:
            annual[qindex(e)] = (float(f["val"]), {qindex(e) - k for k in range(4)})
    out = {}
    for q, (val, span) in annual.items():
        if not (span & quarterly):
            out[q] = val
    return out


# --------------------------------------------------------------------------------------
# Onset and lag  (PRE-001 s5.3)
# --------------------------------------------------------------------------------------

def deterioration_onset(revenue: dict[int, float], q_star: int,
                        min_run: int = MIN_RUN, max_lookback: int = MAX_LOOKBACK):
    """Earliest quarter beginning an unbroken run of YoY revenue decline ending before q_star.

    Returns ``(onset_quarter, censored)`` or ``(None, False)`` when no qualifying run exists.

    The run must end at ``q_star - 1``: the impairment quarter itself is excluded, because a
    charge and the revenue collapse that triggered it routinely land together and counting the
    event quarter as evidence of the run would let the event date itself.

    A missing quarter breaks the run rather than being interpolated across. Interpolation here
    would manufacture exactly the quantity being measured.
    """
    def declining(q: int) -> bool:
        a, b = revenue.get(q), revenue.get(q - 4)
        return a is not None and b is not None and a < b

    q = q_star - 1
    if not declining(q):
        return None, False
    run_end = q
    while declining(q - 1) and (run_end - (q - 1)) + 1 < max_lookback:
        q -= 1
    length = run_end - q + 1
    if length < min_run:
        return None, False
    censored = declining(q - 1)     # the run was still going when the cap stopped us
    return q, censored


# --------------------------------------------------------------------------------------
# Peak-to-charge onset  (PRE-002 s2)
#
# PRE-001 dated onset as the start of an UNBROKEN run of YoY declines. That instrument is
# truncated by revenue volatility rather than by accounting recognition: across 120 retained
# retail events, not one reached the 20-quarter cap and 69% sat at six quarters or fewer, while
# 373 material charges were discarded for having no qualifying run at all. All four tiers drew
# their onset from the same revenue series, so the same truncation compressed the gradient under
# test. The peak rule below has no such ceiling and discards nothing.
#
# `deterioration_onset` is deliberately left exactly as registered. PRE-001's result stands and
# is reproducible; this is an addition, not a correction.
# --------------------------------------------------------------------------------------

def ttm(series: dict[int, float], q: int) -> float | None:
    """Trailing twelve months ending at quarter q, or None if any quarter is missing."""
    vals = [series.get(q - k) for k in range(4)]
    return None if any(v is None for v in vals) else float(sum(vals))


def peak_onset(series: dict[int, float], q_star: int, max_lookback: int = MAX_LOOKBACK,
               min_history: int = 8):
    """Quarter of the pre-charge maximum in the trailing-twelve-month series.

    Returns ``(onset, censored)`` or ``(None, False)`` when there is too little history.

    A firm whose peak is the quarter before the charge yields lag 1. That is an observation --
    the firm was still at its high water mark when it wrote the asset down -- and not a discard.
    Recording it as a discard, which is what the streak rule effectively did, retains only firms
    whose deterioration was *already visible*, which is the opposite of the regime the hypothesis
    is about.
    """
    window = [q for q in range(q_star - max_lookback, q_star) if ttm(series, q) is not None]
    if len(window) < min_history:
        return None, False
    # Ties are broken toward the LATEST quarter achieving the maximum. A flat TTM plateau means
    # the firm was still at its high water mark throughout, so deterioration began after the last
    # of them, not the first. Breaking the other way would inflate every lag -- in the direction
    # that flatters the hypothesis, which is the direction a tie-break must never be chosen for.
    best = max(window, key=lambda q: (ttm(series, q), q))
    return best, best == min(window)


# --------------------------------------------------------------------------------------
# Jonckheere-Terpstra  (PRE-001 s6)
# --------------------------------------------------------------------------------------

def jonckheere_terpstra(groups: list[list[float]]) -> dict:
    """One-sided test for a monotone increasing trend across ORDERED groups.

    Named in PRE-001 s6 before the data were touched, which is the only reason it means anything:
    a test chosen after seeing four medians is a test chosen because of them.

    Tie-corrected variance is used unconditionally. Lags are whole quarters, so ties are not an
    edge case here -- they are most of the sample, and the uncorrected variance would overstate
    significance precisely where this design is weakest.
    """
    groups = [list(g) for g in groups if len(g) > 0]
    if len(groups) < 2:
        return {"J": float("nan"), "z": float("nan"), "p_one_sided": float("nan"), "n": 0}

    J = 0.0
    for i in range(len(groups)):
        for j in range(i + 1, len(groups)):
            for x in groups[i]:
                for y in groups[j]:
                    if x < y:
                        J += 1.0
                    elif x == y:
                        J += 0.5

    ns = [len(g) for g in groups]
    N = sum(ns)
    mean = (N * N - sum(n * n for n in ns)) / 4.0

    counts: dict[float, int] = defaultdict(int)
    for g in groups:
        for x in g:
            counts[x] += 1
    ts = list(counts.values())

    def s1(vals, f):
        return sum(f(v) for v in vals)

    if N < 3:
        return {"J": J, "z": float("nan"), "p_one_sided": float("nan"), "n": N}

    var = ((N * (N - 1) * (2 * N + 5)
            - s1(ns, lambda n: n * (n - 1) * (2 * n + 5))
            - s1(ts, lambda t: t * (t - 1) * (2 * t + 5))) / 72.0
           + (s1(ns, lambda n: n * (n - 1) * (n - 2)) * s1(ts, lambda t: t * (t - 1) * (t - 2)))
           / (36.0 * N * (N - 1) * (N - 2))
           + (s1(ns, lambda n: n * (n - 1)) * s1(ts, lambda t: t * (t - 1)))
           / (8.0 * N * (N - 1)))

    if var <= 0:
        return {"J": J, "z": float("nan"), "p_one_sided": float("nan"), "n": N}
    z = (J - mean) / math.sqrt(var)
    p = 0.5 * math.erfc(z / math.sqrt(2.0))     # upper tail: increasing trend
    return {"J": J, "mean": mean, "var": var, "z": z, "p_one_sided": p, "n": N, "ns": ns}


def mann_whitney_one_sided(a: list[float], b: list[float]) -> dict:
    """U for `b > a`, normal approximation with tie correction. PRE-001 s6 secondary."""
    a, b = list(a), list(b)
    na, nb = len(a), len(b)
    if na == 0 or nb == 0:
        return {"U": float("nan"), "z": float("nan"), "p_one_sided": float("nan")}
    U = sum(1.0 if x < y else 0.5 if x == y else 0.0 for x in a for y in b)
    mean = na * nb / 2.0
    N = na + nb
    counts: dict[float, int] = defaultdict(int)
    for v in a + b:
        counts[v] += 1
    tie = sum(t ** 3 - t for t in counts.values())
    var = na * nb / 12.0 * ((N + 1) - tie / (N * (N - 1))) if N > 1 else 0.0
    if var <= 0:
        return {"U": U, "z": float("nan"), "p_one_sided": float("nan")}
    z = (U - mean) / math.sqrt(var)
    return {"U": U, "z": z, "p_one_sided": 0.5 * math.erfc(z / math.sqrt(2.0))}


def median(xs) -> float:
    xs = sorted(xs)
    n = len(xs)
    if n == 0:
        return float("nan")
    return float(xs[n // 2]) if n % 2 else (xs[n // 2 - 1] + xs[n // 2]) / 2.0


def iqr(xs) -> tuple[float, float]:
    xs = sorted(xs)
    if not xs:
        return float("nan"), float("nan")

    def q(p):
        i = p * (len(xs) - 1)
        lo, hi = int(math.floor(i)), int(math.ceil(i))
        return xs[lo] + (xs[hi] - xs[lo]) * (i - lo)

    return q(0.25), q(0.75)


def bootstrap_median_diff(events_by_firm: dict, tier_hi: int, tier_lo: int,
                          n_boot: int = 10000, seed: int = 20260805) -> tuple[float, float]:
    """Percentile interval for median(lag | tier_hi) - median(lag | tier_lo), resampled BY FIRM.

    Firms contribute several events -- a firm impairing two tiers in one quarter shares an onset
    across both by construction -- so resampling events would treat one company's decision as
    several independent observations and report an interval narrower than the data support.
    """
    import random
    rng = random.Random(seed)
    firms = list(events_by_firm)
    if not firms:
        return float("nan"), float("nan")
    diffs = []
    for _ in range(n_boot):
        hi, lo = [], []
        for _k in range(len(firms)):
            for ev in events_by_firm[firms[rng.randrange(len(firms))]]:
                if ev["tier"] == tier_hi:
                    hi.append(ev["lag"])
                elif ev["tier"] == tier_lo:
                    lo.append(ev["lag"])
        if hi and lo:
            diffs.append(median(hi) - median(lo))
    if not diffs:
        return float("nan"), float("nan")
    diffs.sort()
    return diffs[int(0.025 * (len(diffs) - 1))], diffs[int(0.975 * (len(diffs) - 1))]


# --------------------------------------------------------------------------------------
# Controls  (PRE-002 s3)
# --------------------------------------------------------------------------------------

def permutation_null(events: list[dict], n_perm: int = 1000, seed: int = 20260805) -> dict:
    """Permute tier labels across events, holding the lag distribution fixed.

    Two jobs. It checks the pipeline cannot manufacture a gradient out of nothing -- without
    which a *positive* result is not reportable. And it yields an empirical p-value that does not
    lean on the normal approximation, which matters here because the tier sizes are wildly
    unbalanced (11/12/18/79 in the pilot) and that is exactly where the approximation is worst.
    """
    import random
    if not events:
        return {"z_mean": float("nan"), "z_sd": float("nan"), "p_empirical": float("nan")}
    rng = random.Random(seed)
    lags = [e["lag"] for e in events]
    tiers = [e["tier"] for e in events]
    observed = jonckheere_terpstra([[l for l, t in zip(lags, tiers) if t == k]
                                    for k in (0, 1, 2, 3)])["z"]
    zs = []
    for _ in range(n_perm):
        shuffled = tiers[:]
        rng.shuffle(shuffled)
        z = jonckheere_terpstra([[l for l, t in zip(lags, shuffled) if t == k]
                                 for k in (0, 1, 2, 3)])["z"]
        if z == z:                                   # skip nan
            zs.append(z)
    if not zs:
        return {"z_mean": float("nan"), "z_sd": float("nan"), "p_empirical": float("nan")}
    mean = sum(zs) / len(zs)
    sd = (sum((z - mean) ** 2 for z in zs) / max(1, len(zs) - 1)) ** 0.5
    p = sum(1 for z in zs if z >= observed) / len(zs)
    return {"observed_z": observed, "z_mean": mean, "z_sd": sd,
            "p_empirical": p, "n_perm": len(zs)}


def synthetic_power(tier_sizes: list[int], lag_pool: list[float], effect_per_tier: float = 1.0,
                    n_trials: int = 500, alpha: float = 0.025, seed: int = 20260805) -> dict:
    """How large an effect this design could have detected, at the observed sizes and spread.

    Reported whatever the outcome. A null that arrives without its own detectability attached is
    an absence of evidence being quietly passed off as evidence of absence.
    """
    import random
    rng = random.Random(seed)
    hits = 0
    for _ in range(n_trials):
        groups = [[rng.choice(lag_pool) + effect_per_tier * t for _ in range(n)]
                  for t, n in enumerate(tier_sizes)]
        if jonckheere_terpstra(groups)["p_one_sided"] < alpha:
            hits += 1
    return {"effect_per_tier_quarters": effect_per_tier, "alpha": alpha,
            "power": hits / n_trials, "tier_sizes": list(tier_sizes)}


# --------------------------------------------------------------------------------------
# Event extraction  (PRE-001 s5.2)
# --------------------------------------------------------------------------------------

OPERATING_INCOME_TAGS = ("OperatingIncomeLoss",)


def extract_events(facts: dict, cik: str, name: str, drops: dict,
                   include_annual_attributed: bool = True,
                   onset_rule: str = "streak", signal: str = "revenue") -> list[dict]:
    """Every material impairment event for one firm, with its lag, or nothing with a reason.

    ``onset_rule="streak"`` is PRE-001 as registered. ``onset_rule="peak"`` is PRE-002 s2.
    ``signal="opinc_addback"`` is the PRE-002 secondary: operating income with the impairment
    charges added back, which removes the contamination that made operating income unusable
    under PRE-001 s5.1 -- the add-back was not available until the charges had been extracted.
    """
    revenue, rev_tag, _sup = duration_series(facts, REVENUE_TAGS)
    if rev_tag is None or len(revenue) < MIN_HISTORY_QUARTERS:
        drops["no_revenue_tag" if rev_tag is None else "insufficient_history"] += 1
        return []
    assets = instant_series(facts, ASSETS_TAG)
    if not assets:
        drops["no_assets_denominator"] += 1
        return []

    charges: dict[int, dict[int, float]] = defaultdict(dict)      # quarter -> tier -> value
    attributed: set[tuple[int, int]] = set()
    for tier, tags in TIER_TAGS.items():
        series, _t, sup = duration_series(facts, tags)
        drops["duplicate_restated_fact"] += sup
        for q, v in series.items():
            if v and abs(v) > 0:
                charges[q][tier] = abs(v)
        if include_annual_attributed:
            for q, v in annual_only_charges(facts, tags).items():
                if tier not in charges[q]:
                    charges[q][tier] = abs(v)
                    attributed.add((q, tier))

    combined, _t, _s = duration_series(facts, (COMBINED_TAG,))
    for q, v in combined.items():
        if v and abs(v) > 0:
            if 1 in charges[q] or 2 in charges[q] or 3 in charges[q]:
                drops["ambiguous_tier"] += 1        # a roll-up over charges already counted
            else:
                charges[q][3] = abs(v)

    if signal == "opinc_addback":
        opinc, _t, _s = duration_series(facts, OPERATING_INCOME_TAGS)
        series = {q: v + sum(charges.get(q, {}).values()) for q, v in opinc.items()}
    else:
        series = revenue

    events = []
    for q_star in sorted(charges):
        denom = next((assets[k] for k in range(q_star - 1, q_star - 6, -1) if k in assets), None)
        if not denom or denom <= 0:
            drops["no_assets_denominator"] += 1
            continue
        for tier, val in sorted(charges[q_star].items()):
            if val / denom < MATERIALITY_FLOOR:
                drops["below_materiality"] += 1
                continue
            if onset_rule == "peak":
                onset, censored = peak_onset(series, q_star)
                if onset is None:
                    drops["insufficient_history"] += 1
                    continue
            else:
                onset, censored = deterioration_onset(series, q_star)
                if onset is None:
                    drops["no_deterioration_run"] += 1
                    continue
            if censored:
                drops["right_censored"] += 1
            events.append({"cik": cik, "name": name, "tier": tier, "q_star": q_star,
                           "onset": onset, "lag": q_star - onset, "censored": censored,
                           "charge": val, "assets": denom, "severity": val / denom,
                           "revenue_tag": rev_tag,
                           "annual_attributed": (q_star, tier) in attributed})
    return events


# --------------------------------------------------------------------------------------
# Fetch layer  (everything above here is pure and network-free)
# --------------------------------------------------------------------------------------

USER_AGENT = os.environ.get("SEC_USER_AGENT",
                            "wealth-tensor research (jasoncbraatz@gmail.com)")


def _get(url: str, retries: int = 4) -> bytes:
    last = None
    for k in range(retries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT,
                                                       "Accept-Encoding": "gzip, deflate"})
            with urllib.request.urlopen(req, timeout=60) as r:
                data = r.read()
                if r.headers.get("Content-Encoding") == "gzip":
                    import gzip
                    data = gzip.decompress(data)
                return data
        except Exception as exc:                       # noqa: BLE001
            last = exc
            time.sleep(1.5 * (k + 1))
    raise RuntimeError(f"GET failed after {retries}: {url}: {last}")


def fetch_json(url: str, cache: str | None = None) -> dict:
    if cache and os.path.exists(cache):
        with open(cache) as fh:
            return json.load(fh)
    raw = _get(url)
    if cache:
        os.makedirs(os.path.dirname(cache), exist_ok=True)
        with open(cache, "wb") as fh:
            fh.write(raw)
    time.sleep(0.11)                                    # SEC asks for <= 10 requests/second
    return json.loads(raw)


def company_facts(cik: int, cache_dir: str) -> dict:
    c = f"{int(cik):010d}"
    return fetch_json(f"https://data.sec.gov/api/xbrl/companyfacts/CIK{c}.json",
                      os.path.join(cache_dir, "facts", f"{c}.json"))


def submissions(cik: int, cache_dir: str) -> dict:
    c = f"{int(cik):010d}"
    return fetch_json(f"https://data.sec.gov/submissions/CIK{c}.json",
                      os.path.join(cache_dir, "subs", f"{c}.json"))
