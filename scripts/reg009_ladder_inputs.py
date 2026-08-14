"""REG-009 · THE LADDER-INPUT TEST — §7.3's registered statistics on the disclosed pairs.

WHAT THIS INSTRUMENT IS
-----------------------
Paper III §4.4 evaluates its first rung over a RECTANGLE: a 400x400 uniform grid on lives
asserted in `wt088_disclosed_ladder.py` as LIFE_PPE = (10, 40) and LIFE_FIN = (3, 20),
with delta_0 and delta_1 swept INDEPENDENTLY. A filing does not supply a rectangle. It
supplies one point, for one firm, in one year, with both coordinates chosen by the same
management on the same page.

This script replaces the product measure on an assumed support with the empirical joint
distribution the disclosure actually has -- 683 paired firm-years across 577 firms -- and
that substitution is the experiment. It is registered in
`docs/preregistration/REG-009-p3-lifetime-sourced-delta.md` §§6-12, which was committed
and pushed ALONE before this file existed (§12's stopping rule).

WHAT IT MAY NOT DO, AND WHY THE CODE SAYS SO RATHER THAN THE COMMENTS
--------------------------------------------------------------------
F1 lifts the ruler out of `wt088_disclosed_ladder.py` BY NAME and aborts unless the lifted
constants still reproduce that script's committed poles -- 0.0 % admissible at alpha=0.05,
the first rung rising in 99.7 % of the admissible rectangle at alpha=0.35 -- checked twice:
once against this file's own recomputation from the lifted constants, and once against
wt088's OWN STDOUT, run as a subprocess in the same pass. A drill that carries its own copy
of the logic under test passes forever while the original rots.

F8 keeps `cik`, `name`, `sic`, `adsh`, `period` and `components` out of every row the
statistic sees, and the container RAISES on a touch rather than reading as absent -- a
deleted key that returns None is a key a `.get()` swallows. The two declared exceptions
travel in their own arrays: `cycle` reaches only the splitter, `cik` only the resampler.

F10 parses this file's own AST and refuses any module-level literal that is not in
REGISTERED_CONSTANTS with a provenance string. This programme has refused a free parameter
to absorb an objection six times; the seventh refusal is a test rather than a memory. The
bootstrap's replicate count and seed are LIFTED FROM wt088 (N, SEED) rather than chosen
here, so this instrument picks no number of its own at all.

READING OF §11's "EACH RUNS BEFORE PSI IS COMPUTED"
---------------------------------------------------
F1, F2, F7, F8, F9a and F10 -- every falsifier marked *kills the run*, plus F9's absence
half -- run before any statistic is computed, in §11's order. F3, F4, F5, F6 and F9b assert
properties OF THE REPORT (a qualifier travelling in a table, three rates in one table, a
heaping column beside every Psi), so their subject does not exist until the document is
rendered. They run against the rendered document BEFORE IT IS WRITTEN TO DISK, so a report
that violates them is never published. Nothing about the run's validity is decided after
Psi is seen; what is decided after Psi exists is whether the DOCUMENT may be written. The
reading is recorded in RESULT-REG-009 §0 as well as here.

USAGE
-----
    .venv/bin/python scripts/reg009_ladder_inputs.py
"""

from __future__ import annotations

import ast
import hashlib
import json
import re
import subprocess
import sys
from collections import Counter
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
from severity import check, summary  # noqa: E402

# ======================================================================================
# REGISTERED CONSTANTS -- every module-level literal in this file, with where it came
# from. F10 parses this file's own AST and refuses anything not on this list.
# ======================================================================================
REGISTERED_CONSTANTS = {
    "PPE": "the canonical property tag, REG-009 §7.1's unit definition",
    "FIN": "the canonical finite-lived intangible tag, REG-009 §7.1",
    "RULES": "REG-009 §6, D2: R_MID primary, all three reported side by side",
    "PRIMARY": "REG-009 §6, D2: R_MID is primary",
    "CYCLES": "SOURCE-001 §3b's two cycles, as labelled in the committed records",
    "FORBIDDEN": "REG-009 §11, F8: the keys the statistic may not see",
    "QUALIFIER_MARK": "F4's marker: the substring every Psi/A/S table must carry",
    "RWEIGHT_MARK": "F3's marker: the substring every R_WEIGHT table must carry",
    "LIVES_SHA256": "F7: the sha256 of the two committed record files, pinned here",
    "ALPHA_HAT": "paper III §5.4's measured recognition rate, read from that table",
    "ALPHA_HAT_CI": "paper III §5.4's interval for it, read from that table",
    "LADDER_SRC": "the ruler's path; its CONTENTS are lifted by name at run time",
    "P0_SRC": "D3's bins live here; their SHAPE is lifted at run time, not copied",
    "LADDER_NAMES": "F1: the wt088 symbols lifted by name",
    "LADDER_POLES": "F1: wt088's committed poles, quoted from its own output",
    "POLE_TOL": "F1: the tolerance on a printed percentage rounded to one decimal",
    "BAND_WIDTH": "REG-009 §6, D3: 1.00 year, and no other band width (F10)",
    "THIN_FLOOR": "SOURCE-001 §3b's inherited THIN floor, cited by REG-009 §12",
    "P2_POLE": "REG-009 §9, P2: the manuscript's own 99.7 %",
    "P3_TOL": "REG-009 §9, P3: five points",
    "P1_P4_SIDE": "REG-009 §9, P1 and P4: the 0.50 side",
    "BOOT_CI": "REG-009 §7.3: a bootstrap INTERVAL; the conventional two-sided 95 %",
    "SEEN_COUNTS": "REG-009 §7.1's table, on §7.4's SEEN list, asserted by F2",
    "NETMODS": "F7: the network and archive modules this run must not have imported",
    "NET_PAT": "F7c: the source shapes that would mean a fetch happened",
    "MEDIAN_PAT": "F9a: the source shapes that would mean §6's D4 refusal was broken",
}

PPE = "PropertyPlantAndEquipmentUsefulLife"
FIN = "FiniteLivedIntangibleAssetUsefulLife"
RULES = ("R_MID", "R_MIN", "R_WEIGHT")
PRIMARY = "R_MID"
CYCLES = ("2014-15", "2022-23")
FORBIDDEN = ("cik", "name", "sic", "adsh", "period", "components")

QUALIFIER_MARK = "DISCLOSED δ, not the economic δ"
RWEIGHT_MARK = "amount-backed"

LIVES_SHA256 = {
    "2014-15": "cceade496064c216dd3df4738089ccb6725c38e22bcdd371969ef21a39e26fe7",
    "2022-23": "48cbce0de6cb37841682b7a6d85f31071bfc86f84f3141b3ff92ef171866fdc6",
}

ALPHA_HAT = 0.408
ALPHA_HAT_CI = (0.383, 0.432)

LADDER_SRC = "wt088_disclosed_ladder.py"
P0_SRC = "reg009_p0_lifetime_values.py"
LADDER_NAMES = ("ALPHA", "A_EXT", "PHI", "DELTA", "LIFE_PPE", "LIFE_FIN", "G", "N", "SEED")
LADDER_POLES = {"admissible_at_alpha": 0.0, "rises_at_a_ext": 0.997}
POLE_TOL = 0.0006

BAND_WIDTH = 1.00
THIN_FLOOR = 30
P2_POLE = 0.997
P3_TOL = 0.05
P1_P4_SIDE = 0.50
BOOT_CI = (2.5, 97.5)

SEEN_COUNTS = {
    "pairs_2014_15": 321, "pairs_2022_23": 362, "pairs_pooled": 683,
    "firms_pooled": 577, "firms_both_cycles": 106, "r_weight_both": 273,
    "one_tag_only": 613, "ppe_only": 523, "fin_only": 90,
    "any_2014_15": 612, "any_2022_23": 684,
}

NETMODS = ("socket", "ssl", "urllib.request", "urllib3", "http.client", "requests",
           "zipfile", "ftplib", "tarfile")

