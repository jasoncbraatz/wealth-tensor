"""**C10** · `REG-002` §5 — the re-ask is *"labelled an EXTENSION of E4 throughout, never as E4"*.

THE CONSTRAINT, IN ITS OWN WORDS
---------------------------------
`REG-002` §5 (ERRATA), on E4's registered falsifier turning out to be a share of an empty
set:

    It is reported as vacuous, and the rung question is re-asked at an α where it has a
    domain — **labelled an EXTENSION of E4 throughout, never as E4.**

So the governed object is **THE SUBSTITUTION** — the α = 0.35 re-ask — and not the token
`E4`. That distinction is the whole file, and it is the third session running that the
estate's own sentence about a guard turned out to be the thing that had not been checked.

WHAT THE TEE-UP PROPOSED, AND WHAT MEASURING IT SAID
-----------------------------------------------------
`-49` pre-measured the sites so `-50` would not inherit another unchecked characterisation,
and it was right: `RESULT-REG-002.md` names `E4` four times and **only one of them is the
re-ask**. The other three name E4 *as the registered test*, which is what it is:

    §1's table row   `| **E4** | the disclosed-life rectangle | **0%** … | VACUOUS |`
    §3's heading     `## 3 · E4's falsifier is vacuous at the paper's own calibration …`
    §3's opening     `REG-002 E4 asks what fraction of the **admissible** rectangle …`

A guard requiring every occurrence of `E4` to carry the label is **RED on a compliant
document at three sites** — C21's shape (`-43`), one document over. The discriminator is
therefore the **REFERENT** (`-45`, `-48`): a sentence earns the scan only if it is talking
about the substitution, and `SUBSTITUTION_RE` is what says so.

THE RESOLUTION IS THE LOAD-BEARING CHOICE, AND HERE IT IS THE **SENTENCE**
---------------------------------------------------------------------------
`-49` built C44 at **clause** resolution because at sentence resolution its detector was
red on a compliant document. **C10 runs the other way, and that is measured, not assumed.**
The governed sentence is

    That substitution is labelled in the script, in the manuscript and here as an
    **extension of** REG-002 E4 rather than as the registered test.

and `R4` mutates its tail to *"and here as REG-002 E4, the registered test."* The referent
(*substitution*) and the token (*E4*) are separated by **commas only**. Split on commas —
the natural reading of "clause" — and they fall apart, the detector returns **zero on the
mutation as well as on the real document**, and nothing anywhere is red. Measured, both
ways, before this file had a line in it:

    resolution        real doc     R4 mutant
    sentence                 0             1      <- built at this one
    comma-clause             0             0      <- VACUOUS, and silently so

`test_the_resolution_choice_is_pinned` holds that table down. **`-49`'s tell — the unit is
a design choice and it is where the false verdict lives — is confirmed with its sign
flipped: for C44 the wrong unit was a false RED, for C10 it is a false GREEN.**

Blocks are split on blank lines before sentences are split, so §3's heading (which carries
`E4` and no terminal period) cannot fuse with the paragraph beneath it; soft wraps are
rejoined inside a block, so the governed sentence cannot split at its line break. Both
failure modes were observed while building this.

WHY `own_voice()` IS NOT COPIED WHOLE (`-49`)
----------------------------------------------
`-49`'s finding is that a text-normalising helper is tuned to what its own constraint's
discriminator must read. Asked of C10, one removal at a time:

  * **blockquotes — STRIPPED.** A quotation is not an assertion (`-33`), and the natural
    over-breadth attack here is to blockquote `REG-002` §5's prohibition, which contains
    `E4` twice, into the document it governs.
  * **fenced code — STRIPPED.** A fence is a program, not a claim. `RESULT-REG-002.md`
    carries none today; the removal is a no-op the non-vacuity tests keep honest.
  * **inline code — DELIBERATELY NOT STRIPPED.** This is the removal `-49` was burned by,
    and the answer is different here for a measured reason: this document writes `E4` as
    `**E4**` and as bare `REG-002 E4`, **never in backticks**, so stripping inline code buys
    the discriminator nothing and would silently blind the guard the day someone writes
    `` `E4` ``. An unnecessary removal is not a neutral one.

THE THIRD SURFACE, AND WHY THE TEE-UP'S REMEDY IS NECESSARY BUT NOT SUFFICIENT
-------------------------------------------------------------------------------
C10's witness says the label travels *"in the script, in the manuscript and here"*.

  * **the manuscript is out of scope, and that is a measurement:** `paper-III.md` carries
    `E4` **zero** times, which is what §1's inventory verdict asserted from a reading.
  * **the script surface is real,** and `-49` warned that a naive scan of `scripts/` returns
    ~88 hits *"and essentially all of them are `# noqa: E402`"*, prescribing a word boundary
    that excludes `E40x`. Measured at `11b3b10`: **90 substring hits, 61 of them
    `noqa: E402`, and all 29 survivors are true `\\bE4\\b` matches spread over SEVEN files.**
    Six of those files have nothing to do with `REG-002` — `E4` is this estate's **local
    exhibit label**, reassigned per script (`wt085`'s E4 is *news collapses the continuum*,
    `wt086`'s is *the level*, `reg012`'s is *phase rigidity*). **So the word boundary is
    necessary and NOT sufficient: it removes 61 false positives and leaves 21.** Only
    scoping to `wt088_disclosed_ladder.py` — the one script that runs REG-002 E4 — makes
    the third surface scannable at all. `test_the_third_surface_scope_is_warranted` pins
    that as a number so the scoping cannot decay into a habit nobody can defend.

WHAT THIS CANNOT DO
-------------------
It cannot read English. A sentence that names the substitution and calls it E4 across a
**sentence** boundary — *"The rung question was re-asked at α = 0.35. E4 rises in 99.7%."* —
escapes limb A, and is bounded by limb B only if the label sentence also goes. It does not
scan the manuscript (measured out of scope above) and it does not widen to the other six
scripts (`-47`'s C07 ruling: a guard is not widened past the registration that warrants it).
It says nothing about whether 99.7% is the right number — `tests/test_lag.py` owns §4.4's
closed forms, and duplicating that here would be a coverage claim this file has not made.

Helpers are copied rather than imported, for `-44`'s reason and `-49`'s: an own-voice filter
is tuned to one discriminator, and importing one is how a guard goes vacuous in silence.
"""

