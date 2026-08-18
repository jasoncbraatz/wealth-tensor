#!/usr/bin/env python3
"""wt155 · re-adjudicate every row wt154 flags, with an evidence column that names a READ.

wt154 flagged 25 of the 129 adjudicated rows: 23 whose evidence LOCATED the artefact
instead of reading it, and 2 whose evidence covered one side of a conjunctive sentence.
This script replaces the `evidence` and `note` of all 25 with a command that was actually
run or a passage that was actually read, this pass, on darwin.

WHAT THIS SCRIPT DOES NOT DO
----------------------------
It changes no `sentence`, no `class`, no `promise_id` and no manuscript. Every one of the
25 sentences was checked against its artefact and every one HELD — the defect was in the
adjudication, not in the paper. That is the finding, and a script that also edited a
manuscript would make it unreadable. Post-conditions bind all four invariants, and
`promise_id` is a hash of (paper, artefact, sentence), so leaving those alone is what
keeps wt148 at RC 0 instead of reporting 25 rows STALE.

POST-CONDITIONS: 12, of which 5 are NEGATIVE. The file is restored from a .bak on any
failure — the undo path is created before the edit, not after.
"""
from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys

TSV = "docs/promises-adjudicated.tsv"
BAK = TSV + ".bak-wt155"
SWEEP = "scripts/wt154_evidence_discrimination_sweep.py"

