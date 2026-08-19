#!/usr/bin/env python3
"""wt164 — repair the four bare pointers NO verb list reached, and prove no list could have.

WHY THIS SCRIPT IS SEPARATE FROM `wt163`
----------------------------------------
`wt163` answered the commissioned question and returned RC 0: over the widened vocabulary the
manuscripts carry no undisclosed bare pointer. **That RC 0 is true and it is not enough.** A
vocabulary-free reading of the corpus at `07cd47e` — enumerate by the PREPOSITION, adjudicate the
verb, `docs/REVIEW-028-pointer-vocabulary.md` §3 — found FOUR bare pointers whose verbs sit on
neither `wt160`'s sixteen surface forms nor the commissioned widening:

    III  `visible in`  the parameter sweep
    III  `declared in` the registration before the pilot was run
    III  `printed in`  the same logs
    IV   `verified in` the sessions that introduced them to Papers II or III

They are real: each asks a reader to go and check something and gives them nothing to go on.
They were found by a reader, not by an instrument, and **no widening of the word list would have
found them** — `wt163` post-conditions D4 and D5 pin that as a NEGATIVE, and E4 below re-proves
it against the live files: the repairs must leave `wt163`'s flag set BIT-IDENTICAL. An instrument
that noticed these repairs would be an instrument that could have found the defects, and it
cannot. That silence is the result.

THE TWO SANCTIONED REPAIR MODES (`docs/CO-AUTHOR-CHARTER.md` §2)
----------------------------------------------------------------
R2 and R3 **re-target**: the pointer is real and the artefact exists, so it is named.
R1 and R4 **remove the construction**: R1's "the parameter sweep" names no artefact in this
repository — the sweep is not a committed object, it is the reason itself, so the sentence states
the reason and drops the gesture. R4 pointed at *sessions*, which a reader cannot open; the mark
table it was really invoking is named instead. Neither is an ABSORB: no hedge is added anywhere.

ROLLBACK: every file is copied to `<name>.bak-wt164` first and restored if any post-condition
fails. A rollback is not a verdict on the repair — `wealthTensor-87` lesson (iv).

EXIT: 0 = repaired and all post-conditions hold · 1 = rolled back · 2 = broken.
"""
from __future__ import annotations

import importlib.util
import os
import re
import shutil
import subprocess
import sys

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def _load(name):
    spec = importlib.util.spec_from_file_location(
        name, os.path.join(REPO_ROOT, "scripts", name + ".py"))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


wt160 = _load("wt160_bare_pointer_sweep")
wt163 = _load("wt163_pointer_vocabulary")

P3 = "docs/papers/paper-III-dual-tensor/paper-III.md"
P4 = "docs/papers/paper-IV-composition/paper-IV.md"

# Anchors are matched with EVERY space widened to `\s+`. Anchor strings in hard-wrapped
# markdown span line breaks, and a substring test true of the rendered text is false of the
# file — `wealthTensor-87` lesson (vii), which cost that session two independent failures.
REPAIRS = [
    (P3, "R1 remove",
     "The reason is visible in the parameter sweep:",
     "The reason is that the two monotonicities compound:"),
    (P3, "R2 re-target",
     "declared in the registration before the pilot was run,",
     "declared in `PRE-001` §4.2\nbefore the pilot was run,"),
    (P3, "R3 re-target",
     "printed in the same logs, which permutes",
     "printed in those same run logs\n(`docs/preregistration/RESULT-002-*-run.log`), which permutes"),
    (P4, "R4 remove",
     "Entries marked ✓ were verified in the sessions that introduced them to Papers II or III.",
     "Entries marked ✓ were verified against the sources the mark table in\n"
     "`docs/REFERENCE-POLICY.md` requires."),
]

# The four bare targets that must be GONE afterwards, as they read before the repair.
GONE = ["visible in the parameter sweep",
        "declared in the registration before the pilot was run",
        "printed in the same logs",
        "verified in the sessions that introduced them to Papers II or III"]

BAK = ".bak-wt164"


def _rx(anchor: str) -> re.Pattern:
    return re.compile(r"\s+".join(re.escape(w) for w in anchor.split()))


def _read(path):
    with open(os.path.join(REPO_ROOT, path), encoding="utf-8") as fh:
        return fh.read()


def _write(path, text):
    with open(os.path.join(REPO_ROOT, path), "w", encoding="utf-8") as fh:
        fh.write(text)


def _flat(text):
    return re.sub(r"\s+", " ", text)


def _wt163_flags():
    out = []
    for p in wt163.PAPERS:
        out += [(f["verb"], f["target"]) for f in wt163.sweep_text(_read(p), p)[0]]
    return sorted(out)


def _wt160_flags():
    out = []
    for p in wt160.PAPERS:
        out += [(f["verb"], f["target"]) for f in wt160.sweep_text(_read(p), p)[0]]
    return sorted(out)


