"""wealthTensor-97 · P13e's manifest is now checkable by anything that can run Python.

WHY THIS EXISTS
---------------
`docs/deliverable/LAYOUT-MANIFEST.json` carries P13e's entire claim -- 145 pages, their
hashes, the fonts, the manuscripts, the commit the capture came from. Until this file, the
only three things that could notice a hand-edit were `verify-layout.sh`,
`redproof-layout.sh` and `wt173 --verify`, and ALL THREE need lualatex, pandoc and a clean
git worktree. CI could not check it. A fresh clone could not check it. The container could
not check it. Any session that had not run preflight could not check it. A file nothing
cheap can check is a file that drifts.

WHAT A FAILURE HERE MEANS. Not "a script broke." Either the manifest was edited by hand
away from the deliverable it describes, or one of the registries beside it moved without
the capture being regenerated. The repair is to regenerate the manifest
(`wt176_layout_manifest.py --emit`, then `verify-layout.sh`), never to relax an assertion.

WHAT IT DOES NOT DO, said plainly so nobody mistakes its scope: it cannot tell whether the
manifest describes REALITY. Only a rebuild can, and that is `verify-layout.sh`'s job. This
holds the manifest to ITSELF, to `FONTS.tsv`, to the manuscripts on disk, to the committed
PDF's bytes, and to the commit it names. That division is the same one
`test_recipe_is_held_to_the_measurement.py` documents for RECIPE.md, and for the same
reason: the cheap half must exist, or the expensive half is the only half that runs, which
means in practice that nothing runs.

The load-bearing test is `test_every_declared_failure_has_been_seen_red`. A guard green over
a correct file proves nothing about whether any assertion in it can bite; the red-proof
breaks the manifest twenty-five ways and requires the specific tag each time.
"""

import io
import json
import subprocess
import sys
import time
from contextlib import redirect_stdout
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
GUARD = SCRIPTS / "wt179_manifest_guard.py"
REDPROOF = SCRIPTS / "redproof_wt179_manifest.py"
MANIFEST = ROOT / "docs" / "deliverable" / "LAYOUT-MANIFEST.json"

sys.path.insert(0, str(SCRIPTS))
import wt179_manifest_guard as G  # noqa: E402


def _py(script, *args):
    return subprocess.run([sys.executable, str(script), *args],
                          capture_output=True, text=True, cwd=str(ROOT))


def test_the_guard_is_green_over_the_committed_manifest() -> None:
    r = _py(GUARD)
    assert r.returncode == 0, (
        "scripts/wt179_manifest_guard.py is red on the committed manifest. Its output names "
        "the TAG and the exact disagreement; regenerate the manifest rather than relaxing "
        f"the check.\n\n{r.stdout[-4000:]}\n{r.stderr[-2000:]}")
    assert "0 finding(s)" in r.stdout


def test_it_needs_no_toolchain_and_is_cheap_enough_to_always_run() -> None:
    """The whole point: this must run where lualatex is not.

    The budget is deliberately loose. Measured cost is about 0.07s, so 3s is a ~40x margin.
    `-96` watched a CLOSED lane get downgraded by a 1.6x timeout margin under concurrent
    load -- a threshold that close measures the machine, not the artefact.
    """
    t0 = time.monotonic()
    r = _py(GUARD, "--json")
    elapsed = time.monotonic() - t0
    assert r.returncode == 0, r.stdout[-2000:]
    assert elapsed < 3.0, f"the cheap guard took {elapsed:.2f}s; it is no longer cheap"
    report = json.loads(r.stdout)
    assert report["findings"] == []
    assert report["checks_run"] == len(G.CHECKS) == 10, (
        "the number of checks moved. That is allowed -- but the handoff registers this "
        "count, so move the claim in the same commit.")
    assert (report["pages"], report["fonts"], report["manuscripts"]) == (145, 16, 4)


def test_every_declared_failure_has_been_seen_red() -> None:
    r = _py(REDPROOF)
    assert r.returncode == 0, (
        "a probe in scripts/redproof_wt179_manifest.py is not proven. A guard nobody has "
        f"watched fail is a decoration.\n\n{r.stdout[-8000:]}")
    assert f"{len(G.TAGS)} of {len(G.TAGS)} declared tags proven" in r.stdout