from __future__ import annotations

import pathlib
import re

import pytest

ROOT = pathlib.Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs/preregistration"

REG_002 = DOCS / "REG-002-p3-section-4-4-disclosed-ladder.md"
RESULT_002 = DOCS / "RESULT-REG-002.md"
LADDER_SCRIPT = ROOT / "scripts/wt088_disclosed_ladder.py"
MANUSCRIPT = ROOT / "docs/papers/paper-III-dual-tensor/paper-III.md"

# --------------------------------------------------------------------------- warrants

#: `REG-002` §5's own clause. Losing it is a LOST WARRANT — the errata may have been
#: withdrawn — and NOT a violation, so it gets its own message (`-42`).
WARRANT_C10 = "labelled an EXTENSION of E4 throughout, never as E4"

#: `-42`'s second door: the SECTION HEADING. The warrant is bounded to its own section so a
#: renumbered file fails loudly instead of matching a sentence that moved somewhere else.
ANCHOR_REG002_S5 = "## 5 · ERRATA · two falsifiers this registration got wrong"
ANCHOR_RESULT_S3 = (
    "## 3 · E4's falsifier is vacuous at the paper's own calibration, "
    "and that is the bigger finding"
)

# --------------------------------------------------------------------------- own voice


def _strip_fenced_code(text: str) -> str:
    """Drop ```-fenced blocks. A program is not a claim about how a test is labelled."""
    return re.sub(r"^```.*?^```", "", text, flags=re.S | re.M)


def _strip_blockquotes(text: str) -> str:
    """A blockquote is how this estate reproduces someone else's sentence (`-33`).

    `REG-002` §5's prohibition names `E4` twice; quoting it is not asserting it.
    """
    return "\n".join(ln for ln in text.splitlines() if not ln.lstrip().startswith(">"))


def own_voice(text: str) -> str:
    """The document's own assertions. **Inline code is deliberately kept** — see module docstring."""
    return _strip_blockquotes(_strip_fenced_code(text))


# --------------------------------------------------------------------------- resolution

#: A markdown heading carries no terminal period, so a naive sentence split fuses it with
#: the paragraph below. Blocks first, then soft-wraps rejoined, then sentences.
_BLOCK_SPLIT = re.compile(r"\n\s*\n")
_SENTENCE_SPLIT = re.compile(r"(?<=[.!?])\s+")