def main():
    files = sorted({p for p, *_ in REPAIRS})

    # --- E1 PRE-CONDITION: every anchor is present exactly once, before anything moves ----
    pre = []
    for path, tag, old, _new in REPAIRS:
        n = len(_rx(old).findall(_read(path)))
        pre.append((tag, n))
        if n != 1:
            print(f"wt164: PRE-CONDITION FAILED — {tag} anchor matches {n} time(s), expected 1",
                  file=sys.stderr)
            return 2
    print("  [ok  ] E1 PRE      each of the four anchors matches exactly once — "
          + ", ".join(f"{t}:{n}" for t, n in pre))

    before163 = _wt163_flags()
    before160 = _wt160_flags()

    for path in files:
        shutil.copyfile(os.path.join(REPO_ROOT, path), os.path.join(REPO_ROOT, path + BAK))

    try:
        for path, tag, old, new in REPAIRS:
            text = _read(path)
            text, n = _rx(old).subn(new.replace("\\", "\\\\"), text, count=1)
            if n != 1:
                raise RuntimeError(f"{tag}: substitution applied {n} times")
            _write(path, text)

        checks = []

        # E2 POSITIVE — all four bare pointers are gone, whitespace-flattened.
        left = [g for g in GONE if any(g in _flat(_read(p)) for p in files)]
        checks.append(("E2", "POSITIVE", "all four off-list bare pointers are gone",
                       not left, f"still present: {left}"))

        # E3 POSITIVE — the two RE-TARGETED pointers now carry a followable handle.
        t3 = _flat(_read(P3))
        ok_r2 = "declared in `PRE-001` §4.2 before the pilot was run" in t3
        ok_r3 = ("printed in those same run logs "
                 "(`docs/preregistration/RESULT-002-*-run.log`)") in t3
        checks.append(("E3", "POSITIVE", "R2 and R3 now name an artefact a reader can open",
                       ok_r2 and ok_r3, f"R2={ok_r2} R3={ok_r3}"))

        # E4 NEGATIVE — THE POINT OF THE PASS. wt163's flag set is bit-identical, so the
        # instrument demonstrably could not have found what a reader found.
        after163 = _wt163_flags()
        checks.append(("E4", "NEGATIVE", "wt163's flag set is UNCHANGED by all four repairs",
                       after163 == before163,
                       f"{len(before163)} -> {len(after163)}; a widened word list is blind to "
                       f"defects a reader sees"))

        # E5 NEGATIVE — wt160 likewise unmoved, and still at zero.
        after160 = _wt160_flags()
        checks.append(("E5", "NEGATIVE", "wt160's flag set is UNCHANGED and still empty",
                       after160 == before160 == [],
                       f"{len(before160)} -> {len(after160)}"))

        # E6 POSITIVE — the repaired targets pass the SAME N1-N6 the instruments apply.
        named = []
        for probe in ["declared in `PRE-001` §4.2 before the pilot was run,",
                      "printed in those same run logs "
                      "(`docs/preregistration/RESULT-002-*-run.log`), which permutes",
                      "verified against the sources the mark table in "
                      "`docs/REFERENCE-POLICY.md` requires."]:
            flat, _ = wt160._flatten(probe)
            i = flat.find(" in ")
            named.append(wt160._is_named(wt160._target_window(flat, i + 4)))
        checks.append(("E6", "POSITIVE", "each repaired target passes N1-N6 as NAMED",
                       all(named), f"{named}"))

        # E7 NEGATIVE — no new §N.M or reference breakage.
        rc133 = subprocess.run([sys.executable, "scripts/wt133_crossref_sweep.py"],
                               cwd=REPO_ROOT, capture_output=True).returncode
        checks.append(("E7", "NEGATIVE", "wt133 cross-reference sweep stays clean",
                       rc133 == 0, f"RC {rc133}"))

        # E8 POSITIVE — NOTHING ELSE MOVED. Apply the four substitutions to the FLATTENED
        # pre-repair text and require byte-equality with the flattened post-repair text.
        #
        # The first version of this post-condition asserted "line-count drift is exactly the
        # three added wraps" and FAILED at +1, because three of the four anchors already
        # spanned a line break in the hard-wrapped file, so replacing a two-line span with a
        # two-line span is net zero. That was the post-condition's error, not the repair's —
        # wealthTensor-87 lessons (iv) and (vii), earned again. Flattening removes the wrap
        # from the question entirely, which is what the check should have done from the start.
        drift = {}
        for path in files:
            before = _flat(open(os.path.join(REPO_ROOT, path + BAK), encoding="utf-8").read())
            for rp, _tag, old_a, new_a in REPAIRS:
                if rp == path:
                    before = _rx(old_a).sub(_flat(new_a).replace("\\", "\\\\"), before, count=1)
            drift[os.path.basename(path)] = (before == _flat(_read(path)))
        checks.append(("E8", "POSITIVE", "flattened text differs ONLY in the four repaired spans",
                       all(drift.values()), f"{drift}"))

        ok_all = True
        for cid, kind, desc, ok, detail in checks:
            ok_all &= ok
            print(f"  [{'ok  ' if ok else 'FAIL'}] {cid} {kind:8s} {desc} — {detail}")

        if not ok_all:
            raise RuntimeError("post-conditions failed")

    except Exception as exc:                          # noqa: BLE001
        for path in files:
            shutil.copyfile(os.path.join(REPO_ROOT, path + BAK), os.path.join(REPO_ROOT, path))
        print(f"wt164: ROLLED BACK — {exc}", file=sys.stderr)
        return 1

    print("\nwt164: four off-list bare pointers repaired; wt163 and wt160 both unmoved, "
          "which is the finding.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
