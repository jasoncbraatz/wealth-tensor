#!/usr/bin/env python3
"""wt128 — Paper II's THIRD independent P7 read (wealthTensor-71): five findings, five edits.

Context. Paper II's convergence counter stood at 9 -> 2 and the paper had not been opened
since `-68`. Verified before reading, not believed: `git log -- docs/papers/paper-II-
redistribution/paper-II.md` ends at `3b073bd` (`-68`), the tree is clean, and the diff
against `.bak-wt68-p7` is exactly `-68`'s two repairs. This pass read the paper whole,
end to end, and the five findings below are what a third pair of eyes returned.

ED1  (II-15) §3.1's budget bullet states "for a **stock** base, κ = *r* exactly" as a law.
     It is true only at zero exemption, and §3.3 -- two subsections later, in this same
     paper -- exhibits the counterexample: a threshold at 0.25x the mean "reduc[es] κ by a
     quarter". A reader who quotes the bullet is quoting something the paper itself
     falsifies. Repair: state the condition and point at the sweep that lifts it. No number
     changes; §3.3 is the witness, so nothing new is asserted.

ED2  (II-16a) §3.1's table is SIX rows and does not say it is a selection. The sweep behind
ED3  (II-16b) it is wider on both bases, and §3.4 quantifies over ALL of it: "the bounded
     runs' Gini spans 0.000-0.891 ... their top decile spans 0.100-0.861". Of those four
     numbers only 0.000 appears anywhere in the paper (§3.1's stock frontier). A referee
     who tries to check 0.891 or 0.861 against §3.1 finds a six-row table whose bounded
     Gini range is 0.125-0.812 and whose top-decile range is 0.138-0.734 -- neither
     endpoint matches, and nothing tells them why. This is `-68`'s II-13 (the table's
     configuration was unstated) one turn further out: II-13 said what the rows ARE, and
     this says what they are NOT -- all of it. Same family, two halves, so it is repaired
     from both sides (`-70`'s WT-111: a scope note needs what I read AND what I changed).
     ED2 marks the table a selection; ED3 stops §3.4 pointing at "the sweep of §3.1" as
     though the reader could read the range off it. NO new number enters either side.

ED4  (II-17) §5's limitation 5 says "every number above is a mean over a tail window of a
     **single** path at `seed = 0`". §7 says, in terms, that three numbers above are not:
     "except the three Var[log *a*] values in §3.1, which are quadrature over the
     multiplier's distribution rather than simulation output". The two sections contradict
     each other, and the contradiction runs against the paper: those three values carry
     §3.1's six-decimal "a change of 6 x 10^-6" claim, and limitation 5 -- read literally
     -- withdraws the precision that claim needs. Repair: scope the quantifier and name the
     exception in §7's own words, so the limitation says what §7 already said.

ED5  (II-18) §6 opens "**Two results in that literature are prior to this paper's central
     contrast**" and two paragraphs later says Benhabib, Bisin and Zhu "supply **three
     further results**" -- one of which (Proposition 3) is then said to have made this
     paper's §3.1 frontiers "already visible", i.e. is itself prior. The topic sentence
     counts two and the section delivers five. The noun is what is wrong: two WORKS are
     cited, and the paragraph structure -- exactly two bolded sources -- says so. One word.

CARDED, NOT REPAIRED (II-19). §3.1 and §6 carry near-identical 40-word descriptions of
Bouchaud and Mezard (2000): "carry a flow levy, a stock levy and the per-capita
redistribution of each in a single/one wealth balance, and give the stationary Pareto
exponent in closed form in all four coordinates". Nothing is wrong today -- they agree --
but this is exactly `-70`'s IV-15 shape: a paraphrase of another section's content is a
standing drift generator that nothing measures. It is NOT repaired here because the
placement is settled: `bf07363` (`-67`) placed "the two mandatory citations ... where they
bind", and §3.1's copy carries the verbatim quotations and the mu-collision disclosure that
§6's does not. Moving or deleting either reopens a ruling this pass has no standing to
reopen. Falsifier for the card: edit one description without the other and the paper
describes one source two ways.

Hazards stated in advance (wt122's rule). Anchors are manuscript strings. Census run BEFORE
writing (`WT-099`) and CLASSIFIED (`-70`'s kit): live / `.bak-*` historical / spent
one-shot, printed in all three, uniqueness asserted over LIVE only -- without the
classifier every anchor in this corpus fails on its own backups.
POSITIONAL CHECK (`-70`'s WT-110, the reason it exists): `P3g` is Paper II's positional
criterion -- it greps ITEM 1 of Limitations for 'Endogenising ρ would make the flow base',
and counts items matching '^[0-9]+\\. \\*\\*' at >= 4. ED4 edits item **5** and inserts
nothing, so no ordinal moves and the bold prefix survives. `P3n` greps for '18 tests';
`P3l` requires 'falsified' and 'nested' in the abstract; `P3a` bounds the abstract. The
abstract is NOT touched by any edit here and `check_abstract_size.py` is run anyway
(244/1478, the tightest in the batch).
G-COACH-3: no CONDUCT or CONCESSIVE string enters any replacement -- asserted, not claimed.
"""
import pathlib, re, shutil, sys

