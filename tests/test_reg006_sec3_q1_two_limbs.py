"""`REG-006` §3 Q1 · **C26** — the two limbs of one sentence, which fail for different reasons.

THE SENTENCE, AND ITS REFERENT
------------------------------
`REG-006` §3 Q1 closes with three conjuncts sharing one subject:

    ...so **every statistic in this file is about separately-tagged recognised charges**,
    the word "impairment" never appears in it unqualified, and the count of firm-periods
    behind each ratio is printed next to the ratio.

`-45`'s provenance audit ruled on the referent and the ruling is load-bearing here:
**"it" is the file's own statistics**, not the file, and not the manuscript. The shorter
paraphrase `CONSTRAINT-INVENTORY-001` carried for three sessions — *"the word 'impairment'
never appears unqualified"* — reads as a rule about every sentence, and a guard built on
that reading is RED on a compliant document. See WHAT THIS DOES NOT FLAG below: both live
bare occurrences are lawful under the registration's actual words.

WHY THIS FILE EXISTS
--------------------
C26 sat at the top of `§3.2`'s measured ranking with `machine: none`. Probes `R2a`/`R2b`
(`scripts/mutation_control.py`) were both green in `-47`'s sweep: you may insert a bare
`impairment` beside a percentage, or delete the `n` printed next to a slope, and the
1007-test suite says nothing.

WHAT `-48` FOUND WHILE BUILDING IT, WHICH THE TEE-UP HAD BACKWARDS
------------------------------------------------------------------
`HANDOFF-wealthTensor-47` §3 characterised the document as carrying *"impairment"* eleven
times, *"every one of them qualified"*. It carries it **twelve** times and **two are bare**
(§1's KPMG walk-through, §3's 8-K population sentence). The document is compliant anyway —
but for the referent reason, not the reason the tee-up gave. A guard built from the tee-up's
premise would have gone red on a compliant `RESULT-*` and sent this session to "repair" a
witness. **Fourth session running that this estate's prose about itself is the thing that
did not survive checking.**

THE TWO LIMBS FAIL DIFFERENTLY, SO THEY GET DIFFERENT MESSAGES (`-42`)
-----------------------------------------------------------------------
  limb A — a bare `impairment` naming one of the file's own statistics. The failure is a
           SENTENCE, and the repair is a word.
  limb B — a ratio printed with no firm-period count beside it. The failure is a TABLE ROW
           or a parenthesis, and the repair is a number that has to be read out of the run
           log.

WHAT A "STATISTIC" IS, MECHANICALLY (limb A's discriminator)
-------------------------------------------------------------
Q1's own third conjunct says what kind of statistic it means: one with **a count of
firm-periods behind it** — a ratio or a share. So limb A fires on a bare `impairment`
sharing a sentence with a RATIO TOKEN (`%`, `×`, or an explicit *of the
population/sample/subset*), and not on a bare `impairment` sharing a sentence with any
number at all. That line is drawn by the registration and not by convenience, and it is
what separates `R2a`'s forbidden insertion from the two lawful sites below.

WHAT THIS DOES NOT FLAG, AND WHY — PINNED, WITH REASONS (`-44`: the literals stay)
-----------------------------------------------------------------------------------
Both are bare, both are in the estate's own voice, and neither is one of this file's
statistics. They are pinned so the next session does not re-derive the adjudication, and
`test_the_lawful_bare_sites_are_still_lawful` fails loudly if either sentence changes:

  1. *"Test goodwill first and the impairment is \\$700"* — KPMG *Handbook* Example 4.4.10,
     narrated. The \\$700 is KPMG's arithmetic, not a measurement of this study.
  2. *"1,400 firms recording an impairment"* — the 8-K Item 2.06 population. Here the bare
     word is doing honest work: it means *any* impairment, tagged or folded, which is
     exactly the undifferentiated thing Q1 says the threshold cannot separate. Qualifying
     it would make the sentence WRONG.

WHAT IT CANNOT DO
-----------------
It cannot tell a qualifier that is accurate from one that is merely present — `recognised
goodwill impairment` and `recognised leasehold impairment` are equally qualified to a
regex and only one of them is true of `GoodwillImpairmentLoss`. It cannot see a statistic
reported in the manuscript rather than in these two files; C26's scope is `REG-006` and
`RESULT-REG-006` and that scope is the `-45` ruling. And limb B **bounds** rather than
closes: §2's six-row internal-control table prints twelve ratios and no counts, is
pinned as an open finding, and the assertion is that the set does not GROW. Closing it
means printing counts into a `RESULT-*` table, which is a witness edit and not a test's
call — carded, not repaired. `§2.2`'s four prose couplings are a named residual, out of
the locator's scope and unadjudicated by anyone.
"""
from __future__ import annotations

