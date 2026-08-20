#!/usr/bin/env python3
"""wt181 - Paper II's TWELFTH P7 read: two edits, three findings, and the measurement that
kills a sentence eleven passes carried.

THE THREE FINDINGS AND WHICH CHARTER MODE EACH REPAIR IS (docs/CO-AUTHOR-CHARTER.md section 2)

  II-40  REPLACE  L459  section 7 attributes the 0.035 periodicity span to "section 3.2".
                        The span lives in section 3.3 (Periodicity and threshold are trim, not
                        structure); section 3.2 is Realisation is the crux and contains neither
                        the number nor the sweep. INTRODUCED at 76355d6 (wealthTensor-92) - the
                        commit that repaired section 7's exception clause. It is the exact
                        failure mode section 7 itself names two sentences later: a provenance
                        claim that reads as checked and is not, one level up from a command to
                        a section. wt133_crossref_sweep CANNOT see it: section 3.2 RESOLVES, so
                        the sweep is green on a pointer aimed at the wrong section. A resolving
                        cross-reference is not a correct one, and E4 below is the check that
                        separates them for this one number.

  II-41  REPLACE  L459  the same sentence calls all three quantities "differences of numbers
                        both commands do print". 0.039 is not one: it is the distance from a
                        printed 0.861 to the 0.90 top-decile criterion, and the SAME SENTENCE
                        declares 0.90 unprinted by either command eleven words earlier. Same
                        commit, same clause, same class - REVIEW-021's measurement that naming
                        a defect class does not exhaust it in the site where it was named,
                        now observed inside a single sentence. ONE edit repairs II-40 and II-41.

  II-42  CUT      L329  section 3.4's "The top-share statistic is also horizon-stable where the
                        Gini is not." IS FALSE AS STATED, and E5 is the measurement. Across
                        T = 600 / 1200 / 2400 on six configurations and three seeds, the top
                        decile's spread EXCEEDS the Gini's in 14 of 18 config-seed pairs, and
                        its worst spread (0.171, flow r=0.025) is 3.4x the Gini's worst (0.050).
                        REVIEW-014 section 4 item 2 flagged this claim NOT MEASURED at
                        wealthTensor-74, named the exact check, and said it was "a natural
                        wt133". Five P7 passes went by. Nobody ran it. It is not new here;
                        it was left in the bag.

                        WHY CUT AND NOT REPLACE. The sentence has two readings. Under the
                        natural one - the statistic's VALUE moves less with the horizon - it is
                        false (E5). Under the charitable one - the CRITERION's verdict does not
                        change with the horizon - it is true (E6), and E6 measures that too.
                        REVIEW-008's II-14 already ruled on this shape: a quantity with two
                        readings that disagree is a defect. Stating the true reading needs
                        three numbers section 7 would then have to account for; the sentence it
                        would support is already carried by the sentence in front of it, which
                        gives the separation AND its 0.039 margin. So the slot is unnecessary:
                        the paper is stronger shorter. E6 keeps the true content measured, in
                        docs/, where charter section 1 puts the coach's notes.

NO EDIT IS AN ABSORB. No hedge is added anywhere; one false clause narrows and one false
sentence goes. E7 runs defensive_count.py over the result against Paper II's committed 0.

THE CHEAP SEAM (the general move worth stealing from wealthTensor-98). E5 and E6 PRINT their
counts before the verdict branch and expose measure_horizons() as an import, so a successor can
red-proof the number without re-running the verdict - and E4 exposes section_of() the same way.

ROLLBACK: paper-II.md is copied to paper-II.md.bak-wt181 before the first byte moves and
restored if any post-condition fails. A rollback is not a verdict on the repair.

EXIT: 0 = repaired and every post-condition holds - 1 = rolled back - 2 = refused before writing.
"""
from __future__ import annotations

import os
import re
import shutil
import subprocess
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PII = "docs/papers/paper-II-redistribution/paper-II.md"
OTHERS = ["docs/papers/paper-I-price-formation/paper-I.md",
          "docs/papers/paper-III-dual-tensor/paper-III.md",
          "docs/papers/paper-IV-composition/paper-IV.md"]
BAK = ".bak-wt181"

REPAIRS = [
    ("R1 replace (II-40 + II-41)",
     "and three differences of numbers both commands do print — §3.2's 0.035 "
     "periodicity span, and §3.4's 0.103 Gini gap and 0.039 top-decile margin.",
     "§3.3's 0.035 periodicity span and §3.4's 0.103 Gini gap, each a difference "
     "of two\n  values `wt030_report.py` prints; and §3.4's 0.039 top-decile margin, the "
     "distance from that\n  command's printed 0.861 to the 0.90 threshold above."),

    ("R2 cut (II-42)",
     "clearing the 0.90 threshold with 0.039 to spare. The top-share statistic is also "
     "horizon-stable where the Gini is not.",
     "clearing the 0.90 threshold with 0.039 to spare."),
]

