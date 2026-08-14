"""SCOUTING probe (read-only): how does the domain rescue in paper-III 4.4 behave
across the alpha values REG-003 itself put on the table?

Reads the committed lives files. Writes nothing into the repo.
"""
from pathlib import Path
ROOT = Path(__file__).resolve().parents[3]   # <repo>/docs/scouting/probes/x.py
import json, numpy as np

PPE = "PropertyPlantAndEquipmentUsefulLife"
FIN = "FiniteLivedIntangibleAssetUsefulLife"
PHI = (0.80, 0.60)          # tier 0, tier 1 -- paper 4.4's table
RULE = "R_MID"

rows = []
for p in ["reg-009-p0-lives-2015.json", "reg-009-p0-lives-2023.json"]:
    for r in json.loads((ROOT / "data" / p).read_text())["records"]:
        lv = r["lives"]
        if PPE in lv and FIN in lv:
            rows.append((float(lv[PPE][RULE]), float(lv[FIN][RULE]), int(r["cik"])))

L0 = np.array([r[0] for r in rows]); L1 = np.array([r[1] for r in rows])
d0, d1 = 1.0 / L0, 1.0 / L1
n = len(rows)
print(f"pairs = {n}   (paper 4.4 / REG-009 says 683)")

# The asserted rectangle: property 10-40 yr, finite-lived intangible 3-20 yr.
RECT_FASTEST = 1.0 / 3.0

CUTS = [
    ("REG-003 adverse cut (drop the 175 one-quarter events)", 0.327),
    ("rectangle's fastest disclosed rate (3-yr life)",        RECT_FASTEST),
    ("alpha-hat 95% lower bound",                             0.383),
    ("computer-services universe alone",                      0.394),
    ("alpha-hat, the headline",                               0.408),
    ("retail universe alone",                                 0.433),
    ("alpha-hat 95% upper bound",                             0.432),
    ("unregistered shifted estimate",                         0.460),
]
print(f"\n{'alpha':>7}  {'adm share':>10}  {'n adm':>6}  {'rect fully in?':>15}  what it is")
for label, a in sorted(CUTS, key=lambda x: x[1]):
    adm = (d0 < a) & (d1 < a)
    rect_in = a > RECT_FASTEST
    print(f"{a:7.3f}  {adm.mean():10.4f}  {int(adm.sum()):6d}  {str(rect_in):>15}  {label}")

# how far below the boundary does the adverse cut sit, in disclosed-life terms
print(f"\nrectangle needs alpha > {RECT_FASTEST:.4f}; REG-003's adverse cut gives 0.327 "
      f"({0.327 - RECT_FASTEST:+.4f})")
# share of pairs excluded at the adverse cut that are admissible at the headline
a_lo, a_hi = 0.327, 0.408
lost = ((d0 < a_hi) & (d1 < a_hi)) & ~((d0 < a_lo) & (d1 < a_lo))
print(f"pairs admissible at 0.408 but NOT at 0.327: {int(lost.sum())} of {n} "
      f"({lost.mean():.4f})")
