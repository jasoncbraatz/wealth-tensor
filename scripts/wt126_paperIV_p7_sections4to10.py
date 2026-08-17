#!/usr/bin/env python3
"""wt126 — Paper IV §4-§10 read against the narrowing (wealthTensor-70): three repairs.

Context. `WT-102` narrowed Paper IV's title and abstract; `wt121` touched three places and
`-69`/`wt125` propagated the new framing through §1-§3 and stopped at the section boundary.
§4-§10 had never been read against `WT-102`. `-69`'s tell — a framing patch's blast radius is
every line that agreed with the old framing IN ITS OWN WORDS — predicted paraphrases. Two of
the three findings below are not paraphrases at all: one is the ladder phrase itself, and one
was created by `wt125` two hours earlier.

ED1  (finding IV-14) §4.1, the objection stated at full strength, opens by restating the
     paper's own claim as "*You claim a unit that composes from household to sovereign.*"
     That is the ladder `WT-102` removed, minus two articles — which is exactly why `wt120`'s
     census did not see it: the censused string was "from the household to the sovereign".
     §4.1 is the paper putting words in a referee's mouth about what the paper claims, so
     after `wt121` the paper's own strongest self-statement and its abstract disagree, and
     the abstract is the one that reads as the retreat. Repair: state the objection against
     the claim the paper now makes — one type at three named scales, surviving summation —
     which is also the sharper objection, because it lands directly on §4.1's own closing
     line ("you cannot ... claim structure survives aggregation"). No other sentence of the
     paragraph changes; asserted below over the normalised tail, not merely intended.

ED2  (finding IV-15) §8's chain entry says "What is left is weaker, **is what §3 now says**,
     and is still worth publishing: one question, asked at three scales, answered
     quantitatively at each." `wt125`'s ED2 added a third conjunct to §3's closing (the
     addition of §2.2), so that colon-list stopped being what §3 says at the moment `wt125`
     landed. `-69`'s own repair generated a fresh instance of `-69`'s own species, one
     section outside the range it read. Repair by DELETING the cross-reference rather than
     resyncing it (`WT-098`): §8's first sentence already names §3, the clause carried no
     other load, and a paraphrase of another section's content is a standing drift generator
     that would have to be re-synced every time §3 moves.

ED3  (finding IV-16) The abstract, post-`wt121`, gives second-clause billing to a LIMIT:
     "and on one limit its own end-to-end test imposed: those scales share **one question,
     not one structure**." §9 is titled Limitations, carries seven items, and does not carry
     that one. §4.4's own heading ("stated here rather than in §9") shows the paper treats §9
     as the default home for limits and announces departures from it; this departure was
     never announced, because before the narrowing the limit was a mid-§3 demotion rather
     than an abstract-level claim. Repair: add it as §9's first item, worded from §3 and §8
     so that nothing new is asserted, and renumber. Placement is first because the abstract
     ranks it second of the paper's two headline statements, and §9 is ordered by weight.

Hazards stated in advance (`wt122`'s rule).
  * ED3 renumbers seven list items. The guard is an IDENTITY guard, not a count (`-69(ii)`,
    `WT-108`): the multiset of item BODIES after the edit must equal the bodies before plus
    exactly the one new body. A count of "8 items where there were 7" would pass while
    silently eating item 5.
  * ED1 rewraps a whole paragraph. The guard asserts the normalised text AFTER the changed
    first sentence is byte-identical to the original's, so a rewrap cannot smuggle an edit.
  * Census run BEFORE writing (`WT-099`) across docs/, tests/, scripts/, src/, normalised
    first (`-62`'s line-wrap trap, which runs both ways). Anchor uniqueness is ASSERTED.
  * G-COACH-3: §9 IS in `CONDUCT_ALLOWED_SECTIONS`, so a CONDUCT string there would not
    raise the gate's count — which is precisely why the guard below is document-wide and
    does not consult the allow-list. "an earlier draft" was the natural phrasing for ED3 and
    is refused on that basis.
  * Edit labels are ED-prefixed (`-67`). Post-conditions ASSERTED, not printed (`-67`).
"""
import pathlib, re, shutil, sys