# Both patterns are written with [_] and [f] character classes so that the pattern
# LITERAL in this file does not match itself. A self-matching guard reports a
# violation it invented, which is the phantom tag wearing the opposite costume.
NET_PAT = r"^\s*import (?:zip[f]ile|requests|socket)|^\s*from (?:zip[f]ile|urllib)|"\
          r"urlopen\(|requests\.get\(|https?://"
MEDIAN_PAT = r"industry[_]median|median[_]by[_]sic|by[_]industry|sic[_]median"


# ======================================================================================
# PLUMBING
# ======================================================================================
def _here() -> Path:
    return Path(__file__).resolve().parent


class Tee:
    """stdout and the run log, so the log IS the run rather than a summary of it."""

    def __init__(self, path: Path):
        self._f = path.open("w", encoding="utf-8")
        self._out = sys.stdout

    def write(self, s):
        self._out.write(s)
        self._f.write(s)
        return len(s)

    def flush(self):
        self._out.flush()
        self._f.flush()

    def close(self):
        self._f.close()


def _nan_to_none(o):
    """JSON has no NaN. Ψ_rect at the calibration is genuinely undefined -- an empty
    admissible set -- and `null` says that where `NaN` says only "not valid JSON"."""
    if isinstance(o, dict):
        return {k: _nan_to_none(x) for k, x in o.items()}
    if isinstance(o, (list, tuple)):
        return [_nan_to_none(x) for x in o]
    if isinstance(o, float) and np.isnan(o):
        return None
    return o


def hr(title: str) -> None:
    print("\n" + "=" * 86)
    print(f"  {title}")
    print("=" * 86)


class BlindnessViolation(Exception):
    """F8: the statistic reached for a key that was kept out of its view."""


class Blinded(dict):
    """A row without FORBIDDEN -- and a touch RAISES rather than reading as absent."""

    def __getitem__(self, k):
        if k in FORBIDDEN:
            raise BlindnessViolation(
                f"F8: the statistic touched '{k}', which is kept out of its view. "
                f"§11's own subject is the analyst rather than the filings.")
        return super().__getitem__(k)

    def get(self, k, default=None):
        if k in FORBIDDEN:
            raise BlindnessViolation(f"F8: the statistic probed '{k}' with .get().")
        return super().get(k, default)

    def __contains__(self, k):
        if k in FORBIDDEN:
            raise BlindnessViolation(f"F8: the statistic tested '{k}' for membership.")
        return super().__contains__(k)


# ======================================================================================
# F1 -- THE RULER IS LIFTED, NOT REBUILT
# ======================================================================================
def _grid(life_ppe, life_fin, g):
    d0 = np.linspace(1 / life_ppe[1], 1 / life_ppe[0], int(g))
    d1 = np.linspace(1 / life_fin[1], 1 / life_fin[0], int(g))
    return np.meshgrid(d0, d1, indexing="ij")


def _rect_shares(D0, D1, alpha, phi):
    """(rises share OF the admissible part, admissible share) -- wt088's construction."""
    adm = (D0 < alpha) & (D1 < alpha)
    if not adm.any():
        return float("nan"), 0.0
    with np.errstate(divide="ignore", invalid="ignore"):
        R0 = (1 - phi[0]) * D0 / (alpha - D0)
        R1 = (1 - phi[1]) * D1 / (alpha - D1)
    return float(((R1 > R0) & adm).sum() / adm.sum()), float(adm.mean())


def lift_ruler() -> dict:
    """Lift wt088's constants and its boundary LINE by name, then prove they still rule."""
    src_path = _here() / LADDER_SRC
    src = src_path.read_text()
    ns: dict = {"np": np}
    missing = []
    for name in LADDER_NAMES:
        m = re.search(rf"^{name}\s*=\s*(.+?)\s*(?:#.*)?$", src, re.M)
        if not m:
            missing.append(name)
            continue
        exec(f"{name} = {m.group(1)}", ns)  # noqa: S102

    # The boundary is a LINE in wt088, not a def. Lift it by its name and turn wt088's own
    # expression into a callable by substituting the two symbols it reads. If either
    # substitution finds nothing, the line changed shape and this is not the ruler.
    mb = re.search(r"^\s*d1_boundary\s*=\s*(.+?)\s*(?:#.*)?$", src, re.M)
    boundary = None
    if not mb:
        missing.append("d1_boundary")
    else:
        expr = mb.group(1)
        if "ALPHA" not in expr or "DELTA[0]" not in expr:
            missing.append("d1_boundary (shape changed: ALPHA/DELTA[0] not both present)")
        else:
            boundary = eval("lambda alpha, d0: " + expr.replace("ALPHA", "alpha")
                            .replace("DELTA[0]", "d0"))  # noqa: S307
            ns["_boundary_src"] = expr

    if missing:
        raise SystemExit(
            f"F1 ABORTS: could not lift the ruler out of {LADDER_SRC} -- missing "
            f"{missing}. If wt088 moved, this registration is measuring against a ruler "
            f"the manuscript no longer uses and must be RE-DECIDED rather than re-run.")

    ns["boundary"] = boundary
    ns["_src_sha"] = hashlib.sha256(src.encode()).hexdigest()

    g = int(ns["G"])
    lp, lf = ns["LIFE_PPE"], ns["LIFE_FIN"]
    a0, ae = float(ns["ALPHA"]), float(ns["A_EXT"])
    D0, D1 = _grid(lp, lf, g)
    ns["_grid"] = (D0, D1)
    adm_at_alpha = float(((D0 < a0) & (D1 < a0)).mean())
    rises_e, adm_e = _rect_shares(D0, D1, ae, ns["PHI"])

    # A falsifying world used by three witnesses below: wt088's OTHER rectangle on both
    # axes. Same code, same alpha, same phi -- a different ruler.
    W0, W1 = _grid(lf, lf, g)
    w_rises, _ = _rect_shares(W0, W1, ae, ns["PHI"])

    print(f"  ruler lifted from {LADDER_SRC} (sha256 {ns['_src_sha'][:12]}) by name: "
          f"{', '.join(LADDER_NAMES)}, d1_boundary")
    print(f"    recomputed from the lifted constants : admissible at alpha={a0} is "
          f"{100*adm_at_alpha:.1f} %; at alpha={ae} the rung rises in {100*rises_e:.1f} % "
          f"of an admissible {100*adm_e:.1f} %")

    proc = subprocess.run([sys.executable, str(src_path)], cwd=str(_here().parent),
                          capture_output=True, text=True, timeout=900)
    if proc.returncode != 0:
        raise SystemExit(f"F1 ABORTS: {LADDER_SRC} exited {proc.returncode}; the ruler "
                         f"does not run, so it cannot be checked against.\n"
                         f"{proc.stdout[-2000:]}\n{proc.stderr[-2000:]}")
    m_adm = re.search(r"INSIDE the model's domain \(delta < alpha\):\s*([\d.]+)%",
                      proc.stdout)
    m_ext = re.search(r"EXTENSION, alpha = ([\d.]+): admissible share ([\d.]+)%,"
                      r" first rung RISES in ([\d.]+)% of it", proc.stdout)
    if not (m_adm and m_ext):
        raise SystemExit("F1 ABORTS: wt088 no longer PRINTS its poles in the shape this "
                         "extraction reads. The ruler moved; re-derive the extraction.")
    printed_adm = float(m_adm.group(1)) / 100.0
    printed_alpha = float(m_ext.group(1))
    printed_rises = float(m_ext.group(3)) / 100.0
    print(f"    wt088's own stdout, run in this pass  : admissible "
          f"{100*printed_adm:.1f} %, EXTENSION alpha={printed_alpha}, rung rises in "
          f"{100*printed_rises:.1f} %")
    print(f"    the falsifying world the F1 witnesses use: wt088's intangible rectangle "
          f"on BOTH axes -> rises {100*w_rises:.1f} %")

    check("F1a · the lifted constants reproduce wt088's committed admissible pole "
          "(0.0 % at the paper's alpha)",
          abs(adm_at_alpha - LADDER_POLES["admissible_at_alpha"]) <= POLE_TOL,
          witness=lambda: abs(float(((D0 < ae) & (D1 < ae)).mean())
                              - LADDER_POLES["admissible_at_alpha"]) <= POLE_TOL)
    check("F1b · the lifted constants reproduce wt088's committed rising pole "
          "(99.7 % of the admissible rectangle at alpha=0.35)",
          abs(rises_e - LADDER_POLES["rises_at_a_ext"]) <= POLE_TOL,
          witness=lambda: abs(w_rises - LADDER_POLES["rises_at_a_ext"]) <= POLE_TOL)
    check("F1c · what was lifted is what wt088 still PRINTS — the extraction did not "
          "drift from the script it claims to be using",
          abs(printed_adm - adm_at_alpha) <= POLE_TOL
          and abs(printed_rises - rises_e) <= POLE_TOL
          and printed_alpha == ae,
          witness=lambda: abs(printed_rises - w_rises) <= POLE_TOL)
    check("F1d · phi is paper III §4.4's (0.80, 0.60), lifted rather than retyped",
          (float(ns["PHI"][0]), float(ns["PHI"][1])) == (0.80, 0.60),
          witness=lambda: (float(ns["PHI"][2]), float(ns["PHI"][3])) == (0.80, 0.60))

    R0e = (1 - ns["PHI"][0]) * D0 / (ae - D0)
    R1e = (1 - ns["PHI"][1]) * D1 / (ae - D1)
    dom = (D0 < ae) & (D1 < ae)
    rises_mask = (R1e > R0e) & dom
    closed_mask = (D1 > boundary(ae, D0)) & dom
    disagree = int((rises_mask != closed_mask).sum())
    check("F1e · wt088's closed-form boundary line and the R comparison it summarises "
          "agree on every cell of wt088's own grid",
          disagree == 0,
          witness=lambda: int((rises_mask != ((D1 > boundary(ae, D0) * 1.05) & dom))
                              .sum()) == 0)
    ns["_poles"] = {"admissible_at_alpha": adm_at_alpha, "rises_at_a_ext": rises_e,
                    "wt088_printed_admissible": printed_adm,
                    "wt088_printed_rises": printed_rises}
    return ns


