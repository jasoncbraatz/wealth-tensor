#!/usr/bin/env python3
"""MUTATION CONTROL — measure what the suite actually catches, before grading a constraint.

WHY THIS IS A COMMITTED SCRIPT AND NOT A SCRATCH FILE
------------------------------------------------------
`CONSTRAINT-INVENTORY-001` §2b: three sessions running, a column or a paragraph of this
estate has turned out to be a COVERAGE CLAIM that nobody ever verified — `-44` the
`machine` column, `-45` the `source` column, `-46` the inventory's own ranking prose,
which was wrong by eleven. The reason the claims survive is that verifying one by hand is
tedious and every cheaper check passes. So the tedious thing is an instrument now.

    python3 scripts/mutation_control.py --list
    python3 scripts/mutation_control.py                    # every probe, ~20 min
    python3 scripts/mutation_control.py --only 13 P6 P7    # a few

For each probe it copies the working tree to a scratch directory, applies ONE forbidden
move, runs the WHOLE suite, and reports every test that went red. A probe with no catchers
is an unguarded constraint — that is the measurement, and it is the only evidence that
earns a `FOR` or a `BINDS` in §1's `machine` column (`-44`'s ruling).

TWO THINGS THIS SCRIPT EXISTS TO STOP YOU DOING
------------------------------------------------
1. **Grading from the column.** The `machine` cell names the tests written FOR a
   constraint. It never names the tests that happen to catch it, and for C42 those were
   most of them. Count catchers, not pointers.
2. **Reading a red as the red you wanted.** `--only` prints every catcher, not the first.
   Eight of C42's fifteen were held solely by an instrument-reruns-to-itself test, which
   catches a hand-edit and is blind to a number a changed instrument re-derives. A
   reproducibility pin is not a freeze, and you only see that in the catcher list.

ADDING A PROBE: append to `PROBES`. A probe is `(slug, description, fn)`, or
`(slug, description, fn, opts)` where `opts` is a dict, and `fn` takes the scratch root and
makes exactly one forbidden move. Keep them one-move: a probe that changes two things cannot
tell you which one the suite saw.

    opts = {"git": True}   # the scratch copy is a REAL git work tree

THE HARNESS ITSELF WAS THE FIRST FALSE GREEN (`-47`)
-----------------------------------------------------
`-46` built this script with `.git` in the ignore list, because a scratch copy does not need
history to run the suite. It does need history to be **measured**: nine tests in this estate
skip with *"not a git work tree"*, and one of them —
`test_registrations_precede_their_instruments.py` — is the only machine anywhere near C07,
which §3.2 ranked **first** in cell (b). A C07 probe run under the original harness would have
come back GREEN and the green would have meant *the harness deleted the guard*, not *no guard
exists*.

That is `-37`'s tell one level up: **a mutation that the harness cannot see reports every
guard in the unseen part of the estate as absent.** So `.git` is copied on request, and a
probe whose constraint is about commit order MUST set `{"git": True}` or it is measuring
nothing. The same finding retired the two-tarball cloud stanza: a source tarball without
`.git` runs 990/999, and the nine it drops are exactly the axis nobody had probed.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = "data"
DOCS = "docs/preregistration"
DEFAULT_SCRATCH = Path(os.environ.get("MUTATION_SCRATCH", "/tmp/wt-mutation-control"))


# ----------------------------------------------------------------------------- helpers
def _json_edit(root: Path, rel: str, *path_and_value):
    """Set one key. `_json_edit(root, "data/x.json", "a", "b", 3)` sets x["a"]["b"] = 3."""
    *path, value = path_and_value
    p = root / rel
    obj = json.loads(p.read_text())
    node = obj
    for k in path[:-1]:
        node = node[k]
    if path[-1] not in node:
        raise SystemExit(f"PROBE SITE MISSING: {rel} has no {'.'.join(map(str, path))}")
    node[path[-1]] = value
    p.write_text(json.dumps(obj, indent=2) + "\n")


def _prose_edit(root: Path, rels: list[str], old: str, new: str):
    hits = 0
    for rel in rels:
        p = root / rel
        if not p.exists():
            continue
        text = p.read_text()
        hits += text.count(old)
        p.write_text(text.replace(old, new))
    if hits == 0:
        raise SystemExit(f"PROBE SITE MISSING: {old!r} in {rels}")


def _insert_after(root: Path, rel: str, anchor: str, sentence: str):
    """Write a forbidden CLAIM into a document, immediately after `anchor`.

    The claim probes take this shape rather than `_prose_edit`'s substitution because the
    forbidden-claim family (C16/C20/C23/C25/C30) forbids *asserting* something, not
    mis-stating a number: the violating document says everything the compliant one says and
    one sentence more. A probe that edited an existing sentence would be measuring a
    different constraint.

    Anchoring matters. `-43` ruled that a claim-scanner must be fed the registration's own
    forbidden claim before its green is trusted; the mirror-image rule for a PROBE is that
    the claim must land where a real violation would land — beside the paragraph that
    discusses the thing — and not appended to the end of the file where a section-scoped
    scanner would miss it for a reason that has nothing to do with the constraint.
    """
    p = root / rel
    if not p.exists():
        raise SystemExit(f"PROBE SITE MISSING: {rel} does not exist")
    text = p.read_text()
    if anchor not in text:
        raise SystemExit(f"PROBE SITE MISSING: anchor {anchor[:60]!r} in {rel}")
    p.write_text(text.replace(anchor, anchor + sentence, 1))


def _delete_file(root: Path, rel: str):
    """Remove one committed file.

    The forbidden move for a *beside, never instead of* pair (`-49`): the surviving half
    satisfies every prohibition in the estate and violates the pairing outright, which is
    why an absence guard cannot express that constraint (`-44`'s C49 shape).
    """
    p = root / rel
    if not p.exists():
        raise SystemExit(f"PROBE SITE MISSING: {rel} does not exist")
    p.unlink()


def _drop_section(root: Path, rel: str, heading: str):
    """Delete one `## ` section, heading included, up to the next `## `."""
    p = root / rel
    text = p.read_text()
    if heading not in text:
        raise SystemExit(f"PROBE SITE MISSING: {heading!r} in {rel}")
    head, _, rest = text.partition(heading)
    nxt = rest.find("\n## ")
    p.write_text(head + (rest[nxt + 1:] if nxt >= 0 else ""))


def _git(root: Path, *args: str):
    proc = subprocess.run(["git", *args], cwd=str(root), capture_output=True, text=True)
    if proc.returncode != 0:
        raise SystemExit(f"PROBE GIT FAILED: git {' '.join(args)} -> {proc.stderr.strip()}")


def _amend_after_result(root: Path, rel: str):
    """C07's forbidden move: amend a registration in a commit that lands after its result.

    One move, but it has two parts on purpose — the edit and the COMMIT. C07 is a constraint
    on history, so an uncommitted edit is not the violation; it is a dirty tree. This is the
    one probe whose green would be uninformative without `{"git": True}`.
    """
    p = root / rel
    p.write_text(p.read_text()
                 + "\n\n## 99 · Amendment\n\nThis registration is amended here, after its"
                   " result document was committed.\n")
    _git(root, "add", rel)
    _git(root, "-c", "user.name=mutation-probe", "-c", "user.email=probe@invalid",
         "commit", "-q", "-m", "REG-001: amend the registration after its result")


R9 = f"{DATA}/reg-009-result.json"
R10 = f"{DATA}/reg-010-half-integer-banding.json"
BC = f"{DATA}/reg-009-band-count.json"
BCF = f"{DATA}/reg-009-band-count-filled.json"
PRIMARY = ("psi", "pooled|R_MID|raw")

MS = "docs/papers/paper-III-dual-tensor/paper-III.md"
R12 = f"{DATA}/reg-012-band-edge-phase.json"

BAND_DOCS = [f"{DOCS}/RESULT-REG-009-band-count.md",
             f"{DOCS}/RESULT-REG-009-band-count-filled.md",
             f"{DOCS}/REG-009-p3-lifetime-sourced-delta.md",
             f"{DOCS}/CONSTRUCTION-REG-009-coverage-fill.md"]
RESULT_DOCS = [f"{DOCS}/RESULT-REG-009.md"]


# ------------------------------------------------- REG-010 §4's fifteen, in §4's order
PROBES: list[tuple[str, str, object]] = [
    ("01", "the 683 pairs",
     lambda r: (_json_edit(r, R9, "counts", "pairs_pooled", 684),
                _json_edit(r, R9, *PRIMARY, "n", 684))),
    ("02", "the 428 distinct pairs",
     lambda r: _json_edit(r, R9, *PRIMARY, "distinct_pairs", 429)),
    ("03", "the 665 admissible rows",
     lambda r: _json_edit(r, R9, *PRIMARY, "n_admissible", 666)),
    ("04", "Ψ = 0.6586 and its clustered interval",
     lambda r: (_json_edit(r, R9, *PRIMARY, "psi", 0.6686466165413534),
                _json_edit(r, R9, *PRIMARY, "ci_lo", 0.6310514299447248))),
    ("05", "A", lambda r: _json_edit(r, R9, *PRIMARY, "A", 0.9636456808199122)),
    ("06", "S", lambda r: _json_edit(r, R9, "S", "R_MID", [0.1490922401171303, 95, 683])),
    ("07", "Ψ_rect",
     lambda r: _json_edit(r, R9, "psi_rect", "calibration", "admissible_share", 0.10)),
    ("08", "Ψ_rect(α̂)",
     lambda r: (_json_edit(r, R9, "psi_rect", "measured", "rises_of_admissible", 0.988),
                _json_edit(r, R9, "stopping", "psi_rect_alpha_hat", 0.988))),
    ("09", "α̂", lambda r: _json_edit(r, R9, "alpha_hat", 0.418)),
    ("10", "the verdicts on P1..P4",
     lambda r: _json_edit(r, R9, "predictions", "P3", True)),
    ("11", "REG-009's numbering",
     lambda r: _prose_edit(r, [f"{DOCS}/REG-009-p3-lifetime-sourced-delta.md"],
                           "\n## 12 ", "\n## 13 ")),
    ("12", "the 151 tier-0 events",
     lambda r: (_json_edit(r, BC, "events_total", 152),
                _json_edit(r, BCF, "events_total", 152))),
    ("13", "the 98 firms — PROSE ONLY; it has no artifact field at all",
     lambda r: _prose_edit(r, BAND_DOCS, "98 firms", "99 firms")),
    ("14", "the 110 of the band counts",
     lambda r: _json_edit(r, BC, "events_joinable", 111)),
    ("15", "the 133 of the band counts",
     lambda r: _json_edit(r, BCF, "events_joinable", 134)),
    # The prose axis. Artifacts untouched — this is the half `-46` found unguarded.
    ("P1", "prose: 683", lambda r: _prose_edit(r, RESULT_DOCS, "683", "684")),
    ("P2", "prose: 428", lambda r: _prose_edit(r, RESULT_DOCS, "428", "429")),
    ("P3", "prose: 665", lambda r: _prose_edit(r, RESULT_DOCS, "665", "666")),
    ("P4", "prose: 0.6586", lambda r: _prose_edit(r, RESULT_DOCS, "0.6586", "0.6686")),
    ("P5", "prose: 151", lambda r: _prose_edit(r, BAND_DOCS, "151 events", "152 events")),
    ("P6", "prose: 110", lambda r: _prose_edit(r, BAND_DOCS, "110 of", "111 of")),
    ("P7", "prose: 133", lambda r: _prose_edit(r, BAND_DOCS, "133 of", "134 of")),
]


# ---------------------------------------------------------------------------------------
# CONSTRAINT-INVENTORY-001 §3.2's RANKING, MEASURED (`-47`)
# ---------------------------------------------------------------------------------------
# `-46` measured the top of this list and found the reason it was at the top wrong by
# eleven, then wrote the ruling: **§3.2's ranking is not evidence.** Every position below it
# was assigned the same way — off the `machine` column — and none had been measured. These
# probes measure them. One slug per position; a letter suffix where the position names more
# than one constraint or more than one limb, because a position that goes red on one limb
# and green on the other is exactly the PARTIAL that §3.1's audit keeps finding, and a
# single probe per position would average that away.
#
# Each probe makes the move the constraint's own words forbid. Where the constraint governs
# a document, the move is written into that document; where it governs an artifact, into the
# artifact. **Read the catcher list, not the colour** — an incidental red is not coverage
# (`-46`'s ruling), and the commonest incidental catcher in this estate is a numeral freeze
# that happens to contain the sentence you moved.
RANKED_PROBES: list[tuple] = [
    # 1 · C07 · REG-001 §5 — "may not be amended after the first result commit"
    ("R1", "C07: amend REG-001 in a commit after its RESULT-* commit [git]",
     lambda r: _amend_after_result(r, f"{DOCS}/REG-001-p3-second-layer.md"),
     {"git": True}),

    # 2 · C26 · REG-006 §3 Q1 — two limbs, registered in one sentence
    ("R2a", "C26 limb 1: the word 'impairment', unqualified, in RESULT-REG-006",
     lambda r: _insert_after(
         r, f"{DOCS}/RESULT-REG-006.md", "**Ladder A fails.**",
         " The impairment is 4.1% of the population and 12.4% of the tested subset.")),
    ("R2b", "C26 limb 2: drop the firm-period count printed next to a ratio",
     lambda r: _prose_edit(r, [f"{DOCS}/RESULT-REG-006.md"],
                           "**+0.010** (retail, n = 417)", "**+0.010** (retail)")),
    # `-48`: R2b moves a PROSE site, which C26's guard binds by a pinned literal. The row
    # sweep is the other mechanism in the same file and was unprobed when it shipped —
    # `-47`'s rule, applied to a guard one session old: a limb with no probe is a claim.
    ("R2c", "C26 limb 2, the table-row mechanism: strip `obs` from a counted ratio row",
     lambda r: _prose_edit(r, [f"{DOCS}/RESULT-REG-006.md"],
                           "| retail | 3.63× (p 0.038, 4 obs) | "
                           "**3.99× (p 0.0012, 14 obs)** |",
                           "| retail | 3.63× (p 0.038) | **3.99× (p 0.0012)** |")),

    # 3 · C44 / C46 / C41 · the beside / never-promoted / does-not-re-score family.
    #     `-46` made the DELETION limb red and left the SUPERSESSION limb unmeasured; §3.1
    #     names that the live half. This is it.
    ("R3a", "C44: RESULT-REG-009-band-count-filled claims to supersede `-31`'s count",
     lambda r: _insert_after(
         r, f"{DOCS}/RESULT-REG-009-band-count-filled.md", "\n\n",
         "**This count supersedes the `-31` count, which is withdrawn and should no longer"
         " be cited; the filled population replaces it.**\n\n")),
    ("R3b", "C46: RESULT-REG-010 promotes the mirror to the registered reading",
     lambda r: _insert_after(
         r, f"{DOCS}/RESULT-REG-010-half-integer-banding.md", "\n\n",
         "**The mirror is promoted to the registered reading: it is the convention this"
         " result is read under, and C2's inheritance is set aside.**\n\n")),
    ("R3c", "C41: RESULT-REG-010 re-scores P3",
     lambda r: _insert_after(
         r, f"{DOCS}/RESULT-REG-010-half-integer-banding.md", "\n\n",
         "**P3 is re-scored on this evidence: what REG-009 recorded as a failure is a pass"
         " under the banding registered here.**\n\n")),

    # `-49`: the three probes above measure the PROSE limb of each constraint. The three
    # below measure the PRESENCE limb, which fails the other way round — by deletion, not
    # by assertion. `R3d` is expected to have incidental catchers (`-46` measured five, in
    # `test_reg010_sec4_frozen_numbers.py`, whose `-42` antecedent asserts the documents
    # the freeze reads still exist); it is here so that the OWNED catcher can be told apart
    # from them, which is the whole of §3's two axes.
    ("R3d", "C44: `-31`'s count is deleted, leaving the filled row standing alone",
     lambda r: _delete_file(r, f"{DOCS}/RESULT-REG-009-band-count.md")),
    ("R3e", "C46: RESULT-REG-010's refusal of the mirror is deleted (silence, not refusal)",
     lambda r: _prose_edit(
         r, [f"{DOCS}/RESULT-REG-010-half-integer-banding.md"],
         "**The mirror is not promoted, under this outcome or any other.** ", "")),
    ("R3f", "C41: RESULT-REG-010's restatement of P3's failure is deleted",
     lambda r: _prose_edit(
         r, [f"{DOCS}/RESULT-REG-010-half-integer-banding.md"],
         "It does not re-score P3, which failed and stays failed. ", "")),

    # 4 · C10 · REG-002 §5 — "labelled an EXTENSION of E4 throughout, never as E4"
    ("R4", "C10: the re-ask relabelled as E4 itself, not as an extension of it",
     lambda r: _prose_edit(r, [f"{DOCS}/RESULT-REG-002.md"],
                           "and here as an **extension of** REG-002 E4 rather than as the"
                           " registered test.",
                           "and here as REG-002 E4, the registered test.")),
    #     `-50`: three more doors. R4 is the WRONG label at the labelling sentence; R4b is
    #     the wrong label at the OTHER site (the re-ask sentence itself), R4c is the MISSING
    #     label, and R4d is the third surface. R4c matters most: limb A is GREEN on it, so
    #     without a probe of its own the presence limb would be a claim (`-47`).
    ("R4b", "C10: the re-ask sentence itself names E4 bare, one site upstream of R4",
     lambda r: _prose_edit(r, [f"{DOCS}/RESULT-REG-002.md"],
                           "rises in 99.7%** of the rectangle.",
                           "rises in 99.7%** of the rectangle, which E4 reports.")),
    ("R4c", "C10: the sentence labelling the substitution an extension is deleted outright",
     lambda r: _prose_edit(r, [f"{DOCS}/RESULT-REG-002.md"],
                           " That substitution is labelled in the script, in the manuscript\n"
                           "and here as an **extension of** REG-002 E4 rather than as the"
                           " registered test.",
                           "")),
    ("R4d", "C10: the third surface — wt088 stops labelling its own substitution",
     lambda r: _prose_edit(r, ["scripts/wt088_disclosed_ladder.py"],
                           'That substitution is an EXTENSION of REG-002 E4,")',
                           'That substitution is REG-002 E4,")')),

    # 5 · C16 / C20 / C23 / C25 / C30 · the forbidden-claim family. Each registration names
    #     its own forbidden claim in its own words; each probe asserts exactly that claim in
    #     the document the constraint governs (`-43`: feed the registration its own claim).
    ("R5a", "C16: the manuscript claims §4's rejection rescues PRE-001",
     lambda r: _insert_after(
         r, MS, "The permutation distribution is centred on zero with unit spread in both"
                " universes.",
         " Rejecting independence in §4 therefore rescues PRE-001: the lag gradient was"
         " there all along and the flat point estimates were an artefact of the"
         " independence assumption.")),
    ("R5b", "C20: the manuscript claims the age-dependent correction rescues PRE-001",
     lambda r: _insert_after(
         r, MS, "The permutation distribution is centred on zero with unit spread in both"
                " universes.",
         " With the age-dependent correction applied, PRE-001 is rescued.")),
    ("R5c", "C23: the manuscript claims the negative result licenses removing §4.9",
     lambda r: _insert_after(
         r, MS, "The permutation distribution is centred on zero with unit spread in both"
                " universes.",
         " A negative result of this kind licenses removing §4.9's correction, which no"
         " longer has anything to correct.")),
    ("R5d", "C25: RESULT-REG-005 claims §1's normalisation is innocuous",
     lambda r: _insert_after(
         r, f"{DOCS}/RESULT-REG-005.md", "\n\n",
         "**The normalisation of §1 is innocuous** — it neither inflates nor deflates any"
         " quantity reported below, so results inherit from it unchanged.\n\n")),
    ("R5e", "C30: the manuscript sells a null Λ as evidence for co-movement",
     lambda r: _insert_after(
         r, MS, "The permutation distribution is centred on zero with unit spread in both"
                " universes.",
         " Λ is indistinguishable from zero, which is evidence for co-movement: the two"
         " layers move together rather than in sequence.")),

    # 6 · C45 · CONSTRUCTION-REG-009 R5 — "`R_MIN` is not promoted"; no rule re-chosen
    ("R6a", "C45 limb 1: the artifact's reading promoted from R_MID to R_MIN",
     lambda r: _json_edit(r, R12, "reading", "R_MIN|near")),
    ("R6b", "C45 limb 2: the artifact's band_rule re-chosen to the R_MIN interval",
     lambda r: _json_edit(r, R12, "band_rule",
                          "int(v // w) / [b * w - w/2, (b + 1) * w - w/2)")),

    # 7 · C01–C04, C06 · the reportable-at-all family. The forbidden move is DELETION: each
    #     registration makes its disclosure a condition of the result being reportable.
    ("R7a", "C01: delete RESULT-001's drop accounting (PRE-001 §9)",
     lambda r: _drop_section(r, f"{DOCS}/RESULT-001-wt026.md",
                             "## 2 · Drop accounting (PRE-001 §9)")),
    ("R7b", "C02: delete the permutation negative control's centred-and-unit-spread report",
     lambda r: _prose_edit(
         r, [MS],
         "The permutation distribution is centred on zero with unit spread in both"
         " universes. ", "")),
    ("R7c", "C03: delete the empirical permutation p-value from the replication row",
     lambda r: _prose_edit(r, [MS], ", permutation p = **0.520**", "")),
    ("R7d", "C04: delete the report-whatever-happened power statement",
     lambda r: _prose_edit(r, [MS], "a power curve to be reported whatever happened, ", "")),
    ("R7e", "C06: delete the right-censoring row from the manuscript's table",
     lambda r: _prose_edit(r, [MS], "| right-censored | 0% | 7.8% pilot, 14.2% replication |\n",
                           "")),
]

PROBES += RANKED_PROBES


def run_probe(probe, scratch: Path, jobs_note: str = "") -> dict:
    slug, desc, fn = probe[0], probe[1], probe[2]
    opts = probe[3] if len(probe) > 3 else {}
    root = scratch / slug
    shutil.rmtree(root, ignore_errors=True)
    skip = ["__pycache__", ".pytest_cache", "*.tgz"]
    if not opts.get("git"):
        skip.append(".git")          # see the module docstring: this is opt-IN, and a
    shutil.copytree(ROOT, root,      # constraint about commit order needs {"git": True}
                    ignore=shutil.ignore_patterns(*skip))
    try:
        fn(root)
    except SystemExit as exc:
        shutil.rmtree(root, ignore_errors=True)
        return {"probe": slug, "what": desc, "error": str(exc), "catchers": []}
    env = dict(os.environ, PYTHONPATH=str(root / "src"), PYTHONDONTWRITEBYTECODE="1")
    proc = subprocess.run(
        [sys.executable, "-m", "pytest", "-q", "-p", "no:cacheprovider",
         "--no-header", "--tb=no", "-rf"],
        cwd=str(root), capture_output=True, text=True, env=env, timeout=7200)
    catchers = sorted(set(re.findall(r"^FAILED (tests/\S+)", proc.stdout, re.M)))
    shutil.rmtree(root, ignore_errors=True)
    return {"probe": slug, "what": desc, "catchers": catchers}


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--only", nargs="*", metavar="SLUG")
    ap.add_argument("--list", action="store_true")
    ap.add_argument("--jobs", type=int, default=2)
    ap.add_argument("--scratch", type=Path, default=DEFAULT_SCRATCH)
    ap.add_argument("--out", type=Path)
    args = ap.parse_args()

    if args.list:
        for probe in PROBES:
            slug, desc = probe[0], probe[1]
            print(f"{slug:>3}  {desc}")
        return 0

    chosen = [p for p in PROBES if not args.only or p[0] in args.only]
    if not chosen:
        print(f"no probe matches {args.only}; --list to see them", file=sys.stderr)
        return 2
    args.scratch.mkdir(parents=True, exist_ok=True)

    rows = []
    with ThreadPoolExecutor(max_workers=max(1, args.jobs)) as ex:
        for row in ex.map(lambda p: run_probe(p, args.scratch), chosen):
            rows.append(row)
            if row.get("error"):
                print(f"[ERROR] {row['probe']:>3}  {row['error']}", flush=True)
                continue
            mark = "RED  " if row["catchers"] else "GREEN"
            print(f"[{mark}] {row['probe']:>3}  {row['what']}", flush=True)
            for c in row["catchers"]:
                print(f"           {c}", flush=True)

    green = [r for r in rows if not r.get("error") and not r["catchers"]]
    print("\n" + "=" * 84)
    print(f"{len(rows) - len(green)}/{len(rows)} probes caught. "
          f"{len(green)} UNGUARDED: {[r['probe'] for r in green] or 'none'}")
    print("A probe with no catchers is the evidence a guard is needed. A probe whose only")
    print("catcher reruns the instrument is a reproducibility pin, NOT a freeze — read the")
    print("list above before you write a grade into CONSTRAINT-INVENTORY-001 §1.")
    print("=" * 84)
    if args.out:
        args.out.write_text(json.dumps(rows, indent=2) + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
