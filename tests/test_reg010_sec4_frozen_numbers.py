"""REG-010 §4's fifteen frozen numbers — the freeze, and the document side of it.

WHAT THIS IS, AND WHAT THE CONTROL SAID BEFORE IT WAS WRITTEN
-------------------------------------------------------------
`REG-010` §4 is a literal list of fifteen quantities the estate *"may not move"*.
`CONSTRAINT-INVENTORY-001` §3.2 ranked it first in cell (b) on the strength of a prose
claim — **"twelve of fifteen unpinned"** — that nobody had ever measured. `-46` measured
it first, per `-43`'s rule, on a scratch copy: each of the fifteen moved in `data/`, the
whole suite run.

    ARTIFACT SIDE: 14 of 15 already went RED. The prose claim was wrong by eleven.

That is `-45`'s finding one column further right: a *coverage* sentence, like a `source`
cell and like the `machine` column before it, is a claim nobody verifies. So this file is
NOT the fifteen-assertion chore the tee-up described. It is two things:

  1. **The freeze proper.** Fourteen of the fifteen are caught today only as a side effect
     of instrument-reproduces-itself tests. Those catch a hand-edit of an artifact; they
     do NOT catch a *legitimately re-derived* number, which is the failure mode §4 names.
     A literal freeze is the thing that says *this number, this value, still*.
  2. **The document side, which was the real hole.** The same control moved each number in
     the PROSE ONLY, leaving every artifact untouched. `RESULT-*` documents are the record
     a reader reads. See `test_the_documents_still_report_the_numbers_the_artifacts_hold`.

THE PARSE, STATED BECAUSE §4 IS A SENTENCE AND NOT A TABLE
-----------------------------------------------------------
§4's list is prose, and two readings of it give fifteen items:

  (A) split `Ψ = 0.6586 and its clustered interval` as ONE item and `the 110 and the 133
      of the band counts` as TWO;
  (B) split the first as TWO and the second as ONE.

`FIFTEEN` below is reading (A) — chosen because the interval is not a number that can move
independently of Ψ (the instrument recomputes both from one bootstrap), while 110 and 133
are counts from two different runs over two different cycle sets and have moved
independently once already (`RESULT-REG-009-band-count.md`'s 2026-08-14 amendment). Both
readings freeze the same sixteen underlying quantities; only the bracketing differs, and
`test_section_4_still_says_what_this_file_read` pins the sentence itself so a reword is
red under either reading.

`-42`: THE ANTECEDENT IS ASSERTED. §4's freeze arrives with a clause — REG-010 *"writes
one new artifact of its own and overwrites nothing"*. A freeze on numbers in files that
could be deleted is an absence guard (`-44`), so the artifacts are asserted to exist and
to be distinct files before their contents are read.
"""

from __future__ import annotations

import copy
import json
import re
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
DOCS = ROOT / "docs" / "preregistration"
SCRIPTS = ROOT / "scripts"

sys.path.insert(0, str(SCRIPTS))

REG_010 = DOCS / "REG-010-p3-half-integer-banding.md"
SECTION_4 = "## 4 · What this may not move"

# --------------------------------------------------------------------------------------
# §4, verbatim. Whitespace-normalised because the sentence is hard-wrapped; nothing else
# is normalised, so a reword — including a number moved IN THE REGISTRATION — is red.
# --------------------------------------------------------------------------------------
SECTION_4_SENTENCE = (
    "The 683 pairs, the 428 distinct pairs, the 665 admissible rows, Ψ = 0.6586 and its "
    "clustered interval, A, S, Ψ_rect and Ψ_rect(α̂), α̂, the verdicts on P1, P2, P3 and "
    "P4, REG-009's numbering, the 151 tier-0 events, the 98 firms, the 110 and the 133 of "
    "the band counts, and every artifact under `data/` that a committed test asserts "
    "against."
)

ANTECEDENT = "REG-010 writes **one new artifact of its own** and overwrites nothing"

FIFTEEN = (
    "The 683 pairs",
    "the 428 distinct pairs",
    "the 665 admissible rows",
    "Ψ = 0.6586 and its clustered interval",
    "A",
    "S",
    "Ψ_rect",
    "Ψ_rect(α̂)",
    "α̂",
    "the verdicts on P1, P2, P3 and P4",
    "REG-009's numbering",
    "the 151 tier-0 events",
    "the 98 firms",
    "the 110",
    "the 133 of the band counts",
)

