#!/usr/bin/env python3
"""wealthTensor-98 -- the red-proof for the three claims that were counted by NOTHING.

THE RESIDUE THIS CLOSES. `-96` proved, live, that an exit code is the weakest half of a
claim: it added 27 tests, its registry still said `pytest` 1121, and the RC stayed 0 through
every run. Only the COUNT moved. It then wrote down that three of the twenty-five most
expensive checks in this repository print no count at all -- `verify-layout.sh`,
`redproof-layout.sh`, `wt170 --verify` -- and left their `note:` fields saying so. `-97` did
not close it. Two of the three are the checks that guard the deliverable.

WHAT A COUNT HAS TO BE BEFORE IT IS WORTH REGISTERING. Two things, and this file proves both
separately for each of the three:

  DERIVED   the number follows what the run actually did. The trap here is `-92`'s: a value
            hand-written into a script and printed back is bit-identical to its input on
            every run, which reads as agreement and is tautology. So each probe MOVES the
            world -- a page out of the PDF, a probe out of the script, a row out of the
            adjudication corpus -- and requires the printed number to move with it.

  BITES     the real claims leg reports FALSE-CLAIM when the declared count is wrong. This
            is asserted on the TAG, never on the exit status: `-94` and `-95` each paid for a
            red-proof caught by a DIFFERENT guard than the one under test, and from the
            outside that looks exactly like success. Every BITES probe has a CONTROL beside
            it that replays the same line with the TRUE count and requires FALSE-CLAIM to be
            SILENT -- a tag that fires on the clean case proves nothing when it fires on the
            dirty one.

THE CHEAP HALF AND THE EXPENSIVE HALF, STATED RATHER THAN BLURRED. Running all three real
commands costs four lualatex builds and fifteen re-executed evidence cells -- eight minutes
or so -- and a check that expensive runs in no CI, no fresh clone and no container session,
which in practice means it never runs at all (`-97`'s wt179 lesson, applied to its author's
successor). So the division is explicit:

  * THIS FILE proves the NUMBERS ARE DERIVED, by moving the world through the real code paths
    that produce them, in seconds; and it proves the leg BITES a wrong count, by replaying
    the REAL captured output line through the REAL `claims_leg()`.
  * `handoff_gate.py --claims-all` AT WRAP proves the real commands really print those lines
    with those numbers. That step is not optional and the wrap order names it.

Neither half is sufficient. Do not delete one because the other is green.

COVERAGE IS A DECLARED MATRIX, NOT A DISCOVERED ONE. `-95` wrote a coverage check that
scraped a guard's source for its tags, found nine of fourteen, and printed FULL COVERAGE. So
CLAIMS x TAGS below is declared here, the claim ids are held to the REAL registry in
docs/HANDOFF.md, and a cell with no passing probe prints WEAK. Delete one probe and exactly
one line goes WEAK, naming the cell.
"""
import contextlib
import io
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import handoff_gate as G  # noqa: E402

# The three claims this file exists for, held to the real registry by the REGISTERED probe.
CLAIMS = ("verify-layout.sh", "redproof-layout.sh", "wt170 --verify")

TAGS = {
    "REGISTERED": "the real registry carries a count and a one-group count_re for this claim",
    "DERIVED":    "move what the run measures and the printed number moves with it",
    "BITES":      "the real claims leg reports FALSE-CLAIM when the declared count is wrong",
    "CONTROL":    "the same replay with the TRUE count agrees, and FALSE-CLAIM stays silent",
}

RESULTS = []          # (claim, tag, ok, note)
COMMITTED_PDF = ROOT / "docs" / "deliverable" / "wealth-tensor-capture.pdf"


def record(claim, tag, ok, note):
    RESULTS.append((claim, tag, bool(ok), note))
    return ok


# --------------------------------------------------------------------------- the registry
def registry():
    """The REAL claims block out of docs/HANDOFF.md, as the gate itself parses it."""
    claims, problems = G.parse_claims(G.frontmatter_block())
    return {c["id"]: c for c in claims}, problems


def count_in(text, count_re):
    m = re.search(count_re, text)
    return None if m is None else int(m.group(1))


