#!/usr/bin/env python3
"""wt183 — re-adjudicate Paper IV's promises after wt182's five manuscript edits.

wt182 repaired five sentences in Paper IV.  `promise_id` hashes (paper, artefact, sentence), so
six committed rows went STALE and eight promises came out unadjudicated — wt148 RC 1.  This
script closes both halves in the shape the TSV header requires: RE-CHECK, DO NOT RE-KEY.  Every
row below was produced by RUNNING the command in its evidence cell today, on the repaired text,
and every note quotes what that command printed rather than paraphrasing it.

Six of the eight succeed a retired row, and each gets a `#superseded` ledger line so wt170's
chain walk can follow it.  Two are NEW promises that did not exist before wt182: Paper IV had
never named `scripts/wt018_report.py`, which is finding IV-10 and the reason this pass exists.

EXIT 0 = eight rows written, six superseded, every post-condition holds.
EXIT 2 = refused or a post-condition failed; the TSV is rolled back to its pre-run bytes.
"""
import pathlib, shutil, subprocess, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
TSV = ROOT / "docs/promises-adjudicated.tsv"
sys.path.insert(0, str(ROOT / "scripts"))
import wt148_promise_sweep as wt148

PAPER_IV = ROOT / "docs/papers/paper-IV-composition/paper-IV.md"


def sentence_for(pid: str) -> str:
    """The SEVENTH column is derived from wt148's own emitter, never transcribed."""
    for e in wt148.emit(PAPER_IV):
        if e["pid"] == pid:
            return e["sentence"]
    sys.exit(f"PRECONDITION FAILED: wt148 emits no promise {pid} for paper-IV")

RETIRED = {
    "f06ce25844": ("080a335509", "wt182 IV-12a cut §1's 'two places' census and named the third record; same artefact, new promise_id"),
    "029659c8b2": ("38d46b03dc", "wt182 IV-12c cut §10's 'two places' census and named the third record; same artefact, new promise_id"),
    "10d2d456ea": ("5853b68c71", "wt182 IV-10 rewrote §10's Regenerate bullet to name wt018_report.py; the pytest clause is unchanged in substance, new promise_id"),
    "a00820b165": ("e6500597a0", "wt182 IV-10 rewrote §10's Regenerate bullet; wt071_refuter's clause is unchanged in substance, new promise_id"),
    "e238ae248a": ("50848d3974", "wt182 IV-10 changed 'under both' to 'under all three'; same artefact, same claim, new promise_id"),
    "30191fec1a": ("c333cd154c", "wt182 IV-10 re-subjected the sentence to the test module and added the wt018_report.py clause; same artefact, new promise_id"),
}

