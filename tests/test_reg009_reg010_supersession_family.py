"""The supersession family · **C44 / C46 / C41** — three prohibitions, one shape.

THE THREE CONSTRAINTS, IN THEIR OWN WORDS
------------------------------------------
  C44  `CONSTRUCTION-REG-009` R3 — the filled count is reported
       *"BESIDE `-31`'s, never instead of it"*.
  C46  `CONSTRUCTION-REG-010` C4 — the mirror is *"computed, reported beside, never used
       to choose"*; *"The mirror is never promoted"*; *"The registered reading is C2's
       inherited one under every outcome."*
  C41  `REG-010` §0 — *"P3 failed as registered and REG-010 does not re-score it."*

All three say the same thing about three different objects: **a later measurement stands
BESIDE an earlier verdict and never in place of it.** That is why they get one file.

WHY THIS FILE EXISTS — A LIMB NAMED OPEN, THEN MEASURED OPEN
-------------------------------------------------------------
`-46` deleted `RESULT-REG-009-band-count.md` on a scratch copy and got five red, all in
`test_reg010_sec4_frozen_numbers.py`, whose `-42` antecedent check asserts that the
documents the freeze reads still exist. It then recorded the honest half of that result in
`CONSTRAINT-INVENTORY-001` §3.1: **deleting the file is caught, and rewriting its claim as
superseding still is not** — *"an incidental red is not coverage"*. `-47` measured the
unguarded half with probes `R3a`/`R3b`/`R3c` and all three came back GREEN; `-49`
re-measured them at `469012b` before writing a line here, and they were green again.

So the **presence** half of C44 is incidentally covered and the **prose** half of all three
is not. This file owns both, and only the prose half earns the grade (`-44`: count
catchers, not pointers).

THE RESOLUTION IS THE LOAD-BEARING CHOICE, AND IT IS THE CLAUSE
----------------------------------------------------------------
`CONSTRAINT-INVENTORY-001` §0: *"a compliance grade applied at paragraph resolution against
a sentence-level rule is a false green"*, and `-49` found it runs the other way here.

At **sentence** resolution C44's detector is RED on the compliant document. §0 of
`RESULT-REG-009-band-count-filled.md` opens:

    `RESULT-REG-009-band-count` §3 reported that 41 of the 151 tier-0 property events
    could not be binned at all, … and that the measurement replacing both brackets is the
    coverage fill SOURCE-001 §3b named …

One sentence carrying a reference to the earlier document AND the verb *replacing* — and it
is lawful, because the verb's object is **both brackets**, not the count, and because
reporting what `-31` said is not superseding it. Two more lawful sites live in §6: *"the
conditional is REPLACED … by the measured outcome"* and *"a bound that the measurement has
superseded"*, whose objects are a manuscript sentence and a hedge.

At **clause** resolution — splitting on `.!?;`, an em-dashed aside and a colon — the verb
and the referent fall in different clauses at every one of those sites, and the detector is
clean on the real document and red on `R3a`'s exact insertion. That is the whole design.
`LAWFUL_NEAR_MISS` pins the §0 sentence so a rewrite that fuses its clauses is read by a
human rather than by a regex.

THE DISCRIMINATOR IS DIFFERENT FOR C44 THAN FOR C46/C41, AND THE DIFFERENCE IS THE POINT
-----------------------------------------------------------------------------------------
  C44 — **the REFERENT** (`-45`'s lesson). R3 forbids superseding *`-31`'s count*. Every
        lawful use of a supersession verb in these documents has a different object, so
        the object is the discriminator: verb AND a name for the earlier count, one clause.
  C46/C41 — **the POLARITY**. The lawful sites in `RESULT-REG-010` name the mirror and name
        P3 *in order to refuse them*: *"The mirror is not promoted, under this outcome or
        any other."* · *"It does not re-score P3, which failed and stays failed."* A
        referent test cannot separate a refusal from a promotion; a negator in the same
        clause can. So those two limbs fire on an **unnegated** claim.

`-49`'S FINDING: A COPIED own_voice() HELPER WOULD HAVE MADE C44 VACUOUS
-------------------------------------------------------------------------
`-48`'s `own_voice()` strips inline code, on a correct reason for its own constraint —
*"`GoodwillImpairmentLoss` is an XBRL element, not the word `impairment`"*. Copied here it
is a **false green machine**: this estate writes its cross-references in backticks, so
`` `-31` `` is inline code, and stripping it deletes the referent from BOTH the lawful §0
sentence and `R3a`'s forbidden insertion. The detector would then report zero on the real
document and zero on the mutation, and only `test_c44_detector_is_not_vacuous` — which uses
`R3a`'s **exact** string (`-43`) — would say so. **An own-voice filter is not a portable
utility; it is tuned to what the constraint's discriminator has to read.** Helpers are
copied here rather than imported for `-44`'s reason, and this is the case that shows why
copying is not merely tidier.

WHAT THIS CANNOT DO
-------------------
The polarity limbs read a negator **anywhere in the clause**, so *"P3 is re-scored and no
verdict elsewhere moves"* escapes. That is the honest cost of not parsing English, and it
is bounded by the presence limbs: deleting the document's own refusal sentences is red
whatever the absence limbs see (`-44`'s C49 pair — an absence guard cannot express
*X, not merely Y*). It cannot see a supersession claim made in the manuscript or in a
handoff: C41's and C46's scope is the `RESULT-*` document each governs, C44's is the pair,
and `-47`'s C07 ruling says a guard is not widened past the registration that warrants it.
It cannot tell whether the two artifacts still AGREE — `test_reg009_band_count_filled.py`
and `test_reg010_sec4_frozen_numbers.py` own the `two_cycle` reproduction, and duplicating
it here would be a coverage claim this file has not measured.
"""
from __future__ import annotations