# --------------------------------------------------------------------------------------
# The frozen values. These are LITERALS on purpose: a check that only asserts the document
# agrees with the artifact is a tautology in measurement's clothing (`-38`) — it goes green
# when both move together, which is exactly what a re-run does.
# --------------------------------------------------------------------------------------
PSI_CELL = {
    "n": 683, "n_admissible": 665,
    "A": 0.9736456808199122,
    "psi": 0.6586466165413534,
    "ci_lo": 0.6210514299447248,
    "ci_hi": 0.6964319079649797,
    "distinct_pairs": 428,
}
S_R_MID = [0.1390922401171303, 95, 683]
PSI_RECT = {
    "calibration": {"alpha": 0.05, "rises_of_admissible": None, "admissible_share": 0.0},
    "extension": {"alpha": 0.35, "rises_of_admissible": 0.99733125, "admissible_share": 1.0},
    "measured": {"alpha": 0.408, "rises_of_admissible": 0.998, "admissible_share": 1.0},
}
ALPHA_HAT = 0.408
ALPHA_HAT_CI = [0.383, 0.432]
VERDICTS = {"P1": True, "P2": True, "P3": False, "P4": True}
REG_009_NUMBERING = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)
EVENTS_TOTAL = 151
FIRMS = 98
JOINABLE_TWO_CYCLE = 110
JOINABLE_NINE_CYCLE = 133

REG_009_DOC = "RESULT-REG-009.md"
BAND_COUNT_DOC = "RESULT-REG-009-band-count.md"
FILLED_DOC = "RESULT-REG-009-band-count-filled.md"


# ======================================================================================
# The world, loaded once — and the check, a PURE function over it so the non-vacuity
# test can move a number without touching the working tree.
# ======================================================================================
@pytest.fixture(scope="module")
def world():
    return load_world()


def load_world() -> dict:
    """Missing subjects are loaded as EMPTY rather than raised on. Deleting the file is
    one of the moves the freeze exists to catch (`-44`: an absence guard cannot enforce
    *this value, still*), and a fixture that explodes turns that catch into twenty
    collection errors with `test_the_artifacts_...`'s message buried in them."""
    def js(name, empty):
        p = DATA / name
        return json.loads(p.read_text()) if p.is_file() else empty

    return {
        "reg009": js("reg-009-result.json",
                     {"psi": {"pooled|R_MID|raw": {}}, "counts": {}, "S": {},
                      "psi_rect": {}, "stopping": {}, "predictions": {}}),
        "bandcount": js("reg-009-band-count.json", {}),
        "filled": js("reg-009-band-count-filled.json", {"two_cycle": {}}),
        "reg010": js("reg-010-half-integer-banding.json",
                     {"psi": {"pooled|R_MID|raw": {}}}),
        "firms": recomputed_tier0_firms(),
        "numbering": reg009_section_numbers(),
        "docs": {name: ((DOCS / name).read_text() if (DOCS / name).is_file() else "")
                 for name in (REG_009_DOC, BAND_COUNT_DOC, FILLED_DOC)},
    }


def recomputed_tier0_firms() -> int:
    """The 98 is the ONE frozen number with no field in any artifact — it exists only as
    a numeral in prose. So it is recomputed from the committed filings through the
    instrument's own pure functions, exactly as `test_reg009_band_count` recomputes the
    151 and the 110, and the prose is bound to THAT rather than to a retyped literal."""
    import reg009_band_count as inst

    events = inst.load_events(ROOT, inst.EVENTS_SRC)
    return len({e["cik"] for e in events if e["tier"] == 0})


def reg009_section_numbers() -> tuple[int, ...]:
    text = (DOCS / "REG-009-p3-lifetime-sourced-delta.md").read_text()
    return tuple(int(n) for n in re.findall(r"^## (\d+) · ", text, re.M))


MISSING = "<missing>"