# promise_id -> (evidence, note). Every command below was run on darwin this pass and
# every passage below was read; the note records what came back, not that it came back.
REPAIRS: dict[str, tuple[str, str]] = {

    "2a403db2ef": (
        "read docs/notes/NOTE-001-phi-identifiability.md §2 and its Provenance line",
        "§2 'The finding' carries the conditioning result in full: the collapsed recursion "
        "C(t+1) = C(t)(1-α) + E(t)(α - φδ), the like-for-like table (median abs err 0.21140 "
        "with δ free vs 0.00073 with δ pinned, a 291× improvement) and the no-cliff table "
        "by true δ. The Provenance line names scripts/prototypes/bench_lag_torch.py and "
        "bench_identify.py. Method, scripts and figures, which is what the parenthesis "
        "promises."),

    "0d93854088": (
        "read src/wealth_tensor/lag.py docstring L1-13",
        "'Virtual wealth as a transfer function on real wealth' — the reporting layer as a "
        "filter, with the Real/Reported/Gap layers named. That is Paper III §3's subject, "
        "so the module belongs on the bullet's list."),

    "f4ea301779": (
        "read src/wealth_tensor/lambda_sensitivity.py docstring L1-14",
        "'The numeraire cancels. Demonstrated, so that Lambda stops being the paper's "
        "weakest wall.' — the WT-002 coupling sweep over 1e-6..1e+6 currency/J that is the "
        "empirical leg of the Λ defence. On the bullet's list correctly."),

    "cef5e43665": (
        "read src/wealth_tensor/edgar.py docstring L1-12",
        "'The severe test: does recognition lag scale with GAAP-assigned unobservability?' "
        "followed by the ASC tier table (tier 0 PP&E / ASC 360, tier 1 finite-lived "
        "intangibles / ASC 350-30, ...) that supplies φ. The §5 sampling module, on the "
        "bullet's list correctly."),

    "0833e298f0": (
        "grep -n '244 events' docs/preregistration/RESULT-002-pilot-run.log",
        "L19 '244 events across 121 firms', with L29 'VERDICT: PREDICTION FAILS'. The log "
        "carries §5.3's 244 itself, so the log — not a command — is the record, which is "
        "what the sentence claims. (444 is the replication log's L28, adjudicated at its "
        "own row.)"),

    "fa005fbebe": (
        "git show d655501:tests/test_edgar.py | grep -c '^def test_'",
        "42 at the pin. test_lag.py returns 10 and test_lambda_sensitivity.py returns 10 by "
        "the same command, so 42 + 10 + 10 = 62 — the number the sentence gives for these "
        "three modules."),

    "af9d1b09c3": (
        "git show d655501:tests/test_lambda_sensitivity.py | grep -c '^def test_'",
        "10 at the pin — the third of the three modules whose def-test counts sum to the "
        "sentence's 62 (42 + 10 + 10)."),

    "a3511853e3": (
        "git show --stat 9722342",
        "'1 file changed, 283 insertions(+)', the one file being "
        "docs/preregistration/PRE-001-wt026-observability-lag.md, under the subject "
        "'PRE-001: pre-register the WT-026 severe test, before any lag is computed'. A "
        "single-file commit containing the registration and nothing else, as claimed."),

    "31fea3ed33": (
        "git show --stat d655501",
        "9 files changed: PRE-002-wt026-peak-to-charge.md (132 lines) lands in the same "
        "commit as src/wealth_tensor/edgar.py (622) and scripts/wt026_severe_test.py (224). "
        "The commit 'also contains the implementation', as the sentence says of this "
        "registration and not of PRE-001's."),

    "6db7b7ce3d": (
        "git show --stat 9722342 AND git show --stat d655501",
        "Both halves of the sentence read, not one. 9722342 is '1 file changed, 283 "
        "insertions(+)' — PRE-001's registration alone, nothing else. d655501 is 9 files, "
        "PRE-002's registration beside edgar.py and wt026_severe_test.py — 'also contains "
        "the implementation'. The asymmetry the sentence draws between the two "
        "registrations is real in the commits."),

    "af81f3ed7a": (
        "git log -1 --format=%h d655501 -- src/wealth_tensor/edgar.py",
        "returns d655501 — the sentence's own verification command, run, returning the sha "
        "the sentence pins edgar.py at. The companions return their own too: ad779eb for "
        "lag.py, b9089c7 for lambda_sensitivity.py."),

    "dc4e604aa3": (
        "git log -1 --format=%h d655501 -- src/wealth_tensor/edgar.py "
        "+ git log -1 --format=%h -- src/wealth_tensor/edgar.py",
        "the first returns d655501, the second 93a159b — both shas the byte-identity clause "
        "compares are real commits of this same file, and 93a159b is edgar.py's "
        "last-touching commit, which is what makes it the clause's 'since'."),

    "416f04fc33": (
        "sed -n '/def test_pre001_constants_are_what_was_registered/,/^def /p' "
        "tests/test_edgar.py",
        "the body is ten bare asserts on registered constants — MATERIALITY_FLOOR == 0.01, "
        "MIN_RUN == 2, MAX_LOOKBACK == 20, MIN_HISTORY_QUARTERS == 12, PILOT_SIC, "
        "REPLICATION_SIC, the TIER_TAGS set and two of its entries, REVENUE_TAGS[0]. "
        "Editing any one of them turns it red, which is the sentence's claim; the "
        "docstring says the same in words."),

    "0b29224189": (
        "sed -n '/def test_a_flat_gini_does_not_mean_a_bounded_one/,/^def /p' "
        "tests/test_redistribution.py + grep -n "
        "'def test_excess_demand_is_monotone_here_so_this_is_not_an_SMD_result' "
        "tests/test_excess_demand.py",
        "the Gini guard asserts drift < 0.02 AND top_share > 0.95 AND not is_bounded — it "
        "goes red exactly when a flat Gini would be scored as boundedness, which is the "
        "overclaim it exists to forbid. Its named sibling is at tests/test_excess_demand.py "
        "L105. Both are in companion modules, as the sentence says."),

    "f43958893d": (
        "read docs/LEDGER.md WT-062 (from L1632) AND WT-059 (from L1489)",
        "BOTH ENTRIES READ. WT-062 is titled 'search a personal library by TITLE, not by "
        "author — and a null result from a sprawl is not evidence of absence' and opens "
        "'Two false conclusions in one session'. WT-059 is 'verifying a reference is not "
        "the same act as verifying a citation' and carries the correction and the rule "
        "adopted. The two together are the corrected-reverted-corrected record, and "
        "'the citations were not wrong, the search was' is WT-062's own diagnosis."),

    "cc284d40fa": (
        "git show --stat fff7063 + git log --reverse --format='%h %ad' --date=short -- "
        "scripts/reg013_citation_whitespace.py",
        "fff7063, 2026-08-16, '1 file changed, 157 insertions(+)', subject 'REG-013: the "
        "citation-graph whitespace, registered alone'. The instrument's first commit is "
        "5efe626, after it. Both clauses of the sentence — committed in fff7063, and before "
        "the instrument existed — hold."),

    "680347614f": (
        "read scripts/reg013_citation_whitespace.py docstring L1-16",
        "'REG-013 · the citation-graph whitespace, measured against a ceiling and a floor. "
        "Registered at docs/preregistration/REG-013-citation-graph-whitespace.md, commit "
        "fff7063, BEFORE this file existed.' It then defines the overlap coefficient "
        "O(A,B) = |cite(A) & cite(B)| / min(|cite(A)|, |cite(B)|) it computes. This file is "
        "the instrument the bullet names."),

    "d1a2ee876e": (
        "head -6 docs/preregistration/RESULT-REG-013-run.log "
        "+ grep -n 'run.log' docs/preregistration/RESULT-REG-013.md",
        "the log opens on resolved seed works with their citation counts ('[seed] T: "
        "W4301267015 4839 The Entropy Law and the Economic Process', and five more) — run "
        "output, not a stub. RESULT-REG-013.md L6-7 names this log and the JSON as the "
        "run's record and L8 reads 'Verdict: H1 SURVIVES' off them, which is the "
        "relationship the sentence asserts."),

    "2373b9d310": (
        "python3 -c \"import json; print(list(json.load(open("
        "'docs/preregistration/RESULT-REG-013-run.json'))))\" "
        "+ grep -n 'run.json' docs/preregistration/RESULT-REG-013.md",
        "top-level keys n_max, clusters, seeds, pairs, ceiling, P_ceiling, F_floor, void, "
        "H1 — the machine record of the same 2026-08-16 run, carrying the H1 the verdict is "
        "read off. RESULT-REG-013.md L7 names it beside the log."),

    "d35227f459": (
        "read scripts/wt030_report.py L1-12, which imports src/wealth_tensor/"
        "redistribution.py",
        "L6: 'from wealth_tensor.redistribution import (RedistributiveEconomy as E, "
        "stationary_gini, top_share, is_bounded, reachable_frontier)' — the script computes "
        "Paper II's figures from the module rather than restating them, so 'regenerated by "
        "scripts/wt030_report.py' holds."),

    "91e98bf51b": (
        "read scripts/wt002_lambda_report.py L1-8, which imports src/wealth_tensor/"
        "lambda_sensitivity.py",
        "L3: 'from wealth_tensor.lambda_sensitivity import (sweep_coupling, "
        "invariance_report, scaling_exponent, DIMENSIONLESS)', then it prints the coupling "
        "sweep at φ=0.3 over 1e-6..1e+6 currency/J. 'Regenerated by "
        "scripts/wt002_lambda_report.py' holds for Paper III's second module."),

    "e238ae248a": (
        "read src/wealth_tensor/excess_demand.py docstring L1-10 + grep -on "
        "'src/wealth_tensor/[a-z_]*\\.py' docs/papers/paper-IV-composition/paper-IV.md",
        "the docstring is 'Supply and demand as two readings of a single distribution of "
        "indifference points', the module that makes THIS paper's reservation-price claim "
        "executable. paper-IV.md names exactly four src/ modules: redistribution.py (L675, "
        "Paper II's), lag.py (L676) and lambda_sensitivity.py (L677) (Paper III's), and "
        "excess_demand.py (L689). So it is the only one that is not a sibling's, as "
        "claimed."),

    "2f8a433aa7": (
        "grep -rln 'def test_the_forbidden_claim_is_red' tests/ | wc -l "
        "+ grep -n 'test_pre001_constants_are_what_was_registered' "
        "docs/papers/paper-III-dual-tensor/paper-III.md",
        "2 — tests/test_reg004_sec6_alpha_eff.py and tests/test_reg005_sec7_lag_transfer.py, "
        "both registration modules, so 'two' is counted rather than asserted; and Paper III "
        "L2061 does name the third. A filename count is the right read for THIS sentence, "
        "because the claim is about which files carry the definition — see REVIEW-025 §3."),

    "59ad5eeffd": (
        "sed -n '/def test_pre001_constants_are_what_was_registered/,/^def /p' "
        "tests/test_edgar.py + grep -n "
        "'test_pre001_constants_are_what_was_registered' "
        "docs/papers/paper-III-dual-tensor/paper-III.md",
        "defined in tests/test_edgar.py, and its body asserts the registered constants — an "
        "overclaim-forbidding test of the same kind as the two named beside it. Paper III "
        "L2061 names it, which is the sentence's 'Paper III names a third'."),

    "3df66f9481": (
        "grep -n 'verified against a publisher page' docs/REFERENCE-POLICY.md "
        "+ read docs/REFERENCE-POLICY.md L210",
        "L226 'Pass 1 — record verified against a publisher page, catalogue, Crossref or "
        "issuing body' and L210 'claim gets verified by hand, mechanically, against a "
        "source, before it enters any document'. The policy does prescribe verification "
        "against live sources. (Its twin in the same sentence, the PREPRINT-CHECKLIST row "
        "75220244de, was repaired at REVIEW-024; this is the other half.)"),
}

