"""RECIPE.md's numbers, held to the committed measurement WITHOUT a TeX toolchain.

`wt173 --verify` is the real guard: it rebuilds and re-measures. But it needs lualatex, so on
any machine without TeX Live -- CI, a fresh clone, a session that has not run preflight --
NOTHING checks the recipe at all, and the strongest guard in the row is the one least often
run. These tests are the cheap half: they hold the committed recipe to the committed
METRICS-MEASURED.json, catch a hand-edited number in either file, and run in milliseconds.

They deliberately do NOT re-measure. A drift between recipe and JSON is caught here; a drift
between the JSON and reality is caught only by --verify, and that division is the point.
"""
import json
import pathlib
import re

REPO = pathlib.Path(__file__).resolve().parent.parent
RECIPE = REPO / "docs" / "deliverable" / "RECIPE.md"
METRICS = REPO / "docs" / "deliverable" / "METRICS-MEASURED.json"
BLOCK = re.compile(r"```wt173-measured\n(.*?)\n```", re.S)

# kept in step with wt173's PROSE_KEYS; a value here must appear in the numbered steps
PROSE_KEYS = ["body.size_pt", "body.leading_pt", "body.measure_pt", "body.chars_per_line",
              "page.margin_left_pt", "page.margin_top_pt", "page.margin_bottom_pt",
              "page.textheight_pt", "page.baseline_grid_lines",
              "display_maths.abovedisplayskip", "display_maths.belowdisplayskip",
              "monospace.max_inline_identifier_chars",
              "monospace.corpus_longest_identifier_chars",
              "headings.section.size_pt", "headings.title.size_pt"]


def _flat(m, prefix=""):
    out = {}
    for k, v in m.items():
        key = prefix + k
        if isinstance(v, dict) and k != "packages":
            out.update(_flat(v, key + "."))
        else:
            out[key] = v
    return out


def _block():
    m = BLOCK.search(RECIPE.read_text(encoding="utf-8"))
    assert m, "RECIPE.md carries no wt173-measured block — its numbers are unheld"
    rows = {}
    for line in m.group(1).splitlines():
        if line.strip() and not line.startswith("#"):
            f = line.split("\t")
            rows[f[0].strip()] = (f[1].strip(), f[2].strip() if len(f) > 2 else "")
    return rows


def test_the_recipe_and_the_measurement_agree():
    fm = _flat(json.loads(METRICS.read_text(encoding="utf-8")))
    for key, (value, _cmd) in _block().items():
        assert key in fm, "%s is in RECIPE.md but not in METRICS-MEASURED.json" % key
        assert str(fm[key]) == value, (
            "%s: RECIPE.md says %r, the committed measurement says %r"
            % (key, value, str(fm[key])))


def test_every_value_carries_the_command_that_prints_it():
    for key, (_value, cmd) in _block().items():
        assert cmd.endswith("--print " + key), (
            "%s carries %r, which does not print %s" % (key, cmd, key))


def test_the_load_bearing_values_are_in_the_prose_a_human_executes():
    doc = BLOCK.sub("", RECIPE.read_text(encoding="utf-8"))
    rows = _block()
    for key in PROSE_KEYS:
        assert key in rows, "%s dropped out of the measured block" % key
        assert rows[key][0] in doc, (
            "%s = %s is in the data block but nowhere in the numbered steps — the recipe a "
            "human reads and the recipe a script checks have drifted apart" % (key, rows[key][0]))


def test_the_recipe_states_values_not_instructions_to_imitate():
    doc = RECIPE.read_text(encoding="utf-8").lower()
    for phrase in ("match the existing", "as before", "similar to", "appropriate", "as needed"):
        assert phrase not in doc, "RECIPE.md contains %r where a value belongs" % phrase
    assert not re.search(r"\b(TODO|TBD|FIXME|XXX)\b", doc, re.I), "RECIPE.md has a placeholder"


def test_the_geometry_in_the_recipe_is_internally_consistent():
    """Arithmetic the recipe asserts about itself, checked without rebuilding anything."""
    fm = _flat(json.loads(METRICS.read_text(encoding="utf-8")))
    lines, leading = fm["page.baseline_grid_lines"], fm["body.leading_pt"]
    assert abs(fm["page.textheight_pt"] - lines * leading) < 0.01, (
        "textheight %s is not %d x %s — the block does not close on the baseline grid"
        % (fm["page.textheight_pt"], lines, leading))
    assert abs(2 * fm["page.margin_left_pt"] + fm["page.textwidth_pt"]
               - fm["page.paperwidth_pt"]) < 0.01, "margins and measure do not span the page"
    assert abs(fm["page.margin_top_pt"] + fm["page.textheight_pt"]
               + fm["page.margin_bottom_pt"] - fm["page.paperheight_pt"]) < 0.01, \
        "top, text and bottom do not span the page height"
    assert fm["page.margin_bottom_pt"] > fm["page.margin_top_pt"], "block is not optically centred"


def test_the_longest_identifier_does_not_fit_inline_which_is_why_step_13_exists():
    fm = _flat(json.loads(METRICS.read_text(encoding="utf-8")))
    assert fm["monospace.corpus_longest_identifier_chars"] > \
        fm["monospace.max_inline_identifier_chars"], (
        "the corpus's longest identifier now fits inline, so RECIPE.md step 13 rests on a "
        "measurement that no longer holds — re-derive the rule rather than keeping it")
    assert fm["monospace.longest_fits_inline"] is False