# ------------------------------------------------------------------- replay through the leg
def replay(claim_id, count, count_re, text):
    """Drive the REAL `claims_leg()` over a one-claim handoff whose command replays `text`.

    `cat FILE` is the command on purpose. The line under test is the one the real script
    really printed on this machine minutes ago -- captured, not hand-typed and not a golden
    file that goes stale -- and replaying it costs milliseconds, so the BITES and CONTROL
    probes can both run every time instead of being the ones somebody skips."""
    with tempfile.TemporaryDirectory() as tmp:
        cap = Path(tmp) / "captured.txt"
        cap.write_text(text)
        h = Path(tmp) / "HANDOFF.md"
        h.write_text(
            "---\nclaims:\n"
            "  - id: %s\n    cmd: cat %s\n    rc: 0\n    count: %d\n    count_re: %s\n"
            "---\n\n# body\n" % (claim_id, cap, count, count_re))
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            rc = G.claims_leg(run_slow=True, path=str(h))
        return rc, buf.getvalue()


def bites_and_control(claim, count_re, true_count, text):
    """The pair, always together. A tag that fires on both cases has proven nothing."""
    rc_bad, out_bad = replay(claim, true_count + 1, count_re, text)
    record(claim, "BITES",
           rc_bad == 1 and "FALSE-CLAIM" in out_bad,
           "declared %d, the line says %d -> rc %d, FALSE-CLAIM %s"
           % (true_count + 1, true_count, rc_bad,
              "present" if "FALSE-CLAIM" in out_bad else "ABSENT"))
    rc_ok, out_ok = replay(claim, true_count, count_re, text)
    record(claim, "CONTROL",
           rc_ok == 0 and "OK" in out_ok and "FALSE-CLAIM" not in out_ok,
           "declared %d, the line says %d -> rc %d, FALSE-CLAIM %s"
           % (true_count, true_count, rc_ok,
              "PRESENT ON THE CLEAN CASE" if "FALSE-CLAIM" in out_ok else "silent"))


# ------------------------------------------------------------- verify-layout.sh / wt176
def wt176_verify(pdf):
    r = subprocess.run([sys.executable, "docs/deliverable/wt176_layout_manifest.py",
                        "--verify", str(pdf)],
                       cwd=str(ROOT), capture_output=True, text=True)
    return r.returncode, (r.stdout or "") + (r.stderr or "")


def pdf_minus_one_page(src, dst):
    """A REAL corpus with one fewer member: the committed capture, one page short."""
    import pypdf
    r = pypdf.PdfReader(str(src))
    w = pypdf.PdfWriter()
    for page in r.pages[:-1]:
        w.add_page(page)
    with open(dst, "wb") as fh:
        w.write(fh)
    return len(r.pages) - 1


# ------------------------------------------------------------------ redproof-layout.sh
def tally_says(n):
    """Drive the sourced tally with n verdicts. (rc, stdout+stderr)."""
    script = ('. "%s/docs/deliverable/probe-tally.sh"\ntally_reset\n'
              'i=0; while [ $i -lt %d ]; do tally_bump; i=$((i+1)); done\n'
              'tally_line "redproof-layout"\n' % (ROOT, n))
    r = subprocess.run(["bash", "-c", script], cwd=str(ROOT),
                       capture_output=True, text=True)
    return r.returncode, (r.stdout or "") + (r.stderr or "")


# BOTH probe functions are stubbed. redproof-layout.sh grew a second one (probe_verifier,
# wealthTensor-110) that drives verify-layout.sh rather than build.sh, and stubbing only the
# first left the wiring proof running REAL lualatex builds inside the test suite -- slow, and
# counting verdicts the stub was supposed to be manufacturing.
STUB = ('probe() {\n'
        '  say "ok" "$1 -- STUBBED by redproof_wt180_counts.py; no build was run"\n'
        '}\n'
        'probe_verifier() {\n'
        '  say "ok" "$1 -- STUBBED by redproof_wt180_counts.py; no build was run"\n'
        '}\n')