import pathlib
import re

import pytest

ROOT = pathlib.Path(__file__).resolve().parents[1]
REG_006 = ROOT / "docs/preregistration/REG-006-p3-sequencing-vs-coupling.md"
RESULT = ROOT / "docs/preregistration/RESULT-REG-006.md"

#: The two clauses that warrant this file, quoted from `REG-006` §3 Q1 with their referent
#: intact. Their loss is a LOST WARRANT, not a violation (`-42`).
WARRANT_LIMB_A = 'the word "impairment" never appears in it unqualified'
WARRANT_LIMB_B = (
    "the count of firm-periods behind each ratio is printed next to the ratio"
)

#: `Q1` is unique in `REG-006`, which is why `-45`'s provenance machine nests its locators
#: there. The same anchor bounds this file's warrant check to the right block.
Q1_ANCHOR = "**Q1 · WHICH OUTCOMES DOES THIS THRESHOLD FAIL TO SEPARATE?**"

# --------------------------------------------------------------------------- own voice


def _strip_fenced_code(text: str) -> str:
    """Drop ```-fenced blocks. Element names are not prose and never carry a qualifier."""
    return re.sub(r"^```.*?^```", "", text, flags=re.S | re.M)


def _strip_blockquotes(text: str) -> str:
    """A blockquote is how this estate reproduces someone else's sentence (`-33`)."""
    return "\n".join(
        ln for ln in text.split("\n") if not ln.lstrip().startswith(">")
    )


def _strip_inline_code(text: str) -> str:
    """`GoodwillImpairmentLoss` is an XBRL element, not the word `impairment`."""
    return re.sub(r"`[^`\n]*`", " ", text)


def _strip_quotations(text: str) -> str:
    """Drop double-quoted spans: ASC, KPMG and PwC write their own sentences.

    `-33`'s tell in its sharpest form here — this file's registration QUOTES
    ASC 350-20-35-32's *"all assets that are tested for impairment"*, and a scanner that
    called the standard's own words a violation would be deleted the first time it fired.
    """
    return re.sub(r'"[^"\n]{0,400}"', " ", text)


def _flatten_wraps(text: str) -> str:
    """Join single newlines so a qualifier is not hidden by a line break (`-37`).

    `REG-006` §1 hard-wraps *"separately tag a long-lived-asset\\nimpairment"*. A
    line-oriented scanner reads the second line as a bare occurrence. `-37`'s lesson said
    an anchor and a guard want opposite things from a line break; a guard wants them gone.
    """
    return re.sub(r"(?<!\n)\n(?!\n)", " ", text)


def own_voice(text: str) -> str:
    """The prose this estate asserts, wrap-joined, with everyone else's words removed."""
    return _flatten_wraps(
        _strip_quotations(_strip_inline_code(_strip_blockquotes(_strip_fenced_code(text))))
    )


# ------------------------------------------------------------------------------ limb A