def violations(w: dict) -> dict[str, list[str]]:
    """Every frozen number checked at every site that records it.

    Returns {item from §4: [what moved]}. Empty dict is the only passing state.
    """
    v: dict[str, list[str]] = {}

    def bad(item: str, msg: str):
        v.setdefault(item, []).append(msg)

    r9, bc, fi, r10 = w["reg009"], w["bandcount"], w["filled"], w["reg010"]
    cell = r9["psi"]["pooled|R_MID|raw"]
    r10cell = r10["psi"]["pooled|R_MID|raw"]
    docs = w["docs"]

    # -- 1..5, 7: the primary Ψ cell, at both of its artifact homes ---------------------
    for item, key in (("The 683 pairs", "n"),
                      ("the 428 distinct pairs", "distinct_pairs"),
                      ("the 665 admissible rows", "n_admissible"),
                      ("Ψ = 0.6586 and its clustered interval", "psi"),
                      ("Ψ = 0.6586 and its clustered interval", "ci_lo"),
                      ("Ψ = 0.6586 and its clustered interval", "ci_hi"),
                      ("A", "A")):
        want = PSI_CELL[key]
        if cell.get(key, MISSING) != want:
            bad(item, f"reg-009-result.json psi[pooled|R_MID|raw].{key}: "
                      f"{cell.get(key, MISSING)!r} != {want!r}")
        # REG-010's own artifact restates the cell: BESIDE, never instead of (`-32`).
        if r10cell.get(key, MISSING) != want:
            bad(item, f"reg-010-half-integer-banding.json psi[pooled|R_MID|raw].{key}: "
                      f"{r10cell.get(key, MISSING)!r} != {want!r}")

    if r9["counts"].get("pairs_pooled", MISSING) != PSI_CELL["n"]:
        bad("The 683 pairs", f"reg-009-result.json counts.pairs_pooled: "
                             f"{r9['counts'].get('pairs_pooled', MISSING)!r} != "
                             f"{PSI_CELL['n']!r}")

    # -- 6: S ---------------------------------------------------------------------------
    if r9["S"].get("R_MID", MISSING) != S_R_MID:
        bad("S", f"reg-009-result.json S.R_MID: "
                 f"{r9['S'].get('R_MID', MISSING)!r} != {S_R_MID!r}")

    # -- 7, 8: Ψ_rect, and Ψ_rect at α̂ ---------------------------------------------------
    for arm in ("calibration", "extension"):
        if r9["psi_rect"].get(arm, MISSING) != PSI_RECT[arm]:
            bad("Ψ_rect", f"reg-009-result.json psi_rect.{arm}: "
                          f"{r9['psi_rect'].get(arm, MISSING)!r} != {PSI_RECT[arm]!r}")
    if r9["psi_rect"].get("measured", MISSING) != PSI_RECT["measured"]:
        bad("Ψ_rect(α̂)", f"reg-009-result.json psi_rect.measured: "
                          f"{r9['psi_rect'].get('measured', MISSING)!r} != "
                          f"{PSI_RECT['measured']!r}")
    if r9["stopping"].get("psi_rect_alpha_hat", MISSING) != \
            PSI_RECT["measured"]["rises_of_admissible"]:
        bad("Ψ_rect(α̂)", "reg-009-result.json stopping.psi_rect_alpha_hat: "
                          f"{r9['stopping'].get('psi_rect_alpha_hat', MISSING)!r} != "
                          f"{PSI_RECT['measured']['rises_of_admissible']!r}")

    # -- 9: α̂, at both artifact homes ----------------------------------------------------
    if r9.get("alpha_hat", MISSING) != ALPHA_HAT:
        bad("α̂", f"reg-009-result.json alpha_hat: "
                  f"{r9.get('alpha_hat', MISSING)!r} != {ALPHA_HAT!r}")
    if r9.get("alpha_hat_ci", MISSING) != ALPHA_HAT_CI:
        bad("α̂", f"reg-009-result.json alpha_hat_ci: "
                  f"{r9.get('alpha_hat_ci', MISSING)!r} != {ALPHA_HAT_CI!r}")
    if r10.get("alpha_hat", MISSING) != ALPHA_HAT:
        bad("α̂", f"reg-010-half-integer-banding.json alpha_hat: "
                  f"{r10.get('alpha_hat', MISSING)!r} != {ALPHA_HAT!r}")

    # -- 10: the four verdicts -----------------------------------------------------------
    if r9["predictions"] != VERDICTS:
        bad("the verdicts on P1, P2, P3 and P4",
            f"reg-009-result.json predictions: {r9['predictions']!r} != {VERDICTS!r}")
    if r9["stopping"].get("agree_within_interval", MISSING) is not False:
        bad("the verdicts on P1, P2, P3 and P4",
            "reg-009-result.json stopping.agree_within_interval is no longer False")

    # -- 11: REG-009's numbering ---------------------------------------------------------
    if w["numbering"] != REG_009_NUMBERING:
        bad("REG-009's numbering",
            f"REG-009's section headings: {w['numbering']!r} != {REG_009_NUMBERING!r}")

    # -- 12, 14, 15: the band counts -----------------------------------------------------
    for label, obj, key, want, item in (
        ("reg-009-band-count.json", bc, "events_total", EVENTS_TOTAL,
         "the 151 tier-0 events"),
        ("reg-009-band-count-filled.json", fi, "events_total", EVENTS_TOTAL,
         "the 151 tier-0 events"),
        ("reg-009-band-count.json", bc, "events_joinable", JOINABLE_TWO_CYCLE,
         "the 110"),
        ("reg-009-band-count-filled.json", fi, "events_joinable", JOINABLE_NINE_CYCLE,
         "the 133 of the band counts"),
    ):
        if obj.get(key, MISSING) != want:
            bad(item, f"{label} {key}: {obj.get(key, MISSING)!r} != {want!r}")
    tc = fi.get("two_cycle", {})
    if tc.get("events_total", MISSING) != EVENTS_TOTAL:
        bad("the 151 tier-0 events",
            f"reg-009-band-count-filled.json two_cycle.events_total: "
            f"{tc.get('events_total', MISSING)!r} != {EVENTS_TOTAL!r}")
    if tc.get("events_joinable", MISSING) != JOINABLE_TWO_CYCLE:
        bad("the 110", f"reg-009-band-count-filled.json two_cycle.events_joinable: "
                       f"{tc.get('events_joinable', MISSING)!r} != "
                       f"{JOINABLE_TWO_CYCLE!r}")

    # -- 13: the 98 firms, which has no artifact field ------------------------------------
    if w["firms"] != FIRMS:
        bad("the 98 firms",
            f"tier-0 firms recomputed from the committed filings: "
            f"{w['firms']!r} != {FIRMS!r}")

    # ==================================================================================
    # THE DOCUMENT SIDE. `-46`'s control moved each number in the prose alone, with every
    # artifact untouched, and the estate did not notice. Each row below is BUILT from the
    # artifact rather than retyped, so the document is bound to the record and not to this
    # file's memory of it.
    # ==================================================================================
    try:
        anchors = _anchors(cell, r9, bc, fi, tc, w)
    except (TypeError, ValueError, KeyError, IndexError):
        # A subject is missing or malformed. The freeze above has already said so in
        # its own words; a formatting crash here would bury that message.
        anchors = []
    for items, doc, anchor, what in anchors:
        if anchor not in docs[doc]:
            for item in items:
                bad(item, f"{doc} no longer carries {what} as the artifacts record "
                          f"it: {anchor!r}")

    return v