# ======================================================================================
# D3's BINS, LIFTED FROM THE INSTRUMENT THAT PRICED D3
# ======================================================================================
# Psi_band collapses every delta to "its D3 band midpoint". D3's bands were priced by
# `reg009_p0_lifetime_values.py`, whose bin index and bin edges are two lines of that
# file. Re-typing them here would make Psi_band a statistic about THIS file's idea of a
# band. They are lifted by shape instead, on F1's precedent, and the midpoint is derived
# from the lifted edges rather than assumed to be floor + w/2.
def lift_band_rule() -> tuple:
    src = (_here() / P0_SRC).read_text()
    mi = re.search(r"bands\[(int\(v // w\))\]\.append\(v\)", src)
    me = re.search(r'"band": \[(b \* w), (\(b \+ 1\) \* w)\]', src)
    if not (mi and me):
        raise SystemExit(
            f"ABORTS: could not lift D3's bin rule out of {P0_SRC} -- the bin index or "
            f"the bin edges changed shape. Psi_band would then be a band this file "
            f"invented, and D3 is not this file's to fix.")
    binner = eval("lambda v, w: " + mi.group(1))              # noqa: S307
    lo = eval("lambda b, w: " + me.group(1))                  # noqa: S307
    hi = eval("lambda b, w: " + me.group(2))                  # noqa: S307

    def midpoint(v, w):
        b = binner(v, w)
        return (lo(b, w) + hi(b, w)) / 2.0
    print(f"  D3's bins lifted from {P0_SRC}: index `{mi.group(1)}`, edges "
          f"`[{me.group(1)}, {me.group(2)})` -> midpoint = (lo + hi) / 2")
    return midpoint, f"{mi.group(1)} / [{me.group(1)}, {me.group(2)})"


# ======================================================================================
# F2 / F7 -- THE POPULATION
# ======================================================================================
def load_population(root: Path):
    files = {"2014-15": root / "data" / "reg-009-p0-lives-2015.json",
             "2022-23": root / "data" / "reg-009-p0-lives-2023.json"}
    for cyc, p in files.items():
        got = hashlib.sha256(p.read_bytes()).hexdigest()
        check(f"F7a · {p.name} is the committed file, by digest",
              got == LIVES_SHA256[cyc],
              witness=lambda p=p, cyc=cyc: hashlib.sha256(
                  p.read_bytes() + b"x").hexdigest() == LIVES_SHA256[cyc])

    rows, cyc_arr, cik_arr = [], [], []
    tally = {c: {"any": 0, "ppe": 0, "fin": 0, "pair": 0, "wboth": 0} for c in CYCLES}
    firms = {c: set() for c in CYCLES}
    for cyc, p in files.items():
        for r in json.loads(p.read_text())["records"]:
            lv = r["lives"]
            has_p, has_f = PPE in lv, FIN in lv
            t = tally[cyc]
            t["any"] += 1
            t["ppe"] += has_p
            t["fin"] += has_f
            if not (has_p and has_f):
                continue
            t["pair"] += 1
            firms[cyc].add(r["cik"])
            wb = (bool(lv[PPE].get("R_WEIGHT_backed"))
                  and bool(lv[FIN].get("R_WEIGHT_backed")))
            t["wboth"] += wb
            row = Blinded({"cycle": cyc, "r_weight_backed_both": wb})
            for rule in RULES:
                row[f"L0_{rule}"] = float(lv[PPE][rule])
                row[f"L1_{rule}"] = float(lv[FIN][rule])
            rows.append(row)
            cyc_arr.append(cyc)
            cik_arr.append(int(r["cik"]))
    return rows, np.array(cyc_arr), np.array(cik_arr), tally, firms


# ======================================================================================
# §7.3's STATISTICS
# ======================================================================================
def lives(rows, rule, band=False, mid=None):
    l0 = np.array([r[f"L0_{rule}"] for r in rows], dtype=float)
    l1 = np.array([r[f"L1_{rule}"] for r in rows], dtype=float)
    if band:
        l0 = np.array([mid(v, BAND_WIDTH) for v in l0], dtype=float)
        l1 = np.array([mid(v, BAND_WIDTH) for v in l1], dtype=float)
    return l0, l1


def psi_parts(d0, d1, alpha, phi):
    adm = (d0 < alpha) & (d1 < alpha)
    with np.errstate(divide="ignore", invalid="ignore"):
        R0 = (1 - phi[0]) * d0 / (alpha - d0)
        R1 = (1 - phi[1]) * d1 / (alpha - d1)
    return adm, (R1 > R0) & adm


def heaping(l0, l1, mask):
    keys = [(round(a, 6), round(b, 6)) for a, b in zip(l0[mask], l1[mask])]
    if not keys:
        return 0, float("nan")
    c = Counter(keys)
    return len(c), c.most_common(1)[0][1] / len(keys)


def clustered_bootstrap(adm, rises, cik, rng, reps):
    """Resample FIRMS with replacement. Psi is a ratio of firm-level sums, so a resample
    of firms is exactly a resample of two integers per firm -- exact and vectorised."""
    uniq, inv = np.unique(cik, return_inverse=True)
    fa = np.bincount(inv, weights=adm.astype(float), minlength=len(uniq))
    fr = np.bincount(inv, weights=rises.astype(float), minlength=len(uniq))
    draw = rng.integers(0, len(uniq), size=(reps, len(uniq)))
    den = fa[draw].sum(axis=1)
    num = fr[draw].sum(axis=1)
    out = np.divide(num, den, out=np.full(reps, np.nan, dtype=float), where=den > 0)
    out = out[~np.isnan(out)]
    if out.size == 0:
        return float("nan"), float("nan")
    return float(np.percentile(out, BOOT_CI[0])), float(np.percentile(out, BOOT_CI[1]))