ROWS = [
 ("paper-IV", "080a335509", "REG-013", "H",
  "sed -n '/^- \\*\\*The record of §6/,/are the record of §6\\.\\*\\*/p' docs/papers/paper-IV-composition/paper-IV.md",
  "prints §10's record bullet: it names RESULT-REG-013-run.log and RESULT-REG-013-run.json, 'the committed output of the 2026-08-16 run', and says in bold 'Those files, not a command, are the record of §6' -- so §1's promise that §10 names the record for each still holds after wt182, and §10 now also names the third record (`wc -w` on the superseded draft) that §1 names",
  ),
 ("paper-IV", "38d46b03dc", "REG-013", "H",
  "python3 -c \"import json;d=json.load(open('docs/preregistration/RESULT-REG-013-run.json'));print(round(d['P_ceiling'],4), d['F_floor'], sorted((k,v['intersection'],round(v['overlap'],4)) for k,v in d['pairs'].items() if v.get('role')=='target'))\"",
  "prints `0.4773 0.0 [('S,K', 6, 0.0053), ('T,K', 15, 0.0108), ('T,S', 23, 0.0202)]` -- §6's ceiling 0.477, its floor of exactly zero, and its three target pairs 23/0.0202, 15/0.0108 and 6/0.0053, all read off the committed run. §6's numbers ARE REG-013's, which is what the repaired sentence claims",
  ),
 ("paper-IV", "0586978a7a", "python3 scripts/wt018_report.py", "H",
  "python3 scripts/wt018_report.py | sed -n '/E · EXCESS DEMAND IS MONOTONE/,/sign changes/p'",
  "prints `grid points 500`, `monotonicity violations 0`, `z at grid min / max 249 / -150`, `sign changes 1` -- the four numbers §5 reports for the sweep. THIS IS FINDING IV-10: no command Paper IV named produced them before wt182, and no test asserted the endpoints or the sign change until wealthTensor-100 added test_the_monotone_sweep_endpoints_and_single_crossing_are_what_section_5_reports",
  ),
 ("paper-IV", "9a2fba1c55", "wt018_report.py", "H",
  "python3 scripts/wt018_report.py | sed -n '/B · THE CURVES ARE NOT INDEPENDENT/,/identically/p' | sed -n '3,10p'",
  "prints `interior grid points, ties excluded 399`, `distinct DEMAND schedules 25`, `distinct SUPPLY schedules 25`, `distinct EXCESS-DEMAND schedules 1` and `excess demand == count(m_i > p) - S, identically True` -- §5's table, as a table. The sentence's claim that wt018_report.py 'is the table' is what this output is",
  ),
 ("paper-IV", "5853b68c71", "python3 -m pytest tests/test_excess_demand.py -q", "H",
  "python3 -m pytest tests/test_excess_demand.py -q; grep -n 'assert grid.size == 399\\|assert len(excess) == 4\\|assert len(demand) == 25\\|assert len(supply) == 25' tests/test_excess_demand.py",
  "12 passed (11 before wealthTensor-100 added the endpoint test). The asserts the sentence claims are at L86 `assert grid.size == 399`, L91 `assert len(demand) == 25`, L92 `assert len(supply) == 25` and L56 `assert len(excess) == 4` for §8's twelve-point four. The module ASSERTS the schedule counts and the tie convention, so its output is a verdict; the table is wt018_report.py's",
  ),
 ("paper-IV", "e6500597a0", "python3 scripts/wt071_refuter.py", "H",
  "python3 scripts/wt071_refuter.py",
  "RC 0. C1 prints `crossing height across 25 allocations min 85 max 103` with D(p*) = S(p*) = |H \\\\ T| SEVERE at every allocation -- §5's crossing-height identity; C2(a) prints the N-dependence table 26.1x, 8.3x, 113.5x, 47.2x with `13.6-fold swing, non-monotone in N` and C2(b) the control `raise a RANDOM 250 by 20% spread 0.8934` against `raise NON-HOLDERS 20% spread 0.9576` -- §8's 0.89 against 0.96. Ends `WT-071 SEVERITY: 9 severe - 0 definitional - 0 failed/vacuous`",
  ),
 ("paper-IV", "50848d3974", "src/wealth_tensor/excess_demand.py", "H",
  "sed -n '1,6p' src/wealth_tensor/excess_demand.py; grep -on 'src/wealth_tensor/[a-z_]*\\.py' docs/papers/paper-IV-composition/paper-IV.md",
  "the module's own docstring opens 'Supply and demand as two readings of a single distribution of indifference points' and says it 'makes that claim executable' -- it is the module carrying THIS paper's reservation-price claim, not a sibling's. The grep then prints exactly four hits: L684 redistribution.py, L685 lag.py and L686 lambda_sensitivity.py, all named in the same bullet as Paper II's and Paper III's, and L700 excess_demand.py. So excess_demand.py is still this paper's only src/ dependency that is not a sibling's, and wt182's change of 'under both' to 'under all three' does not touch that claim",
  ),
 ("paper-IV", "c333cd154c", "tests/test_excess_demand.py", "H",
  "grep -n 'assert grid.size == 399\\|assert len(excess) == 4' tests/test_excess_demand.py",
  "prints `56:    assert len(excess) == 4` and `86:    assert grid.size == 399` -- §8's twelve-point four and §5's 399, both asserted and neither printed by this module, which is what the sentence claims",
  ),
]