import pathlib
import re

import pytest

ROOT = pathlib.Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs/preregistration"

CONSTRUCTION_009 = DOCS / "CONSTRUCTION-REG-009-coverage-fill.md"
CONSTRUCTION_010 = DOCS / "CONSTRUCTION-REG-010-edge-convention.md"
REG_010 = DOCS / "REG-010-p3-half-integer-banding.md"

BAND_COUNT = DOCS / "RESULT-REG-009-band-count.md"
BAND_COUNT_FILLED = DOCS / "RESULT-REG-009-band-count-filled.md"
BANDING = DOCS / "RESULT-REG-010-half-integer-banding.md"

ARTIFACT_31 = ROOT / "data/reg-009-band-count.json"
ARTIFACT_FILLED = ROOT / "data/reg-009-band-count-filled.json"

# --------------------------------------------------------------------------- warrants
#: Each constraint's own clause. Losing one is a LOST WARRANT — the rule may have been
#: retired — and not a violation, so each gets its own message (`-42`).
WARRANT_C44 = "The count is reported BESIDE `-31`'s, never instead of it"
WARRANT_C46 = (
    "The mirror is never promoted",
    "The registered reading is C2's inherited one under every outcome.",
)
WARRANT_C41 = "P3 failed as registered and REG-010 does not re-score it."

#: `-42`'s second door: the SECTION HEADING. Each warrant is bounded to its own section so
#: a renumbered file fails loudly instead of matching a sentence that moved elsewhere.
ANCHOR_R3 = "## R3 · The count is reported BESIDE `-31`'s, never instead of it"
ANCHOR_C4 = "## C4 · The mirror convention: computed, reported beside, never used to choose"
ANCHOR_REG010_S0 = "## 0 · What this registers, and the one thing it is forbidden to do"

# --------------------------------------------------------------------------- own voice


def _strip_fenced_code(text: str) -> str:
    """Drop ```-fenced blocks. `mirror(v, w) = -shifted(-v, w)` is an equation, not a claim."""
    return re.sub(r"^```.*?^```", "", text, flags=re.S | re.M)