def measure(rows, cik, rule, alpha, phi, rng, reps, band=False, mid=None):
    l0, l1 = lives(rows, rule, band=band, mid=mid)
    d0, d1 = 1.0 / l0, 1.0 / l1
    adm, rises = psi_parts(d0, d1, alpha, phi)
    n, n_adm = len(rows), int(adm.sum())
    lo, hi = clustered_bootstrap(adm, rises, cik, rng, reps)
    npair, modal = heaping(l0, l1, adm)
    return {
        "rule": rule, "band": band, "n": n, "n_admissible": n_adm,
        "A": (n_adm / n) if n else float("nan"),
        "psi": float(rises.sum() / n_adm) if n_adm else float("nan"),
        "ci_lo": lo, "ci_hi": hi, "distinct_pairs": npair, "modal_share": modal,
        "excl_property_only": int(((d0 >= alpha) & (d1 < alpha)).sum()),
        "excl_intangible_only": int(((d1 >= alpha) & (d0 < alpha)).sum()),
        "excl_both": int(((d0 >= alpha) & (d1 >= alpha)).sum()),
    }


def support_share(rows, rule, life_ppe, life_fin):
    l0, l1 = lives(rows, rule)
    inside = ((l0 >= life_ppe[0]) & (l0 <= life_ppe[1])
              & (l1 >= life_fin[0]) & (l1 <= life_fin[1]))
    return float(inside.mean()), int(inside.sum()), len(rows)


# ======================================================================================
# F10 -- NO FREE PARAMETER
# ======================================================================================
def _module_literals(source: str) -> set:
    out = set()
    for node in ast.parse(source).body:
        if not isinstance(node, ast.Assign):
            continue
        try:
            ast.literal_eval(node.value)
        except (ValueError, SyntaxError, TypeError):
            continue
        for t in node.targets:
            if isinstance(t, ast.Name):
                out.add(t.id)
    return out


def f10_unregistered(source: str) -> set:
    return _module_literals(source) - set(REGISTERED_CONSTANTS) - {"REGISTERED_CONSTANTS"}


# ======================================================================================
# REPORT SCANNERS -- F3, F4, F5, F6
# ======================================================================================
def _tables(md: str):
    return [b for b in md.split("\n\n") if "|" in b and "---" in b]


def _reports_psi_a_or_s(block: str) -> bool:
    head = block.splitlines()[0]
    return ("Ψ" in block or re.search(r"\|\s*A\s*\|", head)
            or re.search(r"\|\s*S\s*\|", head))


def scan_f4(md: str) -> list:
    bad = [b.splitlines()[0][:64] for b in _tables(md)
           if _reports_psi_a_or_s(b) and QUALIFIER_MARK not in b]
    if QUALIFIER_MARK not in md.split("## 7")[-1]:
        bad.append("the summary section does not name the gap")
    return bad


def scan_f3(md: str) -> list:
    return [b.splitlines()[0][:64] for b in _tables(md)
            if "R_WEIGHT" in b and RWEIGHT_MARK not in b]


def scan_f6(md: str) -> list:
    out = []
    for b in _tables(md):
        head = b.splitlines()[0]
        if "Ψ" in head or "first rung rises" in head:
            if "distinct pairs" not in b or "modal share" not in b:
                out.append(head[:64])
    return out


def scan_f9(md: str, got: dict) -> list:
    """F9's printing half: the one-tag-only firm-years are their own row, BROKEN OUT by
    which tag is missing, and no denominator anywhere equals their count."""
    need = (str(got["one_tag_only"]), str(got["ppe_only"]), str(got["fin_only"]))
    missing = [n for n in need if n not in md]
    folded = [b.splitlines()[0][:64] for b in _tables(md)
              if re.search(rf"\|\s*{got['one_tag_only']}\s*\|", b)]
    return missing + folded


def scan_f5(md: str) -> list:
    for b in _tables(md):
        if all(k in b for k in ("0.050", "0.350", "0.408")) and "Ψ (disclosed pairs)" in b:
            return []
    return ["no single table carries Ψ_rect(0.05), Ψ_rect(0.35), Ψ_rect(α̂) and Ψ together"]


# ======================================================================================
# MAIN
# ======================================================================================
def main() -> int:
    root = _here().parent
    tee = Tee(root / "docs" / "preregistration" / "RESULT-REG-009-run.log")
    sys.stdout = tee
    try:
        return _run(root)
    finally:
        sys.stdout = tee._out
        tee.close()