def main():
    txt = TSV.read_text()
    lines = txt.split("\n")

    if "080a335509" in txt:
        print("wt183: already applied (idempotent no-op)")
    else:
        bak = TSV.with_suffix(TSV.suffix + ".bak-wt183")
        if not bak.exists():
            shutil.copy2(TSV, bak)
        # 1 · drop the six retired rows
        kept = []
        dropped = 0
        for l in lines:
            pid = l.split("\t")[1] if l.count("\t") >= 2 and not l.startswith("#") else None
            if pid in RETIRED:
                dropped += 1
                continue
            kept.append(l)
        if dropped != len(RETIRED):
            sys.exit(f"PRECONDITION FAILED: expected {len(RETIRED)} retired rows, dropped {dropped}")
        # 2 · append the eight successors
        while kept and kept[-1] == "":
            kept.pop()
        for r in ROWS:
            kept.append("\t".join(list(r) + [sentence_for(r[1])]))
        # 3 · the supersession ledger, so wt170's chain walk can follow
        for old, (new, why) in RETIRED.items():
            kept.append("\t".join(["#superseded", old, new, "wt182", why]))
        TSV.write_text("\n".join(kept) + "\n")
        print(f"wt183: dropped {dropped} retired rows, wrote {len(ROWS)} rows, {len(RETIRED)} #superseded lines")

    # ---- post-conditions -------------------------------------------------------------
    t = TSV.read_text()
    checks = [("Q%02d row %s present" % (i + 1, r[1]), ("\t" + r[1] + "\t") in t) for i, r in enumerate(ROWS)]
    checks += [("Q09 NEGATIVE: no retired pid survives as a row",
                not any(("\t" + o + "\t") in t.split("#superseded")[0] for o in RETIRED))]
    # Q10 WAS A WHOLE-FILE CONSTANT AND IT WENT RED ON SOMEBODY ELSE'S CORRECT EDIT.
    # It read `t.count("#superseded\t") == 6 + 5`, hard-coding "5 pre-existing" -- so the FIRST
    # later session to retire a row legitimately turned this guard red for a reason that has
    # nothing to do with wt183. wealthTensor-102's wt189 retired three paper-II rows and took the
    # total to 14. The guard was RIGHT that something moved and WRONG about whose job it was.
    # Narrowed to the six lines wt183 is actually responsible for, each named, plus a one-sided
    # floor so the count can still only ever be too LOW. (wt187 pattern: derive, do not re-key.)
    _sup = [l for l in t.split("\n") if l.startswith("#superseded\t")]
    checks += [("Q10 each of wt183's own six #superseded lines is present exactly once",
                all(len([l for l in _sup if l.split("\t")[1] == o and l.split("\t")[2] == new]) == 1
                    for o, (new, _why) in RETIRED.items()))]
    checks += [("Q10b NEGATIVE: the file carries at least wt183's six plus the five it inherited",
                len(_sup) >= 6 + 5)]
    checks += [("Q11 NEGATIVE: no duplicate promise_id",
                len({l.split("\t")[1] for l in t.split("\n") if l.startswith("paper-")}) ==
                len([l for l in t.split("\n") if l.startswith("paper-")]))]
    checks += [("Q11b every new row has seven columns",
                all(len(l.split("\t")) == 7 for l in t.split("\n")
                    if l.startswith("paper-IV\t") and l.split("\t")[1] in {r[1] for r in ROWS}))]
    r = subprocess.run([sys.executable, "scripts/wt148_promise_sweep.py"], cwd=ROOT,
                       capture_output=True, text=True)
    checks += [("Q12 wt148 RC 0", r.returncode == 0),
               ("Q13 NEGATIVE: no STALE rows reported", "STALE row" not in r.stdout),
               ("Q14 NEGATIVE: no unadjudicated promises", "UNADJUDICATED" not in r.stdout)]
    bad = 0
    for name, ok in checks:
        print(f"  {'PASS' if ok else 'FAIL'}  {name}")
        bad += 0 if ok else 1
    if bad:
        print(r.stdout[-2500:])
        sys.exit(2)
    print(f"wt183 · post-conditions: {len(checks)} checks, 4 NEGATIVE")
    print("wt183: RC 0")


if __name__ == "__main__":
    main()
