"""SCOUTING probe (read-only): how load-bearing is 5.3's 'tier 2 is the tallest rung'?
The paper says no reading of the ladder as a noisy version of the predicted one survives
that pattern.  A referee will ask how often the pattern survives resampling.
Firm-clustered bootstrap, since the paper's own 9 says events are not independent.
"""
from pathlib import Path
ROOT = Path(__file__).resolve().parents[3]   # <repo>/docs/scouting/probes/x.py
import json, numpy as np, collections
rng = np.random.default_rng(20260814)
d = json.load(open(str(ROOT / "data") + "/pre-002-events.json"))
REPS = 20000
for name, v in d["universes"].items():
    ev = v["events"]
    byfirm = collections.defaultdict(list)
    for e in ev:
        byfirm[e["cik"]].append((e["tier"], e["lag"]))
    firms = list(byfirm)
    obs = {t: np.median([e["lag"] for e in ev if e["tier"] == t]) for t in range(4)}
    hits = 0; ok = 0; mono = 0
    for _ in range(REPS):
        draw = rng.integers(0, len(firms), len(firms))
        pool = collections.defaultdict(list)
        for i in draw:
            for t, l in byfirm[firms[i]]:
                pool[t].append(l)
        if any(len(pool[t]) == 0 for t in range(4)):
            continue
        ok += 1
        m = [np.median(pool[t]) for t in range(4)]
        if m[2] > max(m[0], m[1], m[3]):
            hits += 1
        if m[0] <= m[1] <= m[2] <= m[3] and m[3] > m[0]:
            mono += 1
    print(f"== {name}: observed medians {obs}")
    print(f"   P(tier 2 strictly the tallest rung)      = {hits/ok:.3f}  ({hits}/{ok} firm-bootstrap draws)")
    print(f"   P(ladder monotone in the predicted order) = {mono/ok:.3f}")