DRY = "--dry" in sys.argv
CENSUS = "--census" in sys.argv
ROOT = pathlib.Path.home() / "repos" / "wealth-tensor"
PAPER = ROOT / "docs/papers/paper-II-redistribution/paper-II.md"
BAK = PAPER.with_name(PAPER.name + ".bak-wt71-p7")

SENTINEL = "These six rows are a selection"

ED1_ANCHOR = "- for a **stock** base, κ = *r* exactly;\n"
ED1_NEW = (
    "- for a **stock** base at zero exemption, κ = *r* exactly — §3.3 raises the threshold and κ\n"
    "  falls;\n"
)

ED2_ANCHOR = "implementation's default; §3.2 is the sweep that lowers it.*\n"
ED2_NEW = (
    "implementation's default; §3.2 is the sweep that lowers it. These six rows are a selection: the\n"
    "rate sweep behind them is wider on both bases, and §3.4 quantifies over all of it.*\n"
)

ED3_ANCHOR = (
    "second condition that does all of the separating. Across the sweep of §3.1 the bounded runs'\n"
    "Gini spans 0.000–0.891 against the condensed run's 0.994, which separates nothing; their top\n"
)
ED3_NEW = (
    "second condition that does all of the separating. Across §3.1's full rate sweep — wider than the\n"
    "six rows tabulated there — the bounded runs' Gini spans 0.000–0.891 against the condensed run's\n"
    "0.994, which separates nothing; their top\n"
)

ED4_ANCHOR = (
    "   and every number above is a mean over a tail window of a **single** path at `seed = 0`\n"
    "   rather than an ensemble average. Seed-robustness is asserted separately rather than averaged\n"
)
ED4_NEW = (
    "   and every *simulated* number above is a mean over a tail window of a **single** path at\n"
    "   `seed = 0` rather than an ensemble average — the exception is §3.1's three Var[log *a*]\n"
    "   values, which are quadrature rather than simulation output (§7). Seed-robustness is asserted\n"
    "   separately rather than averaged\n"
)

ED5_ANCHOR = "several directions. **Two results in that\n"
ED5_NEW = "several directions. **Two works in that\n"

EDITS = (("ED1", ED1_ANCHOR, ED1_NEW), ("ED2", ED2_ANCHOR, ED2_NEW),
         ("ED3", ED3_ANCHOR, ED3_NEW), ("ED4", ED4_ANCHOR, ED4_NEW),
         ("ED5", ED5_ANCHOR, ED5_NEW))

CONCESSIVES = (
    "Admittedly", "Of course", "It must be conceded", "To be fair", "It should be noted",
    "It is worth noting", "We acknowledge", "It must be admitted", "Needless to say",
    "In fairness", "It bears repeating", "It is important to note",
)
CONDUCT = (
    "this programme", "this paper's earlier draft", "revision history",
    "an earlier draft", "the draft that preceded",
)


def norm(s):
    return re.sub(r"\s+", " ", s)


def classify(path):
    """live / historical (.bak-*) / spent one-shot (a committed patch script's own text)."""
    name = path.name
    if ".bak-" in name:
        return "historical"
    if path.parent.name == "scripts" and re.match(r"(wt\d+|patch_)", name):
        return "spent"
    return "live"


def census():
    """WT-099: census BEFORE patching, classified (-70's kit). Uniqueness over LIVE only."""
    buckets = {lbl: {"live": [], "historical": [], "spent": []} for lbl, _, _ in EDITS}
    n_files = 0
    for p in ROOT.rglob("*"):
        if not p.is_file() or ".git/" in str(p):
            continue
        try:
            t = p.read_text(encoding="utf-8")
        except Exception:
            continue
        n_files += 1
        nt = norm(t)
        for lbl, anchor, _ in EDITS:
            c = nt.count(norm(anchor))
            if c:
                buckets[lbl][classify(p)].append(f"{p.relative_to(ROOT)} x{c}")
    print(f"CENSUS over {n_files} readable files under {ROOT}")
    ok = True
    for lbl, _, _ in EDITS:
        b = buckets[lbl]
        print(f"\n{lbl}:")
        for k in ("live", "historical", "spent"):
            print(f"   {k:11s} {len(b[k]):3d}  {b[k] if b[k] else '-'}")
        if len(b["live"]) != 1:
            ok = False
            print(f"   !! {lbl}: LIVE count is {len(b['live'])}, expected 1")
    print("\nCENSUS", "CLEAN" if ok else "DIRTY")
    return 0 if ok else 1