DRY = "--dry" in sys.argv
ROOT = pathlib.Path.home() / "repos" / "wealth-tensor"
PAPER = ROOT / "docs/papers/paper-IV-composition/paper-IV.md"
BAK = PAPER.with_name(PAPER.name + ".bak-wt70-p7")
CENSUS_DIRS = ("docs", "tests", "scripts", "src")
LIVE = "docs/papers/paper-IV-composition/paper-IV.md"
# Spent one-shots that quote the manuscript as it stood when they ran. `-69` verified —
# not assumed — that no test and no Makefile target executes patch_wt56; that verification
# is re-asserted below rather than inherited, because "someone checked once" is not a guard.
SPENT_ONE_SHOTS = ("scripts/patch_wt56_e1_remedy.py",)
EXEC_HINTS = ("python", "import ", "runpy", "subprocess", "exec(", "$(")

SENTINEL = "keeps one type at the household, firm and sovereign scales"

# ---------------------------------------------------------------- ED1 · §4.1
ED1_ANCHOR = (
    "*You claim a unit that composes from household to sovereign. But the best-established result about\n"
    "aggregation in economics says the opposite. Sonnenschein (1972, 1973), Mantel (1974) and Debreu\n"
    "(1974) proved that aggregate excess demand inherits from individually rational agents only\n"
    "continuity, homogeneity of degree zero and Walras's Law — not downward slope, not uniqueness, not\n"
    "stability. Aggregate demand can take essentially arbitrary shape. Worse: your own Paper I cites\n"
    "SMD approvingly, as evidence that doubting inherited aggregation is inside the mainstream. You\n"
    "cannot cite the theorem that aggregation destroys structure and then claim structure survives\n"
    "aggregation.*\n"
)
ED1_NEW = (
    "*You claim a unit that keeps one type at the household, firm and sovereign scales and survives\n"
    "being summed. But the best-established result about aggregation in economics says the opposite.\n"
    "Sonnenschein (1972, 1973), Mantel (1974) and Debreu (1974) proved that aggregate excess demand\n"
    "inherits from individually rational agents only continuity, homogeneity of degree zero and\n"
    "Walras's Law — not downward slope, not uniqueness, not stability. Aggregate demand can take\n"
    "essentially arbitrary shape. Worse: your own Paper I cites SMD approvingly, as evidence that\n"
    "doubting inherited aggregation is inside the mainstream. You cannot cite the theorem that\n"
    "aggregation destroys structure and then claim structure survives aggregation.*\n"
)
ED1_OLD_HEAD = "*You claim a unit that composes from household to sovereign."
ED1_NEW_HEAD = ("*You claim a unit that keeps one type at the household, firm and sovereign "
                "scales and survives being summed.")

# ---------------------------------------------------------------- ED2 · §8
ED2_ANCHOR = (
    "scale carries a release rate α for which the sovereign scale has no counterpart. What is left is\n"
    "weaker, is what §3 now says, and is still worth publishing: one question, asked at three scales,\n"
    "answered quantitatively at each. The surviving resemblance is not nothing and is not a structure —\n"
)
ED2_NEW = (
    "scale carries a release rate α for which the sovereign scale has no counterpart. What is left is\n"
    "weaker and is still worth publishing: one question, asked at three scales, answered\n"
    "quantitatively at each. The surviving resemblance is not nothing and is not a structure —\n"
)

# ---------------------------------------------------------------- ED3 · §9
SEC9_OPEN = "## 9 · Limitations\n\n"
SEC10_OPEN = "## 10 · Data and code availability"
ED3_NEW_ITEM = (
    "**The three scales share one question, not one structure.** The corpus's own end-to-end test\n"
    "   (`END-TO-END-001` leg `E1`) asked whether the sovereign scale's realisation share and the\n"
    "   firm scale's observability share are one object seen twice, and rejected it: what the firm\n"
    "   scale's filter does not recognise is deferred and released at rate α, what the sovereign\n"
    "   scale's base does not recognise is never assessed, and there is no parameter on one side\n"
    "   playing α's part on the other. What the framework offers across scales is therefore one\n"
    "   type, one question answered quantitatively at each, and addition within a scale — not a\n"
    "   correspondence between the scales' parameters. §3 records the demotion and §8 the route.\n"
)