def _strip_blockquotes(text: str) -> str:
    """A blockquote is how this estate reproduces someone else's sentence (`-33`).

    `RESULT-REG-010` §3 blockquotes `f61f75a`'s Branch B paragraph, which contains
    *"P3 STILL FAILS"* and *"no verdict is amended"*. Quoting a registration is not
    asserting a re-score.
    """
    return "\n".join(ln for ln in text.split("\n") if not ln.lstrip().startswith(">"))


def _strip_quotations(text: str) -> str:
    """Drop double-quoted spans (`-33`).

    Sharpest here in `RESULT-REG-010` §3, which SPELLS OUT the forbidden reading in order
    to refuse it: *"the failure was an artefact of the translation; under the banding §4
    itself asked for, Ψ moves half a point"*. A scanner that called that a violation would
    be deleted the first time it fired.
    """
    return re.sub(r'"[^"\n]{0,400}"', " ", text)


def _flatten_wraps(text: str) -> str:
    """Join single newlines so a clause is not split by a line break (`-37`)."""
    return re.sub(r"(?<!\n)\n(?!\n)", " ", text)


def own_voice(text: str) -> str:
    """The prose these documents assert — **with inline code left in place**.

    Deliberately NOT `-48`'s `own_voice()`. See the module docstring: `` `-31` `` is this
    estate's name for the earlier count and it is written in backticks, so stripping inline
    code deletes C44's discriminator from the lawful sites and from the probe alike.
    """
    return _flatten_wraps(_strip_quotations(_strip_blockquotes(_strip_fenced_code(text))))


#: Clause resolution: sentence terminators, the semicolons this estate stacks its reports
#: on, an em-dashed aside, and the colon that introduces a gloss. See the module docstring
#: for why this and not the sentence.
_CLAUSE_SPLIT = re.compile(r"(?:[.!?;]|\s—\s|:\s)")


def clauses(text: str) -> list[str]:
    out: list[str] = []
    for line in text.split("\n"):
        line = line.strip()
        if line:
            out.extend(c.strip() for c in _CLAUSE_SPLIT.split(line) if c.strip())
    return out


# ------------------------------------------------------------------ C44 · the referent

#: Frozen as literals (`-44`): a verb list that grows silently is a rule that shrinks
#: silently. `instead of` and `in place of` are R3's own words for the forbidden move.
SUPERSESSION_VERB = re.compile(
    r"\b(?:supersed\w+|replac\w+|withdraw\w*|no longer be cited|instead of|in place of)\b",
    re.IGNORECASE,
)

#: The names this estate gives `-31`'s count. THE DISCRIMINATOR — R3 forbids superseding
#: THIS object and nothing else, and every lawful supersession verb in these two documents
#: has a different one (a bracket, a manuscript conditional, a hedge).
EARLIER_COUNT = re.compile(
    r"`-31`|-31's|RESULT-REG-009-band-count|reg-009-band-count"
    r"|two-cycle count|the earlier count|the committed count",
    re.IGNORECASE,
)

#: The compliant sentence that a SENTENCE-resolution detector flags and a CLAUSE-resolution
#: one does not. Pinned so the adjudication is not re-derived, and so a rewrite that fuses
#: its clauses is read by a human. Keyed on the fragment carrying the verb.
LAWFUL_NEAR_MISS = "the measurement replacing both brackets is the coverage fill"


def supersession_claims_about_the_earlier_count(text: str) -> list[str]:
    """Clauses asserting that something supersedes, replaces or withdraws `-31`'s count."""
    return [
        c
        for c in clauses(own_voice(text))
        if SUPERSESSION_VERB.search(c) and EARLIER_COUNT.search(c)
    ]


# ------------------------------------------------------------------ C46/C41 · polarity

#: A negator anywhere in the clause makes the clause a REFUSAL, which is what compliance
#: looks like in these documents. See WHAT THIS CANNOT DO.
NEGATOR = re.compile(
    r"\b(?:not|never|no|nor|cannot|can't|without|neither|refus\w*|unamended)\b"
    r"|stays failed",
    re.IGNORECASE,
)