def _anchors(cell, r9, bc, fi, tc, w):
    """Document anchors BUILT from the artifacts, never retyped, so the prose is bound
    to the record. An anchor usually carries several of the fifteen — a table row
    carries five — so blame is a SET and the caller reports a moved row under every
    frozen number it carries."""
    return [
        (("The 683 pairs", "the 665 admissible rows", "A",
          "Ψ = 0.6586 and its clustered interval", "the 428 distinct pairs"),
         REG_009_DOC,
         f"| {cell['n']} | {cell['n_admissible']} | {cell['A']:.3f} | {cell['psi']:.4f} |"
         f" [{cell['ci_lo']:.4f}, {cell['ci_hi']:.4f}] | {cell['distinct_pairs']} |",
         "§2's primary Ψ row"),
        (("S", "The 683 pairs"), REG_009_DOC,
         f"| `R_MID` | {r9['S']['R_MID'][0]:.4f} | {r9['S']['R_MID'][1]} | "
         f"{r9['S']['R_MID'][2]} |",
         "the S row"),
        (("the 151 tier-0 events", "the 98 firms", "the 110"), BAND_COUNT_DOC,
         f"**{bc['events_total']} events, {w['firms']} firms, "
         f"{bc['events_joinable']} joining to a disclosed life**",
         "the counts paper III prints"),
        (("the 151 tier-0 events", "the 98 firms", "the 110"), BAND_COUNT_DOC,
         f"{bc['events_total']} property events across {w['firms']} firms … with "
         f"{bc['events_joinable']} of the {bc['events_total']} joining to a disclosed life",
         "§4.7's surviving sentence"),
        (("the 110", "the 133 of the band counts", "the 151 tier-0 events"), FILLED_DOC,
         f"**{tc['events_joinable']} of {fi['events_total']} joinable becomes "
         f"{fi['events_joinable']} of {fi['events_total']}.**",
         "the fill's headline"),
    ]