def stub_probe_run(drop_probes=0):
    """Run the REAL redproof-layout.sh with its probe BODY stubbed out.

    This is the wiring proof, and it is the reason the tally lives in a sourced file. The
    four `probe` CALL SITES, `say()`, the bump and the summary line are all the real ones;
    only the four lualatex builds are gone. Drop a call site and the number has to drop with
    it -- a corpus with one fewer member, on the actual script, in under a second."""
    src = (ROOT / "docs" / "deliverable" / "redproof-layout.sh").read_text()
    stubbed = src
    for fn in ("probe() {", "probe_verifier() {"):
        head = stubbed.index(fn)
        tail = stubbed.index("\n}\n", head) + len("\n}\n")
        stubbed = stubbed[:head] + stubbed[tail:]
    # both bodies are gone; put the two stubs where the first one stood
    anchor = stubbed.index("echo \"== red-proofing")
    stubbed = stubbed[:anchor] + STUB + stubbed[anchor:]
    for _ in range(drop_probes):
        lines = stubbed.split("\n")
        last = max(i for i, ln in enumerate(lines)
                   if ln.startswith("probe ") or ln.startswith("probe_verifier "))
        del lines[last]
        stubbed = "\n".join(lines)
    # It must live beside its siblings: the script resolves everything from `dirname $0`.
    dst = ROOT / "docs" / "deliverable" / (".wt180-stub-%d.sh" % os.getpid())
    try:
        dst.write_text(stubbed)
        r = subprocess.run(["bash", str(dst)], cwd=str(ROOT),
                           capture_output=True, text=True)
        return r.returncode, (r.stdout or "") + (r.stderr or "")
    finally:
        if dst.exists():
            dst.unlink()


# ------------------------------------------------------------------------ wt170 --verify
def wt170_verify(tsv=None):
    """The REAL verify(), in-process, optionally reading a perturbed adjudication corpus."""
    sys.path.insert(0, str(ROOT / "scripts"))
    import wt170_paperII_promises as W
    old = W.TSV
    if tsv:
        W.TSV = str(tsv)          # absolute, so os.path.join(REPO, TSV) yields it unchanged
    buf = io.StringIO()
    try:
        with contextlib.redirect_stdout(buf):
            rc = W.verify()
    finally:
        W.TSV = old
    return rc, buf.getvalue()


def live_pids():
    """The pids `verify()` actually RE-RUNS: adjudicated in the committed corpus, not
    superseded away, not re-evidenced elsewhere.

    Worth a function rather than a slice of PIDS, and `-98` learned it the hard way: its
    first cut took the first two of PIDS, one of which is RETIRED in the real corpus, and
    asserted two rows would be verified. One was. The check bit on its own author inside a
    minute -- which is the cheapest possible place to find out that a list of intentions is
    not a list of what runs."""
    sys.path.insert(0, str(ROOT / "scripts"))
    import wt170_paperII_promises as W
    lines = (ROOT / "docs" / "promises-adjudicated.tsv").read_text().splitlines()
    reevidenced = {ln.split("\t")[1].strip() for ln in lines
                   if ln.startswith("#reevidenced") and "\t" in ln}
    return [ln.split("\t")[1] for ln in lines
            if "\t" in ln and not ln.startswith("#") and len(ln.split("\t")) >= 6
            and ln.split("\t")[1] in W.EV and ln.split("\t")[1] not in reevidenced]


def tsv_minus_one_row(dst):
    """A REAL corpus with one fewer member: one adjudicated row retired to a living successor.

    Not a deletion -- a deletion is REFUSED (orphaned), which would prove the wrong thing by
    exiting on a different path. A retirement is the corpus change this file actually sees in
    practice, and it is the one that moves the verified count by exactly one."""
    lines = (ROOT / "docs" / "promises-adjudicated.tsv").read_text().splitlines()
    live = live_pids()
    if len(live) < 2:
        raise RuntimeError("fewer than two live adjudicated rows -- nothing to retire")
    victim, heir = live[0], live[1]
    kept = [ln for ln in lines
            if not ("\t" in ln and not ln.startswith("#") and ln.split("\t")[1] == victim)]
    kept.append("#superseded\t%s\t%s\twt180\tred-proof: a retirement, so the count must drop "
                "by exactly one" % (victim, heir))
    Path(dst).write_text("\n".join(kept) + "\n")
    return victim, heir


