#!/usr/bin/env python3
"""wt159 · re-adjudicate every row wt156 flags, with evidence a reader can run TODAY.

wt156 flags 46 of the 129 adjudicated rows: 36 under D1 (the evidence's account of where the
result lives is a session, a log, or a machine that is not in the repository) and 10 under D2
(the evidence is a verb or a back-reference with no operand).  Step 1 of the file's own
falsification procedure — *take the evidence column; it names a command to run or a file to
read* — could not be carried out on any of them.

Every replacement `evidence` below is a command that was RUN on darwin on 2026-08-18, and every
replacement `note` carries the value that came back THAT DAY.  Three notes were found to be wrong
and are corrected here rather than reproduced:

  · d9f85198a4 / ff83025f93 — the shared note said "RESULT-001-* logs entered at d655501 and the
    analysed result later".  RESULT-001-wt026.md is IN d655501.  PRE-002's own outcome,
    RESULT-002-wt026.md, is the one that came later, at c43c484, twelve minutes on.  Both
    SENTENCES hold; the note conflated two results.
  · 150f86a167 — the note put "written before the leg ran" in E1 §2.2.  §2.2 is the type check;
    §6 is where "the FAIL branch of the design's E1 table, written before the run" appears.  The
    sentence holds; the note mis-assigned the section.
  · d4dd6baf17 — the note said "a clean run would not regenerate §6 either".  A clean run on
    2026-08-18 returned RC 0 and every figure §6 reports, unchanged.  Repaired in the manuscript
    by scripts/wt157_paperIV_s10_reg013_rerun.py.

One SENTENCE was found false and is repaired by scripts/wt158_twelve_point_four.py: §10 said
tests/test_excess_demand.py ASSERTS §8's twelve-point four, and the module asserted no such thing.
It does now, so 30191fec1a and 10d2d456ea are true rather than weaker.

RC 0 repaired · RC 2 refused or rolled back (from .bak-wt159).
"""

import json
import shutil
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
TSV = REPO / "docs/promises-adjudicated.tsv"
BAK = Path(str(TSV) + ".bak-wt159")
COLUMNS = ("paper", "promise_id", "artefact", "class", "evidence", "note", "sentence")

D = "2026-08-18"