PROMOTION = re.compile(
    r"\bpromot(?:e|es|ed|ing)\b|\bset aside\b|\bis the registered reading\b"
    r"|\bthe convention this result is read under\b",
    re.IGNORECASE,
)

RE_SCORING = re.compile(r"\bre-?scor(?:e|es|ed|ing)\b|\bis a pass\b|\brescu\w+\b", re.IGNORECASE)


def _unnegated(text: str, claim: re.Pattern[str]) -> list[str]:
    return [c for c in clauses(own_voice(text)) if claim.search(c) and not NEGATOR.search(c)]


def promotion_claims(text: str) -> list[str]:
    """Clauses promoting the mirror to the reading this result is read under."""
    return _unnegated(text, PROMOTION)


def re_scoring_claims(text: str) -> list[str]:
    """Clauses re-scoring P3 — turning a recorded failure into a pass."""
    return _unnegated(text, RE_SCORING)


#: The documents' own refusals, in their own voice. C49's pair shape (`-44`): an ABSENCE
#: guard cannot express *reported beside, not instead of*, so the presence of the refusal
#: is asserted separately from the absence of the claim.
REFUSALS_C46 = ("The mirror is not promoted, under this outcome or any other.",)
REFUSALS_C41 = (
    "**P3 failed as registered and REG-010 does not re-score it.**",
    "It does not re-score P3, which failed and stays failed.",
)

# --------------------------------------------------------------------------- fixtures


@pytest.fixture(scope="module")
def filled_text() -> str:
    return BAND_COUNT_FILLED.read_text(encoding="utf-8")


@pytest.fixture(scope="module")
def count_text() -> str:
    return BAND_COUNT.read_text(encoding="utf-8")


@pytest.fixture(scope="module")
def banding_text() -> str:
    return BANDING.read_text(encoding="utf-8")


# ---------------------------------------------------------------------------- warrants


def test_the_registrations_still_carry_all_three_clauses() -> None:
    """LOST WARRANT, one message per constraint — they can be retired separately."""
    r009 = CONSTRUCTION_009.read_text(encoding="utf-8")
    assert ANCHOR_R3 in r009, (
        f"LOST WARRANT (C44) — {CONSTRUCTION_009.name} no longer carries the R3 heading "
        "this file is scoped to. Read the construction registration, then restore the "
        "section or retire this file's C44 limb and amend C44's row."
    )
    assert WARRANT_C44 in _flatten_wraps(r009), (
        f"LOST WARRANT (C44) — `CONSTRUCTION-REG-009` R3 no longer says {WARRANT_C44!r}. "
        "This is not a violation: the rule may have been retired. Restore the clause, or "
        "delete this limb and amend CONSTRAINT-INVENTORY-001's C44 row."
    )

    r010c = _flatten_wraps(CONSTRUCTION_010.read_text(encoding="utf-8"))
    assert ANCHOR_C4 in r010c, (
        f"LOST WARRANT (C46) — {CONSTRUCTION_010.name} no longer carries the C4 heading. "
        "Restore it or retire this file's C46 limb."
    )
    for clause in WARRANT_C46:
        assert clause in r010c, (
            f"LOST WARRANT (C46) — `CONSTRUCTION-REG-010` C4 no longer says {clause!r}. "
            "The mirror's prohibition and the registered reading's primacy are two "
            "separate promises and this limb needs both. Restore, or retire the limb."
        )

    reg010 = _flatten_wraps(REG_010.read_text(encoding="utf-8"))
    assert ANCHOR_REG010_S0 in reg010, (
        f"LOST WARRANT (C41) — {REG_010.name} no longer carries the §0 heading."
    )
    assert WARRANT_C41 in reg010, (
        f"LOST WARRANT (C41) — `REG-010` §0 no longer says {WARRANT_C41!r}. That sentence "
        "is the whole of C41. Restore it, or retire this limb and amend C41's row."
    )


# ------------------------------------------------------- C44 · limb 1, the presence pair


