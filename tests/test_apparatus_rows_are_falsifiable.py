"""Every writable apparatus row must be FALSIFIABLE, and the suite is where that is enforced.

wealthTensor-54. The board went 27/36 green, then 40 sub-rows green, and none of it meant
anything until a mutation was applied and the row was watched to go red. The first run of
`scripts/redproof_apparatus.py` reported five rows WEAK; all five were the harness's own
mis-aimed mutations, which is the cheaper failure but not the harmless one -- a mutation
that does not mutate reports a sound guard as weak, and invites the next session to
"strengthen" a check that was already right.

These tests keep three things true:
  1. the harness still leaves the working tree byte-for-byte identical (reversibility, tested
     rather than trusted);
  2. no apparatus row survives its own mutation;
  3. the CENSUS -- a paper that acquires `cmd:` apparatus rows cannot quietly skip red-proofing.
     This mirrors `test_defensive_count.py::test_every_manuscript_in_the_estate_is_covered`,
     which fired on Paper IV exactly as designed.
"""
import hashlib
import pathlib
import re
import subprocess
import sys

import pytest

REPO = pathlib.Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "redproof_apparatus.py"
TSV = REPO / "docs" / "done-criteria.tsv"

sys.path.insert(0, str(REPO / "scripts"))
import redproof_apparatus as rp  # noqa: E402


def _digests():
    return {k: hashlib.sha256(v.read_bytes()).hexdigest() for k, v in rp.PAPER.items()}


def test_no_apparatus_row_survives_its_own_mutation():
    before = _digests()
    r = subprocess.run([sys.executable, str(SCRIPT)], cwd=str(REPO),
                       stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    out = r.stdout.decode("utf-8", "replace")
    assert before == _digests(), (
        "redproof_apparatus.py did NOT restore the manuscripts byte-for-byte. "
        "Recover with: git checkout -- docs/papers/\n" + out)
    assert r.returncode == 0, (
        "an apparatus row survived the mutation that should have broken it -- it is a "
        "decoration, not a criterion:\n" + out)
    assert "0 survived (WEAK)" in out, out


def test_every_paper_with_cmd_rows_is_red_proofed():
    """The census. A paper with writable apparatus rows and no entry in the harness would
    be scored by checks nobody has ever seen fail."""
    prefixes = set()
    for line in TSV.read_text(encoding="utf-8").split("\n"):
        f = line.split("\t")
        # A sub-row id is P<digit><letter> -- matched as a SHAPE. Slicing f[0][:2] read
        # "P11" (a CORPUS row) as family "P1", which was harmless only by luck.
        if len(f) == 4 and f[3].startswith("cmd:") and re.fullmatch(r"P[0-9][a-z]", f[0]):
            prefixes.add(f[0][:2])
    missing = sorted(p for p in prefixes if p not in rp.PAPER)
    assert not missing, (
        "these row families have cmd: apparatus rows but no manuscript registered in "
        "redproof_apparatus.PAPER, so their greens are unproven: %s" % missing)


@pytest.mark.parametrize("prefix", sorted(rp.PAPER))
def test_each_manuscript_has_a_full_row_family(prefix):
    """A paper measured by four legs is not measured by the same bar as one measured by
    twelve. -54 found Paper II carrying zero sub-rows while III and IV carried thirteen."""
    have = {rid[len(prefix):] for rid in
            (l.split("\t")[0] for l in TSV.read_text(encoding="utf-8").split("\n")
             if len(l.split("\t")) == 4)
            if re.fullmatch(re.escape(prefix) + r"[a-z]", rid)}
    required = set("abcdefghijklm")
    assert required <= have, "%s is missing apparatus rows: %s" % (
        prefix, sorted(required - have))