def sentences(text: str) -> list[str]:
    out: list[str] = []
    for block in _BLOCK_SPLIT.split(text):
        flat = " ".join(block.split())
        if flat:
            out += [s.strip() for s in _SENTENCE_SPLIT.split(flat) if s.strip()]
    return out


def clauses_on_commas(text: str) -> list[str]:
    """NOT the resolution this guard uses. Kept so the choice can be re-measured, not recalled."""
    out: list[str] = []
    for block in _BLOCK_SPLIT.split(text):
        flat = " ".join(block.split())
        out += [c.strip() for c in re.split(r"[.!?;:,]", flat) if c.strip()]
    return out


# --------------------------------------------------------------------------- detectors

#: `\b` on both sides: `E402` is a flake8 code, not this falsifier. 61 of the 90 substring
#: hits under `scripts/` are exactly that.
E4_TOKEN = re.compile(r"\bE4\b")

#: The REFERENT. A sentence is inside C10's scope only if it is talking about the
#: substitution — the α = 0.35 re-ask — rather than about the registered test.
SUBSTITUTION_RE = re.compile(r"\bsubstitution\b|\bre-ask(?:ed|s|ing)?\b", re.I)

#: The label, matched as a unit rather than by a character window, so the guard does not
#: carry a magic number. Tolerates the document's `**extension of**` emphasis and the
#: optional `REG-002` qualifier, and the script's upper-case `EXTENSION of`.
LABELLED_E4 = re.compile(r"extension\s+of\**\s+(?:REG-002\s+)?E4\b", re.I)


def wrong_label_hits(text: str) -> list[str]:
    """Limb A · sentences that name the substitution and call it `E4` **unlabelled**."""
    bad: list[str] = []
    for sentence in sentences(own_voice(text)):
        if not SUBSTITUTION_RE.search(sentence):
            continue
        covered = [m.span() for m in LABELLED_E4.finditer(sentence)]
        for hit in E4_TOKEN.finditer(sentence):
            if not any(lo <= hit.start() < hi for lo, hi in covered):
                bad.append(sentence)
                break
    return bad


def labelled_sentences(text: str) -> list[str]:
    """Limb B · sentences that name the substitution AND carry the `extension of E4` label."""
    return [
        s
        for s in sentences(own_voice(text))
        if SUBSTITUTION_RE.search(s) and LABELLED_E4.search(s)
    ]


def _wrong_label_count_on_commas(text: str) -> int:
    """The counterfactual resolution, for the pin only. Never used to grade."""
    n = 0
    for clause in clauses_on_commas(own_voice(text)):
        if not SUBSTITUTION_RE.search(clause):
            continue
        covered = [m.span() for m in LABELLED_E4.finditer(clause)]
        if any(
            not any(lo <= h.start() < hi for lo, hi in covered)
            for h in E4_TOKEN.finditer(clause)
        ):
            n += 1
    return n


# --------------------------------------------------------------------------- probe strings

#: `R4`'s **exact** move, so the non-vacuity test proves the guard sees the probe the sweep
#: runs and not a paraphrase of it (`-43`).
R4_OLD = "and here as an **extension of** REG-002 E4 rather than as the registered test."
R4_NEW = "and here as REG-002 E4, the registered test."

#: `R4b` · the second door, at the OTHER site: the re-ask sentence itself names E4 bare.
R4B_OLD = "rises in 99.7%** of the rectangle."
R4B_NEW = "rises in 99.7%** of the rectangle, which E4 reports."

#: `R4c` · the missing-label door: the labelling sentence is deleted outright. Limb A stays
#: green here — which is precisely why limb B has to exist.
R4C_OLD = (
    " That substitution is labelled in the script, in the manuscript\n"
    "and here as an **extension of** REG-002 E4 rather than as the registered test."
)

#: `R4d` · the third surface: the script stops labelling its own substitution.
R4D_OLD = 'That substitution is an EXTENSION of REG-002 E4,")'
R4D_NEW = 'That substitution is REG-002 E4,")'


# ============================================================================ warrants


