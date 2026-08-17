#!/usr/bin/env python3
"""wt127 — Paper IV §9: move the new limitation from position 1 to position 2 (wealthTensor-70).

Why this exists, and why it is a SECOND script rather than an edit to `wt126`. `wt126`'s ED3
added the abstract's headline limit ("one question, not one structure") to §9 and placed it
FIRST, reasoning that §9 is ordered by weight and the abstract ranks that limit second of its
two headline statements. That reasoning was about prose. Position 1 of §9 is not prose: it is
board criterion `P5g`, whose check greps ITEM 1 specifically for `A composed state nobody can
read`. `regen-board.sh --check` went STALE on the next run and `P5g` flipped ✅ → 🔨 — the
first board movement in five sessions, caused by an insertion that changed no sentence.

The lesson, which is `-70`'s and belongs in the ledger: A CENSUS AND AN IDENTITY GUARD PROVE
WHAT THE TEXT SAYS; NEITHER LOOKS AT WHERE IT SITS. `wt126` asserted that every pre-existing
§9 body survived byte-identically under the renumber, and every one of them did. What moved
was an ORDINAL, and an ordinal is a criterion in a corpus that measures list position. Any
insertion at the head of a numbered list in a manuscript is an edit to a criterion.

The repair is placement, not phrasing. Rewording the new item to carry `P5g`'s phrase would
satisfy the checker while silently demoting the item the criterion was written to protect —
which is gaming a green, the species `-66b` named. Item 1 stays where the board put it.

Hazards. The swap is guarded on the MULTISET of item bodies (unchanged) plus the exact new
ORDER, so a swap cannot become a deletion. Idempotence is checked on position, since neither
body changes. `.bak` first. No CONDUCT or CONCESSIVE string enters.
"""
import pathlib, re, shutil, sys

DRY = "--dry" in sys.argv
ROOT = pathlib.Path.home() / "repos" / "wealth-tensor"
PAPER = ROOT / "docs/papers/paper-IV-composition/paper-IV.md"
BAK = PAPER.with_name(PAPER.name + ".bak-wt70-p9order")

SEC9_OPEN = "## 9 · Limitations\n\n"
SEC10_OPEN = "## 10 · Data and code availability"
NEW_LIMIT_HEAD = "**The three scales share one question, not one structure.**"
P5G_PHRASE = "A composed state nobody can read"
ITEM_RE = re.compile(r"^(\d+)\. (.*)$")

CONDUCT = ("this programme", "this paper's earlier draft", "revision history",
           "an earlier draft", "the draft that preceded")
CONCESSIVES = ("Admittedly", "Of course", "It must be conceded", "To be fair",
               "It should be noted", "It is worth noting", "We acknowledge",
               "It must be admitted", "Needless to say", "In fairness",
               "It bears repeating", "It is important to note")


def norm(s):
    return re.sub(r"\s+", " ", s).strip()


def split_items(section):
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
    i, j = text.index(SEC9_OPEN) + len(SEC9_OPEN), text.index(SEC10_OPEN)
    sec9 = text[i:j]
    before = split_items(sec9)

    assert [n for n, _ in before] == list(range(1, 9)), \
        f"§9 items are not 1..8: {[n for n, _ in before]}"
    # idempotence, checked on POSITION because no body changes (WT-096: fire it, do not read it)
    if before[1][1].startswith(NEW_LIMIT_HEAD):
        print("already applied; refusing (exit 2)")
        sys.exit(2)
    assert before[0][1].startswith(NEW_LIMIT_HEAD), "§9 item 1 is not wt126's new limit"
    assert P5G_PHRASE in norm(before[1][1]), "§9 item 2 is not P5g's comfort item"

    order = [1, 0] + list(range(2, len(before)))
    rebuilt = ""
    for pos, src in enumerate(order, start=1):
        rebuilt += ("" if pos == 1 else "\n") + f"{pos}. {before[src][1]}"
    rebuilt += sec9[len(sec9.rstrip("\n")):]

    after_items = split_items(rebuilt)
    assert [n for n, _ in after_items] == list(range(1, 9)), "§9 renumber is not 1..8"
    assert sorted(b for _, b in after_items) == sorted(b for _, b in before), \
        "§9 bodies changed under the swap"
    assert P5G_PHRASE in norm(after_items[0][1]), "P5g's comfort item is not item 1"
    assert after_items[1][1].startswith(NEW_LIMIT_HEAD), "new limit is not item 2"

    new = text[:i] + rebuilt + text[j:]
    assert sorted(norm(new).split(" ")) == sorted(norm(text).split(" ")), \
        "a pure reordering changed the paper's words"
    assert "µ" not in new, "U+00B5 MICRO SIGN found in output"
    wide = {ln for ln in new.splitlines() if len(ln) > 100 and not ln.startswith("|")}
    old_wide = {ln for ln in text.splitlines() if len(ln) > 100 and not ln.startswith("|")}
    assert wide <= old_wide, f"introduced long lines: {sorted(wide - old_wide)}"
    for c in CONDUCT + CONCESSIVES:
        assert new.count(c) <= text.count(c), f"coach string {c!r} count rose"

    if DRY:
        print("DRY: §9 items 1 and 2 would swap; bodies unchanged, word multiset unchanged")
        return

    shutil.copy2(PAPER, BAK)  # the undo path comes FIRST
    PAPER.write_text(new, encoding="utf-8")

    fresh = PAPER.read_text(encoding="utf-8")
    after = split_items(fresh[fresh.index(SEC9_OPEN) + len(SEC9_OPEN):fresh.index(SEC10_OPEN)])
    assert [n for n, _ in after] == list(range(1, 9)), "§9 is not 1..8 after apply"
    assert P5G_PHRASE in norm(after[0][1]), "P5g's comfort item is not item 1 after apply"
    assert after[1][1].startswith(NEW_LIMIT_HEAD), "new limit is not item 2 after apply"
    print("APPLIED: §9 items 1 and 2 swapped; bak =", BAK.name)


if __name__ == "__main__":
    main()
