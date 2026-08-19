"""wealthTensor-95 · P13f is bound to the suite, not to a handoff.

WHY THIS EXISTS
---------------
`WT-116`, banked long before this session: *a procedure that lives in a ledger entry is a
procedure the next session re-derives.* P13f's guard and its red-proof are exactly the kind
of thing that otherwise survives only as a line of ritual in a handoff — *"and run the
figure guard, and say its RC"* — which is one forgetful session away from silence.

WHAT A FAILURE HERE MEANS. Not "a script broke." It means either a figure has entered the
corpus without a committed script and committed numbers behind it, or the manifest that is
supposed to notice has rotted. The fix is to list the figure or repair the manifest, never
to relax an assertion.

The corpus has zero figures today, so three of these tests are cheap. The fourth is the one
that matters: it re-runs the red-proof, which manufactures figures in a temp directory and
requires the guard to go red on each — because a green over an empty corpus proves nothing
about a guard nobody has watched fail.
"""

import json
import pathlib
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
GUARD = ROOT / "scripts" / "wt177_figure_guard.py"
REDPROOF = ROOT / "scripts" / "redproof_wt177_figures.py"
MANIFEST = ROOT / "docs" / "deliverable" / "FIGURES.tsv"
RECEIPT = ROOT / "docs" / "deliverable" / "FIGURES-MEASURED.json"


def _py(script, *args):
    return subprocess.run([sys.executable, str(script), *args],
                          capture_output=True, text=True, cwd=str(ROOT))


def test_the_guard_is_green_over_the_live_corpus() -> None:
    r = _py(GUARD)
    assert r.returncode == 0, (
        "scripts/wt177_figure_guard.py is red. Its output names the FAIL[TAG] and the line; "
        f"list the figure or repair the manifest, and do not relax this.\n\n{r.stdout[-4000:]}")


def test_the_p13f_criterion_passes_and_a_header_only_file_would_not() -> None:
    """The row's own awk, both ways. `n>=1` is the clause that kills the empty manifest —
    if it is ever loosened, this test is what says so."""
    crit = (r"""awk -F'\t' 'NR>1 && $1!~/^#/{if(system("test -f " $2)) exit 1; n++} """
            r"""END{exit !(n>=1)}' """)
    ok = subprocess.run(["bash", "-c", f"test -f {MANIFEST} && {crit} {MANIFEST}"],
                        capture_output=True, cwd=str(ROOT))
    assert ok.returncode == 0, "the committed FIGURES.tsv does not satisfy the P13f criterion"

    import tempfile
    with tempfile.TemporaryDirectory() as tmp:
        empty = pathlib.Path(tmp) / "header-only.tsv"
        empty.write_text("figure\tscript\tsource\n", encoding="utf-8")
        bad = subprocess.run(["bash", "-c", f"test -f {empty} && {crit} {empty}"],
                             capture_output=True, cwd=str(ROOT))
        assert bad.returncode != 0, (
            "a header-only FIGURES.tsv now PASSES the P13f criterion. That is the vacuous "
            "close the whole row exists to prevent — restore the n>=1 clause.")


def test_every_guard_check_has_been_seen_red() -> None:
    r = _py(REDPROOF)
    assert r.returncode == 0, (
        "a probe in scripts/redproof_wt177_figures.py is not PROVEN. A guard check nobody "
        f"has watched fail is a decoration.\n\n{r.stdout[-6000:]}")


def test_the_receipt_still_matches_what_the_guard_measures() -> None:
    """`-94`'s third trap, pointed at a manifest instead of a build directory: a committed
    artefact is STATE, and state drifts. The shas are provenance and are allowed to move
    when a manuscript is edited; the figure COUNT and the corpus LIST are the claim, and
    they are held here."""
    assert RECEIPT.is_file(), "docs/deliverable/FIGURES-MEASURED.json is missing"
    committed = json.loads(RECEIPT.read_text(encoding="utf-8"))
    live = json.loads(_py(GUARD, "--json").stdout)
    assert [m["path"] for m in committed["manuscripts"]] == \
           [m["path"] for m in live["manuscripts"]], (
        "the corpus moved under the receipt. Re-run: python3 scripts/wt177_figure_guard.py --emit")
    assert committed["figure_references_total"] == live["figure_references_total"], (
        f"the receipt records {committed['figure_references_total']} figure reference(s) and "
        f"the guard now measures {live['figure_references_total']}. Re-run: "
        f"python3 scripts/wt177_figure_guard.py --emit")
    assert committed["pdf"]["image_xobjects"] == live["pdf"]["image_xobjects"], (
        "the built PDF's image count moved under the receipt. Re-run --emit and explain why "
        "the deliverable gained or lost an image.")