#: Qualifiers registered by `REG-006` §2's own definitions of `L` and `G`, plus the two
#: idioms the accounting literature forces into the estate's voice. Frozen as literals:
#: a qualifier list that grows silently is a rule that shrinks silently (`-44`).
QUALIFIER = re.compile(
    r"(?:"
    r"goodwill\s+impairment"
    r"|recognised\s+impairment|recognized\s+impairment"
    r"|impairment\s+of\s+assets\s+other\s+than\s+goodwill"
    r"|long-lived-asset\s+impairment|long-lived\s+asset\s+impairment"
    r"|leasehold\s+impairment|tangible\s+asset\s+impairment"
    r"|impairment\s+standards?|impairment\s+tests?|impairment\s+testing"
    r"|tested\s+for\s+impairment|test\s+for\s+impairment"
    r"|Impairment\s+or\s+Disposal"
    r"|Impairment\s+of\s+nonfinancial\s+assets"
    r")",
    re.IGNORECASE,
)

#: What makes a sentence a STATISTIC of this file, per Q1's own third conjunct: a ratio.
#: Not "any number" — see the module docstring's two pinned lawful sites.
RATIO_TOKEN = re.compile(
    r"\d\s*%|\d\s*×|\bof\s+the\s+(?:population|sample|subset|eligible)", re.IGNORECASE
)

#: The two bare-but-lawful sentences, pinned verbatim (wrap-joined). Adjudication in the
#: module docstring. If either changes, this file says so rather than going quietly green.
LAWFUL_BARE_SITES = (
    "Test goodwill first and the impairment is",
    "1,400 firms recording an impairment",
)

_SENTENCE_SPLIT = re.compile(r"(?<=[.!?])\s+(?=[A-Z*`\[(])")


def _sentences(text: str) -> list[str]:
    out: list[str] = []
    for para in text.split("\n"):
        para = para.strip()
        if para:
            out.extend(s for s in _SENTENCE_SPLIT.split(para) if s.strip())
    return out


def bare_impairment_in_statistics(text: str) -> list[str]:
    """Sentences stating a ratio in which the word `impairment` carries no qualifier."""
    hits: list[str] = []
    for sentence in _sentences(own_voice(text)):
        if not re.search(r"\bimpairment\b", sentence, re.IGNORECASE):
            continue
        if not RATIO_TOKEN.search(sentence):
            continue
        stripped = QUALIFIER.sub(" ", sentence)
        if re.search(r"\bimpairment\b", stripped, re.IGNORECASE):
            hits.append(sentence.strip())
    return hits


# ------------------------------------------------------------------------------ limb B

#: Ratio sites in `RESULT-REG-006` that DO print their firm-period count, pinned as
#: (ratio, count) pairs that must appear together. `-47`'s probe `R2b` deletes the first
#: of these; the frozen pair is what makes that deletion red rather than invisible.
COUNTED_RATIOS = (
    ("**+0.010** (retail, n = 417)", "n = 417"),
    ("**+0.665** (computer services, n = 318)", "n = 318"),
    ("3.63× (p 0.038, 4 obs)", "4 obs"),
    ("**3.99× (p 0.0012, 14 obs)**", "14 obs"),
    ("4.14× (p 0.0096, 5 obs)", "5 obs"),
    ("**2.17× (p 0.085, 8 obs)**", "8 obs"),
    ("**43 of 1,079, or 4.0%**", "1,079"),
)

#: Table rows that print a ratio and NO count. This is an OPEN FINDING, bounded rather
#: than closed: the counts exist (`RESULT-REG-006-ladderC-run.log`, the `obs` column of
#: each pair block) but printing them into a `RESULT-*` table edits a witness, which
#: `-37`'s precedent and `HANDOFF` §4.2 say is a dated addendum's job and not a test's.
#: Keyed by the row's leading cell, so a re-run that moves the numbers still matches.
#: The assertion below is that this set does not GROW.
UNCOUNTED_ROWS = (
    "indefinite-lived intangible × goodwill (retail)",
    "finite-lived intangible × goodwill (retail)",
    "finite × indefinite (retail)",
    "indefinite-lived intangible × goodwill (computer services)",
    "finite-lived intangible × goodwill (computer services)",
    "finite × indefinite (computer services)",
)

#: A ratio, and a p-value, stripped before counting integers — otherwise `3.63×` and
#: `p 0.038` supply the digits that would certify their own row as counted.
_RATIO = re.compile(r"[\d.]+\s*×")
_PVALUE = re.compile(r"\bp[\s=]*[\d.]+")
_INTEGER = re.compile(r"\b\d[\d,]*\b")