CONDUCT = ("this programme", "this paper's earlier draft", "revision history",
           "an earlier draft", "the draft that preceded")
CONCESSIVES = ("Admittedly", "Of course", "It must be conceded", "To be fair",
               "It should be noted", "It is worth noting", "We acknowledge",
               "It must be admitted", "Needless to say", "In fairness",
               "It bears repeating", "It is important to note")

ITEM_RE = re.compile(r"^(\d+)\. (.*)$")


def norm(s):
    return re.sub(r"\s+", " ", s).strip()


def census(anchors):
    """WT-099: every anchor's occurrences across the corpus, normalised, BEFORE any write."""
    hits, n_files = {label: [] for label, _ in anchors}, 0
    for d in CENSUS_DIRS:
        for p in sorted((ROOT / d).rglob("*")):
            if not p.is_file():
                continue
            try:
                body = norm(p.read_text(encoding="utf-8"))
            except (UnicodeDecodeError, OSError):
                continue
            n_files += 1
            for label, anchor in anchors:
                c = body.count(norm(anchor))
                if c:
                    hits[label].append((str(p.relative_to(ROOT)), c))
    print(f"  census: {n_files} files read across {', '.join(CENSUS_DIRS)}/")
    for label, found in hits.items():
        print(f"    {label}: " + (", ".join(f"{f} x{c}" for f, c in found) or "NOWHERE"))
    return hits


def split_items(section):
    """Return [(number, body)] for a section's top-level numbered list."""
    items, cur = [], None
    for line in section.split("\n"):
        m = ITEM_RE.match(line)
        if m:
            if cur:
                items.append(cur)
            cur = [int(m.group(1)), m.group(2)]
        elif cur is not None:
            cur[1] += "\n" + line
    if cur:
        items.append(cur)
    return [(n, b.rstrip("\n")) for n, b in items]