def main():
    if CENSUS:
        sys.exit(census())

    text = PAPER.read_text(encoding="utf-8")

    # idempotence guard, normalised and ASSERTED (fire it, do not read it -- WT-096)
    if norm(SENTINEL) in norm(text):
        print("already applied; refusing (exit 2)")
        sys.exit(2)

    # every anchor asserted exactly once, literal AND normalised, before any write
    for label, anchor, _ in EDITS:
        n_lit = text.count(anchor)
        n_norm = norm(text).count(norm(anchor))
        assert n_lit == 1, f"{label}: literal anchor count {n_lit} != 1"
        assert n_norm == 1, f"{label}: normalised anchor count {n_norm} != 1"

    new = text
    for _, anchor, repl in EDITS:
        new = new.replace(anchor, repl)

    # REWRAP GUARD (-70's kit, generalised): every one of these edits re-wraps its
    # paragraph, so a stray word could vanish into a line break and no anchor guard would
    # see it. Assert the whole document's NORMALISED text is exactly the normalised
    # original with the normalised replacements applied -- i.e. the only thing that
    # changed is what the edits say changed, and re-wrapping introduced nothing.
    expect = norm(text)
    for _, anchor, repl in EDITS:
        expect = expect.replace(norm(anchor), norm(repl))
    assert norm(new) == expect, "rewrap guard: normalised output is not the intended text"

    # glyph guard: no MICRO SIGN may enter a manuscript
    assert "µ" not in new, "U+00B5 MICRO SIGN found in output"
    # character-width guard, SET subset (-69's lesson: name the defect, don't count it)
    wide = {ln for ln in new.splitlines() if len(ln) > 100 and not ln.startswith("|")}
    old_wide = {ln for ln in text.splitlines() if len(ln) > 100 and not ln.startswith("|")}
    assert wide <= old_wide, f"introduced long lines: {sorted(wide - old_wide)}"
    # G-COACH guard: counts must not rise from these edits
    for c in CONDUCT + CONCESSIVES:
        assert new.count(c) <= text.count(c), f"coach string {c!r} count rose"
    # P3g guard: Limitations must still open at item 1 with its phrase, and still carry
    # >= 4 bold-prefixed items. ED4 edits item 5; this proves it did not touch item 1.
    def limitations(t):
        out, f = [], False
        for ln in t.split("\n"):
            if re.match(r"^## \d+ · Limitations", ln):
                f = True
                continue
            if f and ln.startswith("## "):
                break
            if f:
                out.append(ln)
        return "\n".join(out)
    for tag, t in (("before", text), ("after", new)):
        lim = limitations(t)
        item1 = re.split(r"^2\. ", lim, flags=re.M)[0]
        assert "Endogenising ρ would make the flow base" in norm(item1), f"P3g item 1 broken {tag}"
        assert len(re.findall(r"^\d+\. \*\*", lim, flags=re.M)) >= 4, f"P3g item count {tag}"
    # P3n / P3l guards: the couplings this paper punishes you for
    assert new.count("18 tests") == text.count("18 tests"), "'18 tests' count changed"
    abstract = new.split("## Abstract")[1].split("**Keywords")[0]
    assert abstract == text.split("## Abstract")[1].split("**Keywords")[0], "abstract changed"
    assert "falsified" in abstract and "nested" in abstract, "P3l strings absent"

    if DRY:
        print("DRY: all five edits would apply cleanly; every guard passed")
        return

    shutil.copy2(PAPER, BAK)  # the undo path comes FIRST
    PAPER.write_text(new, encoding="utf-8")

    # post-conditions ASSERTED against a fresh read
    after = PAPER.read_text(encoding="utf-8")
    assert norm(SENTINEL) in norm(after), "ED2 sentinel absent after apply"
    for label, anchor, repl in EDITS:
        assert repl in after, f"{label}: replacement absent after apply"
        assert anchor not in after, f"{label}: old text survived"
    assert "µ" not in after
    print("APPLIED: ED1 + ED2 + ED3 + ED4 + ED5; bak =", BAK.name)


if __name__ == "__main__":
    main()
