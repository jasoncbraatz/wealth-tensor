"""wealthTensor-98 · the three claims that were held to an exit code and nothing else.

WHY THIS EXISTS
---------------
`-96` proved live that an exit code is the WEAK half of a claim: it added 27 tests, its
registry still said `pytest` 1121, and the RC stayed 0 through every run -- only the COUNT
moved. It then named three claims that print no count at all (`verify-layout.sh`,
`redproof-layout.sh`, `wt170 --verify`), two of them the checks that guard the deliverable,
and left their `note:` fields saying so. This file is the cheap half of closing that.

WHAT IT HOLDS. Three things, per claim, and the third is the one people forget:

  * the REGISTRY declares a `count` and a one-group `count_re` (so the gate can observe it);
  * the number is DERIVED -- move the corpus and the printed number moves with it. A value
    hand-written into a script and printed back is bit-identical to its input on every run,
    which reads as agreement and is `-92`'s tautology;
  * the leg BITES a wrong count, asserted on the FALSE-CLAIM TAG, with a CONTROL beside it
    requiring that tag to be SILENT on the clean case. A tag that fires on both proves
    nothing.

WHAT IT DOES NOT DO, said plainly. It never runs the four lualatex builds or the fifteen
evidence cells; it drives the real code paths that PRODUCE the numbers, cheaply, so that
CI, a fresh clone and a container session all get this coverage. That the real commands
really print these lines with these numbers is proven by `handoff_gate.py --claims-all` at
wrap, and by `scripts/redproof_wt180_counts.py`, which perturbs the full corpus. Neither
half is sufficient; do not delete one because the other is green.
"""

import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
DELIV = ROOT / "docs" / "deliverable"

sys.path.insert(0, str(SCRIPTS))
import handoff_gate as G          # noqa: E402
import redproof_wt180_counts as R  # noqa: E402

THREE = ("verify-layout.sh", "redproof-layout.sh", "wt170 --verify")


def _registry():
    claims, problems = G.parse_claims(G.frontmatter_block())
    assert not problems, "the committed handoff's claims block does not parse: %s" % problems
    return {c["id"]: c for c in claims}


# ------------------------------------------------------------------------------- registry
def test_all_three_claims_carry_a_count_and_a_one_group_count_re() -> None:
    reg = _registry()
    for cid in THREE:
        c = reg.get(cid)
        assert c is not None, f"docs/HANDOFF.md declares no claim with id {cid!r}"
        assert c.get("count") is not None, (
            f"{cid} carries no count. An exit code alone stays 0 while the corpus moves "
            "underneath it -- that is the whole reason this card existed.")
        assert c.get("count_re"), f"{cid} carries no count_re, so its count cannot be observed"
        assert re.compile(c["count_re"]).groups == 1, (
            f"{cid}: count_re must capture exactly one group; the gate refuses anything else")


def test_no_claim_still_advertises_that_it_prints_no_count() -> None:
    """The residue was NAMED in the notes. If a note still says it, the card is not closed."""
    for cid, c in _registry().items():
        assert "no count" not in (c.get("note") or ""), (
            f"{cid}'s note still says it prints no count -- either it does, and the claim is "
            "held to an exit code, or it does not, and the note is stale. Both are bugs.")


# ------------------------------------------------------------- redproof-layout.sh · tally
def test_the_tally_counts_verdicts_rather_than_printing_a_constant() -> None:
    rx = _registry()["redproof-layout.sh"]["count_re"]
    for n in (1, 3, 7):
        rc, out = R.tally_says(n)
        assert rc == 0 and R.count_in(out, rx) == n, (
            f"driven with {n} verdicts the tally printed {out!r}")


def test_a_tally_that_counted_nothing_refuses_to_print_a_number() -> None:
    """A check reporting having verified nothing, in the SHAPE of one that verified
    everything, is worse than no line at all -- a count_re would happily match `0`."""
    rc, out = R.tally_says(0)
    assert rc == 1 and "NO PROBES REPORTED" in out, out


