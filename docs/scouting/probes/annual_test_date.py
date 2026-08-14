"""SCOUTING probe (read-only).  REVIEW-004 C12 named ASC 350-20-35-28's elected annual
test date as a delay bolted onto every lag, identical across tiers, and proposed a
diagnostic that was never run and never reached the manuscript.

SCOPE GUARD: this measures a property of the INSTRUMENT (do charges concentrate on a
firm's own calendar quarter?).  It does NOT compute a tier gradient on any subsample --
PRE-002's stopping rule and REG-003 7 forbid a third instrument for the lag gradient,
and a subsample gradient is exactly that.  Nothing here is a re-test.
"""
from pathlib import Path
ROOT = Path(__file__).resolve().parents[3]   # <repo>/docs/scouting/probes/x.py
import json, collections, numpy as np
d = json.load(open(str(ROOT / "data") + "/pre-002-events.json"))
rng = np.random.default_rng(20260814)

for name, v in d["universes"].items():
    ev = v["events"]
    print(f"== {name}  n={len(ev)}")
    aa = collections.Counter((e["tier"], bool(e["annual_attributed"])) for e in ev)
    for t in range(4):
        y, n = aa[(t, True)], aa[(t, False)]
        print(f"   tier {t}: annual_attributed {y}/{y+n} = {y/(y+n):.3f}")
    byfirm = collections.defaultdict(list)
    for e in ev:
        byfirm[e["cik"]].append(e["q_star"] % 4)
    for kmin in (2, 3, 4):
        fs = {c: q for c, q in byfirm.items() if len(q) >= kmin}
        if not fs: continue
        obs = np.mean([collections.Counter(q).most_common(1)[0][1] / len(q) for q in fs.values()])
        # null: charge quarters iid uniform on 4, same per-firm counts
        null = []
        for _ in range(4000):
            null.append(np.mean([collections.Counter(rng.integers(0, 4, len(q))).most_common(1)[0][1] / len(q)
                                 for q in fs.values()]))
        null = np.array(null)
        p = (null >= obs).mean()
        print(f"   firms with >= {kmin} charges: {len(fs):3d} | modal-quarter share obs {obs:.3f} "
              f"vs null {null.mean():.3f} [{np.percentile(null,2.5):.3f},{np.percentile(null,97.5):.3f}]  p={p:.4f}")
    # calendar-quarter mix of charges overall
    qc = collections.Counter(e["q_star"] % 4 for e in ev)
    print(f"   charge calendar-quarter mix (q index mod 4): {[qc[i] for i in range(4)]}")