def test_the_warrant_is_still_in_force_and_in_its_own_section():
    """`-42` · if `REG-002` §5's clause is gone, this file is stale — RETIRE IT, don't trust it."""
    text = REG_002.read_text(encoding="utf-8")
    assert ANCHOR_REG002_S5 in text, (
        "LOST WARRANT (anchor): `REG-002` §5's heading has moved or been renumbered. "
        "C10's warrant is scoped to that section; re-anchor this file before trusting it."
    )
    section = text.split(ANCHOR_REG002_S5, 1)[1]
    assert WARRANT_C10 in section, (
        "LOST WARRANT: `REG-002` §5 no longer says "
        f"{WARRANT_C10!r}. This is NOT a violation of C10 — the errata may have been "
        "withdrawn. Re-read §5 and retire or re-aim this file."
    )


def test_the_governed_section_still_exists():
    """`-42` · the re-ask lives in `RESULT-REG-002` §3. A renumber must fail loudly."""
    assert ANCHOR_RESULT_S3 in RESULT_002.read_text(encoding="utf-8"), (
        "LOST WARRANT (anchor): `RESULT-REG-002` §3's heading moved. The substitution this "
        "file scans lives there; re-anchor before reading a green as coverage."
    )


# ============================================================================ limb A


def test_limb_a_the_substitution_is_never_called_e4():
    """C10 limb A · the WRONG label — the re-ask named as `E4` rather than an extension of it."""
    hits = wrong_label_hits(RESULT_002.read_text(encoding="utf-8"))
    assert not hits, (
        "C10 VIOLATION (wrong label): a sentence names the α = 0.35 substitution and calls "
        "it `E4` without labelling it an extension of E4. `REG-002` §5: "
        f"{WARRANT_C10!r}.\n  " + "\n  ".join(hits)
    )


def test_limb_a_scope_the_three_lawful_e4_sites_are_untouched():
    """The near-miss pin. These three name the REGISTERED TEST and must stay lawful.

    If a rewrite pulls a substitution word into one of them the guard goes red for a real
    reason and a human reads it — rather than a future session widening the predicate.
    """
    text = own_voice(RESULT_002.read_text(encoding="utf-8"))
    lawful = [s for s in sentences(text) if E4_TOKEN.search(s) and not SUBSTITUTION_RE.search(s)]
    assert len(lawful) >= 3, (
        "The three lawful `E4` sites (§1's table row, §3's heading, §3's opening sentence) "
        f"no longer read as sites that name the registered test — found {len(lawful)}. "
        "Either the document was rewritten or the referent test has drifted; read §3."
    )
    assert not any("substitution" in s.lower() for s in lawful)


# ============================================================================ limb B


def test_limb_b_the_substitution_is_labelled_an_extension_somewhere():
    """C10 limb B · the MISSING label. Silence and mislabelling are the same to an absence guard.

    `-44`'s C49 shape: an absence guard cannot express *X, not merely not-Y*. Limb A is
    green on a document that simply deletes the labelling sentence; this is the limb that
    is not.
    """
    labelled = labelled_sentences(RESULT_002.read_text(encoding="utf-8"))
    assert labelled, (
        "C10 VIOLATION (missing label): `RESULT-REG-002` no longer labels the α = 0.35 "
        "substitution an EXTENSION of REG-002 E4 anywhere in its own voice. `REG-002` §5 "
        f"requires it {WARRANT_C10!r} — throughout, which includes at least once."
    )


# ============================================================================ limb C · the script


def test_limb_c_the_script_labels_its_own_substitution():
    """C10's third surface. `RESULT-REG-002` §3 asserts the label travels *in the script*."""
    labelled = labelled_sentences(LADDER_SCRIPT.read_text(encoding="utf-8"))
    assert labelled, (
        "C10 VIOLATION (third surface): `scripts/wt088_disclosed_ladder.py` no longer "
        "labels its α = 0.35 substitution an EXTENSION of REG-002 E4. `RESULT-REG-002` §3 "
        "says the label travels 'in the script, in the manuscript and here' — deleting it "
        "there makes the RESULT document's own sentence false."
    )


def test_limb_c_the_script_does_not_call_the_substitution_e4():
    """Limb A's predicate, scoped to the one script that runs REG-002 E4."""
    hits = wrong_label_hits(LADDER_SCRIPT.read_text(encoding="utf-8"))
    assert not hits, (
        "C10 VIOLATION (third surface, wrong label): wt088 names the substitution and calls "
        "it `E4`.\n  " + "\n  ".join(hits)
    )