def _run(root: Path) -> int:
    src_self = Path(__file__).resolve().read_text()
    body = src_self.split("REGISTERED_CONSTANTS = {", 1)[1]

    hr("REG-009 · LADDER INPUTS — §11's falsifiers, in order, before any statistic")
    print("  F1, F2, F7, F8, F9a and F10 run here, before anything is computed. F3, F4,")
    print("  F5 and F6 assert properties OF THE REPORT and run against the rendered")
    print("  document before it is written to disk. See RESULT-REG-009 §0.\n")

    print("F1 · THE RULER IS LIFTED, NOT REBUILT")
    ns = lift_ruler()
    phi = ns["PHI"]
    reps, seed = int(ns["N"]), int(ns["SEED"])
    print(f"  bootstrap replicates and seed are LIFTED from wt088 (N={reps}, SEED={seed}); "
          f"this instrument chooses neither.")

    print("\nF2 · THE POPULATION IS THE ONE §7.1 COUNTED  (F7's digests gate the read)")
    rows, cyc_arr, cik_arr, tally, firms = load_population(root)
    pooled_firms = firms["2014-15"] | firms["2022-23"]
    got = {
        "pairs_2014_15": tally["2014-15"]["pair"],
        "pairs_2022_23": tally["2022-23"]["pair"],
        "pairs_pooled": len(rows), "firms_pooled": len(pooled_firms),
        "firms_both_cycles": len(firms["2014-15"] & firms["2022-23"]),
        "r_weight_both": tally["2014-15"]["wboth"] + tally["2022-23"]["wboth"],
        "one_tag_only": sum(t["any"] - t["pair"] for t in tally.values()),
        "ppe_only": sum(t["ppe"] - t["pair"] for t in tally.values()),
        "fin_only": sum(t["fin"] - t["pair"] for t in tally.values()),
        "any_2014_15": tally["2014-15"]["any"], "any_2022_23": tally["2022-23"]["any"],
    }
    for k, v in got.items():
        print(f"    {k:<20} {v}")
    check("F2a · the pair join reproduces §7.1's table exactly — 321 · 362 · 683 · 577 · 273",
          got == SEEN_COUNTS,
          witness=lambda: {**got, "pairs_pooled": got["pairs_pooled"] + 1} == SEEN_COUNTS)
    check(f"F2b · each cycle carries at least §3b's THIN floor of {THIN_FLOOR} pairs",
          min(tally[c]["pair"] for c in CYCLES) >= THIN_FLOOR,
          witness=lambda: min(1, tally[CYCLES[0]]["pair"]) >= THIN_FLOOR)
    check("F2c · all three D2 rules resolve on all 683 pairs",
          all(r[f"L{i}_{rule}"] > 0 for r in rows for i in (0, 1) for rule in RULES),
          witness=lambda: all(r[f"L0_{PRIMARY}"] > 1e9 for r in rows))
    check("F2d · alpha_hat, read from paper III §5.4, is the rate the committed records "
          "themselves carry",
          all(json.loads((root / "data" / f"reg-009-p0-lives-{y}.json").read_text())
              ["alpha_measured"] == ALPHA_HAT for y in (2015, 2023)),
          witness=lambda: all(
              json.loads((root / "data" / f"reg-009-p0-lives-{y}.json").read_text())
              ["alpha_measured"] == ALPHA_HAT + 0.01 for y in (2015, 2023)))

    print("\nD3 · THE BAND MIDPOINT IS P0's BIN, LIFTED  (not a registered falsifier — an "
          "implementation-provenance guard, counted by severity like any other)")
    mid, mid_desc = lift_band_rule()
    all_lives = [r[f"L{i}_{rule}"] for r in rows for i in (0, 1) for rule in RULES]
    check("D3a · every band midpoint is the centre of P0's own bin for that life",
          all(abs(mid(v, BAND_WIDTH) - (int(v // BAND_WIDTH) + 0.5) * BAND_WIDTH) < 1e-12
              for v in all_lives),
          witness=lambda: all(abs(round(v) - (int(v // BAND_WIDTH) + 0.5) * BAND_WIDTH)
                              < 1e-12 for v in all_lives))
    int_share = float(np.mean([abs(v - round(v)) < 1e-6 for v in all_lives]))
    print(f"    integer share of the lives entering Ψ_band: {int_share:.3f} — and P0's "
          f"bins are [b·w, (b+1)·w), so an integer life sits on a bin's LEFT EDGE and a "
          f"midpoint collapse TRANSLATES it by +{BAND_WIDTH/2:.2f} y rather than rounding "
          f"it. Read P3 with that in the same sentence.")

    print("\nF7 · NO NEW SOURCE, NO NETWORK, NO ZIP")
    present = sorted(set(NETMODS) & set(sys.modules))
    print(f"    network/archive modules resident: {present or 'none'}")
    check("F7b · the instrument has imported no network module and no archive reader",
          not present,
          witness=lambda: not (set(NETMODS) & (set(sys.modules) | {"socket"})))
    check("F7c · the instrument's own source opens no archive and names no URL",
          not re.search(NET_PAT, body, re.M),
          witness=lambda: not re.search(NET_PAT, "import " + "zipfile", re.M))

    print("\nF8 · THE STATISTIC DOES NOT SEE ANYTHING BUT THE PAIR")
    leaked = sorted({k for r in rows for k in dict.keys(r)} & set(FORBIDDEN))
    print(f"    forbidden keys present in any row the statistic receives: "
          f"{leaked or 'none'}")
    check("F8a · cik, name, sic, adsh, period and components are absent from every row",
          not any(set(FORBIDDEN) & set(dict.keys(r)) for r in rows),
          witness=lambda: not any(
              set(FORBIDDEN) & (set(dict.keys(r)) | {"cik"}) for r in rows))

    def _touched():
        try:
            rows[0]["sic"]
        except BlindnessViolation:
            return "raised"
        return None
    check("F8b · and a touch RAISES rather than reading as absent — a key that returns "
          "None is a key a .get() swallows",
          _touched() == "raised",
          witness=lambda: dict.get(rows[0], "sic") is not None)
    print("    declared exceptions: `cycle` reaches only the splitter and `cik` only the "
          "resampler; both travel in their own arrays, never in the row.")

    print("\nF9 · EMPTY IS DISTINGUISHABLE FROM ABSENT, AND ABSENCE IS ASSERTED")
    print(f"    one-tag-only firm-years: {got['one_tag_only']} = {got['ppe_only']} "
          f"property-only + {got['fin_only']} intangible-only. Their own row; no "
          f"denominator.")
    check("F9a · no industry-median variant is computed anywhere in this run (§6, D4)",
          "sic" in FORBIDDEN and not re.search(MEDIAN_PAT, body),
          # The falsifying world is BUILT FROM FRAGMENTS: a source-text guard and a
          # witness that must contain the forbidden string are in direct conflict, and
          # the first run of this check failed on its own witness's literal. The guard
          # caught the guard. Keep the fragments.
          witness=lambda: not re.search(MEDIAN_PAT, "def industry" + "_median(): pass"))

    print("\nF10 · NO FREE PARAMETER")
    unreg = f10_unregistered(src_self)
    print(f"    module-level literals not in REGISTERED_CONSTANTS: {sorted(unreg) or 'none'}")
    check("F10 · the instrument exposes no tunable that was not fixed in REG-009 before "
          "this file was written",
          not unreg,
          witness=lambda: not f10_unregistered(src_self + "\nFUDGE = 0.5\n"))

    # ==================================================================================
    hr("§7.3 · THE REGISTERED STATISTICS — one pass, all rates")
    rng = np.random.default_rng(seed)
    subsets = {"pooled": list(range(len(rows)))}
    for c in CYCLES:
        subsets[c] = [i for i, x in enumerate(cyc_arr) if x == c]

    res = {"pass_id": hashlib.sha256(
        (ns["_src_sha"] + "".join(sorted(LIVES_SHA256.values()))).encode()
    ).hexdigest()[:16], "psi": {}}
    for sub, idx in subsets.items():
        sub_rows = [rows[i] for i in idx]
        sub_cik = cik_arr[idx]
        for rule in RULES:
            for band in (False, True):
                res["psi"][f"{sub}|{rule}|{'band' if band else 'raw'}"] = measure(
                    sub_rows, sub_cik, rule, ALPHA_HAT, phi, rng, reps, band=band,
                    mid=mid)
    res["S"] = {r: support_share(rows, r, ns["LIFE_PPE"], ns["LIFE_FIN"]) for r in RULES}

    D0, D1 = ns["_grid"]
    res["psi_rect"] = {}
    for label, a in (("calibration", float(ns["ALPHA"])),
                     ("extension", float(ns["A_EXT"])), ("measured", ALPHA_HAT)):
        r, adm = _rect_shares(D0, D1, a, phi)
        res["psi_rect"][label] = {"alpha": a, "rises_of_admissible": r,
                                  "admissible_share": adm}
    res["counts"] = got
    res["alpha_hat"] = ALPHA_HAT
    res["alpha_hat_ci"] = list(ALPHA_HAT_CI)
    res["wt088_poles"] = ns["_poles"]
    res["band_rule"] = {"lifted_from": P0_SRC, "shape": mid_desc,
                        "integer_share_of_lives": int_share}

    p = res["psi"]
    for sub in ("pooled",) + CYCLES:
        for rule in RULES:
            r, b = p[f"{sub}|{rule}|raw"], p[f"{sub}|{rule}|band"]
            print(f"  {sub:<9} {rule:<9} n={r['n']:>4} adm={r['n_admissible']:>4} "
                  f"A={r['A']:.3f}  Ψ={r['psi']:.4f} [{r['ci_lo']:.4f},{r['ci_hi']:.4f}] "
                  f" Ψ_band={b['psi']:.4f}  distinct={r['distinct_pairs']:>3} "
                  f"modal={r['modal_share']:.3f}  excl(p/i/both)="
                  f"{r['excl_property_only']}/{r['excl_intangible_only']}/{r['excl_both']}")
    for label, d in res["psi_rect"].items():
        rr = "vacuous (admissible set empty)" if np.isnan(d["rises_of_admissible"]) \
            else f"{d['rises_of_admissible']:.4f}"
        print(f"  Ψ_rect[{label:<11} alpha={d['alpha']:.3f}]  admissible="
              f"{d['admissible_share']:.4f}  rises_of_admissible={rr}")
    for rule, (s, k, n) in res["S"].items():
        print(f"  S[{rule:<9}] = {s:.4f}  ({k}/{n} pairs inside the asserted rectangle)")

    # ==================================================================================
    hr("§9 · THE REGISTERED PREDICTIONS, SCORED")
    prim = {sub: p[f"{sub}|{PRIMARY}|raw"] for sub in ("pooled",) + CYCLES}
    band_pooled = p[f"pooled|{PRIMARY}|band"]
    v = {
        "P1": all(prim[c]["psi"] > P1_P4_SIDE for c in CYCLES),
        "P2": (prim["pooled"]["psi"] < P2_POLE
               and not (prim["pooled"]["ci_lo"] <= P2_POLE <= prim["pooled"]["ci_hi"])),
        "P3": abs(band_pooled["psi"] - prim["pooled"]["psi"]) < P3_TOL,
        "P4": len({p[f"pooled|{r}|raw"]["psi"] > P1_P4_SIDE for r in RULES}) == 1,
    }
    for k, ok in v.items():
        print(f"  {k}: {'HOLDS' if ok else 'FAILS'}")
    res["predictions"] = v

    rect_hat = res["psi_rect"]["measured"]["rises_of_admissible"]
    agree = bool(prim["pooled"]["ci_lo"] <= rect_hat <= prim["pooled"]["ci_hi"])
    res["stopping"] = {"psi_pooled": prim["pooled"]["psi"],
                       "psi_rect_alpha_hat": rect_hat, "agree_within_interval": agree}
    print(f"  §12: Ψ={prim['pooled']['psi']:.4f} vs Ψ_rect(α̂)={rect_hat:.4f} — "
          f"{'AGREE' if agree else 'DISAGREE'} within [{prim['pooled']['ci_lo']:.4f}, "
          f"{prim['pooled']['ci_hi']:.4f}]")

    # ==================================================================================
    hr("Q6 · RESOLUTION AUDIT — every identifier resolved against this sample")
    audit = {
        "tags": {PPE: got["ppe_only"] + got["pairs_pooled"],
                 FIN: got["fin_only"] + got["pairs_pooled"]},
        "rules": {r: sum(1 for row in rows if row[f"L0_{r}"] > 0) for r in RULES},
        "R_WEIGHT_backed_both": got["r_weight_both"],
        "R_WEIGHT_backed_share": got["r_weight_both"] / got["pairs_pooled"],
        "wt088_symbols": {n: repr(ns[n].tolist() if hasattr(ns[n], "tolist") else ns[n])
                          for n in LADDER_NAMES},
        "wt088_boundary_expr": ns["_boundary_src"],
        "wt088_sha256": ns["_src_sha"],
        "pass_id": res["pass_id"],
    }
    resolved = {**audit["tags"], **audit["rules"]}
    audit["dead"] = [k for k, n in resolved.items() if not n]
    for k, n in resolved.items():
        print(f"    {k:<52} {n}")
    print(f"    DEAD by name: {audit['dead'] or 'none'}")
    check("Q6 · every identifier this registration names resolves to something in its "
          "own sample",
          not audit["dead"],
          witness=lambda: not [k for k, n in {**resolved, "PHANTOM": 0}.items() if not n])
    (root / "data" / "reg-009-resolution-audit.json").write_text(
        json.dumps(audit, indent=2) + "\n")

    # ==================================================================================
    hr("THE REPORT — rendered, scanned by F3/F4/F5/F6, then written")
    md = render(res, ns, tally, got, v, agree)
    for name, scanner in (("F3", scan_f3), ("F4", scan_f4), ("F5", scan_f5),
                          ("F6", scan_f6), ("F9b", lambda m: scan_f9(m, got))):
        bad = scanner(md)
        print(f"    {name}: {'clean' if not bad else bad}")
    check("F3 · every table printing an R_WEIGHT quantity prints the amount-backed share "
          "beside it",
          not scan_f3(md), witness=lambda: not scan_f3(md.replace(RWEIGHT_MARK, "xxx")))
    check("F4 · no table reports Ψ, A, S or Ψ_band without the disclosed-versus-economic "
          "δ gap named in it, and the summary names it too",
          not scan_f4(md), witness=lambda: not scan_f4(md.replace(QUALIFIER_MARK, "xxx")))
    check("F5 · Ψ_rect(0.05), Ψ_rect(0.35), Ψ_rect(α̂) and Ψ are produced in one "
          "invocation and printed in one table",
          not scan_f5(md), witness=lambda: not scan_f5(md.replace("0.350", "x.xxx")))
    check("F6 · the distinct-pair count and the modal-pair share are printed beside "
          "every Ψ",
          not scan_f6(md), witness=lambda: not scan_f6(md.replace("modal share", "xxx")))
    check("F9b · the one-tag-only firm-years are their own row, broken out by which tag "
          "is missing, and are not a denominator anywhere",
          not scan_f9(md, got),
          witness=lambda: not scan_f9(md.replace(str(got["ppe_only"]), "xxx"), got))

    (root / "docs" / "preregistration" / "RESULT-REG-009.md").write_text(md)
    (root / "data" / "reg-009-result.json").write_text(
        json.dumps(_nan_to_none(res), indent=2) + "\n")
    print("    written: docs/preregistration/RESULT-REG-009.md · data/reg-009-result.json "
          "· data/reg-009-resolution-audit.json")

    summary("REG-009 LADDER INPUTS")
    return 0


# ======================================================================================
# THE DOCUMENT
# ======================================================================================
def _psi_row(r, label):
    return (f"| {label} | {r['n']} | {r['n_admissible']} | {r['A']:.3f} | "
            f"{r['psi']:.4f} | [{r['ci_lo']:.4f}, {r['ci_hi']:.4f}] | "
            f"{r['distinct_pairs']} | {r['modal_share']:.3f} |")


def render(res, ns, tally, got, v, agree) -> str:
    p, rect = res["psi"], res["psi_rect"]
    prim = p[f"pooled|{PRIMARY}|raw"]
    band = p[f"pooled|{PRIMARY}|band"]
    share = got["r_weight_both"] / got["pairs_pooled"]
    cap = (f"*Every number in this table is {QUALIFIER_MARK} — paper III §4.7's weak "
           f"joint, unmeasured, and the slack in every row. `R_WEIGHT` is "
           f"{RWEIGHT_MARK} on both tags in {got['r_weight_both']} of "
           f"{got['pairs_pooled']} pairs ({share:.3f}); on the other "
           f"{got['pairs_pooled'] - got['r_weight_both']} it is `R_MID` under another "
           f"name.*")
    L = []
    A = L.append

    A("# RESULT-REG-009 · The ladder's first rung, measured on the disclosure rather "
      "than on a rectangle")
    A(f"*wealthTensor-30 · 2026-08-14 · REG-009 §§6–12's registered run. Instrument: "
      f"`scripts/reg009_ladder_inputs.py`, written after Part II was committed and pushed "
      f"alone. Full output: `RESULT-REG-009-run.log`. Table: `data/reg-009-result.json`. "
      f"Resolution audit: `data/reg-009-resolution-audit.json`. Pass id "
      f"`{res['pass_id']}`.*")
    A("")
    A("---")
    A("")
    A("## 0 · What ran, and the one reading §11 required")
    A("")
    A("§11 says each falsifier runs **before Ψ is computed, in the order listed**. Six of "
      "them can, and did: F1, F2, F7, F8, F9's absence half and F10 are properties of the "
      "ruler, the population and the instrument, and all six ran before any statistic "
      "existed. **F3, F4, F5 and F6 are properties of the report** — a qualifier "
      "travelling inside a table, three rates printed in one table, a heaping column "
      "beside every Ψ — and their subject does not exist until the document is rendered. "
      "They ran against the rendered document **before it was written to disk**, so a "
      "report violating any of them would never have been published. Nothing about the "
      "run's validity was decided after Ψ was seen; what was decided after Ψ existed is "
      "whether this file could be written. The reading is recorded rather than taken "
      "silently.")
    A("")
    A("**The ruler was lifted, not rebuilt, and checked twice.** F1 extracts `ALPHA`, "
      "`A_EXT`, `PHI`, `DELTA`, `LIFE_PPE`, `LIFE_FIN`, `G`, `N`, `SEED` and the "
      "`d1_boundary` line out of `wt088_disclosed_ladder.py` by name, recomputes that "
      "script's committed poles from them, **and runs `wt088` as a subprocess in the same "
      "pass to compare against its own stdout**: "
      f"{100*res['wt088_poles']['admissible_at_alpha']:.1f} % admissible at α = "
      f"{rect['calibration']['alpha']}, the first rung rising in "
      f"{100*res['wt088_poles']['rises_at_a_ext']:.1f} % of the admissible rectangle at "
      f"α = {rect['extension']['alpha']}, both figures matching wt088's own printed line. "
      "The closed-form boundary and the R comparison it summarises were checked for "
      "agreement on every cell of `wt088`'s own grid. The bootstrap's replicate count and "
      f"seed are `wt088`'s `N` = {int(ns['N'])} and `SEED` = {int(ns['SEED'])}: **this "
      "instrument chooses no number of its own**, which is what makes F10 checkable "
      "rather than rhetorical.")
    A("")
    A("## 1 · The population, unmoved")
    A("")
    A("| | 2014-15 | 2022-23 | pooled |")
    A("|---|---|---|---|")
    A(f"| firm-years with any canonical life | {got['any_2014_15']} | "
      f"{got['any_2022_23']} | {got['any_2014_15'] + got['any_2022_23']} |")
    A(f"| **… with BOTH — the registered unit** | **{got['pairs_2014_15']}** | "
      f"**{got['pairs_2022_23']}** | **{got['pairs_pooled']}** |")
    A(f"| distinct firms carrying a pair | {tally['2014-15']['pair']} | "
      f"{tally['2022-23']['pair']} | **{got['firms_pooled']}** |")
    A(f"| … appearing in both cycles | — | — | **{got['firms_both_cycles']}** |")
    A(f"| `R_WEIGHT` {RWEIGHT_MARK} on both tags | {tally['2014-15']['wboth']} | "
      f"{tally['2022-23']['wboth']} | **{got['r_weight_both']} ({share:.3f})** |")
    A("")
    A(f"**F2 passed against §7.1's table exactly.** F9's row: **{got['one_tag_only']} "
      f"firm-years carry one tag and not the other** — {got['ppe_only']} property-only, "
      f"{got['fin_only']} intangible-only. They are counted here and enter no denominator "
      "anywhere below. No industry-median variant was computed (§6, D4); F9 asserts the "
      "absence rather than leaving a reader to notice it.")
    A("")
    A("## 2 · Ψ, A and the heaping columns — the registered table")
    A("")
    A(f"α̂ = {res['alpha_hat']} (paper III §5.4; interval [{res['alpha_hat_ci'][0]}, "
      f"{res['alpha_hat_ci'][1]}]), φ = (0.80, 0.60) lifted from `wt088`. **A is a gate on "
      "the run, not evidence about the world** — Q3 spends its direction, so it is "
      "reported and not interpreted. Pairs outside the admissible region are counted and "
      "named, never clipped and never folded into Ψ's denominator.")
    A("")
    for sub in ("pooled",) + CYCLES:
        A(f"**{sub}**")
        A("")
        A("| rule | pairs | admissible | A | Ψ | 95 % clustered CI | distinct pairs "
          "| modal share |")
        A("|---|---|---|---|---|---|---|---|")
        for rule in RULES:
            lbl = f"**`{rule}`** (primary)" if rule == PRIMARY else f"`{rule}`"
            A(_psi_row(p[f"{sub}|{rule}|raw"], lbl))
        A(_psi_row(p[f"{sub}|{PRIMARY}|band"], "`R_MID` **banded** (D3, 1.00 y)"))
        A(cap)
        A("")
    r0 = p[f"pooled|{PRIMARY}|raw"]
    A(f"**What A excludes, by coordinate.** Of the {got['pairs_pooled']} pooled pairs, "
      f"{r0['excl_property_only']} are inadmissible on the property life alone, "
      f"{r0['excl_intangible_only']} on the intangible life alone and {r0['excl_both']} on "
      f"both — a life at or under {1/res['alpha_hat']:.2f} years under `R_MID`. R is "
      "undefined there; they are excluded and counted, not clipped.")
    A("")
    A("## 3 · The bridge — Ψ against the manuscript's own rectangle, three rates, one pass")
    A("")
    A("| quantity | α | admissible share | first rung rises | distinct pairs | modal share |")
    A("|---|---|---|---|---|---|")
    for label, note in (("calibration", "Ψ_rect · asserted rectangle, uniform 400×400 "
                                        "(the manuscript's calibration)"),
                        ("extension", "Ψ_rect · asserted rectangle (wt088's labelled "
                                      "EXTENSION, where 99.7 % is computed)"),
                        ("measured", "Ψ_rect · asserted rectangle, at the MEASURED rate")):
        d = rect[label]
        rr = "— (vacuous: the admissible set is empty)" \
            if np.isnan(d["rises_of_admissible"]) else f"{d['rises_of_admissible']:.4f}"
        A(f"| {note} | {d['alpha']:.3f} | {d['admissible_share']:.4f} | {rr} | grid | "
          f"grid |")
    A(f"| **Ψ (disclosed pairs)**, `R_MID` | {res['alpha_hat']:.3f} | {prim['A']:.4f} | "
      f"**{prim['psi']:.4f}** | {prim['distinct_pairs']} | {prim['modal_share']:.3f} |")
    A(cap)
    A("")
    A("**Without the third row this table would not be readable.** A gap between Ψ and "
      "99.7 % could be the disclosure or it could be the recognition rate; Ψ_rect(α̂) "
      "holds the rectangle fixed and moves only the rate, so the two channels separate.")
    A("")
    A(f"**S — the support share.** The share of disclosed pairs falling inside the "
      f"manuscript's asserted rectangle, L₀ ∈ [{ns['LIFE_PPE'][0]:.0f}, "
      f"{ns['LIFE_PPE'][1]:.0f}] and L₁ ∈ [{ns['LIFE_FIN'][0]:.0f}, "
      f"{ns['LIFE_FIN'][1]:.0f}]. This measures the assumption directly rather than "
      f"arguing about it.")
    A("")
    A("| rule | S | pairs inside | pairs |")
    A("|---|---|---|---|")
    for rule in RULES:
        s, k, n = res["S"][rule]
        A(f"| `{rule}` | {s:.4f} | {k} | {n} |")
    A(cap)
    A("")
    A("## 4 · Ψ_band — the heaping robustness row, and the control that failed")
    A("")
    delta_band = abs(band["psi"] - prim["psi"])
    gap = abs(rect["measured"]["rises_of_admissible"] - prim["psi"])
    A(f"Every δ collapsed to its D3 band midpoint (1.00 year) and Ψ recomputed: "
      f"**Ψ_band = {band['psi']:.4f}** against **Ψ = {prim['psi']:.4f}**, a difference of "
      f"**{delta_band:.4f}**, on {band['distinct_pairs']} distinct banded pairs against "
      f"{prim['distinct_pairs']} raw ones. P3 registered five points as the line beyond "
      f"which Ψ would be a statistic about the granularity of the disclosure rather than "
      f"about the ladder.")
    A("")
    if not v["P3"]:
        A(f"**P3 FAILS, and §9 says what that means: Ψ is sensitive to the granularity of "
          f"the disclosure, and §10 records it rather than the registration arguing its "
          f"way out.** A one-year regranulation moves the registered statistic by "
          f"{delta_band:.3f}, above the five points registered before the number existed. "
          f"The banding was not changed after the failure and no second band width was "
          f"tried: F10 refuses a free parameter introduced to reconcile a number, and a "
          f"control rescued after it fails is not a control.")
        A("")
        A(f"**What the failure does NOT do is close the gap in §3.** Ψ_band = "
          f"{band['psi']:.4f} is still {abs(rect['measured']['rises_of_admissible'] - band['psi']):.3f} "
          f"below Ψ_rect(α̂) = {rect['measured']['rises_of_admissible']:.4f}. The "
          f"granularity channel moves Ψ by {delta_band:.3f}; the distance to the "
          f"manuscript's rectangle is {gap:.3f}. At its worst the channel is about "
          f"{delta_band/gap:.0%} of what would have to be explained, so P2 survives P3's "
          f"failure — which is the only reason both are reported in the same section "
          f"rather than one of them in a footnote.")
        A("")
        A(f"**Post-hoc, and labelled as such because it was not registered: the mechanism "
          f"is visible in the bin edges.** D3's bins are lifted from `{P0_SRC}` at run "
          f"time — index `{res['band_rule']['shape'].split(' / ')[0]}`, edges "
          f"`{res['band_rule']['shape'].split(' / ')[1]}` — so this file did not choose "
          f"them. Those bins are half-open on the left, and "
          f"**{res['band_rule']['integer_share_of_lives']:.1%} of the lives entering "
          f"Ψ_band are integers**, which sit exactly on a bin's left edge. A midpoint "
          f"collapse therefore *translates* a heaped disclosure by half a year rather "
          f"than *rounding* it, which is not the operation the phrase 'a one-year "
          f"rounding' in §9 brings to mind. That is an observation about the operator, "
          f"checkable from two lines of committed source, and it is **not** offered as a "
          f"reason to discount the verdict: P3 failed as registered.")
        A("")
        A(f"**Repair, attached, per charter §2 — TEE UP, priced now so it cannot become a "
          f"rescue later.** A second banding whose bin edges fall on half-integers, so "
          f"the heap sits at a bin's *centre* and the collapse is a rounding rather than "
          f"a translation, is the robustness row this failure asks for. It costs one "
          f"function and one run on committed data. It must be **registered in its own "
          f"document before it is run**, beside this failure rather than instead of it, "
          f"and both rows reported — otherwise it is the seventh free parameter arriving "
          f"in the costume of a fix. REG-010's, not this one's.")
        A("")
    A("## 5 · The registered predictions, scored")
    A("")
    A("| prediction | registered claim | verdict |")
    A("|---|---|---|")
    A(f"| **P1** | Ψ > 0.50 under `R_MID`, in **both cycles separately** | "
      f"**{'HOLDS' if v['P1'] else 'FAILS'}** |")
    A(f"| **P2** | Ψ < 0.997 under `R_MID`, with 0.997 **outside** the clustered "
      f"interval | **{'HOLDS' if v['P2'] else 'FAILS'}** |")
    A(f"| **P3** | Ψ_band within five points of Ψ under `R_MID` | "
      f"**{'HOLDS' if v['P3'] else 'FAILS'}** |")
    A(f"| **P4** | `R_MIN` and `R_WEIGHT` land on the same side of 0.50 as `R_MID` | "
      f"**{'HOLDS' if v['P4'] else 'FAILS'}** |")
    A(cap)
    A("")
    rmin = {sub: p[f"{sub}|R_MIN|raw"] for sub in ("pooled",) + CYCLES}
    straddle = [c for c in CYCLES if rmin[c]["ci_lo"] < P1_P4_SIDE < rmin[c]["ci_hi"]]
    if straddle:
        psis = ", ".join("%.4f" % rmin[c]["psi"] for c in straddle)
        cis = ", ".join("[%.4f, %.4f]" % (rmin[c]["ci_lo"], rmin[c]["ci_hi"])
                        for c in straddle)
        A(f"**P4 holds pooled, and the pooled verdict hides a cell — so here it is.** "
          f"Under `R_MIN` in {' and '.join(straddle)}, Ψ = {psis} with a clustered "
          f"interval {cis} "
          f"— which straddles 0.50. That is not a direction flip, which is what P4 was "
          f"written to catch and what §9 says would be the larger finding; it is a cell "
          f"the data does not resolve. `R_MIN` is the rule §6 refused as primary because "
          f"it heaps hardest, and it carries the smallest admissible sample "
          f"({rmin['pooled']['n_admissible']} of {rmin['pooled']['n']} pooled, against "
          f"{prim['n_admissible']} under `R_MID`) on the fewest distinct points "
          f"({rmin['pooled']['distinct_pairs']} against {prim['distinct_pairs']}). "
          f"Reported here rather than left for a reader to compute from §2.")
        A("")
    A("## 6 · §12's stopping rule, applied")
    A("")
    if agree:
        A(f"**Ψ = {prim['psi']:.4f} and Ψ_rect(α̂) = {rect['measured']['rises_of_admissible']:.4f} "
          f"agree to within Ψ's clustered interval [{prim['ci_lo']:.4f}, "
          f"{prim['ci_hi']:.4f}]: at the measured recognition rate the manuscript's "
          f"asserted rectangle is an adequate stand-in for the disclosure, and §4.4 needs "
          f"only its α named.** That is the registered finding, reported in one sentence "
          f"with its number, per §12 — a result, not a null to be buried.")
    else:
        rate_move = abs(rect["measured"]["rises_of_admissible"]
                        - rect["extension"]["rises_of_admissible"])
        gap6 = abs(rect["measured"]["rises_of_admissible"] - prim["psi"])
        s_mid = res["S"][PRIMARY][0]
        A(f"**Ψ = {prim['psi']:.4f} and Ψ_rect(α̂) = "
          f"{rect['measured']['rises_of_admissible']:.4f} disagree**: Ψ_rect(α̂) falls "
          f"outside Ψ's clustered interval [{prim['ci_lo']:.4f}, {prim['ci_hi']:.4f}], by "
          f"{gap6:.3f}. §12 says the difference is attributed by S, by the distinct-pair "
          f"columns and by Ψ_rect(α̂), never by narration. Attributed:")
        A("")
        A(f"- **The recognition rate is not doing the work, and this is the row that says "
          f"so.** Holding the manuscript's rectangle fixed and moving α from "
          f"{rect['extension']['alpha']} to α̂ = {rect['measured']['alpha']} moves the "
          f"rectangle's answer by {rate_move:.4f}. That is {rate_move/gap6:.1%} of the "
          f"gap. Without Ψ_rect(α̂) this sentence could not be written, and the gap would "
          f"have been attributable to whichever channel a reader preferred.")
        A(f"- **The support is wrong, and S measures it rather than arguing it.** "
          f"S = {s_mid:.4f} under `R_MID`: {res['S'][PRIMARY][1]} of "
          f"{res['S'][PRIMARY][2]} disclosed pairs fall inside L₀ ∈ "
          f"[{ns['LIFE_PPE'][0]:.0f}, {ns['LIFE_PPE'][1]:.0f}] × L₁ ∈ "
          f"[{ns['LIFE_FIN'][0]:.0f}, {ns['LIFE_FIN'][1]:.0f}]. "
          f"**{1 - s_mid:.1%} of the disclosure lives outside the rectangle the "
          f"manuscript integrates over.**")
        A(f"- **The measure is not uniform and not a product.** "
          f"{prim['distinct_pairs']} distinct pairs carry {prim['n_admissible']} "
          f"admissible rows, with a modal pair share of {prim['modal_share']:.3f}; the "
          f"two coordinates are chosen by one management on one page, and §4.4 sweeps "
          f"them independently.")
        A("")
        A(f"**What this attribution does NOT do is split the last two.** The rate channel "
          f"is ruled out quantitatively; support and measure jointly carry the remaining "
          f"{gap6 - rate_move:.3f}, and this design does not decompose them — Q1 "
          f"registered that all three channels would be computed and printed together, "
          f"not that the last two would be separated. Saying which of support or measure "
          f"carries more would need a fourth quantity nobody registered, and F10 is why "
          f"it is not being invented here.")
        A("")
        A(f"**Stated positively, which is what the paper needs:** at the measured "
          f"recognition rate, the first rung of §4.4's ladder rises in "
          f"**{prim['psi']:.1%} of the firm-years that disclose both lives** "
          f"({prim['n_admissible']} admissible pairs across "
          f"{res['counts']['firms_pooled']} firms), in both cycles separately "
          f"({p[f'2014-15|{PRIMARY}|raw']['psi']:.1%} and "
          f"{p[f'2022-23|{PRIMARY}|raw']['psi']:.1%}). The 99.7 % is a property of an "
          f"asserted rectangle under a uniform product measure, not of the disclosure — "
          f"and the direction the manuscript claims survives; only the magnitude does "
          f"not.")
    A("")
    A("No free parameter was introduced to reconcile Ψ with 99.7 %. F10 asserts the "
      "seventh refusal, and it passed.")
    A("")
    A("## 7 · What this does not measure")
    A("")
    A(f"**Every quantity above is {QUALIFIER_MARK}.** Ψ, A, S, Ψ_band, and every recovery "
      "number `RESULT-P0` printed, are computed from the life a filing DISCLOSES. Paper "
      "III §4.7's weak joint is the gap between that and the rate at which the asset "
      "actually declines; REG-009 §10 says this registration does not measure it, and it "
      "does not. Every number here is an upper bound in that sense.")
    A("")
    A("This run did not re-test §5.1's lag gradient, did not read φ per firm, did not run "
      "the industry-median variant, did not quote a price for §7.5's property-impairing "
      "universe, and did not touch σ. No zip was opened, no network module was imported, "
      "and both record files were checked by digest before they were read.")
    A("")
    return "\n".join(L)


if __name__ == "__main__":
    raise SystemExit(main())
