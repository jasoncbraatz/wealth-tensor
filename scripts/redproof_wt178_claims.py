#!/usr/bin/env python3
"""wealthTensor-96 -- the red-proof for G-CLAIMS (scripts/handoff_gate.py).

A GATE THAT HAS NEVER BEEN SHOWN TO BLOCK IS NOT A GATE. This drives the real
`claims_leg()` -- not a copy of its logic -- against handoffs built to fail, and asserts on
the TAG each one produces, never merely on the exit code.

WHY THE TAG AND NOT THE EXIT CODE. `-94` and `-95` both paid for this: a red-proof caught by
a DIFFERENT guard than the one under test proves the wrong thing and is indistinguishable
from success. `-95`'s mutated probe exited 1 because ROOT broke, not because the check bit.
Exit 1 alone would have passed every probe in here for the wrong reason; the tag cannot.

WHY IT IMPORTS CLAIM_TAGS INSTEAD OF SCANNING THE SOURCE. `-95` wrote a coverage check that
regexed a guard's source for its failure tags, found NINE of FOURTEEN, and printed FULL
COVERAGE. A check that DISCOVERS its own scope under-discovers it silently. Here the code
under test DECLARES its scope in CLAIM_TAGS, this file declares which tag each probe proves,
and the two sets are held to each other in both directions: a tag with no probe prints WEAK,
and a probe naming a tag the leg cannot emit is an error. Adding a verdict without a probe
goes red BY CONSTRUCTION.
"""
import contextlib
import io
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import handoff_gate as G  # noqa: E402

FENCE = "---\n"
RESULTS = []


def handoff(frontmatter_body, tmp):
    """Write a throwaway handoff and return its path."""
    p = Path(tmp) / "HANDOFF.md"
    p.write_text(FENCE + frontmatter_body.rstrip("\n") + "\n" + FENCE + "\n# body\n")
    return p


def drive(path, run_slow=False):
    """(exit_code, printed_output) from the REAL leg."""
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        rc = G.claims_leg(run_slow=run_slow, path=str(path))
    return rc, buf.getvalue()


def probe(name, tag, body, expect_rc, run_slow=False, must_contain=(), extra=None):
    """One probe. `tag` is the verdict it exists to prove; it MUST appear in the output."""
    with tempfile.TemporaryDirectory() as tmp:
        body = body.replace("{TMP}", tmp)
        p = handoff(body, tmp)
        rc, out = drive(p, run_slow=run_slow)
        ok = rc == expect_rc and tag in out and all(m in out for m in must_contain)
        note = ""
        if extra is not None:
            extra_ok, note = extra(tmp, rc, out)
            ok = ok and extra_ok
        RESULTS.append((name, tag, ok, rc, expect_rc, note, out))
    return ok


COUNTER = """claims:
  - id: counter
    cmd: bash {TMP}/counter.sh
    rc: 0
"""


def write_counter(tmp, threshold):
    """A command that fails until it has been run `threshold` times. The only honest way to
    build a check that fails once and then passes is to make it actually do that."""
    Path(tmp, "counter.sh").write_text(
        "f=%s/n\nn=$(cat $f 2>/dev/null || echo 0)\nn=$((n+1))\necho $n > $f\n"
        "echo attempt $n\ntest $n -ge %d\n" % (tmp, threshold))


