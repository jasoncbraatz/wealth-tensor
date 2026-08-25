#!/usr/bin/env python3
"""wt216 — reconcile P7's closure with the two wiring guards that pin its OPEN state.

THE COLLISION. `wt191` C6 and `wt192b` B10 assert "P7 is still manual:". They were written at
-102 to prove Jason's ruling had been WIRED INTO THE BOARD while the four-pass plan ran, and
they are correct for exactly as long as the plan is running. DoD section 3, Pass D, item 5 is
"close P7". A guard that fires when the plan's last step executes is asserting the plan will
never finish. Both are MOVING SUBJECTS, and this is the eleventh and twelfth instance.

AND `wt192b` DOES NOT ONLY CHECK -- IT WRITES. It re-appends its amendment paragraph to P7's
fourth column whenever that paragraph is absent, so the first `--claims-all` after the closure
appended 900 words of prose onto the end of a shell command. Caught by the claim re-runner,
which is the run that matters, and repaired here.

THE REPAIR IS ONE CHARACTER OF INSIGHT: a `cmd:` criterion runs through `bash -c`, so the
amendment narrative survives as a TRAILING SHELL COMMENT. The check runs; every string B4, B5,
B6 and B11 look for is still in the row; nothing is deleted. The two status assertions are then
widened -- from "P7 is manual" to "P7's check is wired to the DoD rather than to the retired
convergence clause", which is what they were always about and is true on both sides of the ship.

Idempotent; exit 2 if a site matches neither state.
"""
import pathlib, sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
TSV = ROOT / "docs/done-criteria.tsv"

EDITS = [
("wt191-C6", "scripts/wt191_ship_dod_wiring.py",
 '''chk("C6 P7 is still manual: (PENDING-HUMAN, not auto-closable)",
    [l for l in t.split("\\n") if l.startswith("P7\\t")][0].split("\\t")[3].startswith("manual:"))''',
 '''# -106: WIDENED FROM A STATUS TO A WIRING CLAIM. This asserted "P7 is still manual:", which is
# true only while the four-pass plan is running -- and DoD section 3, Pass D, item 5 is "close
# P7". What C6 was always about is that P7's check answers to the DoD and not to the retired
# convergence clause, which holds on both sides of the ship: manual: while the plan runs, and a
# cmd: over the DoD's own ship conditions once it has.
_p7 = [l for l in t.split("\\n") if l.startswith("P7\\t")][0].split("\\t")[3]
chk("C6 P7's check is wired to the DoD, not to the retired convergence clause",
    ("DEFINITION-OF-DONE-SHIP" in _p7) and
    (_p7.startswith("manual:") or
     (_p7.startswith("cmd:") and "SHIP-LIST.md" in _p7 and "FIGURE-PLAN.md" in _p7)))'''),

("wt192b-noclobber", "scripts/wt192b_board_amendment.py",
 '''        if ADD.strip() not in c[3]:
            c[3] = c[3] + ADD''',
 '''        # -106: DO NOT RE-APPEND ONCE P7 HAS SHIPPED. This block appended ADD whenever it was
        # absent from the cell -- and after Pass D closed P7 the cell is a shell command, so the
        # first --claims-all after the closure appended 900 words of prose onto the end of it.
        # A patch script must recognise a legitimately-changed successor state, which is the
        # LANDED-marker rule -105 established for wt182. The marker here is the cmd: prefix.
        if ADD.strip() not in c[3] and not c[3].startswith("cmd:"):
            c[3] = c[3] + ADD'''),

("wt192b-B10", "scripts/wt192b_board_amendment.py",
 '''chk("B10 P7 is still manual/PENDING-HUMAN", row.split("\\t")[3].startswith("manual:"))''',
 '''# -106: same widening as wt191's C6, and for the same reason.
chk("B10 P7's check answers to the DoD -- manual while the plan runs, cmd once it has shipped",
    row.split("\\t")[3].startswith("manual:") or
    (row.split("\\t")[3].startswith("cmd:") and "SHIP-LIST.md" in row))'''),
]

def restore_p7_narrative():
    """Put the amendment back where every guard can still see it: after a shell comment."""
    lines = TSV.read_text(encoding="utf-8").split("\n")
    for i, l in enumerate(lines):
        f = l.split("\t")
        if f and f[0] == "P7" and f[3].startswith("cmd:"):
            if " # " in f[3]:
                print("ALREADY-APPLIED: P7 already carries the narrative as a comment"); return 0
            head, sep, tail = f[3].partition("git rev-parse -q --verify refs/tags/v1.0-preprint >/dev/null")
            if not sep:
                print("FAIL: P7's check does not end where expected"); return 2
            narrative = tail.strip()
            if not narrative:
                print("NOTE: no trailing narrative to reconcile"); return 0
            f[3] = head + sep + "   # " + narrative
            lines[i] = "\t".join(f)
            TSV.write_text("\n".join(lines), encoding="utf-8")
            print("APPLIED: P7's amendment narrative preserved as a trailing shell comment")
            return 0
    print("NOTE: P7 is not a cmd: criterion; nothing to reconcile"); return 0

def main():
    rc = restore_p7_narrative()
    if rc: return rc
    applied = already = 0; fail = []; new = {}
    for tag, rel, old, repl in EDITS:
        p = ROOT / rel
        t = new.get(rel) or p.read_text(encoding="utf-8")
        if t.count(old) == 1 and t.count(repl) == 0:
            new[rel] = t.replace(old, repl, 1); applied += 1; print("APPLIED         %s" % tag)
        elif t.count(old) == 0 and t.count(repl) == 1:
            new[rel] = t; already += 1; print("ALREADY-APPLIED %s" % tag)
        else:
            new[rel] = t; fail.append(tag)
            print("!! NEITHER      %s  old=%d new=%d" % (tag, t.count(old), t.count(repl)))
    if fail:
        print("\nFAIL: %d site(s); NOTHING WRITTEN to scripts/" % len(fail)); return 2
    for rel, t in new.items():
        p = ROOT / rel
        if p.read_text(encoding="utf-8") != t:
            bak = p.with_suffix(p.suffix + ".bak-wt216")
            if not bak.exists(): bak.write_text(p.read_text(encoding="utf-8"), encoding="utf-8")
            p.write_text(t, encoding="utf-8"); print("WROTE %s" % rel)
    print("\napplied=%d already=%d" % (applied, already)); return 0

if __name__ == "__main__":
    sys.exit(main())