GONE = [
    "§3.2's 0.035",
    "three differences of numbers both commands do print",
    "horizon-stable",
]

CONFIGS = [("none", {}),
           ("stock r=0.025", dict(base="stock", rate=0.025)),
           ("stock r=0.100", dict(base="stock", rate=0.100)),
           ("flow r=0.025", dict(base="flow", rate=0.025)),
           ("flow r=0.100", dict(base="flow", rate=0.100)),
           ("flow r=1.000", dict(base="flow", rate=1.000))]
HORIZONS = (600, 1200, 2400)
SEEDS = (0, 1, 2)


def _rx(anchor):
    return re.compile(r"\s+".join(re.escape(w) for w in anchor.split()))


def _read(path):
    with open(os.path.join(REPO, path), encoding="utf-8") as fh:
        return fh.read()


def _write(path, text):
    with open(os.path.join(REPO, path), "w", encoding="utf-8") as fh:
        fh.write(text)


# ---------------------------------------------------------------- the importable seams

def section_of(text, needle):
    """Every '### N.M' subsection whose body contains `needle`. The check wt133 cannot run:
    wt133 asks whether a cross-reference RESOLVES; this asks whether it is CORRECT.

    A subsection ends at the NEXT heading of ANY level, not at the next '###'. The first
    version of this function ended the last '###' at end-of-file, which swallowed sections 4
    through 7 into '3.4' and reported 0.035 in two subsections - the repaired section 7 clause
    counting as an occurrence of the thing it points AT. It failed closed and is recorded here
    rather than quietly corrected: a locator whose ranges are wrong reports the pointer as its
    own referent, which is the one answer that cannot falsify anything."""
    bounds = [m.start() for m in re.finditer(r"^#{2,3} ", text, re.M)]
    heads = [(m.start(), m.group(1)) for m in re.finditer(r"^### (\d+\.\d+)", text, re.M)]
    hits = []
    for pos, num in heads:
        nxt = [b for b in bounds if b > pos]
        end = nxt[0] if nxt else len(text)
        if needle in text[pos:end]:
            hits.append(num)
    return hits


def measure_horizons():
    """(rows, top_worse, pairs). rows = (config, seed, dGini, dTop10). Reads only committed code."""
    sys.path.insert(0, os.path.join(REPO, "src"))
    from wealth_tensor.redistribution import (RedistributiveEconomy, stationary_gini,
                                              top_share)
    rows = []
    for name, kw in CONFIGS:
        for s in SEEDS:
            g, t = [], []
            for h in HORIZONS:
                r = RedistributiveEconomy(seed=s, **kw).run(h)
                g.append(stationary_gini(r))
                t.append(top_share(r))
            rows.append((name, s, max(g) - min(g), max(t) - min(t)))
    worse = sum(1 for _, _, dg, dt in rows if dt > dg)
    return rows, worse, len(rows)


def separation_by_horizon():
    """(horizon, condensed_top, worst_bounded_top) for the 0.90 criterion, seed 0.
    The TRUE reading of the sentence II-42 cuts - kept measured, in docs/."""
    sys.path.insert(0, os.path.join(REPO, "src"))
    from wealth_tensor.redistribution import RedistributiveEconomy, top_share
    out = []
    for h in HORIZONS:
        cond = top_share(RedistributiveEconomy(seed=0).run(h))
        bounded = [top_share(RedistributiveEconomy(seed=0, **kw).run(h))
                   for name, kw in CONFIGS if kw]
        out.append((h, cond, max(bounded)))
    return out


def _defensive(path):
    r = subprocess.run([sys.executable, "scripts/defensive_count.py", path],
                       cwd=REPO, capture_output=True, text=True)
    return r.returncode, r.stdout