# promise_id -> (evidence, note)   — evidence is runnable; note is what it returned on D
REPAIRS = {
    # ---------------- the sixteen: `run on darwin, wealthTensor-82; output in the session log`
    "ac16838bdb": (
        "`python3 scripts/wt027_report.py` re-run " + D + " (RC 0)",
        "RC 0, and the output carries exactly the five blocks the bullet enumerates: A the filter "
        "in isolation, A' §3.1's prose-only figures (phi=0.9 -> 199.8990, phi=0.1 -> 1799.0906, "
        "D(0)=1998.9895 at phi=0.0), B the full-path volatility ratios (0.93 / 2.71 / 3.27), C the "
        "entropy-rate sweep, D the sawtooth. Same five blocks and same figures as the "
        "wealthTensor-82 run"),
    "d6c6430592": (
        "`python3 scripts/wt002_lambda_report.py` re-run " + D + " (RC 0)",
        "RC 0; the output sweeps the coupling over twelve orders (1e-06 to 4.2e+01 against an "
        "energy scale of 6.02e+23) and closes with 'collapses_onto(A, B): True' -- §A.2.3's "
        "twelve-orders sweep, regenerated today"),
    "314390a26e": (
        "`python3 scripts/wt026_severe_test.py --universe pilot --onset peak` re-run " + D + " (RC 0)",
        "RC 0, and its drop accounting reports 'firms with facts fetched 672' -- it re-pulls "
        "companyfacts, so it reproduces the instrument and not the sample, which is what the "
        "bullet's own text says"),
    "f7674cbd06": (
        "`python3 scripts/wt089_recognition_and_offdiagonal.py` re-run " + D + " (RC 0)",
        "RC 0; §3 A1 POOLED n=695 d=613 alpha_yr=0.4077 [0.3827,0.4319], A2 discrete Weibull "
        "k=1.210 [1.135,1.285], the off-diagonal lifts 4.12x and 2.02x at p=0.0002 and the power "
        "curve 1.00 at pi=0.05; and its §2 reconciles the rebuild against RESULT-002 (688 against "
        "a rebuilt 695, agreement 99.0%) before computing a statistic, exactly as the bullet says"),
    "070d5c7a60": (
        "`python3 scripts/wt026_severe_test.py --universe pilot --onset peak` re-run " + D +
        " then `grep -ci 'recognition rate\\|off-diagonal'` on its output",
        "the grep returns 0: wt026's output contains no recognition rate and no off-diagonal "
        "figure. -81's IV-1 finding stated from the other side, and still true on a run made today"),
    "6d9934a0bc": (
        "`python3 -m pytest tests/ -q` re-run " + D + " (RC 0)",
        "1095 passed, 0 failed at wealthTensor-86's HEAD (1090 at 73b77f9 when wealthTensor-82 ran "
        "it; the HEAD suite grows, and wt158 added one). The sentence's 100 and 62 are about the "
        "PINNED commit d655501, which tests/test_paper_test_counts_are_derived.py asserts"),
    "a01f12e7be": (
        "`python3 scripts/wt089_recognition_and_offdiagonal.py` re-run " + D + " (RC 0), §4",
        "4.12x and 2.02x, both two-sided p = 0.0002, and a power curve reading 1.00 at pi = 0.05 "
        "-- every figure unchanged from the wealthTensor-82 run. RESULT-REG-006 carries the "
        "tag-list-repaired 4.01x/2.10x survival"),
    "d4dd6baf17": (
        "`python3 scripts/reg013_citation_whitespace.py` re-run " + D +
        " (RC 0); output committed at docs/preregistration/RESULT-REG-013-rerun-2026-08-18.json",
        "FAILED AS WRITTEN. §10 said 'Regenerate §6:' and named this command; the committed record "
        "(RESULT-REG-013-run.log/.json) was named nowhere in §10. Repaired in-pass by "
        "scripts/wt150_paperIV_reg013_record.py. NOTE CORRECTED AT wealthTensor-86: the prior note "
        "said 'a clean run would not regenerate §6 either', and a clean run on " + D + " returned "
        "RC 0 with every figure §6 reports unchanged -- 23/15/6, 0.0202/0.0108/0.0053, 134/155/380, "
        "P_ceiling 0.4773, F_floor 0.0, H1 SURVIVES -- only the seed cited_by counts had moved. "
        "scripts/wt157_paperIV_s10_reg013_rerun.py repaired §10 to say replication, not regeneration"),
    "c14cdd1f1b": (
        "`python3 -m pytest tests/ -q` re-run " + D + " (RC 0)",
        "1095 passed, 0 failed at wealthTensor-86's HEAD (1090 at 73b77f9 when wealthTensor-82 ran it)"),
    "f8f41df587": (
        "`python3 scripts/wt030_report.py` re-run " + D + " (RC 0)",
        "RC 0; it prints the redistribution table (thr=2.00x Gini=0.589, 5.00x 0.675, 20.00x 0.770, "
        "bounded=True throughout) and the flow-base kappa residual against r*E[eta+], so it does "
        "regenerate redistribution.py's figures as the bullet claims"),
    "e91d103026": (
        "`python3 scripts/wt027_report.py` re-run " + D + " (RC 0)",
        "RC 0, five blocks A / A' / B / C / D, with D(0)=1998.9895 printed in A' -- lag.py's "
        "figures, regenerated today"),
    "4c35bb44b7": (
        "`python3 scripts/wt002_lambda_report.py` re-run " + D + " (RC 0)",
        "RC 0; ends 'collapses_onto(A, B): True' after the twelve-orders sweep -- "
        "lambda_sensitivity.py's figures, regenerated today"),
    "12dc448265": (
        "`python3 scripts/wt089_recognition_and_offdiagonal.py` re-run " + D + " (RC 0), §4",
        "RC 0 and it does print all four: 4.12x, 2.02x, two-sided p = 0.0002, and the power curve "
        "at pi = 0.05 -> 1.00. -81's repair holds, and the four numbers are byte-identical today"),
    "41744fe2ae": (
        "`python3 scripts/wt026_severe_test.py --universe pilot --onset peak` re-run " + D +
        " then grep for 4.12, 2.02 and 0.0002 in its output",
        "RC 0 and the grep finds none of them -- the negative claim the bullet makes about this "
        "command is true on a run made today"),
    "10d2d456ea": (
        "`python3 -m pytest tests/test_excess_demand.py -q` re-run " + D +
        " (RC 0) + `grep -n 'assert' tests/test_excess_demand.py`",
        "11 passed. The module ASSERTS rather than prints: L70 'assert grid.size == 399' for §5's "
        "interior grid, L118 the 500-point monotonicity sweep, and (added at wealthTensor-86 by "
        "scripts/wt158_twelve_point_four.py, because it was NOT there before) an assertion that "
        "the twelve-point grid returns exactly 4 distinct excess-demand schedules -- §8's number. "
        "So the command's output is a verdict and not a table, as the bullet says"),
    "a00820b165": (
        "`python3 scripts/wt071_refuter.py` re-run " + D + " (RC 0)",
        "RC 0; it prints the crossing-height identity across the 25 allocations with the "
        "locked-in-holders control and ends 'WT-071 SEVERITY: 9 severe - 0 definitional - 0 "
        "failed/vacuous' -- the same three counts as the wealthTensor-82 run"),

    # ---------------- the seventeen: `git log/cat-file on darwin, wealthTensor-82`
    "988f2c17eb": (
        "`git show --name-only --format= 9722342`",
        "returns exactly one path, docs/preregistration/PRE-001-wt026-observability-lag.md. "
        "Committed alone, as claimed"),
    "c8ce16780e": (
        "`git cat-file -t 9722342` + `git log -1 --format='%h %ad %s' --date=iso 9722342`",
        "commit; 9722342 2026-08-05 17:11:01 -0500 'PRE-001: pre-register the WT-026 severe test, "
        "before any lag is computed'; and git show --name-only lists one file"),
    "d9f85198a4": (
        "`git show --name-only --format= d655501`",
        "d655501's file list contains BOTH docs/preregistration/PRE-002-wt026-peak-to-charge.md "
        "and scripts/wt026_severe_test.py -- the registration shipped in the same commit as the "
        "implementation of the instrument, which is what the sentence claims. (The prior note said "
        "'RESULT-001-* logs entered at d655501 and the analysed result later'; RESULT-001-wt026.md "
        "is IN d655501. PRE-002's own outcome came later -- see ff83025f93.)"),
    "6d3081f7d0": (
        "`git cat-file -t d655501` + `git log -1 --format='%h %ad %s' --date=iso d655501`",
        "commit; d655501 2026-08-05 17:46:52 -0500 'WT-026 severe test: the prediction FAILS on "
        "both registered universes'"),
    "ff83025f93": (
        "`git log -1 --format='%h %ad' --date=iso d655501` + `git log --format='%h %ad %s' "
        "--date=iso -- docs/preregistration/RESULT-002-wt026.md`",
        "PRE-002 registered at d655501 2026-08-05 17:46:52; PRE-002's outcome "
        "RESULT-002-wt026.md has exactly one commit, c43c484 2026-08-05 17:58:10 'PRE-002 also "
        "fails -- with power. Stopping rule fired; WT-026 closed.' Twelve minutes later, so the "
        "result did come at a subsequent commit, as the sentence says"),
    "e982f4354d": (
        "`git log -1 --format='%h %ad' --date=iso -- "
        "docs/preregistration/REG-003-p3-recognition-rate-and-off-diagonal.md` + `git log "
        "--reverse --format='%h %ad' --date=iso -- scripts/wt089_recognition_and_offdiagonal.py`",
        "REG-003 registered at b088cc8 2026-08-12 12:57:06; the instrument first appears at "
        "0569ab6 2026-08-12 13:37:24 -- 40 minutes later. Two questions, both returned"),
    "b027807bb2": (
        "`git cat-file -t cc1d198` + `git log -1 --format='%h %ad %s' --date=iso cc1d198` + "
        "`git show --name-only --format= cc1d198`",
        "commit; cc1d198 2026-08-12 12:23:01 -0500 'REG-002 results, errata, ledger WT-088, and "
        "three tests S4.4 needed'; the file list is four paths and includes tests/test_lag.py"),
    "f0e2d9c802": (
        "`git show --name-only --format= 9722342 | wc -l`",
        "1 -- a single-file commit containing the registration and nothing else; the ledger entry "
        "is at docs/LEDGER.md L1188"),
    "a1e418ec3d": (
        "`git show --name-only --format= d655501 | grep wt026_severe_test`",
        "returns scripts/wt026_severe_test.py, which is in d655501's nine-path file list -- the "
        "commit does also contain the implementation, which is the disclosure the bullet points "
        "§5.1 at"),
    "08661953ec": (
        "`git cat-file -t ad779eb` + `git log --format='%h' -- src/wealth_tensor/lag.py`",
        "commit; ad779eb 2026-08-05 07:05:36 'lag: reporting layer as a filter'; and the log over "
        "that path returns ad779eb and nothing else, so it is that file's only commit, as the "
        "parenthesis claims"),
    "3de6bdab52": (
        "`git cat-file -t b9089c7` + `git log -1 --format='%h %ad %s' --date=iso b9089c7`",
        "commit; b9089c7 2026-08-05 09:24:36 -0500 'lambda_sensitivity: WT-002 item 4 - the "
        "numeraire cancels, demonstrated across 12 orders of magnitude'"),
    "9add6ff45d": (
        "`git cat-file -t 93a159b` + `git show --name-only --format= 93a159b | grep edgar`",
        "commit; 93a159b 2026-08-13 05:02:50 -0500, the REG-006 commit; the grep returns "
        "src/wealth_tensor/edgar.py -- the post-pin move the sentence discloses"),
    "e1e02600e0": (
        "`git cat-file -t 0569ab6` + `git show --name-only --format= 0569ab6 | grep pre-002`",
        "commit; 0569ab6 2026-08-12 13:37:24 -0500; the grep returns data/pre-002-events.json and "
        "data/pre-002-riskset.json -- committed rather than re-fetched, as claimed"),
    "d0729375b9": (
        "`git merge-base --is-ancestor fff7063 5efe626; echo $?`",
        "0 -- fff7063 (the registration, 2026-08-16 09:40:55) is an ancestor of 5efe626 (the "
        "instrument, 09:56:54): sixteen minutes, and the order is confirmed rather than assumed"),
    "55a9b6a983": (
        "`git cat-file -t fff7063` + `git log -1 --format='%h %ad %s' --date=iso fff7063` + "
        "`git show --name-only --format= fff7063`",
        "commit; fff7063 2026-08-16 09:40:55 -0500 'REG-013: the citation-graph whitespace, "
        "registered alone'; the file list is one path, "
        "docs/preregistration/REG-013-citation-graph-whitespace.md"),
    "e087b31b91": (
        "`git log --format='%h' -- scripts/reg013_citation_whitespace.py` + `git show "
        "--name-only --format= 5efe626`",
        "the log returns 5efe626 and nothing else, so it is the last AND the only commit touching "
        "the instrument; and 5efe626's file list contains "
        "docs/papers/paper-IV-composition/paper-IV.md -- 'entered the repository together', as "
        "claimed"),
    "ffc2d520de": (
        "`git log --format='%h' -- scripts/reg013_citation_whitespace.py | wc -l`",
        "1 -- the single-commit history the sentence's 5efe626 pin rests on"),

    # ---------------- shasum, and the one `ls -l + git ls-files` row
    "37b5a0dc57": (
        "`shasum -a 256 data/pre-002-events.json`",
        "974d156b53dfb915f48bdc3df99d7f2f2dd146427fa537fd7bdff4a503006bf0 -- character for "
        "character what §11 prints"),
    "aebdfa4d76": (
        "`shasum -a 256 data/pre-002-riskset.json`",
        "60627429d937bc42b9cf96a1be4bcfb78d198948a3212ac8f8c5e4412a436cce -- character for "
        "character what §11 prints"),
    "6c9aacc322": (
        "`grep -n 'events across' docs/preregistration/RESULT-002-replication-run.log` + "
        "`git ls-files docs/preregistration/RESULT-002-replication-run.log`",
        "L28 '444 events across 190 firms', and the pilot log's L19 reads '244 events across 121 "
        "firms'; the replication log is tracked. 244 + 444 = 688, the count §5.3 reports"),

    # ---------------- the ten with no operand
    "e949f42f3b": (
        "`git log -1 --format='%h %ad' --date=iso -- "
        "docs/preregistration/REG-005-p3-lag-shape-identifiability.md` + `git log --reverse "
        "--format='%h %ad' --date=iso -- scripts/wt091*.py`",
        "REG-005 committed 6f0e7be 2026-08-12 15:10:24; wt091 first appears at 42ca377 "
        "2026-08-12 16:24:12 -- the registration precedes the instrument by 74 minutes"),
    "6399cc6879": (
        "`grep -n '^def test_' tests/test_paper_test_counts_are_derived.py` (green in the 1095)",
        "L74 test_paper_iii_suite_total_at_the_pin_is_what_paper_iii_says and L96 "
        "test_paper_ii_module_count_is_live_and_is_what_paper_ii_says -- the module does fail if "
        "either count drifts, which is what the sentence claims"),
    "1ae72956c3": (
        "`git log -1 --format=%h ad779eb -- src/wealth_tensor/lag.py`",
        "ad779eb -- the pin the sentence gives, returned by the command the sentence names"),
    "6efe91d805": (
        "`git log -1 --format=%h b9089c7 -- src/wealth_tensor/lambda_sensitivity.py`",
        "b9089c7 -- the pin the sentence gives, returned by the command the sentence names"),
    "150f86a167": (
        "`grep -n 'What was done to the corpus' docs/RESULT-END-TO-END-001-E1.md` + "
        "`grep -n 'The type check' docs/RESULT-END-TO-END-001-E1.md`",
        "L61 '### 2.2 - The type check' is the check itself; L246 '## 6 - What was done to the "
        "corpus' opens 'The FAIL branch of the design's E1 table, written before the run, applied "
        "in full and in scope'. Both facts the sentence names are in E1. (The prior note put "
        "'written before the leg ran' in §2.2; it is in §6.)"),
    "79d2484c84": (
        "`grep -n 'third copy' docs/RESULT-END-TO-END-001-E3.md`",
        "L291 carries the admission row \"E1's applied remedy left a third copy of the withdrawn "
        "identification standing in Paper III\" -- which is what this sentence says E3 records"),
    "01ed28c1a8": (
        "`for n in variance_suppression variance_concentration n_crises; do grep -c $n "
        "scripts/wt002_lambda_report.py src/wealth_tensor/lambda_sensitivity.py; done`",
        "each of the three names returns a non-zero count in BOTH files (1/3, 1/3, 1/2) -- the "
        "parenthesis names them correctly"),
    "1d538d6e60": (
        "`grep -n 'E7' scripts/wt085_returns_conditioning.py`",
        "L63 'E7  THE ECONOMICS PRECEDENT, CHECKED RATHER THAN CITED' and L411 the runner's "
        "hr('E7 - the economics precedent, derived rather than taken on report') -- the Nerlove "
        "reduced form is derived in-repository, which is exactly the annotation's claim"),
    "b64ff1c700": (
        "`head -12 docs/preregistration/RESULT-REG-013.md`",
        "its Run line reads '2026-08-16, wealthTensor-53, darwin. Log RESULT-REG-013-run.log, "
        "JSON RESULT-REG-013-run.json' and its Verdict line reads 'H1 SURVIVES' off them, which "
        "is the reading-off the sentence claims"),
    "30191fec1a": (
        "`grep -n 'assert grid.size == 399\\|assert len(excess) == 4' tests/test_excess_demand.py`",
        "L70 'assert grid.size == 399'; and §8's twelve-point four is asserted by "
        "test_the_twelve_point_grid_returns_the_four_schedules_section_8_reports, ADDED AT "
        "wealthTensor-86 by scripts/wt158_twelve_point_four.py because it was not there before -- "
        "the sentence said the four was asserted and until " + D + " it was not. Both numbers are "
        "now asserts and not prints"),
}