def test_the_beside_pair_is_still_a_pair() -> None:
    """*Beside, never instead of* is a PRESENCE pair — C49's shape, one domain over.

    An absence guard cannot express *X, not merely Y*: a world in which `-31`'s row was
    deleted and the filled row left standing alone satisfies every prohibition in this
    file and violates R3 outright. This assertion is the only thing here that expresses
    the *beside*, and it is NOT what grades the row — deleting either document is already
    incidentally red in `test_reg010_sec4_frozen_numbers.py` (`-46`), and an incidental
    red is not coverage. It is owned here so the red arrives with the right message.
    """
    for path, role in (
        (BAND_COUNT, "`-31`'s two-cycle count — the row the fill stands BESIDE"),
        (BAND_COUNT_FILLED, "the coverage-filled count"),
        (ARTIFACT_31, "`-31`'s artifact, which R3 says stands untouched"),
        (ARTIFACT_FILLED, "the filled run's own artifact"),
    ):
        assert path.exists(), (
            f"BESIDE BROKEN — {path.name} is gone. It is {role}. "
            "`CONSTRUCTION-REG-009` R3: the filled count is reported *beside* `-31`'s, "
            "never instead of it, and R3 names the committed artifact as standing "
            "untouched. Restore the file; do not re-derive it from the survivor."
        )


# --------------------------------------------------- C44 · limb 2, the supersession scan


def test_the_filled_count_claims_no_supersession(filled_text: str, count_text: str) -> None:
    for name, text in ((BAND_COUNT_FILLED.name, filled_text), (BAND_COUNT.name, count_text)):
        hits = supersession_claims_about_the_earlier_count(text)
        assert not hits, (
            f"SUPERSESSION CLAIMED — {name} states that something supersedes, replaces or "
            "withdraws `-31`'s count:\n\n  " + "\n  ".join(hits) + "\n\n"
            "`CONSTRUCTION-REG-009` R3 forbids exactly this: the filled count is reported "
            "BESIDE `-31`'s, never instead of it, and `-31`'s row and every assertion in "
            "`tests/test_reg009_band_count.py` stand untouched. If the clause's object is "
            "a bracket, a manuscript conditional or a hedge rather than the count, it is "
            "lawful — re-read it, and pin it in LAWFUL_NEAR_MISS with the adjudication "
            "rather than widening the verb list."
        )


def test_the_lawful_near_miss_is_still_lawful(filled_text: str) -> None:
    """The compliant sentence that sentence-resolution would flag, pinned with its reason.

    A pinned exception that vanishes is the more dangerous half (`-48`): the guard goes
    green while the sentence it was excusing has been rewritten into something nobody
    graded. This one additionally proves the resolution choice is still doing work — if
    the clauses fuse, the detector above turns red on a compliant document.
    """
    flat = _flatten_wraps(filled_text)
    assert LAWFUL_NEAR_MISS in flat, (
        f"PINNED SITE MOVED — {BAND_COUNT_FILLED.name} no longer contains "
        f"{LAWFUL_NEAR_MISS!r}. That §0 sentence names the earlier document and the verb "
        "*replacing* in one sentence, and was adjudicated lawful because the verb's "
        "object is *both brackets*. If it was rewritten, re-read it against R3 and update "
        "the pin; do not simply delete the entry."
    )
    offenders = [
        c
        for c in clauses(own_voice(filled_text))
        if LAWFUL_NEAR_MISS in c and EARLIER_COUNT.search(c)
    ]
    assert not offenders, (
        "PINNED SITE FUSED — the §0 sentence now carries the supersession verb and a name "
        "for `-31`'s count in the SAME CLAUSE, which is the resolution this file draws "
        "the line at. Either split it back, or re-adjudicate C44's resolution in "
        "CONSTRAINT-INVENTORY-001 before touching the detector."
    )