def _row_label(line: str) -> str:
    return line.strip().strip("|").split("|")[0].strip().strip("*").strip()


def ratio_rows_missing_a_count(text: str) -> list[str]:
    """Every results-table row printing a ratio with no count in the same row.

    **Scoped to table rows on purpose, and the scope is the load-bearing choice here.**
    *"printed NEXT TO the ratio"* is a placement rule (C29's shape) and a table row is
    the one place in this document where *next to* has an unambiguous machine reading.
    A line-scoped sweep over all prose instead returns twenty-five sites, most of them
    re-mentions of a ratio whose count is in the table three lines above, or constants
    §4's Q5 records as READ from `RESULT-REG-003` rather than computed here. Flagging
    those would enforce a rule nobody wrote — the C07 precedent — and the guard would be
    deleted the first time it fired. The prose sites that DO carry their own count are
    pinned individually in `COUNTED_RATIOS` above, which is what makes probe `R2b` red.

    The residual, named rather than hidden: `§2.2`'s four discovered couplings (0.00×,
    3.27×, 7.70×, 6.33×) are reported in prose with p-values and no counts. They are out
    of this locator's scope and nobody has adjudicated them. Teed up, not graded.
    """
    missing: list[str] = []
    for line in _strip_blockquotes(_strip_fenced_code(text)).split("\n"):
        if not line.lstrip().startswith("|") or not _RATIO.search(line):
            continue
        residue = _PVALUE.sub(" ", _RATIO.sub(" ", line))
        if _INTEGER.search(residue):
            continue
        missing.append(_row_label(line))
    return missing


# --------------------------------------------------------------------------- fixtures


@pytest.fixture(scope="module")
def reg_text() -> str:
    return REG_006.read_text(encoding="utf-8")


@pytest.fixture(scope="module")
def result_text() -> str:
    return RESULT.read_text(encoding="utf-8")


# ---------------------------------------------------------------------------- warrant


def test_the_registration_still_carries_both_limbs(reg_text: str) -> None:
    """LOST WARRANT check, one message per limb — they can be lost separately."""
    assert Q1_ANCHOR in reg_text, (
        f"LOST WARRANT — {REG_006.name} no longer carries the Q1 block this file is "
        "scoped to. Read §3, then either restore it or retire this file and C26's row."
    )
    q1 = reg_text.split(Q1_ANCHOR, 1)[1].split("**Q2 ·", 1)[0]
    flat = _flatten_wraps(q1)
    for limb, clause in (("A", WARRANT_LIMB_A), ("B", WARRANT_LIMB_B)):
        assert clause in flat, (
            f"LOST WARRANT (limb {limb}) — `REG-006` §3 Q1 no longer contains "
            f"{clause!r}. This is not a violation: the rule may have been retired. "
            "Restore the clause, or delete this limb's tests and amend C26's row."
        )


def test_the_referent_is_still_the_files_own_statistics(reg_text: str) -> None:
    """`-45`'s ruling, pinned where a rewrite would hit it.

    The clause reads *in it*, and *it* is the file's own statistics. Drop those two
    words and the sentence becomes a rule about every sentence in the document — which
    the document does not obey, at two lawful sites, and never promised to.
    """
    assert '"impairment" never appears in it unqualified' in _flatten_wraps(reg_text), (
        "REFERENT LOST — `REG-006` §3 Q1 no longer says *in it*. `-45` ruled that *it* "
        "is the file's own statistics; without the referent the clause reads as a rule "
        "about every sentence, and this file's discriminator would be wrong. Restore "
        "the words, or re-adjudicate the scope in CONSTRAINT-INVENTORY-001 §2 first."
    )


# ----------------------------------------------------------------------------- limb A