NEW_ROW_PID = "df3cdc8d2a"
NEW_ROW_ARTEFACT = "docs/preregistration/RESULT-REG-013-rerun-2026-08-18.json"
NEW_ROW_CLASS = "H"
NEW_ROW_EVIDENCE = ("`python3 -c \"import json;a=json.load(open('docs/preregistration/"
                    "RESULT-REG-013-run.json'));b=json.load(open('docs/preregistration/"
                    "RESULT-REG-013-rerun-2026-08-18.json'));print([k for k in "
                    "('pairs','ceiling','P_ceiling','F_floor','H1') if a[k]!=b[k]])\"`")
NEW_ROW_NOTE = ("prints [] -- the re-run agrees with the committed run on every block §6 reports. "
                "The file is the " + D + " re-run's own JSON, committed by "
                "scripts/wt157_paperIV_s10_reg013_rerun.py, so the sentence's 'that second run is "
                "committed at' names a file that exists and carries what it claims")


def read_rows(path):
    head, rows = [], []
    for line in Path(path).read_text().splitlines():
        if line.startswith("#") or not line.strip():
            head.append(line)
            continue
        parts = line.split("\t")
        if len(parts) != len(COLUMNS):
            raise SystemExit(f"wt159: malformed row: {line[:80]!r}")
        rows.append(parts)
    return head, rows