def test_c44_detector_is_not_vacuous(filled_text: str) -> None:
    """`R3a`'s exact insertion, asserting the CONJUNCTION (`-43`).

    The exact string matters more than usual here: `R3a` writes its referent as
    `` `-31` ``, inside backticks. A detector built on a copied `own_voice()` that strips
    inline code reports zero on the real document AND zero on this mutation, and this is
    the only assertion that would say so. See the module docstring.
    """
    violation = (
        "**This count supersedes the `-31` count, which is withdrawn and should no longer"
        " be cited; the filled population replaces it.**"
    )
    mutated = filled_text.replace("\n\n", "\n\n" + violation + "\n\n", 1)
    assert mutated != filled_text, "fixture is broken: no paragraph break to insert at"
    if supersession_claims_about_the_earlier_count(filled_text):
        pytest.skip(
            "the document is already violating — see "
            "test_the_filled_count_claims_no_supersession, which is the failure"
        )
    assert supersession_claims_about_the_earlier_count(mutated), (
        "VACUOUS — the detector does not see `-31`'s count declared superseded and "
        "withdrawn. It would pass for a scanner that flags nothing."
    )


def test_c44_detector_does_not_fire_on_the_registrations_own_prohibition(
    filled_text: str,
) -> None:
    """Over-breadth (`-33`): reporting a prohibition is not performing the forbidden move.

    The assertion is that the quotation CONTRIBUTES no hit, not that the document has
    none. Asserting the latter makes this test a second red on an already-violating
    document — `-39`'s tell — and it would then fire during `R3a`'s probe run and be
    mis-read as an over-breadth defect the guard does not have.
    """
    quoted = (
        "\n\n> `CONSTRUCTION-REG-009` R3: the count is reported BESIDE `-31`'s, never"
        " instead of it.\n\nThe registration says the filled row may not be reported"
        ' "instead of `-31`\'s count".\n\n'
    )
    before = supersession_claims_about_the_earlier_count(filled_text)
    after = supersession_claims_about_the_earlier_count(filled_text + quoted)
    assert after == before, (
        "OVER-BROAD — the detector flagged R3's own words, quoted:\n\n  "
        + "\n  ".join(c for c in after if c not in before)
        + "\n\nA document that restates the rule it obeys is the compliant case, not the "
        "violating one."
    )


# ------------------------------------------------------------ C46 · the mirror's promotion


def test_the_mirror_is_not_promoted(banding_text: str) -> None:
    hits = promotion_claims(banding_text)
    assert not hits, (
        f"MIRROR PROMOTED — {BANDING.name} states that the mirror convention is the "
        "reading this result is read under:\n\n  " + "\n  ".join(hits) + "\n\n"
        "`CONSTRUCTION-REG-010` C4: the mirror is computed, reported beside, and never "
        "used to choose — *The registered reading is C2's inherited one under every "
        "outcome*, and *a session that finds itself preferring it has found the seventh "
        "free parameter*. The mirror is the reading under which Ψ_band′ sits FURTHEST "
        "from Ψ, which is exactly why C4 fixed this before the run."
    )


def test_the_mirrors_refusal_is_asserted_in_the_documents_own_voice(banding_text: str) -> None:
    """The presence limb. C49's pair: absence and presence fail differently (`-44`)."""
    flat = _flatten_wraps(banding_text)
    for sentence in REFUSALS_C46:
        assert sentence in flat, (
            f"REFUSAL GONE — {BANDING.name} no longer says {sentence!r}. C4's prohibition "
            "is discharged by the document SAYING it declines the mirror, not merely by "
            "the document being silent: silence and refusal have the same truth value for "
            "an absence guard, which is `-44`'s C49 finding. Restore the sentence."
        )


def test_c46_detector_is_not_vacuous(banding_text: str) -> None:
    """`R3b`'s exact insertion, asserting the CONJUNCTION (`-43`)."""
    violation = (
        "**The mirror is promoted to the registered reading: it is the convention this"
        " result is read under, and C2's inheritance is set aside.**"
    )
    mutated = banding_text.replace("\n\n", "\n\n" + violation + "\n\n", 1)
    assert mutated != banding_text, "fixture is broken: no paragraph break to insert at"
    if promotion_claims(banding_text):
        pytest.skip(
            "the document is already violating — see test_the_mirror_is_not_promoted, "
            "which is the failure"
        )
    assert promotion_claims(mutated), (
        "VACUOUS — the detector does not see the mirror declared the registered reading. "
        "It would pass for a scanner that flags nothing."
    )


