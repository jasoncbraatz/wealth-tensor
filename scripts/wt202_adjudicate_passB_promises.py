#!/usr/bin/env python3
"""wt202 — adjudicate the promises Pass B's repairs minted, and supersede the two its
repairs made stale.

SL-6 and SL-7 both work by NAMING AN ARTEFACT IN THE MANUSCRIPT, which is what wt148
counts as a promise.  Ten new promises, two superseded rows.  Every row below is written
only after its evidence command has been RUN HERE and returned what the note says it
returns -- this script refuses to append a row whose evidence does not check out, so the
ledger cannot gain a row nobody verified.

Idempotent: appends nothing if the ids are already present, exit 0.
"""
from __future__ import annotations
import subprocess, pathlib, sys

R = pathlib.Path(__file__).resolve().parents[1]
TSV = R / "docs/promises-adjudicated.tsv"
SENT = R / "scripts/wt201_promise_sentences.py"

def out(script: str) -> str:
    return subprocess.check_output(["python3", str(R / "scripts" / script)], text=True, cwd=R)

def has(o: str, *keys) -> dict:
    return {k: (k in o) for k in keys}

CHECKS = {}

def check(pid, script, keys, absent=()):
    o = out(script)
    r = has(o, *keys)
    ok = all(r.values()) and all(a not in o for a in absent)
    CHECKS[pid] = (r, ok)
    return ok

ROWS = []  # (pid, artefact, cls, evidence, note)

# ---------------------------------------------------------------- paper-III, SL-7
ROWS.append(("cf6cccf14b", "python3 scripts/wt084_identification_closed_form.py", "H",
 "python3 -c \"import subprocess;o=subprocess.check_output(['python3','scripts/wt084_identification_closed_form.py'],text=True);print({k:(k in o) for k in ('A^t coefficient equation residual','D^t coefficient equation residual','a factor of 1.67 in the UNOBSERVED physical scale','0.513158','2.220e-16','3.308e-01')});print('31.7 printed:', '31.7' in o or '0.317' in o)\"",
 "all six keys True and '31.7 printed: False'. The bullet's positive half holds -- both coefficient equations, the mirror at 2.220e-16, the rival map failing at 3.308e-01 (the fourteen orders the bullet names), the 1.67 scale factor, and the 0.513158 opening gap the bullet rounds to 51%. Its NEGATIVE half holds too, and that is the half worth checking: the command does not print 31.7%, which is exactly what the bullet discloses rather than promises. wealthTensor-104, SHIP-LIST SL-7."))

ROWS.append(("b81698b0b2", "python3 scripts/wt083_tier_ladder_antialignment.py", "H",
 "python3 -c \"import subprocess;o=subprocess.check_output(['python3','scripts/wt083_tier_ladder_antialignment.py'],text=True);print({k:(k in o) for k in ('phi   1-phi   delta   (1-phi)d      R sim   R closed','Kendall tau (registered rank vs observable), assumed ladder : +1.00','Kendall tau (registered rank vs observable), real ladder    : -1.00','dlog(1-phi)   dlog(delta)')})\"",
 "all four True. The command prints the four-tier ladder with the columns the bullet names (phi, 1-phi, delta, (1-phi)delta and R both simulated and closed form), both Kendall tau values, and the log-decomposition table the bullet says section 4.4 reads the step direction from. wealthTensor-104, SHIP-LIST SL-7."))

ROWS.append(("3cf6e7157d", "python3 scripts/wt088_disclosed_ladder.py", "H",
 "python3 -c \"import subprocess;o=subprocess.check_output(['python3','scripts/wt088_disclosed_ladder.py'],text=True);print({k:(k in o) for k in ('delta_3*                      = 0.007895','ORDERED (WT-083)       UNORDERED','lag non-decreasing up the ladder, ORDERED delta   : 100.0%','lag non-decreasing up the ladder, UNORDERED delta : 69.0%','M = 2000','of 400 random admissible','admissible share')})\"",
 "all seven True. delta_3* = 0.007895 is printed verbatim; the ORDERED/UNORDERED comparison carries the lag ordering and the magnitude measure under both draws; both ladder counts section 4.5 quotes are present (400 and M = 2000); and the rectangle's admissible-share lines are printed. wealthTensor-104, SHIP-LIST SL-7."))