def test_the_third_surface_scope_is_warranted():
    """The scoping is a MEASUREMENT, not a habit — `E4` is a per-script local exhibit label.

    `-49` prescribed a word boundary excluding `E40x`. Necessary; not sufficient. Pinned as
    numbers so a future session can see what the boundary actually buys.
    """
    bodies = {p.name: p.read_text(encoding="utf-8", errors="ignore")
              for p in sorted((ROOT / "scripts").rglob("*.py"))}
    substring = sum(len(re.findall(r"E4", b)) for b in bodies.values())
    noqa = sum(len(re.findall(r"noqa: E402", b)) for b in bodies.values())
    carriers = {n: len(E4_TOKEN.findall(b)) for n, b in bodies.items() if E4_TOKEN.search(b)}

    assert noqa > 0, "the `noqa: E402` homograph is gone; re-read this test's premise"
    assert substring - noqa == sum(carriers.values()), (
        "substring hits minus `noqa: E402` no longer equals the word-boundary hits — a THIRD "
        f"homograph has appeared ({substring} - {noqa} != {sum(carriers.values())}). Find it "
        "before trusting either number."
    )
    assert LADDER_SCRIPT.name in carriers, "wt088 must carry REG-002's E4"
    assert len(carriers) > 1, (
        "Only one script carries `\\bE4\\b`, so the scoping this file documents is no longer "
        "load-bearing. That is good news — simplify limb C's justification and say so."
    )


def test_the_manuscript_is_out_of_scope_as_a_measurement():
    """§1's inventory verdict — *out of manuscript scope* — restated as a number (`-46`)."""
    assert not E4_TOKEN.search(MANUSCRIPT.read_text(encoding="utf-8")), (
        "The manuscript now names `E4`. C10's scope verdict was 'out of manuscript scope' "
        "BECAUSE there were zero occurrences. That premise just changed — re-grade C10 "
        "rather than widening this file on reflex."
    )


# ============================================================================ non-vacuity (`-43`)


@pytest.mark.parametrize(
    "slug, old, new",
    [
        ("R4", R4_OLD, R4_NEW),
        ("R4b", R4B_OLD, R4B_NEW),
    ],
)
def test_limb_a_is_not_vacuous(slug, old, new):
    """The probe's EXACT string, and the assertion is the CONJUNCTION (`-43`)."""
    text = RESULT_002.read_text(encoding="utf-8")
    if wrong_label_hits(text):
        pytest.skip("the real document is already violating; limb A's own red says so (`-39`)")
    if old not in text:
        # `-39` · DO NOT ASSERT HERE. `R4c` deletes the sentence `R4`'s anchor lives in, so
        # this test cannot do its job and limb B is already red naming exactly that. An
        # assertion would make this file a second catcher for a defect limb B owns.
        pytest.skip(f"{slug}'s anchor is not in the document; limb B owns whatever removed it")
    mutated = text.replace(old, new)
    hits = wrong_label_hits(mutated)
    assert hits, (
        f"LIMB A IS VACUOUS against {slug}: the exact mutation the sweep applies leaves the "
        "detector silent. A green grade for C10 would be measuring nothing."
    )
    only = hits[0]
    assert SUBSTITUTION_RE.search(only) and E4_TOKEN.search(only), (
        "the hit does not carry BOTH the referent and the token — the conjunction is not "
        "what fired, so the detector is red for some other reason"
    )


def test_limb_b_is_not_vacuous():
    """`R4c` · deleting the labelling sentence must be caught, and by limb B specifically."""
    text = RESULT_002.read_text(encoding="utf-8")
    if not labelled_sentences(text):
        pytest.skip("the real document already carries no label; limb B's own red says so")
    if wrong_label_hits(text):
        # `-39` · limb A is already red and owns it. The separability claim below is only
        # meaningful measured from a clean document.
        pytest.skip("the real document is already violating limb A; separability is unmeasurable")
    if R4C_OLD not in text:
        pytest.skip("R4c's anchor is not in the document; limb B's own red owns that")
    mutated = text.replace(R4C_OLD, "")
    assert not labelled_sentences(mutated), "LIMB B IS VACUOUS: the label survives its own deletion"
    assert not wrong_label_hits(mutated), (
        "limb A is red on the deletion too, so limb B is not separably load-bearing here. "
        "That is a finding, not a failure — re-read which limb owns `R4c` before grading."
    )