# ------------------------------------------------------------------------------- the probes
def main():
    print("RED-PROOF wt180 -- the three claims that were held to an exit code and nothing else")
    reg, problems = registry()
    for p in problems:
        print("  REGISTRY PROBLEM  %s" % p)

    # ------------------------------------------------------------------ REGISTERED (x3)
    for cid in CLAIMS:
        c = reg.get(cid)
        why = []
        if c is None:
            why.append("no claim with this id in docs/HANDOFF.md")
        else:
            if c.get("count") is None:
                why.append("carries no count")
            if not c.get("count_re"):
                why.append("carries no count_re")
            else:
                try:
                    if re.compile(c["count_re"]).groups != 1:
                        why.append("count_re captures %d group(s), needs exactly 1"
                                   % re.compile(c["count_re"]).groups)
                except re.error as e:
                    why.append("count_re does not compile (%s)" % e)
            if "no count" in (c.get("note") or ""):
                why.append("its note still says it prints no count -- stale residue")
        record(cid, "REGISTERED", not why, "; ".join(why) or "count=%s  count_re=%r"
               % (c.get("count"), c.get("count_re")))

    # ------------------------------------------------------------------ verify-layout.sh
    cid = "verify-layout.sh"
    c = reg.get(cid, {})
    rx = c.get("count_re")
    if rx:
        rc0, out0 = wt176_verify(COMMITTED_PDF)
        n0 = count_in(out0, rx)
        with tempfile.TemporaryDirectory() as tmp:
            short = Path(tmp) / "short.pdf"
            want = pdf_minus_one_page(COMMITTED_PDF, short)
            rc1, out1 = wt176_verify(short)
            n1 = count_in(out1, rx)
        record(cid, "DERIVED",
               rc0 == 0 and n0 == c.get("count") and n1 == want == (n0 or 0) - 1 and rc1 != 0,
               "committed PDF -> rc %s, %s pages compared; one page removed -> rc %s, %s"
               % (rc0, n0, rc1, n1))
        if n0 is not None:
            bites_and_control(cid, rx, n0, out0)

    # ---------------------------------------------------------------- redproof-layout.sh
    cid = "redproof-layout.sh"
    c = reg.get(cid, {})
    rx = c.get("count_re")
    if rx:
        rc3, out3 = tally_says(3)
        rc7, out7 = tally_says(7)
        rc0, out0 = tally_says(0)
        rc_full, full = stub_probe_run()
        rc_drop, drop = stub_probe_run(drop_probes=1)
        n_full, n_drop = count_in(full, rx), count_in(drop, rx)
        record(cid, "DERIVED",
               count_in(out3, rx) == 3 and count_in(out7, rx) == 7
               and rc0 == 1 and "NO PROBES REPORTED" in out0
               and rc_full == 0 and n_full == c.get("count")
               and n_drop == (n_full or 0) - 1,
               "tally 3->%s 7->%s 0->rc %s; real script stubbed: %s probes, one call site "
               "removed: %s probes" % (count_in(out3, rx), count_in(out7, rx), rc0,
                                       n_full, n_drop))
        if n_full is not None:
            bites_and_control(cid, rx, n_full, full)

    # ------------------------------------------------------------------- wt170 --verify
    cid = "wt170 --verify"
    c = reg.get(cid, {})
    rx = c.get("count_re")
    if rx:
        rc_clean, clean = wt170_verify()
        with tempfile.TemporaryDirectory() as tmp:
            tsv = Path(tmp) / "promises-adjudicated.tsv"
            victim, heir = tsv_minus_one_row(tsv)
            rc_pert, pert = wt170_verify(tsv)
        n_clean, n_pert = count_in(clean, rx), count_in(pert, rx)
        record(cid, "DERIVED",
               rc_clean == 0 and n_clean == c.get("count")
               and n_pert == (n_clean or 0) - 1,
               "committed corpus -> rc %s, %s rows verified; %s retired to %s -> rc %s, %s"
               % (rc_clean, n_clean, victim, heir, rc_pert, n_pert))
        if n_clean is not None:
            bites_and_control(cid, rx, n_clean, clean)

    # ------------------------------------------------------------------------- the report
    print()
    failures = 0
    for claim, tag, ok, note in RESULTS:
        print("  %-4s %-20s %-11s %s" % ("PASS" if ok else "FAIL", claim, tag, note))
        if not ok:
            failures += 1

    print("\nCOVERAGE (a declared CLAIMS x TAGS matrix, not a scraped one):")
    proven = {(c, t) for c, t, ok, _n in RESULTS if ok}
    stray = {(c, t) for c, t, _o, _n in RESULTS} - {(c, t) for c in CLAIMS for t in TAGS}
    for cell in sorted(stray):
        print("  ERROR   probe claims cell %r, which the matrix does not declare" % (cell,))
        failures += 1
    for c in CLAIMS:
        for t in sorted(TAGS):
            if (c, t) not in proven:
                print("  WEAK    %-20s %-11s declared by the matrix and proven by no probe"
                      % (c, t))
                failures += 1
    total = len(CLAIMS) * len(TAGS)
    print("  %d of %d declared probes proven." % (len(proven & {(c, t) for c in CLAIMS
                                                                for t in TAGS}), total))

    print("\n%s -- %d probe(s), %d failure(s)."
          % ("RED-PROOF PASSED" if failures == 0 else "RED-PROOF FAILED",
             len(RESULTS), failures))
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