def test_no_statistic_names_impairment_unqualified(reg_text: str, result_text: str) -> None:
    for name, text in ((REG_006.name, reg_text), (RESULT.name, result_text)):
        hits = bare_impairment_in_statistics(text)
        assert not hits, (
            f"UNQUALIFIED IN A STATISTIC — {name} states a ratio and calls its subject "
            f"plain `impairment`:\n\n  " + "\n  ".join(hits) + "\n\n"
            "`REG-006` §3 Q1 forbids exactly this: the threshold `charge > 0` cannot "
            "separate a folded charge from a separately-tagged one, so a statistic must "
            "say WHICH impairment it counts. Name it (recognised goodwill impairment, "
            "recognised impairment of assets other than goodwill), or move the sentence "
            "off the ratio."
        )


def test_the_lawful_bare_sites_are_still_lawful(result_text: str) -> None:
    """The two pinned exceptions, so the adjudication is not re-derived — or lost.

    A pinned exception that vanishes is the more dangerous half: the guard would go
    green while the sentence it was excusing had been rewritten into something nobody
    graded.
    """
    flat = _flatten_wraps(result_text)
    for site in LAWFUL_BARE_SITES:
        assert site in flat, (
            f"PINNED SITE MOVED — {RESULT.name} no longer contains {site!r}. This "
            "sentence was adjudicated bare-but-lawful (see this file's docstring: it "
            "states no ratio of this study). If it was rewritten, re-read it against "
            "`REG-006` §3 Q1 and update the pin; do not simply delete the entry."
        )
        sentence = next(
            (s for s in _sentences(own_voice(result_text)) if site in s), None
        )
        assert sentence is not None and not RATIO_TOKEN.search(sentence), (
            f"PINNED SITE NOW STATES A RATIO — {site!r} has acquired a percentage or a "
            "lift. It was excused because it was not one of this file's statistics. "
            "It is now. Qualify the word or remove the ratio."
        )


def test_limb_a_detector_is_not_vacuous(result_text: str) -> None:
    """Feed the document its own forbidden claim, and assert the CONJUNCTION (`-43`).

    `R2a`'s exact insertion. A detector that only ever reports zero is indistinguishable
    from no detector, and one that reports the real document is worse than none.
    """
    violation = (
        " The impairment is 4.1% of the population and 12.4% of the tested subset."
    )
    mutated = result_text.replace(
        "**Ladder A fails.**", "**Ladder A fails.**" + violation, 1
    )
    assert mutated != result_text, "fixture is broken: the anchor moved"
    if bare_impairment_in_statistics(result_text):
        # `-39`, via `test_reg012_sec7_refusal_is_asserted`: on an already-violating
        # document this self-test would turn one defect into two red lines and bury the
        # one that names it. The detector proves itself only where there is a clean
        # baseline to move away from.
        pytest.skip(
            "the document is already violating — see "
            "test_no_statistic_names_impairment_unqualified, which is the failure"
        )
    assert bare_impairment_in_statistics(mutated), (
        "VACUOUS — the detector does not see a bare `impairment` stated beside two "
        "percentages. It would pass for a scanner that flags nothing."
    )


def test_limb_a_does_not_flag_the_standards_own_words(reg_text: str) -> None:
    """The other half of the conjunction: it must not fire on a quotation (`-33`).

    `REG-006` §1 quotes ASC 350-20-35-32 and 35-31 and cites KPMG's *Handbook:
    Impairment of nonfinancial assets*. A scanner that called those violations would be
    correct about the characters and wrong about the document, and it would be deleted
    the first time it fired.
    """
    quoted = (
        '\n\nThe standard says "the requirement applies to all assets that are tested '
        'for impairment" in 42% of the cells and 5.8× the base rate.\n\n'
    )
    assert not bare_impairment_in_statistics(reg_text + quoted), (
        "OVER-BROAD — the detector flagged a sentence whose only bare `impairment` sits "
        "inside a quotation, beside a ratio. Reporting the standard's words is not "
        "making a claim about this study's statistics."
    )


# ----------------------------------------------------------------------------- limb B


def test_every_counted_ratio_still_prints_its_count(result_text: str) -> None:
    flat = _flatten_wraps(result_text)
    for ratio, count in COUNTED_RATIOS:
        assert ratio in flat, (
            f"RATIO MOVED — {RESULT.name} no longer contains {ratio!r}. Either the "
            "number changed (update this pin in the same commit) or the count was "
            "dropped along with it — read the next assertion's message."
        )
        assert count in ratio, "fixture is broken: the pin's count is not in its ratio"