def main():
    full = os.path.join(REPO, PII)

    # ---- E1 PRE-CONDITION -------------------------------------------------------------
    pre = []
    for tag, old, _new in REPAIRS:
        n = len(_rx(old).findall(_read(PII)))
        pre.append((tag.split()[0], n))
        if n != 1:
            print("wt181: PRE-CONDITION FAILED - %s anchor matches %d time(s), expected 1"
                  % (tag, n), file=sys.stderr)
            return 2
    print("  [ok  ] E1 PRE      both anchors match exactly once - "
          + ", ".join("%s:%d" % (t, n) for t, n in pre))

    others_before = {p: _read(p) for p in OTHERS if os.path.exists(os.path.join(REPO, p))}
    shutil.copyfile(full, full + BAK)
    checks = []

    try:
        for tag, old, new in REPAIRS:
            text, n = _rx(old).subn(lambda _m, _n=new: _n, _read(PII), count=1)
            if n != 1:
                raise RuntimeError("%s: substitution applied %d times" % (tag, n))
            _write(PII, text)
        t = _read(PII)

        # ---- E2 NEGATIVE: the three old strings are gone --------------------------------
        for s in GONE:
            checks.append(("E2 NEGATIVE gone: %r" % s, s not in t))

        # ---- E3: the repaired clause is present, once ----------------------------------
        checks.append(("E3 the repaired clause names 3.3 exactly once",
                       len(re.findall(r"§3\.3's 0\.035 periodicity span", t)) == 1))
        checks.append(("E3 the repaired clause still enumerates five quantities",
                       "except five\n  quantities neither command prints" in t))

        # ---- E4: THE CHECK wt133 CANNOT RUN -------------------------------------------
        secs = section_of(t, "0.035")
        print("  [meas] E4 SEAM    subsections whose body contains 0.035: %s" % (secs,))
        checks.append(("E4 0.035 lives in 3.3", secs == ["3.3"]))
        checks.append(("E4 NEGATIVE 0.035 is absent from 3.2", "3.2" not in secs))

        # ---- E5: the measurement that kills the sentence -------------------------------
        rows, worse, pairs = measure_horizons()
        wg = max(dg for _, _, dg, _ in rows)
        wt = max(dt for _, _, _, dt in rows)
        print("  [meas] E5 SEAM    top decile moves MORE than the Gini in %d of %d "
              "config-seed pairs; worst spread Gini %.4f, top decile %.4f"
              % (worse, pairs, wg, wt))
        checks.append(("E5 the cut sentence is false: top decile is the LESS stable one",
                       worse > pairs / 2))
        checks.append(("E5 and not marginally: its worst spread exceeds the Gini's", wt > wg))

        # ---- E6: the TRUE reading, kept measured --------------------------------------
        sep = separation_by_horizon()
        for h, cond, bnd in sep:
            print("  [meas] E6 SEAM    T=%-5d condensed top10 %.4f   worst bounded top10 %.4f"
                  % (h, cond, bnd))
        checks.append(("E6 the 0.90 criterion separates at every horizon tested",
                       all(bnd < 0.90 <= cond for _, cond, bnd in sep)))

        # ---- E7: defensive count non-increasing ---------------------------------------
        rc, out = _defensive(PII)
        print("  [meas] E7 SEAM    %s" % out.strip().splitlines()[0])
        checks.append(("E7 defensive_count RC 0", rc == 0))
        checks.append(("E7 paper-II is still 0 outside Limitations",
                       "0 defensive sentence(s) outside" in out))

        # ---- E8 NEGATIVE: no other manuscript moved -----------------------------------
        for p, before in others_before.items():
            checks.append(("E8 NEGATIVE %s byte-identical" % os.path.basename(p),
                           _read(p) == before))

        # ---- E9: the numbers the repaired clause now claims are printed, are -----------
        r = subprocess.run([sys.executable, "scripts/wt030_report.py"],
                           cwd=REPO, capture_output=True, text=True)
        o = r.stdout
        checks.append(("E9 wt030_report RC 0", r.returncode == 0))
        for n in ("0.861", "0.891", "0.994", "0.486", "0.451"):
            checks.append(("E9 wt030 prints %s" % n, n in o))
        checks.append(("E9 NEGATIVE wt030 does not print 0.90 as the criterion",
                       "0.90 " not in o and "0.9000" not in o))

        # ---- E10: the suite that holds the claims --------------------------------------
        r = subprocess.run([sys.executable, "-m", "pytest", "tests/test_redistribution.py", "-q"],
                           cwd=REPO, capture_output=True, text=True)
        tail = [ln for ln in r.stdout.strip().splitlines() if "passed" in ln]
        n_pass = int(re.search(r"(\d+) passed", tail[-1]).group(1)) if tail else -1
        print("  [meas] E10 SEAM   %s" % (tail[-1] if tail else "no pytest summary line"))
        checks.append(("E10 tests/test_redistribution.py green", r.returncode == 0))
        checks.append(("E10 the count section 7 quotes is still 18", n_pass == 18))

    except Exception as exc:                                     # noqa: BLE001
        shutil.copyfile(full + BAK, full)
        print("wt181: ROLLED BACK - %s" % exc, file=sys.stderr)
        return 1

    bad = [c for c, ok in checks if not ok]
    for c, ok in checks:
        print("  [%s] %s" % ("ok  " if ok else "FAIL", c))
    print("\nwt181: %d post-conditions, %d NEGATIVE, %d failed"
          % (len(checks), sum(1 for c, _ in checks if "NEGATIVE" in c), len(bad)))
    if bad:
        shutil.copyfile(full + BAK, full)
        print("wt181: ROLLED BACK", file=sys.stderr)
        return 1
    print("wt181: 2 edits, 3 findings (II-40, II-41, II-42) - repaired")
    return 0


if __name__ == "__main__":
    sys.exit(main())