def test_the_real_redproof_script_reports_one_verdict_per_probe_call_site() -> None:
    """The WIRING, on the real script: real call sites, real say(), real summary line, with
    only the four lualatex builds stubbed out."""
    reg = _registry()["redproof-layout.sh"]
    rc, out = R.stub_probe_run()
    assert rc == 0, out
    assert R.count_in(out, reg["count_re"]) == reg["count"], out


def test_removing_one_probe_call_site_lowers_the_number() -> None:
    """A corpus with one fewer member. If the number did not move it was never derived."""
    reg = _registry()["redproof-layout.sh"]
    rc, out = R.stub_probe_run(drop_probes=1)
    assert rc == 0, out
    assert R.count_in(out, reg["count_re"]) == reg["count"] - 1, out


# ------------------------------------------------------------- verify-layout.sh · wt176
def test_wt176_prints_the_pages_it_compared_and_the_number_follows_the_pdf(tmp_path) -> None:
    reg = _registry()["verify-layout.sh"]
    rc, out = R.wt176_verify(R.COMMITTED_PDF)
    assert rc == 0, out
    n = R.count_in(out, reg["count_re"])
    assert n == reg["count"], out
    short = tmp_path / "short.pdf"
    want = R.pdf_minus_one_page(R.COMMITTED_PDF, short)
    rc2, out2 = R.wt176_verify(short)
    assert R.count_in(out2, reg["count_re"]) == want == n - 1, out2
    assert rc2 != 0, "a PDF one page short must not verify"


def test_verify_layout_reads_the_same_line_the_registry_reads() -> None:
    """The script cross-checks wt176's count against a fresh pypdf read and dies if they
    disagree. That extractor is a `sed` program in bash and the registry is a Python regex;
    this is the only place the two are ever shown to be looking at the same line."""
    script = (DELIV / "verify-layout.sh").read_text()
    m = re.search(r"SAID=\"\$\(sed -n '([^']+)' ", script)
    assert m, "verify-layout.sh no longer extracts wt176's count -- the cross-check is gone"
    _rc, out = R.wt176_verify(R.COMMITTED_PDF)
    said = subprocess.run(["sed", "-n", m.group(1)], input=out,
                          capture_output=True, text=True).stdout.strip()
    assert said == str(_registry()["verify-layout.sh"]["count"]), (
        f"the script's own extractor pulled {said!r} out of wt176's real output")


# --------------------------------------------------------------- wt170 --verify · rows
def test_wt170_counts_the_rows_it_actually_re_ran(monkeypatch) -> None:
    """The real verify(), over a deliberately narrowed corpus. Two rows in, two rows said."""
    import wt170_paperII_promises as W
    rx = _registry()["wt170 --verify"]["count_re"]
    live = R.live_pids()[:2]
    assert len(live) == 2, "the committed corpus carries fewer than two live rows"
    monkeypatch.setattr(W, "PIDS", tuple(live))
    monkeypatch.setattr(W, "EV", {p: W.EV[p] for p in live})
    rc, out = R.wt170_verify()
    assert R.count_in(out, rx) == 2, out
    assert rc == 0, out


# --------------------------------------------------------------------- the leg bites
def test_the_leg_reports_false_claim_when_a_registered_count_is_wrong() -> None:
    """Asserted on the TAG, never the exit code: `-94` and `-95` each paid for a red-proof
    caught by a different guard than the one under test."""
    reg = _registry()
    _rc, wt176_out = R.wt176_verify(R.COMMITTED_PDF)
    _rc2, tally_out = R.stub_probe_run()
    for cid, text in (("verify-layout.sh", wt176_out), ("redproof-layout.sh", tally_out)):
        c = reg[cid]
        rc, out = R.replay(cid, c["count"] + 1, c["count_re"], text)
        assert rc == 1 and "FALSE-CLAIM" in out, out


def test_the_clean_case_is_silent() -> None:
    """A tag that fires on the correct number would make every probe above meaningless."""
    reg = _registry()
    _rc, wt176_out = R.wt176_verify(R.COMMITTED_PDF)
    _rc2, tally_out = R.stub_probe_run()
    for cid, text in (("verify-layout.sh", wt176_out), ("redproof-layout.sh", tally_out)):
        c = reg[cid]
        rc, out = R.replay(cid, c["count"], c["count_re"], text)
        assert rc == 0 and "FALSE-CLAIM" not in out, out
