#!/usr/bin/env python3
"""wealthTensor-65 · measure candidate abstracts BEFORE choosing one.

Paper II's abstract sits at 249 words against a 250 ceiling — ONE word of slack, which `-64`
left deliberately for `DECISION-001`. Jason ticked **A**, so this is the pass that spends it.

`-64`'s rule, learned by nearly spending the slack twice: NEVER hand-count, and measure the
CANDIDATES, not just the winner. This writes each candidate into a copy of the manuscript and
runs `scripts/check_abstract_size.py` on it — the committed instrument, on a real file, which
is the only measurement that counts.

ROUND 1 (12 candidates) ALL BLEW THE CEILING, 262–274 words against 250, because every one of
them ADDED a "kappa is a budget, not a mechanism" clause. That clause is unnecessary: the
demotion is achieved by DELETING the assertion, not by arguing with it, and an abstract that
argues with a claim it no longer makes is defensive narration besides. Round 2 demotes by
subtraction. Characters were never binding — 1509 against 1920.
"""
from __future__ import annotations

import itertools
import pathlib
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
PAPER = ROOT / "docs/papers/paper-II-redistribution/paper-II.md"
SCRATCH = ROOT / ".wt65-abstract"

KAPPA_OLD = (
    "rate the two bases differ by roughly an order of magnitude in compression. The mechanism is κ,\n"
    "the share of aggregate wealth moved per assessment, for which the flow base admits a closed\n"
    "form."
)

KAPPA = {
    # demote by deletion: the sentence asserting mechanism simply goes
    "k5": (
        "rate the two bases differ by roughly an order of magnitude in κ, the share of aggregate\n"
        "wealth moved per assessment, for which the flow base admits a closed form."
    ),
    # demote by deletion AND name it a budget, which is shorter than the gloss it replaces
    "k6": (
        "rate the two bases differ by roughly an order of magnitude in κ, the levy's compressive\n"
        "budget, for which the flow base admits a closed form."
    ),
    "k7": (
        "rate the two bases differ by roughly an order of magnitude in κ, the levy's compressive\n"
        "budget — the share of wealth moved per assessment — for which the flow base admits a\n"
        "closed form."
    ),
}

RHO_OLD = (
    "At zero realisation a **100 % levy on flow is indistinguishable from no levy\n"
    "at all** (Gini 0.994 and top decile 1.000 in both)."
)

RHO = {
    "r4": (
        "At zero realisation the flow base is uniform, so a **100 % levy on flow\n"
        "leaves wealth exactly unchanged** (Gini 0.994 and top decile 1.000 in both)."
    ),
    "r5": (
        "At zero realisation the flow base is uniform, and a **100 % levy on flow\n"
        "changes nothing at all** (Gini 0.994 and top decile 1.000 in both)."
    ),
    "r6": (
        "At zero realisation the flow base carries no dispersion, so a **100 % levy\n"
        "on flow leaves wealth exactly unchanged** (Gini 0.994 and top decile 1.000 in both)."
    ),
}


def measure(text: str, tag: str) -> str:
    SCRATCH.mkdir(exist_ok=True)
    p = SCRATCH / f"paper-II-{tag}.md"
    p.write_text(text, encoding="utf-8")
    out = subprocess.run(
        (sys.executable, str(ROOT / "scripts/check_abstract_size.py"), str(p), "--print"),
        capture_output=True, text=True,
    )
    return (out.stdout + out.stderr).strip().splitlines()[-1]


src = PAPER.read_text(encoding="utf-8")
assert src.count(KAPPA_OLD) == 1, f"kappa anchor {src.count(KAPPA_OLD)}x"
assert src.count(RHO_OLD) == 1, f"rho anchor {src.count(RHO_OLD)}x"

print("baseline                    ", measure(src, "baseline"), "  (ceiling 250 words / 1920 chars)")
print()
for (kt, kv), (rt, rv) in itertools.product(KAPPA.items(), RHO.items()):
    text = src.replace(KAPPA_OLD, kv).replace(RHO_OLD, rv)
    widest = max(len(l) for l in text.split("\n"))
    m = measure(text, f"{kt}-{rt}")
    words = int(m.split("words=")[1].split()[0])
    flag = "  <-- OVER" if words > 250 else ("   ok" if widest <= 100 else "  <-- RAGGED")
    print(f"  {kt}+{rt}   {m}  widest_line={widest}{flag}")

print()
print("WT-094 guard — '18 tests' must survive every candidate:")
for (kt, kv), (rt, rv) in itertools.product(KAPPA.items(), RHO.items()):
    assert "18 tests" in src.replace(KAPPA_OLD, kv).replace(RHO_OLD, rv)
print(f"  ok — present in all {len(KAPPA) * len(RHO)} candidates")