# ======================================================================================
# §4 itself — the list, and the clause it arrives with
# ======================================================================================
def section_4_block() -> str:
    text = REG_010.read_text()
    m = re.search(rf"^{re.escape(SECTION_4)}\n(.*?)(?=^## )", text, re.S | re.M)
    assert m, f"{REG_010.name} no longer has a section headed {SECTION_4!r}"
    return m.group(1)


def test_section_4_still_says_what_this_file_read():
    """The freeze is only as good as the list, and the list is a sentence in a
    REGISTRATION — which C07's rule says may not be amended after its result commit. A
    number quietly moved in §4 itself would make every assertion below agree with a
    changed rule, so §4's sentence is pinned before anything is read out of it."""
    block = section_4_block()
    got = " ".join(block.split()).split(" The instrument refuses")[0]
    assert got == SECTION_4_SENTENCE, (
        "REG-010 §4's list has been reworded. This is not a test failure to route around: "
        "§4 is a pre-registration, and C07's rule is that a registration may not be "
        "amended after its result commit. Read the diff, then read `RESULT-REG-010`."
    )
    assert ANTECEDENT in " ".join(block.split()), (
        "§4's antecedent — REG-010 writes one new artifact and overwrites nothing — is "
        "gone. The freeze below is scoped by that clause (`-42`)."
    )


def test_section_4_lists_exactly_fifteen_and_each_one_is_checked_below():
    """`-45`: deleting the subject is the cheapest way to silence a check, so the list's
    LENGTH is pinned and every item is asserted to still be in §4's own words."""
    sentence = SECTION_4_SENTENCE
    assert len(FIFTEEN) == 15, f"the parse yielded {len(FIFTEEN)}, not fifteen"
    for item in FIFTEEN:
        assert item in sentence, f"§4 no longer names {item!r}"
    checked = set(violations_keyspace())
    assert checked == set(FIFTEEN), (
        "the fifteen items of §4 and the items this file checks have diverged: "
        f"unchecked={set(FIFTEEN) - checked}, invented={checked - set(FIFTEEN)}"
    )


def violations_keyspace() -> set[str]:
    """Every item `violations` can report — read off the mutation table below, so an item
    that no mutation can trigger cannot be counted as covered."""
    return set(MUTATIONS)


# ======================================================================================
# The antecedent (`-42`), asserted before any content is read
# ======================================================================================
def test_the_artifacts_the_freeze_reads_exist_and_are_distinct_files():
    """`-44`: a freeze on numbers inside a file that could simply be deleted is an
    absence guard, and an absence guard cannot enforce *this value, still*. And §4's own
    clause is that REG-010 wrote ONE NEW artifact and overwrote nothing — so REG-010's
    artifact and REG-009's are asserted to be different files that both exist."""
    paths = [DATA / n for n in ("reg-009-result.json", "reg-009-band-count.json",
                                "reg-009-band-count-filled.json",
                                "reg-010-half-integer-banding.json")]
    for p in paths:
        assert p.is_file(), f"{p.name} is gone; §4's freeze has lost its subject"
    assert len({p.resolve() for p in paths}) == 4, "REG-010 overwrote a REG-009 artifact"
    for name in (REG_009_DOC, BAND_COUNT_DOC, FILLED_DOC):
        assert (DOCS / name).is_file(), f"{name} is gone; the document side has no subject"