def main():
    print("RED-PROOF wt178 -- G-CLAIMS in scripts/handoff_gate.py")
    print("=" * 78)

    # ---------------------------------------------------------------- the three the card names
    print("\nTHE THREE THE CARD DEMANDS, SAID OUT LOUD:")

    # RP1 -- a handoff asserting TRUE RCs must PASS.
    probe("RP1 true claims PASS", "OK",
          'phase: "`true-thing` RC 0"\n'
          "claims:\n"
          "  - id: true-thing\n"
          "    cmd: true\n"
          "    rc: 0\n",
          expect_rc=0)

    # RP2 -- a handoff asserting a FALSE RC must FAIL, and must have been re-run first.
    with tempfile.TemporaryDirectory() as tmp:
        write_counter(tmp, 99)          # never satisfied: disagrees on every attempt
        probe("RP2 false claim FAILS", "FALSE-CLAIM",
              'phase: "`counter` RC 0"\n' + COUNTER.replace("{TMP}", tmp),
              expect_rc=1, must_contain=("re-running before reporting it",))
        # asserted here, where the counter file is still alive: the leg did not report the
        # claim false until it had asked CLAIM_ATTEMPTS times.
        n = int(Path(tmp, "n").read_text().strip())
        RESULTS.append(("RP2b re-run BEFORE reporting", "FALSE-CLAIM",
                        n == G.CLAIM_ATTEMPTS, n, G.CLAIM_ATTEMPTS,
                        "the false claim was run %d time(s) before it was called false" % n, ""))

    # RP3 -- fail once, then pass: FLAKY, not a false claim.
    with tempfile.TemporaryDirectory() as tmp:
        write_counter(tmp, 2)           # red on attempt 1, green on attempt 2
        p = handoff('phase: "`counter` RC 0"\n' + COUNTER.replace("{TMP}", tmp), tmp)
        rc, out = drive(p)
        good = rc == 2 and "FLAKY" in out and "FALSE-CLAIM" not in out
        RESULTS.append(("RP3 flaky is FLAKY not FALSE", "FLAKY", good, rc, 2,
                        "and the words FALSE-CLAIM do not appear", out))

    # ---------------------------------------------------------------- every other tag
    probe("skipped slow is not a pass", "SKIPPED-SLOW",
          'phase: "`slowthing` RC 0"\n'
          "claims:\n  - id: slowthing\n    cmd: true\n    rc: 0\n    slow: true\n",
          expect_rc=2)

    probe("slow claims run with --claims-all", "OK",
          'phase: "`slowthing` RC 0"\n'
          "claims:\n  - id: slowthing\n    cmd: true\n    rc: 0\n    slow: true\n",
          expect_rc=0, run_slow=True)

    probe("prose claims, no registry", "MISSING-REGISTRY",
          'phase: "`wt172 --verify` RC 0"\n', expect_rc=1)

    probe("a line it cannot parse", "PARSE-REFUSED",
          'phase: "`x` RC 0"\n'
          "claims:\n  - id: x\n    cmd: true\n    rc: 0\n      wonky: yes\n", expect_rc=1)

    probe("a claim with no rc", "MISSING-FIELD",
          'phase: "`x` RC 0"\n' "claims:\n  - id: x\n    cmd: true\n", expect_rc=1)

    probe("a key the leg does not define", "UNKNOWN-FIELD",
          'phase: "`x` RC 0"\n'
          "claims:\n  - id: x\n    cmd: true\n    rc: 0\n    rcx: 0\n", expect_rc=1)

    probe("two claims, one id", "DUPLICATE-ID",
          'phase: "`x` RC 0"\n'
          "claims:\n  - id: x\n    cmd: true\n    rc: 0\n  - id: x\n    cmd: true\n    rc: 0\n",
          expect_rc=1)

    probe("rc that is not an integer", "BAD-INT",
          'phase: "`x` RC 0"\n' "claims:\n  - id: x\n    cmd: true\n    rc: zero\n", expect_rc=1)

    probe("slow that is neither true nor false", "BAD-BOOL",
          'phase: "`x` RC 0"\n'
          "claims:\n  - id: x\n    cmd: true\n    rc: 0\n    slow: maybe\n", expect_rc=1)

    probe("count_re that does not compile", "BAD-COUNT-RE",
          'phase: "`x` RC 0"\n'
          "claims:\n  - id: x\n    cmd: true\n    rc: 0\n    count: 1\n    count_re: ([0-9]+\n",
          expect_rc=1)

    probe("count_re with two groups", "BAD-COUNT-RE",
          'phase: "`x` RC 0"\n'
          "claims:\n  - id: x\n    cmd: true\n    rc: 0\n    count: 1\n"
          "    count_re: ([0-9]+) (passed)\n", expect_rc=1)

    probe("a count the output does not carry", "COUNT-NOT-FOUND",
          'phase: "`x` RC 0"\n'
          "claims:\n  - id: x\n    cmd: true\n    rc: 0\n    count: 5\n"
          "    count_re: ([0-9]+) passed\n",
          expect_rc=1, must_contain=("FALSE-CLAIM",))

    probe("a piped command may not be registered", "PIPED-CLAIM",
          'phase: "`x` RC 0"\n'
          "claims:\n  - id: x\n    cmd: echo hi | cat\n    rc: 0\n", expect_rc=1)

    probe("prose asserts more than the registry declares", "UNREGISTERED-CLAIM",
          'phase: "`declared` RC 0 and `undeclared` RC 0"\n'
          "claims:\n  - id: declared\n    cmd: true\n    rc: 0\n", expect_rc=1)

    # TIMEOUT: the only probe that changes a module constant, and it puts it back.
    old = G.CLAIM_TIMEOUT
    G.CLAIM_TIMEOUT = 1
    try:
        probe("a command that never returns", "TIMEOUT",
              'phase: "`x` RC 0"\n' "claims:\n  - id: x\n    cmd: sleep 30\n    rc: 0\n",
              expect_rc=1)
    finally:
        G.CLAIM_TIMEOUT = old

    # UNREGISTERED-TAG: the enforcement point is _tag() itself, so it is probed directly.
    msg = G._tag("NOT-A-REAL-TAG", "hello")
    RESULTS.append(("an undeclared tag cannot escape", "UNREGISTERED-TAG",
                    msg.startswith("UNREGISTERED-TAG"), 0, 0, msg[:70], ""))

    # ---------------------------------------------------------------- report
    print("\nPROBES:")
    failures = 0
    for name, tag, ok, rc, want, note, _out in RESULTS:
        print("  %-4s %-34s %-19s (rc %s, wanted %s) %s"
              % ("PASS" if ok else "FAIL", name, tag, rc, want, note))
        if not ok:
            failures += 1

    print("\nCOVERAGE (declared by the code under test, not scraped from it):")
    probed = {t for _, t, _, _, _, _, _ in RESULTS}
    stray = probed - set(G.CLAIM_TAGS)
    for t in sorted(stray):
        print("  ERROR   probe claims tag %r, which CLAIM_TAGS does not declare" % t)
        failures += 1
    weak = sorted(set(G.CLAIM_TAGS) - probed)
    for t in weak:
        print("  WEAK    %-19s declared by CLAIM_TAGS and proven by no probe" % t)
        failures += 1
    print("  %d of %d declared tags proven by a probe."
          % (len(set(G.CLAIM_TAGS) & probed), len(G.CLAIM_TAGS)))

    print("\n%s -- %d probe(s), %d failure(s)."
          % ("RED-PROOF PASSED" if failures == 0 else "RED-PROOF FAILED",
             len(RESULTS), failures))
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