def test_the_schema_and_the_committed_manifest_agree_on_the_manifests_shape() -> None:
    """The anti-drift surface, asserted directly rather than only through the guard.

    `-95`'s defect was a check that discovered its own scope and under-discovered it in
    silence. The inverse is this: SCHEMA declares the manifest's keys, so a key added to the
    file without a check added to the guard turns this red instead of arriving unexamined.
    """
    m = json.loads(MANIFEST.read_text(encoding="utf-8"))
    assert set(m) == set(G.SCHEMA), (
        "the manifest and wt179's SCHEMA disagree.\n"
        f"  in the file, not declared: {sorted(set(m) - set(G.SCHEMA))}\n"
        f"  declared, not in the file: {sorted(set(G.SCHEMA) - set(m))}\n"
        "Write the check for the new key, then add it to SCHEMA.")


def test_a_hand_edited_manifest_is_refused_through_the_cli(tmp_path) -> None:
    """The red-proof drives `check_all` directly, so the command-line path -- the one CI
    and every future session actually invoke -- gets its own proof that it goes red."""
    m = json.loads(MANIFEST.read_text(encoding="utf-8"))
    m["page_count"] = m["page_count"] + 1          # the single most likely hand-edit
    edited = tmp_path / "LAYOUT-MANIFEST.json"
    edited.write_text(json.dumps(m), encoding="utf-8")
    r = _py(GUARD, "--manifest", str(edited))
    assert r.returncode == 1, "the CLI accepted a manifest whose page_count is a lie"
    assert "PAGE-COUNT-DISAGREES" in r.stdout, r.stdout[-2000:]


def test_the_coverage_report_is_not_vacuous() -> None:
    """A declared tag with no probe must print WEAK and turn the red-proof red.

    Proven by adding a tag the guard declares and nothing provokes, in this process only.
    Run out-of-process as well by deleting a probe: exactly one line goes WEAK, 24 of 25.
    """
    sys.path.insert(0, str(SCRIPTS))
    import redproof_wt179_manifest as RP

    RP.RESULTS.clear()
    RP.BASELINE_TAGS.clear()
    G.TAGS["A-TAG-NOBODY-PROBES"] = "planted by the suite, removed below"
    try:
        buf = io.StringIO()
        with redirect_stdout(buf):
            rc = RP.main()
        out = buf.getvalue()
    finally:
        G.TAGS.pop("A-TAG-NOBODY-PROBES", None)
        RP.RESULTS.clear()
        RP.BASELINE_TAGS.clear()
    assert rc == 1, "an unprobed tag did not turn the red-proof red"
    assert "WEAK    A-TAG-NOBODY-PROBES" in out, out[-3000:]


def test_a_probe_naming_a_tag_the_guard_cannot_emit_is_an_error() -> None:
    """The other direction of the same binding: the red-proof may not claim coverage of a
    verdict that does not exist. Without this, a renamed tag would leave a probe quietly
    proving nothing while the coverage line still read full."""
    sys.path.insert(0, str(SCRIPTS))
    import redproof_wt179_manifest as RP

    RP.RESULTS.clear()
    RP.BASELINE_TAGS.clear()
    real = G.TAGS.pop("BAD-CHARS")
    try:
        buf = io.StringIO()
        with redirect_stdout(buf):
            rc = RP.main()
        out = buf.getvalue()
    finally:
        G.TAGS["BAD-CHARS"] = real
        RP.RESULTS.clear()
        RP.BASELINE_TAGS.clear()
    assert rc == 1
    assert "ERROR   probe claims tag 'BAD-CHARS'" in out, out[-3000:]


def test_the_guard_refuses_to_emit_an_undeclared_tag() -> None:
    assert G._tag("NOT-A-REAL-TAG", "x").startswith("UNREGISTERED-TAG")
    assert G._tag("BAD-SHA", "x") == "BAD-SHA x"