def test_no_new_ratio_is_printed_without_its_count(result_text: str) -> None:
    """The bound. Ten sites are open; an eleventh is a regression.

    `REG-006` §3 Q1's third conjunct is a PLACEMENT rule — *next to* the ratio — so a
    count in the run log or three paragraphs away does not discharge it.
    """
    missing = ratio_rows_missing_a_count(result_text)
    new = sorted(set(missing) - set(UNCOUNTED_ROWS))
    assert not new, (
        f"RATIO WITHOUT A COUNT — {RESULT.name} has table rows {new} printing a ratio "
        "with no firm-period count in the row, and they are not in the pinned open set. "
        "`REG-006` §3 Q1 requires the count next to the ratio. The counts live in the "
        "`obs` column of each pair block in `RESULT-REG-006-ladderC-run.log`."
    )


def test_the_open_finding_has_not_silently_closed(result_text: str) -> None:
    """The other direction. If somebody prints the counts, this file must be edited.

    An open-finding pin that survives its own repair is how a bounded violation becomes
    a permanent one: the next session reads ten pinned sites and assumes they are still
    uncounted. C07's EXTEND ME, run backwards.
    """
    still_missing = set(ratio_rows_missing_a_count(result_text))
    closed = sorted(set(UNCOUNTED_ROWS) - still_missing)
    assert not closed, (
        f"SHRINK ME — the rows {closed} now print a count (or have left the document). "
        "The open finding recorded in this file's docstring is smaller than it says. "
        "Remove these from UNCOUNTED_ROWS, and if the set is now empty, delete it and "
        "let test_no_new_ratio_is_printed_without_its_count stand alone."
    )


def test_limb_b_detector_is_not_vacuous_on_a_table_row(result_text: str) -> None:
    """Delete the counts from a counted row and the locator must report it.

    The `-43` conjunction: the real document must be clean of UNPINNED rows AND the
    mutated one must not be. Asserting only the second half passes for a locator that
    flags every row in the file.
    """
    mutated = result_text.replace(
        "| retail | 3.63× (p 0.038, 4 obs) | **3.99× (p 0.0012, 14 obs)** |",
        "| retail | 3.63× (p 0.038) | **3.99× (p 0.0012)** |",
        1,
    )
    assert mutated != result_text, "fixture is broken: the anchor moved"
    if set(ratio_rows_missing_a_count(result_text)) - set(UNCOUNTED_ROWS):
        pytest.skip(
            "the document already carries an unpinned uncounted row — see "
            "test_no_new_ratio_is_printed_without_its_count, which is the failure"
        )
    assert "retail" in ratio_rows_missing_a_count(mutated), (
        "VACUOUS — stripping `4 obs` and `14 obs` from a ratio row changed nothing the "
        "locator can see. It would pass for a detector that never fires."
    )


def test_limb_b_binds_the_prose_sites_that_carry_their_own_count(result_text: str) -> None:
    """`R2b`'s exact deletion, which is in PROSE and outside the row locator's scope.

    This is the assertion that makes probe `R2b` red, and it is deliberately a separate
    mechanism from the row sweep: *next to* is well-defined inside a table row and is a
    judgement call in a paragraph, so the paragraph sites are pinned one at a time
    rather than swept. A pin is narrower than a sweep and it is also honest about being
    narrower — the sweep would have to guess, and `-44` says a guess in a coverage
    claim is the failure mode, not the coverage.
    """
    mutated = _flatten_wraps(
        result_text.replace("**+0.010** (retail, n = 417)", "**+0.010** (retail)", 1)
    )
    assert not all(ratio in mutated for ratio, _ in COUNTED_RATIOS), (
        "VACUOUS — deleting `n = 417` from the retail slope left every pinned prose "
        "ratio intact, so test_every_counted_ratio_still_prints_its_count would stay "
        "green through `R2b`. The pin is not binding its count."
    )