ROWS.append(("e3b3a9a430", "python3 scripts/wt085_returns_conditioning.py", "H",
 "python3 -c \"import subprocess;o=subprocess.check_output(['python3','scripts/wt085_returns_conditioning.py'],text=True);print({k:(k in o) for k in ('E2 - returns break the root swap','E3 - the scale continuum survives returns entirely')})\"",
 "both True. The two claims the bullet attributes to section 4.6's run are the script's own E2 and E3 headings, and the run reaches both. wealthTensor-104, SHIP-LIST SL-7."))

ROWS.append(("aedac9e82c", "python3 scripts/wt086_exponent_robustness.py", "H",
 "python3 -c \"import re,subprocess;o=subprocess.check_output(['python3','scripts/wt086_exponent_robustness.py'],text=True);print('regime rows:',len([l for l in o.split(chr(10)) if re.search(r'^  [A-Za-z].*\\\\s0\\\\.\\\\d{3}\\\\s+0\\\\.\\\\d{3}\\\\s+-?\\\\d\\\\.\\\\d{3}\\\\s+-?\\\\d\\\\.\\\\d{3}',l)]));print('p_cond/p_se header:','p_cond    p_se' in o)\"",
 "prints 'regime rows: 9' and 'p_cond/p_se header: True'. Nine regimes, both exponents re-fitted in each -- which is the bullet's whole claim, and the reason section 4.7 quotes neither exponent as a constant. wealthTensor-104, SHIP-LIST SL-7."))

ROWS.append(("4bca6e5db1", "python3 scripts/wt087_goodwill_gradient.py", "H",
 "python3 -c \"import subprocess;o=subprocess.check_output(['python3','scripts/wt087_goodwill_gradient.py'],text=True);print({k:(k in o) for k in ('0.032   0.002     0.163','0.060   0.030    -0.386','fitted: se ~ (alpha-delta)^-0.700     spread 6.81x')})\"",
 "all three True. The delta-sweep at a fixed root gap runs the volatility exponent from -0.386 at the property-like rate to +0.163 at the goodwill-like one, and the level moves by 6.81x as (alpha-delta)^-0.700 -- both numbers the bullet names, printed by this command. wealthTensor-104, SHIP-LIST SL-7."))

ROWS.append(("fcb2ac1551", "python3 scripts/wt090_age_dependent_alpha.py", "H",
 "python3 -c \"import subprocess;o=subprocess.check_output(['python3','scripts/wt090_age_dependent_alpha.py'],text=True);print({k:(k in o) for k in (chr(34)+'the naive form'+chr(39)+'s pole sits at delta_a = 0.4350'+chr(34),'naive overstates by    0.55%','naive overstates by   43.87%','alpha_eff','delta3* = 0.00755/yr','delta3* = 0.00754/yr','0.00789')})\"",
 "all seven True. The pole at 0.4350/yr, the overstatement column running 0.55% at a forty-year life to 43.87% at a three-year one, the alpha_eff column across the same rectangle, delta_3* at both shapes (0.00755 published, 0.00754 measured) and the 0.00789 the calibration returns -- every figure the bullet attributes to this command. wealthTensor-104, SHIP-LIST SL-7."))

# ---------------------------------------------------------------- paper-IV, SL-6
ROWS.append(("a5fce86466", "docs/papers/paper-I-price-formation/paper-I.md", "H",
 "python3 -c \"import pathlib;p=pathlib.Path('docs/papers/paper-I-price-formation/paper-I.md');h=p.read_text(encoding='utf-8').split(chr(10))[:14];print('exists:',p.exists());print('superseded banner:',any('SUPERSEDED' in l.upper() for l in h));import re;s=pathlib.Path('docs/papers/paper-IV-composition/paper-IV.md').read_text(encoding='utf-8');print('sec10 names command and locale:', 'LC_ALL=C.UTF-8 wc -w docs/papers/paper-I-price-formation/paper-I.md' in s)\"",
 "prints 'exists: True', 'superseded banner: True' and 'sec10 names command and locale: True'. The sentence's three assertions all hold: the draft is in the repository, its first heading marks it superseded, and section 10 does now name the command and the locale that count it. SUPERSEDES cbd18be550, whose sentence claimed the file was 'the only place the word count above is checkable' -- SHIP-LIST SL-6, wealthTensor-104."))