def test_limb_c_is_not_vacuous():
    """`R4d` · the script's label, deleted."""
    text = LADDER_SCRIPT.read_text(encoding="utf-8")
    if not labelled_sentences(text):
        pytest.skip("wt088 already carries no label; limb C's own red says so")
    assert R4D_OLD in text, "R4d's anchor no longer matches wt088 — re-measure"
    assert not labelled_sentences(text.replace(R4D_OLD, R4D_NEW)), (
        "LIMB C IS VACUOUS: wt088's label survives its own deletion"
    )


def test_the_resolution_choice_is_pinned():
    """`-49`'s tell, sign-flipped. The unit is a design choice and here the false verdict is GREEN.

    At comma-clause resolution the referent and the token fall apart at the governed site,
    so the detector reports zero on `R4` as well as on the real document — vacuous, and
    silently. This test is the reason the sentence unit is not a preference.
    """
    text = RESULT_002.read_text(encoding="utf-8")
    if wrong_label_hits(text) or R4_OLD not in text:
        # `-39` · this pin compares two resolutions on a CLEAN base. On a document that is
        # already violating, the comparison measures the violation, not the resolution —
        # and limbs A and B are red and own it. Do not pile on.
        pytest.skip("the base document is not clean; limbs A/B own the red that says why")
    mutated = text.replace(R4_OLD, R4_NEW)
    assert mutated != text

    assert len(wrong_label_hits(text)) == 0
    assert len(wrong_label_hits(mutated)) == 1, "sentence resolution must be red on R4"

    assert _wrong_label_count_on_commas(text) == 0
    assert _wrong_label_count_on_commas(mutated) == 0, (
        "comma-clause resolution has become red on R4. The trade-off this file was built "
        "around has moved — RE-MEASURE BOTH RESOLUTIONS before simplifying the splitter, "
        "and read the module docstring's table first."
    )


def test_the_governed_sentence_has_not_fused_with_its_neighbour():
    """The near-miss pin (`-49`). §3's two sentences must stay two.

    *"… the first rung rises in 99.7% of the rectangle."* names the substitution and no
    `E4`; the sentence after it carries the label. Fuse them — swap the full stop for a
    comma or a dash — and the guard reads one sentence where the document makes two claims.

    **THE PREDICATE IS STRUCTURAL ONLY.** A first draft closed with
    `assert not any(E4_TOKEN.search(s) for s in found if not LABELLED_E4.search(s))`, which
    is limb A restated — an ABSENCE predicate inside a file the sweep mutates, so it went
    red on `R4`, `R4b` AND `R4c` and stood in all three catcher lists as an over-breadth
    defect this guard does not have (`-49`'s third tell, reproduced here in a new shape and
    caught by the sweep rather than by review). **Limb A owns compliance; this owns SHAPE.**
    """
    found = [s for s in sentences(own_voice(RESULT_002.read_text(encoding="utf-8")))
             if SUBSTITUTION_RE.search(s)]
    assert len(found) >= 2, (
        "the substitution is now described in fewer sentences than when this guard was "
        f"built (found {len(found)}). If §3 was rewritten, re-measure limb A's resolution — "
        "a fused sentence can hide a bare `E4` behind the labelled one."
    )


# ============================================================================ over-breadth (`-49`)


@pytest.mark.parametrize(
    "what, quotation",
    [
        ("REG-002 §5's prohibition", "> " + WARRANT_C10 + "."),
        (
            "the forbidden reading, quoted",
            "> The substitution is re-asked and reported as REG-002 E4, the registered test.",
        ),
    ],
)
def test_quoting_the_prohibition_contributes_no_hit(what, quotation):
    """The predicate is CONTRIBUTION, not absence — `-49`'s own bug, banked.

    An absence predicate (`assert not detector(doc + quotation)`) is red on every mutant of
    the document too, and shows up in a probe sweep as a second catcher naming a defect the
    guard does not have. Equality is true on a clean document and on a violating one.
    """
    text = RESULT_002.read_text(encoding="utf-8")
    assert len(wrong_label_hits(text + "\n\n" + quotation)) == len(wrong_label_hits(text)), (
        f"quoting {what} changes limb A's verdict — the guard is reading quotations as "
        "assertions (`-33`)"
    )