def wt156_flags():
    out = subprocess.run([sys.executable, "scripts/wt156_reproducibility_sweep.py",
                          "--json", "--skip-postconditions"],
                         cwd=REPO, capture_output=True, text=True)
    if out.returncode == 2:
        raise SystemExit("wt159: REFUSING — wt156 itself returns 2; fix the sweep first.")
    j = json.loads(out.stdout)
    return {r["promise_id"] for r in j["d1"] + j["d2"]}


def wt148_sentence(pid):
    out = subprocess.run([sys.executable, "scripts/wt148_promise_sweep.py", "--json"],
                         cwd=REPO, capture_output=True, text=True)
    for p in json.loads(out.stdout):
        if p["pid"] == pid:
            return p["sentence"], p["paper"]
    raise SystemExit(f"wt159: REFUSING — wt148 does not emit promise {pid}.")


def main():
    flags = wt156_flags()
    if flags != set(REPAIRS):
        only_sweep = sorted(flags - set(REPAIRS))
        only_here = sorted(set(REPAIRS) - flags)
        print("wt159: REFUSING — the repair set is not the flag set.")
        print(f"    flagged but not repaired here : {only_sweep}")
        print(f"    repaired here but not flagged : {only_here}")
        return 2

    sentence, paper = wt148_sentence(NEW_ROW_PID)

    head, rows = read_rows(TSV)
    before = {r[1]: list(r) for r in rows}
    if NEW_ROW_PID in before:
        print(f"wt159: REFUSING — {NEW_ROW_PID} is already adjudicated.")
        return 2

    shutil.copy2(TSV, BAK)
    try:
        for r in rows:
            if r[1] in REPAIRS:
                ev, note = REPAIRS[r[1]]
                if "\t" in ev or "\t" in note:
                    raise SystemExit(f"wt159: a replacement for {r[1]} contains a TAB")
                r[4], r[5] = ev, note
        rows.append([paper, NEW_ROW_PID, NEW_ROW_ARTEFACT, NEW_ROW_CLASS,
                     NEW_ROW_EVIDENCE, NEW_ROW_NOTE, sentence])
        TSV.write_text("\n".join(head + ["\t".join(r) for r in rows]) + "\n")

        _, after_rows = read_rows(TSV)
        after = {r[1]: list(r) for r in after_rows}

        checks = []

        def c(name, pol, cond, detail=""):
            checks.append((name, pol, bool(cond), detail))

        c("C1 exactly 46 rows had their evidence rewritten", "POSITIVE",
          sum(1 for p in REPAIRS if after[p][4] != before[p][4]) == 46,
          str(sum(1 for p in REPAIRS if after[p][4] != before[p][4])))
        c("C2 the file grew by exactly one row (129 -> 130)", "POSITIVE",
          len(after_rows) == len(before) + 1, f"{len(before)} -> {len(after_rows)}")
        c("C3 every repaired row's promise_id is unchanged", "POSITIVE",
          all(p in after for p in REPAIRS))
        c("C4 every repaired row's class is unchanged", "POSITIVE",
          all(after[p][3] == before[p][3] for p in REPAIRS))
        c("C5 every repaired row's sentence is unchanged", "POSITIVE",
          all(after[p][6] == before[p][6] for p in REPAIRS))
        c("C6 every repaired row's artefact is unchanged", "POSITIVE",
          all(after[p][2] == before[p][2] for p in REPAIRS))
        c("C7 the new row carries wt148's sentence byte-for-byte", "POSITIVE",
          after[NEW_ROW_PID][6] == sentence)

        sweep = subprocess.run([sys.executable, "scripts/wt156_reproducibility_sweep.py"],
                               cwd=REPO, capture_output=True, text=True)
        c("C8 wt156 returns 0 at the working tree — the file is clean at its own criterion",
          "POSITIVE", sweep.returncode == 0, f"rc={sweep.returncode}\n{sweep.stdout[-900:]}")

        sweep148 = subprocess.run([sys.executable, "scripts/wt148_promise_sweep.py"],
                                  cwd=REPO, capture_output=True, text=True)
        c("C9 wt148 returns 0 — nothing STALE and nothing unadjudicated in scope", "POSITIVE",
          sweep148.returncode == 0, f"rc={sweep148.returncode}\n{sweep148.stdout[-700:]}")

        # ---- NEGATIVE
        untouched = [p for p in before if p not in REPAIRS]
        c("C10 NEGATIVE the 83 rows wt156 did not flag are byte-identical", "NEGATIVE",
          all(after[p] == before[p] for p in untouched),
          str([p for p in untouched if after[p] != before[p]]))
        c("C11 NEGATIVE no repaired evidence still names a session, a log or a machine",
          "NEGATIVE",
          not [p for p in REPAIRS if "session log" in after[p][4]
               or "on darwin" in after[p][4] or "wealthTensor-8" in after[p][4]],
          str([p for p in REPAIRS if "session log" in after[p][4]
               or "on darwin" in after[p][4] or "wealthTensor-8" in after[p][4]]))
        c("C12 NEGATIVE the sweep still flags all 46 at b50bccd — the repair moved the FILE, "
          "not the instrument", "NEGATIVE", _still_flags_at_before())
        c("C13 NEGATIVE no manuscript is dirty beyond paper-IV", "NEGATIVE",
          _dirty_manuscripts() in ([], ["docs/papers/paper-IV-composition/paper-IV.md"]),
          str(_dirty_manuscripts()))

        ok = all(x[2] for x in checks)
        nneg = sum(1 for x in checks if x[1] == "NEGATIVE")
        print(f"wt159 · POST-CONDITIONS ({len(checks)} total, {nneg} NEGATIVE, "
              f"{len(checks) - nneg} POSITIVE)")
        for name, pol, passed, detail in checks:
            print(f"    [{'ok  ' if passed else 'FAIL'}] {name}" +
                  (f"\n           {detail}" if detail and not passed else ""))
        if not ok:
            shutil.copy2(BAK, TSV)
            print("\nwt159: ROLLED BACK from .bak-wt159.")
            return 2
        print(f"\nwt159: 46 rows re-adjudicated with runnable evidence; 1 new row adjudicated.")
        return 0
    except Exception as exc:  # noqa: BLE001
        shutil.copy2(BAK, TSV)
        print(f"wt159: EXCEPTION {exc!r} — ROLLED BACK from .bak-wt159.")
        return 2


def _still_flags_at_before():
    out = subprocess.run([sys.executable, "scripts/wt156_reproducibility_sweep.py",
                          "--rev", "b50bccd", "--json"],
                         cwd=REPO, capture_output=True, text=True)
    j = json.loads(out.stdout)
    return {r["promise_id"] for r in j["d1"] + j["d2"]} == set(REPAIRS)


def _dirty_manuscripts():
    out = subprocess.run(["git", "status", "--porcelain"], cwd=REPO,
                         capture_output=True, text=True).stdout
    return [l[3:] for l in out.splitlines()
            if "docs/papers/" in l and l.rstrip().endswith(".md")]


if __name__ == "__main__":
    sys.exit(main())