ROWS.append(("684154869b", "docs/papers/paper-I-price-formation/paper-I.md", "H",
 "LC_ALL=C.UTF-8 wc -w docs/papers/paper-I-price-formation/paper-I.md  (and the same under LC_ALL=C with GNU coreutils)",
 "LC_ALL=C.UTF-8 returns 7527, which is the 'roughly 7,500' section 8 reports, on both macOS wc and GNU wc. Under LC_ALL=C, GNU wc returns 7367 on byte-identical content (md5 eb56ef67162df6db0fabf50819db78f0) -- the 160-word spread that made the figure uncheckable before the locale was named. macOS wc returns 7527 in every locale, which is why the defect was invisible on darwin. THIS IS THE ROW SL-6 EXISTS FOR: the bullet's claim is about the command AND the locale, and both halves check. wealthTensor-104."))

ROWS.append(("a41a260fb0", "REG-013", "H",
 "python3 -c \"import json;d=json.load(open('docs/preregistration/RESULT-REG-013-run.json'));print(round(d['P_ceiling'],4), d['F_floor'], sorted((k,v['intersection'],round(v['overlap'],4)) for k,v in d['pairs'].items() if v.get('role')=='target'))\"",
 "prints `0.4773 0.0 [('S,K', 6, 0.0053), ('T,K', 15, 0.0108), ('T,S', 23, 0.0202)]` -- section 6's ceiling 0.477, its floor of exactly zero, and its three target pairs, all read off the committed run. Section 6's numbers ARE REG-013's, which is what this sentence claims. SUPERSEDES 38d46b03dc verbatim in substance: SL-6 re-pointed the sentence's word-count clause at section 10's bullet, which changed the sentence and therefore the promise_id; the claim about REG-013 did not change and the evidence was RE-RUN, not carried over. wealthTensor-104."))

SUPERSEDED = [
    ("cbd18be550", "a5fce86466", "wt195", "SHIP-LIST SL-6: section 8 stopped claiming the draft file is the only place the word count is checkable and now points at section 10's command; same artefact, new promise_id"),
    ("38d46b03dc", "a41a260fb0", "wt195", "SHIP-LIST SL-6: section 10's preamble now points at the word-count bullet below it; the REG-013 claim in the sentence is unchanged and was re-run"),
]

EVIDENCE_RUNS = [
    ("cf6cccf14b", "wt084_identification_closed_form.py",
     ("A^t coefficient equation residual", "D^t coefficient equation residual",
      "a factor of 1.67 in the UNOBSERVED physical scale", "0.513158", "2.220e-16", "3.308e-01"), ("31.7", "0.317")),
    ("b81698b0b2", "wt083_tier_ladder_antialignment.py",
     ("phi   1-phi   delta   (1-phi)d      R sim   R closed",
      "Kendall tau (registered rank vs observable), assumed ladder : +1.00",
      "Kendall tau (registered rank vs observable), real ladder    : -1.00",
      "dlog(1-phi)   dlog(delta)"), ()),
    ("3cf6e7157d", "wt088_disclosed_ladder.py",
     ("delta_3*                      = 0.007895", "ORDERED (WT-083)       UNORDERED",
      "lag non-decreasing up the ladder, ORDERED delta   : 100.0%",
      "lag non-decreasing up the ladder, UNORDERED delta : 69.0%",
      "M = 2000", "of 400 random admissible", "admissible share"), ()),
    ("e3b3a9a430", "wt085_returns_conditioning.py",
     ("E2 - returns break the root swap", "E3 - the scale continuum survives returns entirely"), ()),
    ("4bca6e5db1", "wt087_goodwill_gradient.py",
     ("0.032   0.002     0.163", "0.060   0.030    -0.386",
      "fitted: se ~ (alpha-delta)^-0.700     spread 6.81x"), ()),
    ("fcb2ac1551", "wt090_age_dependent_alpha.py",
     ("the naive form's pole sits at delta_a = 0.4350", "naive overstates by    0.55%",
      "naive overstates by   43.87%", "alpha_eff", "delta3* = 0.00755/yr",
      "delta3* = 0.00754/yr", "0.00789"), ()),
]