def main():
    text = PAPER.read_text(encoding="utf-8")

    # idempotence guard, normalised and ASSERTED — fire it, do not read it (WT-096)
    if norm(SENTINEL) in norm(text):
        print("already applied; refusing (exit 2)")
        sys.exit(2)

    hits = census([("ED1", ED1_ANCHOR), ("ED2", ED2_ANCHOR)])
    for label, anchor in (("ED1", ED1_ANCHOR), ("ED2", ED2_ANCHOR)):
        assert text.count(anchor) == 1, f"{label}: literal anchor count != 1"
        assert norm(text).count(norm(anchor)) == 1, f"{label}: normalised anchor count != 1"
        # A census over a corpus that keeps its own undo paths and its own spent one-shots
        # will always find the anchor in them. Reporting those separately is the point
        # (`-66b`); folding them into the live count would make every anchor look ambiguous
        # and folding them in silently would make a live duplicate invisible.
        live, historical, spent = [], [], []
        for f, c in hits[label]:
            (historical if ".bak-" in f else spent if f in SPENT_ONE_SHOTS
             else live).append((f, c))
        print(f"    {label}: live={[f for f, _ in live]} "
              f"historical={len(historical)} .bak · spent={[f for f, _ in spent]}")
        assert [f for f, _ in live] == [LIVE], f"{label}: live occurrences are {live}"

    # Re-verify, rather than inherit, that the spent one-shots are dead code. A line that
    # merely NAMES the script (wt125's docstring does) is a citation; a line that names it
    # next to an execution verb is a caller.
    for s in SPENT_ONE_SHOTS:
        stem = pathlib.Path(s).name.removesuffix(".py")
        callers = []
        targets = [p for d in ("tests", "scripts") for p in (ROOT / d).rglob("*.py")]
        targets += [p for p in (ROOT.glob("Makefile"), ROOT.glob("*.mk")) for p in p]
        for p in targets:
            if str(p.relative_to(ROOT)) == s:
                continue
            try:
                lines = p.read_text(encoding="utf-8").split("\n")
            except (UnicodeDecodeError, OSError):
                continue
            callers += [f"{p.relative_to(ROOT)}:{i}" for i, ln in enumerate(lines, 1)
                        if stem in ln and any(h in ln for h in EXEC_HINTS)]
        assert not callers, f"{s} is executed by {callers} — it is not a spent one-shot"
        print(f"    spent one-shot {s}: no caller in tests/, scripts/ or make targets")

    # ED1: the paragraph is rewrapped, so prove that ONLY the first sentence changed.
    tail_old = norm(ED1_ANCHOR)[len(norm(ED1_OLD_HEAD)):]
    tail_new = norm(ED1_NEW)[len(norm(ED1_NEW_HEAD)):]
    assert norm(ED1_ANCHOR).startswith(norm(ED1_OLD_HEAD)), "ED1: old head is not the head"
    assert norm(ED1_NEW).startswith(norm(ED1_NEW_HEAD)), "ED1: new head is not the head"
    assert tail_old == tail_new, "ED1: rewrap altered text after the first sentence"

    new = text.replace(ED1_ANCHOR, ED1_NEW).replace(ED2_ANCHOR, ED2_NEW)

    # ED3: renumber §9 and insert the new first item, guarded on the IDENTITY of the bodies.
    i, j = new.index(SEC9_OPEN) + len(SEC9_OPEN), new.index(SEC10_OPEN)
    sec9 = new[i:j]
    before = split_items(sec9)
    assert [n for n, _ in before] == list(range(1, len(before) + 1)), \
        f"§9 items are not 1..N as read: {[n for n, _ in before]}"
    assert len(before) == 7, f"§9 carries {len(before)} items, expected 7"

    rebuilt = "1. " + ED3_NEW_ITEM.rstrip("\n")
    for n, body in before:
        rebuilt += f"\n{n + 1}. {body}"
    rebuilt += sec9[len(sec9.rstrip("\n")):]  # preserve the section's trailing whitespace
    after_items = split_items(rebuilt)
    assert [n for n, _ in after_items] == list(range(1, 9)), "§9 renumber is not 1..8"
    assert [b for _, b in after_items[1:]] == [b for _, b in before], \
        "§9 bodies changed under the renumber"
    assert norm(after_items[0][1]) == norm(ED3_NEW_ITEM), "§9 new item body is not the new item"
    new = new[:i] + rebuilt + new[j:]

    # glyph guard: no MICRO SIGN may enter a manuscript
    assert "µ" not in new, "U+00B5 MICRO SIGN found in output"
    # width guard as a SET, not a count (-69(ii)): name the introduced lines, nothing else
    wide = {ln for ln in new.splitlines() if len(ln) > 100 and not ln.startswith("|")}
    old_wide = {ln for ln in text.splitlines() if len(ln) > 100 and not ln.startswith("|")}
    assert wide <= old_wide, f"introduced long lines: {sorted(wide - old_wide)}"
    # G-COACH guard, document-wide and deliberately blind to CONDUCT_ALLOWED_SECTIONS
    for c in CONDUCT + CONCESSIVES:
        assert new.count(c) <= text.count(c), f"coach string {c!r} count rose"
    # the ladder phrase must not survive anywhere in the manuscript, in either article form
    for ladder in ("composes from household to sovereign",
                   "composes from the household to the sovereign"):
        assert ladder not in new, f"ladder phrase survived: {ladder!r}"

    if DRY:
        print("DRY: ED1 + ED2 + ED3 would apply cleanly; §9 goes 7 items -> 8")
        for ln in new.splitlines():
            if len(ln) > 100 and not ln.startswith("|"):
                print("  long (pre-existing):", ln)
        return

    shutil.copy2(PAPER, BAK)  # the undo path comes FIRST
    PAPER.write_text(new, encoding="utf-8")

    after = PAPER.read_text(encoding="utf-8")
    assert norm(SENTINEL) in norm(after), "ED1 sentinel absent after apply"
    assert ED1_ANCHOR not in after and ED1_NEW in after, "ED1 did not land"
    assert ED2_ANCHOR not in after and ED2_NEW in after, "ED2 did not land"
    assert norm(ED3_NEW_ITEM) in norm(after), "ED3 did not land"
    assert "\n8. **The whitespace measurement is about occupancy" in after, "ED3 renumber lost"
    assert "µ" not in after
    print("APPLIED: ED1 + ED2 + ED3; bak =", BAK.name)


if __name__ == "__main__":
    main()