# ---------------------------------------------------------------- C41 · P3's verdict


def test_p3_is_not_re_scored(banding_text: str) -> None:
    hits = re_scoring_claims(banding_text)
    assert not hits, (
        f"P3 RE-SCORED — {BANDING.name} turns a recorded failure into a pass:\n\n  "
        + "\n  ".join(hits)
        + "\n\n`REG-010` §0: *P3 failed as registered and REG-010 does not re-score it.* "
        "REG-009 is closed and §4's verdict stands whatever this run returned. The "
        "thirteenfold drop from 0.0650 to 0.0050 is the SIZE of the problem, not a "
        "rescue — a control that failed on the banding it was registered against cannot "
        "be un-failed by a banding built after the failure was seen."
    )


def test_p3s_failure_is_restated_in_the_documents_own_voice(banding_text: str) -> None:
    """The presence limb for C41 — the same pair shape, and for the same reason."""
    flat = _flatten_wraps(banding_text)
    for sentence in REFUSALS_C41:
        assert sentence in flat, (
            f"REFUSAL GONE — {BANDING.name} no longer says {sentence!r}. `REG-010` §0's "
            "promise is that this document says so; a document that merely omits a "
            "re-score is indistinguishable from one that never considered the question. "
            "Restore the sentence, or re-adjudicate C41 in CONSTRAINT-INVENTORY-001."
        )


def test_c41_detector_is_not_vacuous(banding_text: str) -> None:
    """`R3c`'s exact insertion, asserting the CONJUNCTION (`-43`)."""
    violation = (
        "**P3 is re-scored on this evidence: what REG-009 recorded as a failure is a pass"
        " under the banding registered here.**"
    )
    mutated = banding_text.replace("\n\n", "\n\n" + violation + "\n\n", 1)
    assert mutated != banding_text, "fixture is broken: no paragraph break to insert at"
    if re_scoring_claims(banding_text):
        pytest.skip(
            "the document is already violating — see test_p3_is_not_re_scored, which is "
            "the failure"
        )
    assert re_scoring_claims(mutated), (
        "VACUOUS — the detector does not see P3 declared a pass. It would pass for a "
        "scanner that flags nothing."
    )


def test_the_polarity_limbs_do_not_fire_on_the_refused_reading(banding_text: str) -> None:
    """Over-breadth, and the site is a real one (`-33`).

    §3 of this document SPELLS OUT the flattering reading in order to refuse it, and §3's
    blockquote reproduces `f61f75a`'s Branch B paragraph. Both are quotations. A detector
    that read either as the claim would be deleted the first time it fired — and the
    sentence it would delete is the most valuable one in the document.

    As above, the predicate is CONTRIBUTION and not absence (`-39`): on the `R3b`/`R3c`
    mutants this test must stay green, because the defect there is the asserted claim and
    this file already has an assertion that names it.
    """
    quoted = (
        "\n\n> Quoted from the registration: *P3 is re-scored and the mirror is promoted"
        " to the registered reading.*\n\nA session holding the tee-up could have written"
        ' "P3 is re-scored on this evidence and the mirror is promoted", and the'
        " registration is what stops it.\n\n"
    )
    for detector, label in ((re_scoring_claims, "re-score"), (promotion_claims, "promotion")):
        before, after = detector(banding_text), detector(banding_text + quoted)
        assert after == before, (
            f"OVER-BROAD — the detector read a quoted {label} as an asserted one:\n\n  "
            + "\n  ".join(c for c in after if c not in before)
            + "\n\n§3 names the forbidden reading in order to refuse it; that paragraph "
            "is the document's best work and a guard that flags it will be deleted."
        )