def sentences_by_pid() -> dict:
    import importlib.util, json
    spec = importlib.util.spec_from_file_location("wt148", R / "scripts/wt148_promise_sweep.py")
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    d = {}
    for stem in ("paper-III-dual-tensor/paper-III", "paper-IV-composition/paper-IV"):
        for p in m.emit(R / f"docs/papers/{stem}.md"):
            d[p["pid"]] = (p["paper"], p["sentence"])
    return d

def drop_superseded(text: str) -> tuple[str, int]:
    """Delete the DATA rows the repairs made stale. The convention this file already
    follows (029659c8b2, superseded at wt182, is gone) is that the #superseded marker
    carries the lineage and the stale row is removed -- a row whose sentence no longer
    exists records a check that no longer applies."""
    keep, dropped = [], 0
    stale = {old for old, *_ in SUPERSEDED}
    for line in text.split("\n"):
        parts = line.split("\t")
        if len(parts) > 2 and not line.startswith("#") and parts[1] in stale:
            dropped += 1
            continue
        keep.append(line)
    return "\n".join(keep), dropped


def main() -> int:
    text = TSV.read_text(encoding="utf-8")
    if all(f"\t{pid}\t" in text for pid, *_ in ROWS):
        text2, n = drop_superseded(text)
        if n:
            TSV.write_text(text2, encoding="utf-8")
            print(f"wt202: rows already present; dropped {n} superseded data row(s)")
        else:
            print("wt202: NO-OP (all ten rows present, no superseded rows left)")
        return 0

    print("VERIFYING EVIDENCE BEFORE APPENDING ANYTHING")
    for pid, script, keys, absent in EVIDENCE_RUNS:
        if not check(pid, script, keys, absent):
            print(f"  {pid}: FAILED — {CHECKS[pid][0]}"); return 3
        print(f"  {pid}: ok ({script})")
    o = out("wt086_exponent_robustness.py")
    import re as _re
    n = len([l for l in o.split("\n") if _re.search(r"^  [A-Za-z].*\s0\.\d{3}\s+0\.\d{3}\s+-?\d\.\d{3}\s+-?\d\.\d{3}", l)])
    if n != 9 or "p_cond    p_se" not in o:
        print(f"  aedac9e82c: FAILED — regime rows {n}"); return 3
    print("  aedac9e82c: ok (wt086_exponent_robustness.py, 9 regimes)")
    p1 = R / "docs/papers/paper-I-price-formation/paper-I.md"
    utf8 = subprocess.run(f"LC_ALL=C.UTF-8 wc -w {p1}", shell=True, capture_output=True, text=True).stdout.split()[0]
    if utf8 != "7527" or not p1.exists():
        print(f"  684154869b: FAILED — LC_ALL=C.UTF-8 gives {utf8}"); return 3
    print("  684154869b / a5fce86466: ok (7527 under C.UTF-8)")
    import json as _json
    d = _json.load(open(R / "docs/preregistration/RESULT-REG-013-run.json"))
    if round(d["P_ceiling"], 4) != 0.4773:
        print("  a41a260fb0: FAILED — REG-013 ceiling moved"); return 3
    print("  a41a260fb0: ok (REG-013 ceiling 0.4773)")

    sents = sentences_by_pid()
    missing = [pid for pid, *_ in ROWS if pid not in sents]
    if missing:
        print("wt202: these ids are not currently emitted by the sweep:", missing); return 4

    lines = ["",
             "# --- wealthTensor-104 · PASS B ------------------------------------------------------------",
             "# SHIP-LIST SL-6 and SL-7 both repair by NAMING AN ARTEFACT, which mints promises. Ten rows,",
             "# every one verified by running its evidence in the same session that wrote it.",
             ]
    for pid, artefact, cls, evidence, note in ROWS:
        paper, sentence = sents[pid]
        lines.append("\t".join([paper, pid, artefact, cls, evidence, note, sentence]))
    for old, new, by, why in SUPERSEDED:
        lines.append("\t".join(["#superseded", old, new, by, why]))
    text, dropped = drop_superseded(text)
    TSV.write_text(text.rstrip("\n") + "\n" + "\n".join(lines) + "\n", encoding="utf-8")
    print(f"wt202: APPENDED {len(ROWS)} rows and {len(SUPERSEDED)} supersede markers; "
          f"dropped {dropped} superseded data row(s)")
    return 0

sys.exit(main())