# ======================================================================================
# The freeze
# ======================================================================================
def test_every_frozen_number_is_still_where_the_registration_left_it(world):
    v = violations(world)
    assert v == {}, "REG-010 §4 froze these and they moved:\n" + "\n".join(
        f"  · {item}\n      " + "\n      ".join(msgs) for item, msgs in sorted(v.items()))


def test_the_documents_still_report_the_numbers_the_artifacts_hold(world):
    """THE HOLE `-46`'s CONTROL FOUND. Fourteen of the fifteen were already caught in
    `data/`; every one of them could be moved in the `RESULT-*` prose with the artifacts
    untouched and the suite stayed green. The rows below are BUILT from the artifacts, so
    this fails when the document and the record disagree — in either direction."""
    v = violations(world)
    doc_failures = {i: [m for m in msgs if ".md" in m] for i, msgs in v.items()}
    doc_failures = {i: m for i, m in doc_failures.items() if m}
    assert doc_failures == {}, "a RESULT document no longer reports its own record:\n" + \
        "\n".join(f"  · {i}: {m}" for i, m in sorted(doc_failures.items()))


# ======================================================================================
# NON-VACUITY — `-43`: feed the guard its own forbidden move, one per frozen number,
# and require that it names THAT number. Twelve of these were asserted to pass today.
# ======================================================================================
def _mut(path, value):
    def apply(w):
        node = w
        for k in path[:-1]:
            node = node[k]
        node[path[-1]] = value
    return apply


PROSE_SITES: list[tuple[str, str]] = []


def _doc_sub(name, old, new):
    PROSE_SITES.append((name, old))

    def apply(w):
        # If the anchor is already gone, the estate itself has moved it and the freeze
        # tests above are red saying exactly that. Rewriting nothing here keeps the blame
        # on the real failure instead of adding a confusing second one. The mutation can
        # never become a silent no-op on a clean tree (`-37`), because
        # `test_every_prose_mutation_has_a_real_site` asserts every anchor exists.
        w["docs"][name] = w["docs"][name].replace(old, new)
    return apply


MUTATIONS: dict[str, list] = {
    "The 683 pairs": [
        _mut(("reg009", "counts", "pairs_pooled"), 684),
        _mut(("reg009", "psi", "pooled|R_MID|raw", "n"), 684),
        _mut(("reg010", "psi", "pooled|R_MID|raw", "n"), 684),
    ],
    "the 428 distinct pairs": [
        _mut(("reg009", "psi", "pooled|R_MID|raw", "distinct_pairs"), 429),
        _doc_sub(REG_009_DOC, "| [0.6211, 0.6964] | 428 |", "| [0.6211, 0.6964] | 429 |"),
    ],
    "the 665 admissible rows": [
        _mut(("reg009", "psi", "pooled|R_MID|raw", "n_admissible"), 666),
    ],
    "Ψ = 0.6586 and its clustered interval": [
        _mut(("reg009", "psi", "pooled|R_MID|raw", "psi"), 0.6686466165413534),
        _mut(("reg009", "psi", "pooled|R_MID|raw", "ci_lo"), 0.6310514299447248),
        _doc_sub(REG_009_DOC, "| 683 | 665 | 0.974 | 0.6586 |",
                 "| 683 | 665 | 0.974 | 0.6587 |"),
    ],
    "A": [_mut(("reg009", "psi", "pooled|R_MID|raw", "A"), 0.9636456808199122)],
    "S": [
        _mut(("reg009", "S", "R_MID"), [0.1490922401171303, 95, 683]),
        _doc_sub(REG_009_DOC, "| `R_MID` | 0.1391 | 95 | 683 |",
                 "| `R_MID` | 0.1392 | 95 | 683 |"),
    ],
    "Ψ_rect": [
        _mut(("reg009", "psi_rect", "calibration", "admissible_share"), 0.10),
        _mut(("reg009", "psi_rect", "extension", "rises_of_admissible"), 0.98733125),
    ],
    "Ψ_rect(α̂)": [
        _mut(("reg009", "psi_rect", "measured", "rises_of_admissible"), 0.988),
        _mut(("reg009", "stopping", "psi_rect_alpha_hat"), 0.988),
    ],
    "α̂": [
        _mut(("reg009", "alpha_hat"), 0.418),
        _mut(("reg009", "alpha_hat_ci"), [0.393, 0.442]),
        _mut(("reg010", "alpha_hat"), 0.418),
    ],
    "the verdicts on P1, P2, P3 and P4": [
        _mut(("reg009", "predictions", "P3"), True),
        _mut(("reg009", "predictions", "P1"), False),
        _mut(("reg009", "stopping", "agree_within_interval"), True),
    ],
    "REG-009's numbering": [
        _mut(("numbering",), (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13)),
    ],
    "the 151 tier-0 events": [
        _mut(("bandcount", "events_total"), 152),
        _mut(("filled", "events_total"), 152),
        _mut(("filled", "two_cycle", "events_total"), 152),
    ],
    "the 98 firms": [
        _mut(("firms",), 99),
        _doc_sub(BAND_COUNT_DOC, "151 events, 98 firms", "151 events, 99 firms"),
        _doc_sub(BAND_COUNT_DOC, "151 property events across 98 firms",
                 "151 property events across 99 firms"),
    ],
    "the 110": [
        _mut(("bandcount", "events_joinable"), 111),
        _mut(("filled", "two_cycle", "events_joinable"), 111),
    ],
    "the 133 of the band counts": [
        _mut(("filled", "events_joinable"), 134),
        _doc_sub(FILLED_DOC, "becomes 133 of 151.", "becomes 134 of 151."),
    ],
}


