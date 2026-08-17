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
history to run the suite. It does need history to be **measured**: fourteen tests in this estate
skip with *"not a git work tree"*, and one of them is the only machine anywhere near C07,
which §3.2 ranked **first** in cell (b). A C07 probe run under the original harness would have
come back GREEN and the green would have meant *the harness deleted the guard*, not *no guard
exists*.

**THAT MACHINE IS `test_reg001_sec5_no_amendment_after_result.py`, AND THIS PARAGRAPH NAMED
THE WRONG FILE FOR FOUR SESSIONS.** It said `test_registrations_precede_their_instruments.py`
— a guard on a different invariant, whose own docstring says *"it cannot see a registration
edited after its result existed"*, which is precisely C07. `-47` diagnosed exactly that
confusion and corrected it in `CONSTRAINT-INVENTORY-001` §2b (*"the row inherited the file
because the names rhymed"*) — and left the identical claim standing HERE, in the file the
handoff's ORIENT list tells every session to read *before it grades anything*. `-50` read it,
believed it, and wrote it into its pre-measurement of the git axis; `-51` ran `R1` and
measured the catcher: `test_reg001_sec5_no_amendment_after_result.py::
test_the_registration_was_not_amended_after_its_result_commit`, alone.

**A CORRECTION APPLIED TO ONE ARTEFACT WHILE A SECOND ASSERTS THE SAME CLAIM IS A CORRECTION
WITH A LIVE RESERVOIR**, and the reservoir is usually the instrument, because the estate
grades documents and reads instruments. `-50`'s rule was *edit the artefact, not just the
handoff*; the corollary is **grep the CLAIM, not the file**. Note what did NOT catch this:
the residual count was right. `-50` computed 13 = 14 − 1 by running the command, and the
subtraction is correct no matter which test the 1 is; **a right total is what makes a wrong
attribution invisible.**

That is `-37`'s tell one level up: **a mutation that the harness cannot see reports every
guard in the unseen part of the estate as absent.** So `.git` is copied on request, and a
probe whose constraint is about commit order MUST set `{"git": True}` or it is measuring
nothing. The same finding retired the two-tarball cloud stanza: a source tarball without
`.git` drops exactly the axis nobody had probed.

**DO NOT QUOTE A COUNT OF THEM FROM MEMORY — RUN IT.** `-47` wrote *"nine tests"* and it was
true; at `142d386` it is **fourteen, across six files**, because the suite grew and nobody
recomputed (`-46`'s tell, fifth session running). The count is one command:

    rm -rf /tmp/nogit && cp -r . /tmp/nogit && rm -rf /tmp/nogit/.git \\
      && (cd /tmp/nogit && PYTHONPATH=$PWD/src python3 -m pytest -q -rs | grep '^SKIPPED')
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

#: How a red is recognised in pytest's short summary. **`ERROR` is not optional.** A probe
#: that mutates a MODULE breaks an import; pytest reports those files as `ERROR`, not
#: `FAILED`, and past a handful it stops at collection having run no test at all. `-51`
#: found this reading `FAILED` only, which made a suite that would not even collect arrive
#: as an EMPTY catcher list — printed as GREEN, whose documented meaning in this file is
#: *no guard exists*. The instrument was anti-monotonic in severity: the worse the damage,
#: the cleaner the green. `tests/test_mutation_control_reads_errors.py` pins both halves.
CATCHER_RE = re.compile(r"^(?:FAILED|ERROR) (tests/\S+)", re.M)


def is_unparsed_red(returncode: int, catchers: list) -> bool:
    """True when the run did not complete AND nothing was attributable.

    pytest exits 0 (all passed) or 1 (tests failed); 2 is interrupted-or-collection-error,
    3 internal, 4 usage. Any of the latter with no parsed catcher means the probe measured
    NOTHING, and the one thing it must never be called is green.
    """
    return returncode not in (0, 1) and not catchers



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
GUARD = "tests/test_reg012_sec6_sec47_frozen.py"
PAPER_I = "docs/papers/paper-I-price-formation/paper-I.md"
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


# ------------------------------------------------------------------ git-axis helpers (-51)
def _git_commit(root: Path, msg: str, *paths: str):
    """Stage the named paths and commit. The probe identity is fixed so that a scratch
    tree left behind by a crash is legible as a probe's work and not as somebody's."""
    _git(root, "add", "--", *paths)
    _git(root, "-c", "user.name=mutation-probe", "-c", "user.email=probe@invalid",
         "commit", "-q", "-m", msg)


def _git_mv_commit(root: Path, src_rel: str, dst_rel: str, msg: str):
    """Rename a tracked path and commit it.

    The forbidden move behind four of the git-axis guards: a document renamed out from
    under a ledger, a pin, an ancestry check, or a scan. It is one move in the sense that
    matters — a session does it in one `git mv` — and it is a HISTORY move, not a tree
    edit, which is why every probe using it needs `{"git": True}`.
    """
    if not (root / src_rel).exists():
        raise SystemExit(f"PROBE SITE MISSING: {src_rel}")
    _git(root, "mv", src_rel, dst_rel)
    _git(root, "-c", "user.name=mutation-probe", "-c", "user.email=probe@invalid",
         "commit", "-q", "-m", msg)


def _register_with_instrument(root: Path):
    """G1 - a registration and its own instrument in ONE commit: the PRE-001/PRE-002 move.

    The registration's text says "registered alone", exactly as `REG-008`'s commit subject
    did, so the probe reproduces the shape the ledger records and not a strawman.
    """
    reg = f"{DOCS}/REG-099-probe-registration.md"
    code = "scripts/reg099_probe.py"
    (root / reg).write_text(
        "# REG-099 - probe registration\n"
        "\n"
        "Registered alone, ahead of any instrument.\n")
    (root / code).write_text(
        "# the instrument this registration says it does not have\n")
    _git_commit(root, "REG-099: the probe registration, registered alone", reg, code)


def _unignore_backups(root: Path):
    """G4 - strip the *.bak patterns from .gitignore: the exact state `-47` found."""
    p = root / ".gitignore"
    text = p.read_text()
    keep = [ln for ln in text.split("\n")
            if ln.strip() not in ("*.bak", "*.bak[0-9]", "*.bak-*")]
    out = "\n".join(keep)
    if out == text:
        raise SystemExit("PROBE SITE MISSING: no *.bak patterns in .gitignore")
    p.write_text(out)


def _track_a_backup(root: Path):
    """G5 - force one backup into the index.

    `.gitignore` is left alone on purpose. Ignoring and not-tracking are two facts, the
    test file asserts both, and a probe that changed the ignore rules would be measuring
    G4's limb instead of this one.
    """
    baks = sorted(q for q in root.rglob("*.bak*")
                  if q.is_file() and ".git/" not in str(q))
    if not baks:
        raise SystemExit("PROBE SITE MISSING: no *.bak* on disk to track")
    rel = str(baks[0].relative_to(root))
    _git(root, "add", "-f", "--", rel)
    _git(root, "-c", "user.name=mutation-probe", "-c", "user.email=probe@invalid",
         "commit", "-q", "-m", "chore: sweep in a backup")


def _delete_all_backups(root: Path):
    """G6 - the non-vacuity move: somebody tidies the backups away and the ignore guard
    starts passing over an empty set."""
    baks = [q for q in root.rglob("*.bak*") if q.is_file() and ".git/" not in str(q)]
    if not baks:
        raise SystemExit("PROBE SITE MISSING: no *.bak* on disk to delete")
    for q in baks:
        q.unlink()


def _touch_pinned_file(root: Path):
    """G7 - commit a change to a pinned module: the PIN-001 defect, reintroduced."""
    rel = "src/wealth_tensor/edgar.py"
    p = root / rel
    p.write_text(p.read_text()
                 + "\n# a later edit that the manuscript does not disclose\n")
    _git_commit(root, "edgar: an edit after the pin", rel)


def _edit_tier_tags(root: Path):
    """G8 - edit a tag INSIDE the registered TIER_TAGS block: what PRE-001 forbids without
    an amendment, and what §11's published digest exists to make impossible in silence.

    THE MOVE IS DELIBERATELY NARROW, AND `-51`'s FIRST DRAFT WAS NOT. Renaming the block
    (`TIER_TAGS:` -> something else) also turns it red, but for the wrong reason: three
    modules reference `TIER_TAGS` by name, the import dies, pytest stops at COLLECTION, and
    the catcher list comes back as two file-level import errors with the digest guard never
    having run at all. A mutation big enough to stop the suite cannot tell you which guard
    saw it. Change one registered tag string and the module still imports, so the digest
    guard gets its turn - which is the whole measurement.
    """
    rel = "src/wealth_tensor/edgar.py"
    p = root / rel
    text = p.read_text()
    old_tag = '"ImpairmentOfLeasehold"'
    if "TIER_TAGS: " not in text or old_tag not in text:
        raise SystemExit("PROBE SITE MISSING: TIER_TAGS block or its tier-0 tag")
    p.write_text(text.replace(old_tag, '"ImpairmentOfLeaseholdProbe"', 1))


def _retarget_a_pin(root: Path):
    """G9 - point a §11 pin at a real commit that never touched that file.

    `8cdf78e` is a docs-only commit in this repository's history: it resolves, so the pin
    still LOOKS like a pin, which is the failure mode worth probing. A garbage hex string
    would be caught by something cheaper.
    """
    rel = "scripts/wt099_edits_pin001.py"
    p = root / rel
    text = p.read_text()
    old = '"src/wealth_tensor/lag.py": "ad779eb"'
    if old not in text:
        raise SystemExit(f"PROBE SITE MISSING: {old}")
    p.write_text(text.replace(old, '"src/wealth_tensor/lag.py": "8cdf78e"', 1))


def _orphan_sha_in_manuscript(root: Path):
    """G11 - write a real commit SHA into the paper that no instrument names.

    This is the PIN-001 CLASS rather than the instance: the SHA resolves, so it reads as a
    pin, and nothing in the repository is watching it.

    THE SHA IS CHOSEN AT RUN TIME AND DELIBERATELY NOT WRITTEN DOWN HERE. `-51`'s first
    draft named one in this docstring and the probe came back GREEN, correctly: the guard
    asks whether the SHA appears anywhere under scripts/, tests/ or src/, and this file is
    under scripts/. **A probe whose forbidden move is "introduce an identifier no
    instrument names" cannot name the identifier, because the harness lives inside the
    estate it mutates.** Writing the literal is what falsifies the probe's own premise.
    """
    _orphan_sha_in(root, MS)


def _orphan_sha_in(root: Path, rel: str):
    """`G11`'s forbidden move, aimed at whichever manuscript is named.

    Extracted by `-65` so `G16` can make the identical move in a different paper without
    the harness carrying two copies of it — which would be the PIN-001 shape arriving in
    the instrument that probes for the PIN-001 shape.
    """
    text = (root / rel).read_text()
    instruments = "\n".join(
        q.read_text(encoding="utf-8", errors="ignore")
        for d in ("scripts", "tests", "src")
        for q in sorted((root / d).rglob("*.py"))
    )
    picked = None
    for line in subprocess.run(
            ["git", "log", "--format=%h", "-60"], cwd=str(root),
            capture_output=True, text=True).stdout.split():
        if (len(line) >= 7 and any(c.isdigit() for c in line)
                and any(c in "abcdef" for c in line)
                and line not in instruments and line not in text):
            picked = line
            break
    if picked is None:
        raise SystemExit("PROBE SITE MISSING: no commit is absent from every instrument")
    i = text.find("\n## ", len(text) // 2)
    if i < 0:
        raise SystemExit(f"PROBE SITE MISSING: no mid-document heading in {rel}")
    claim = f"\n\nThe analysis in this section was produced at commit {picked}.\n"
    (root / rel).write_text(text[:i] + claim + text[i:])


def _orphan_sha_in_paper_i(root: Path):
    """G16 - the same move as G11, in a manuscript the OLD instrument could not see.

    `test_manuscript_shas_are_instrumented.py` hardcoded paper III until `-65`. Its own
    docstring said it repaired the CLASS; it touched one file of four, and `-64` found the
    shape alive in paper IV. Against a tree where that instrument is still a constant this
    probe is GREEN, and the green is the finding. Against this commit it is RED.

    Paper I is chosen deliberately: it is the manuscript that pins NOTHING today, so a
    catcher here cannot be an accident of some other guard already watching its SHAs.
    """
    _orphan_sha_in(root, PAPER_I)


def _rename_prereg_dir(root: Path):
    """G12 - the convention change the registration scan's non-vacuity guard exists to
    catch. Deliberately broad: see the note above `GIT_PROBES` about what its catcher
    list is and is not evidence of."""
    _git_mv_commit(root, "docs/preregistration", "docs/prereg-archive",
                   "docs: move the registrations under a new convention")


def _edit_sec_47_today(root: Path):
    """G13 - edit manuscript §4.7 at HEAD, after REG-012 froze it.

    The REG-012 digest pin reads the blob at `ba59370`, not the working tree. This probe
    exists to MEASURE whether that pin can see a present-day edit at all - `-46`'s
    question (is this a freeze or a reproducibility pin?) asked of a pin whose subject is
    immutable history. Read its catcher list for which test actually owns the freeze.
    """
    p = root / MS
    text = p.read_text()
    m = re.search(r"^### 4\.7 · .*$", text, re.M)
    if not m:
        raise SystemExit("PROBE SITE MISSING: no §4.7 heading in the manuscript")
    j = text.find("\n", m.end()) + 1
    p.write_text(text[:j] + "\nThis section is edited after REG-012 froze it.\n" + text[j:])


def _launder_reading_a(root: Path):
    """G14 - edit §4.7 AND record an amendment whose licence is REG-012's own outcome.

    `-65` replaced the single `SEC_47_SHA256` with a registration anchor, a current digest
    and an `AMENDMENTS` ledger, because the old file's prescribed remedy - re-pin in the same
    commit - was forbidden by its own sibling test and could be executed zero times. A ledger
    that records warranted edits opens a door the freeze did not have: write the violation
    down and it becomes a record instead of a violation. This probe walks through that door.
    `G13` cannot express it, because `G13` predates the ledger.
    """
    _edit_sec_47_today(root)
    p = root / GUARD
    text = p.read_text()
    old = "AMENDMENTS: tuple[Amendment, ...] = ("
    if old not in text:
        raise SystemExit("PROBE SITE MISSING: no AMENDMENTS ledger in the REG-012 guard")
    entry = (
        "AMENDMENTS: tuple[Amendment, ...] = (\n"
        "    Amendment(\n"
        '        sha="HEAD",\n'
        "        licence=(\n"
        "            \"REG-012's outcome licenses this edit, padded well past the length \"\n"
        '            "floor so that only the citation limb can possibly catch it."\n'
        "        ),\n"
        '        digest_after="' + "0" * 64 + '",\n'
        "    ),\n"
    )
    p.write_text(text.replace(old, entry, 1))


def _repin_the_registration_anchor(root: Path):
    """G15 - move `SEC_47_AT_REGISTRATION`, which the guard declares immutable.

    The forbidden move the OLD file's own red message invited: it told the next session to
    re-pin, and the only way to make a one-constant guard green after a legitimate edit was
    to point the freeze at today. That is a snapshot wearing a freeze's clothes - `-43`'s own
    words for it, in a file that then made it the prescribed remedy. The anchor is a fact
    about `ba59370`; this probe asserts a session cannot quietly make it a fact about now.
    """
    p = root / GUARD
    text = p.read_text()
    anchor = 'SEC_47_AT_REGISTRATION = "'
    if anchor not in text:
        raise SystemExit("PROBE SITE MISSING: no SEC_47_AT_REGISTRATION in the REG-012 guard")
    head, _, rest = text.partition(anchor)
    _old, _, tail = rest.partition('"')
    p.write_text(head + anchor + "0" * 64 + '"' + tail)


# --------------------------------------------------------------------------- THE GIT AXIS
# `-47` found that a harness which deletes `.git` reports every git-gated guard as ABSENT.
# `.git` became opt-in and exactly ONE probe (`R1`) ever set it. Fourteen tests in this
# suite skip without a work tree and `R1` spends one of them; **these probe the other
# thirteen**, which had never had a mutation run against them. Until this file, that axis
# was the only place the estate had proof its instrument was blind.
#
# EVERY probe here sets `{"git": True}`. Without it the scratch copy has no history, the
# thirteen skip, and the probe measures nothing while printing a green. That is `-47`'s
# ruling and it is the whole reason this axis stayed dark for four sessions.
#
# TWO OF THE THIRTEEN ARE NOT ISOLABLE BY A SINGLE MOVE, AND THAT IS A MEASUREMENT.
# `G12` (the registration scan's non-vacuity guard) and `G13` (REG-012's historical digest
# pin) are here to establish WHY, not to earn a grade. Read their catcher lists as
# evidence about the guard's reach, never as coverage - `-46`'s ruling.
GIT_PROBES: list[tuple] = [
    ("G1", "commit a registration together with its own instrument [git]",
     _register_with_instrument, {"git": True}),
    ("G2", "rename a ledgered registration out from under KNOWN_VIOLATIONS [git]",
     lambda r: _git_mv_commit(r, f"{DOCS}/PRE-002-wt026-peak-to-charge.md",
                              f"{DOCS}/PRE-002-renamed.md",
                              "docs: rename PRE-002"),
     {"git": True}),
    ("G3", "rename REG-010, the instance asserted to have been registered alone [git]",
     lambda r: _git_mv_commit(r, f"{DOCS}/REG-010-p3-half-integer-banding.md",
                              f"{DOCS}/REG-010-renamed.md",
                              "docs: rename REG-010"),
     {"git": True}),
    ("G4", "drop the *.bak patterns from .gitignore [git]",
     _unignore_backups, {"git": True}),
    ("G5", "git add -f a backup into the index [git]",
     _track_a_backup, {"git": True}),
    ("G6", "delete every *.bak, emptying the set the ignore guard scans [git]",
     _delete_all_backups, {"git": True}),
    ("G7", "commit an edit to a pinned module after the pin [git]",
     _touch_pinned_file, {"git": True}),
    ("G8", "edit the registered TIER_TAGS block [git]",
     _edit_tier_tags, {"git": True}),
    ("G9", "retarget a §11 pin at a commit that never touched that file [git]",
     _retarget_a_pin, {"git": True}),
    # G10 is an ESTABLISHING probe, like G13: it is expected GREEN and the green is the
    # measurement. See the note above and the docstring it corrected.
    ("G10", "rename RESULT-REG-001 — establishes that a rename does NOT empty "
            "rev-list, so the non-vacuity guard is unreachable from the tree [git]",
     lambda r: _git_mv_commit(r, f"{DOCS}/RESULT-REG-001.md",
                              f"{DOCS}/RESULT-REG-001-renamed.md",
                              "docs: rename RESULT-REG-001"),
     {"git": True}),
    ("G11", "write an uninstrumented commit SHA into the manuscript [git]",
     _orphan_sha_in_manuscript, {"git": True}),
    ("G12", "move docs/preregistration to a new naming convention [git]",
     _rename_prereg_dir, {"git": True}),
    ("G13", "edit manuscript §4.7 at HEAD, after REG-012 froze it [git]",
     _edit_sec_47_today, {"git": True}),
    ("G14", "record REG-012's own outcome as an amendment licence, laundering "
            "reading (a) into the ledger [git]",
     _launder_reading_a, {"git": True}),
    ("G15", "re-pin SEC_47_AT_REGISTRATION, the constant the guard calls immutable [git]",
     _repin_the_registration_anchor, {"git": True}),
    ("G16", "write an uninstrumented commit SHA into PAPER I — the move G11 makes in "
            "paper III, aimed where the instrument was blind until -65 [git]",
     _orphan_sha_in_paper_i, {"git": True}),
]

PROBES += GIT_PROBES


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
         "--no-header", "--tb=no", "-rfE"],
        cwd=str(root), capture_output=True, text=True, env=env, timeout=7200)
    # `-rfE`, not `-rf`. A mutation to a MODULE breaks an import, pytest reports the
    # affected files as ERROR rather than FAILED, and with enough of them it stops at
    # collection and never runs a test at all. `-51` found the harness reading only
    # `FAILED` lines, which made the LOUDEST possible red — a suite that will not even
    # collect — arrive as an empty catcher list, i.e. as `UNGUARDED`. The instrument was
    # anti-monotonic in severity: the worse the damage, the cleaner the green.
    catchers = sorted(set(CATCHER_RE.findall(proc.stdout)))
    # The belt to that suspenders. Anything other than pytest's 0 (all passed) or 1 (tests
    # failed) means the run did not complete normally — 2 is interrupted/collection error,
    # 3 internal, 4 usage. If we ALSO parsed no catchers, the probe measured nothing and
    # must never be graded as a green. Report it, loudly, as its own state.
    unparsed = is_unparsed_red(proc.returncode, catchers)
    shutil.rmtree(root, ignore_errors=True)
    return {"probe": slug, "what": desc, "catchers": catchers,
            "rc": proc.returncode, "unparsed_red": unparsed}


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
            if row.get("unparsed_red"):
                # NOT a green. The suite did not finish and nothing was parseable; the
                # probe measured nothing. `-51`: this state used to print as GREEN.
                print(f"[UNPARSED RED] {row['probe']:>3}  {row['what']}", flush=True)
                print(f"           pytest exited {row['rc']} with no FAILED/ERROR lines "
                      f"— the run did not complete. This is NOT evidence of an unguarded "
                      f"constraint; it is evidence the probe broke the suite in a way "
                      f"this harness cannot attribute. Narrow the move and re-run.",
                      flush=True)
                continue
            mark = "RED  " if row["catchers"] else "GREEN"
            print(f"[{mark}] {row['probe']:>3}  {row['what']}", flush=True)
            for c in row["catchers"]:
                print(f"           {c}", flush=True)

    unparsed = [r for r in rows if r.get("unparsed_red")]
    green = [r for r in rows
             if not r.get("error") and not r["catchers"] and not r.get("unparsed_red")]
    print("\n" + "=" * 84)
    print(f"{len(rows) - len(green) - len(unparsed)}/{len(rows)} probes caught. "
          f"{len(green)} UNGUARDED: {[r['probe'] for r in green] or 'none'}")
    if unparsed:
        print(f"{len(unparsed)} UNPARSED RED (measured nothing, NOT green): "
              f"{[r['probe'] for r in unparsed]}")
    print("A probe with no catchers is the evidence a guard is needed. A probe whose only")
    print("catcher reruns the instrument is a reproducibility pin, NOT a freeze — read the")
    print("list above before you write a grade into CONSTRAINT-INVENTORY-001 §1.")
    print("=" * 84)
    if args.out:
        args.out.write_text(json.dumps(rows, indent=2) + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