FIELDS = ("paper", "promise_id", "artefact", "class", "evidence", "note", "sentence")


def read_rows(path):
    head, rows = [], []
    for line in open(path, encoding="utf-8"):
        if line.startswith("#") or not line.strip():
            head.append(line)
            continue
        rows.append(line.rstrip("\n").split("\t"))
    return head, rows


def sweep_ids(root, rev=None):
    cmd = [sys.executable, SWEEP, "--json", "--skip-postconditions"]
    if rev:
        cmd += ["--rev", rev]
    out = subprocess.run(cmd, cwd=root, capture_output=True, text=True)
    if out.returncode == 2:
        raise SystemExit("wt155: wt154 post-conditions failed; refusing to repair")
    return {f["promise_id"] for f in json.loads(out.stdout)["flagged"]}


def main() -> int:
    root = subprocess.run(["git", "rev-parse", "--show-toplevel"],
                          capture_output=True, text=True).stdout.strip()
    path = os.path.join(root, TSV)

    before_flagged = sweep_ids(root)
    checks: list[tuple[bool, str, str]] = []
    checks.append((set(REPAIRS) == before_flagged, "POSITIVE",
                   f"the {len(REPAIRS)} rows repaired are exactly the rows wt154 flags "
                   f"({len(before_flagged)})"))
    if not checks[0][0]:
        missing = sorted(before_flagged - set(REPAIRS))
        extra = sorted(set(REPAIRS) - before_flagged)
        print(f"wt155: REFUSING — flagged-but-unrepaired {missing}, "
              f"repaired-but-unflagged {extra}", file=sys.stderr)
        return 2

    head, rows = read_rows(path)
    before = {r[1]: list(r) for r in rows}

    shutil.copy2(path, os.path.join(root, BAK))          # undo path FIRST
    n = 0
    for r in rows:
        rep = REPAIRS.get(r[1])
        if rep:
            r[4], r[5] = rep
            n += 1
    with open(path, "w", encoding="utf-8") as fh:
        for line in head:
            fh.write(line)
        for r in rows:
            fh.write("\t".join(r) + "\n")

    after = {r[1]: list(r) for r in rows}
    checks.append((n == len(REPAIRS), "POSITIVE", f"{n} rows rewritten"))
    checks.append((len(after) == 129, "POSITIVE", "the file still holds 129 rows"))
    checks.append((set(before) == set(after), "NEGATIVE",
                   "no promise_id changed — evidence and note are not hashed, so wt148 "
                   "reports nothing STALE"))
    checks.append((all(before[k][6] == after[k][6] for k in before), "NEGATIVE",
                   "no `sentence` changed — this pass repairs adjudications, not "
                   "manuscripts"))
    checks.append((all(before[k][3] == after[k][3] for k in before), "NEGATIVE",
                   "no `class` changed — every one of the 25 sentences HELD on reading"))
    checks.append((all(before[k][2] == after[k][2] for k in before), "NEGATIVE",
                   "no `artefact` changed"))
    checks.append((all("\t" not in v and "\n" not in v
                       for pair in REPAIRS.values() for v in pair), "NEGATIVE",
                   "no repair text carries a tab or a newline (the file is TSV)"))
    unchanged = [k for k in before if before[k][4:6] == after[k][4:6] and k in REPAIRS]
    checks.append((not unchanged, "POSITIVE",
                   "every repaired row's evidence or note actually moved"))

    after_flagged = sweep_ids(root)
    checks.append((not after_flagged, "POSITIVE",
                   f"wt154 flags 0 rows after the repair (was {len(before_flagged)})"))

    still_before = sweep_ids(root, rev="8855aba")
    checks.append((len({"bf2138f041", "75220244de", "76617b04e0", "7e1c612368"}
                       & still_before) == 4, "POSITIVE",
                   "the sweep still flags all four REVIEW-024 rows at 8855aba — the "
                   "repair moved the file, not the instrument"))

    dirty = subprocess.run(["git", "status", "--porcelain", "--", "docs/papers"],
                           cwd=root, capture_output=True, text=True).stdout.strip()
    checks.append((dirty == "", "NEGATIVE",
                   "no manuscript under docs/papers/ is dirty"))

    ok = all(c[0] for c in checks)
    print(f"wt155 · POST-CONDITIONS ({sum(1 for c in checks if c[0])}/{len(checks)} ok, "
          f"{sum(1 for c in checks if c[1] == 'NEGATIVE')} negative)")
    for good, pol, desc in checks:
        print(f"  {'ok  ' if good else 'FAIL'} [{pol}] {desc}")
    if not ok:
        shutil.copy2(os.path.join(root, BAK), path)
        print("\nwt155: ROLLED BACK from " + BAK, file=sys.stderr)
        return 2
    print(f"\nwt155: {n} rows re-adjudicated. Backup at {BAK}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