def test_the_guard_is_green_on_the_committed_estate(world):
    assert violations(world) == {}


def test_every_prose_mutation_has_a_real_site(world):
    """`-37`: a mutation that does not mutate reports the guard as strong. Every prose
    anchor the non-vacuity table edits is asserted to exist on the committed tree, so a
    `.replace` that quietly matched nothing cannot be read as a passing test."""
    assert PROSE_SITES, "the prose mutations vanished; the document limb is unverified"
    for name, old in PROSE_SITES:
        assert old in world["docs"][name], (
            f"the non-vacuity table edits {old!r} in {name} and it is not there. TWO "
            f"READINGS, AND ONLY ONE IS A STALE TABLE: (1) the estate moved this number, "
            f"in which case `test_every_frozen_number_is_still_where_the_registration_"
            f"left_it` is ALSO red and IS the real failure — read that one and ignore "
            f"this; (2) the document was legitimately reworded around a number that did "
            f"not move, in which case re-anchor this table. If neither, the mutation was "
            f"a no-op and the prose limb has been passing vacuously (`-37`).")


@pytest.mark.parametrize("item", sorted(MUTATIONS), ids=lambda s: s[:38])
def test_moving_each_frozen_number_is_caught_and_named(world, item):
    """One forbidden move per frozen number, each required to name ITS OWN item — not
    merely to make something somewhere go red (`-37`: a mutation that does not mutate
    reports the guard as strong)."""
    for apply in MUTATIONS[item]:
        w = copy.deepcopy(world)
        apply(w)
        v = violations(w)
        assert v != {}, f"{item}: the guard did not notice"
        assert item in v, (
            f"{item}: the guard went red but blamed {sorted(v)} — a guard that cannot "
            f"name what moved sends the next session to the wrong file")


def test_the_prose_limb_is_not_vacuous(world):
    """The document side is the half the control found unguarded, so it gets its own
    non-vacuity: a `RESULT-*` edited alone, every artifact untouched, must be red."""
    for name, old, new in (
        (REG_009_DOC, "| 683 | 665 | 0.974 | 0.6586 |", "| 683 | 665 | 0.974 | 0.6587 |"),
        (BAND_COUNT_DOC, "151 events, 98 firms", "151 events, 99 firms"),
        (FILLED_DOC, "becomes 133 of 151.", "becomes 134 of 151."),
    ):
        w = copy.deepcopy(world)
        _doc_sub(name, old, new)(w)
        v = violations(w)
        assert any(".md" in m for msgs in v.values() for m in msgs), (
            f"{name}: the prose moved alone and the guard stayed green — which is the "
            f"state `-46`'s control measured before this file existed")
