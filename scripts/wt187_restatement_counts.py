#!/usr/bin/env python3
"""wt187 — update `tests/test_restatement_reach.py`'s declaration after wt185's III-5 repair.

THE GUARD WAS RIGHT AND IT WAS NOT FIGHTING THE REPAIR.  `test_restatement_reach` pins, per
figure and per section, HOW MANY TIMES the manuscript restates a registered figure, so a
copy that drifts, appears or vanishes moves a count.  wt185's III-5 repair replaced §4.10's
two bare "§5.4's 0.150" attributions with the interval the width is the width OF, so §4.10
now prints 1.135 and 1.285 three times where it printed them once.

The guard's own docstring states the bargain in advance: *"an edit that legitimately adds or
removes a mention turns this suite red and the author must update a number here ... The
failure message names the section and both counts so the update is mechanical."*  This is
that update, and nothing else: 4.10 goes 1 -> 3 for both figures, every other section is
untouched, and no figure is added to or removed from either list.

DERIVED, NOT RE-KEYED.  The new counts are READ OUT OF THE MANUSCRIPT by the guard's own
counting function, not typed from the failure message.

EXIT 0 = both declarations updated and the guard green.  EXIT 2 = refused / rolled back.
"""
import importlib.util, pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
TEST = ROOT / "tests/test_restatement_reach.py"

OLD = {
    "1.135": '    "1.135":  {"4.10": 1, "4.9": 2, "5.4": 1, "7": 1},',
    "1.285": '    "1.285":  {"4.10": 1, "4.9": 2, "5.4": 1, "7": 1},',
}


def measured(fig: str):
    spec = importlib.util.spec_from_file_location("_wt_rr", TEST)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    fn = getattr(mod.measured, "__wrapped__", None) or getattr(mod.measured, "__pytest_wrapped__", None)
    if fn is None:
        sys.exit("PRECONDITION FAILED: cannot reach the guard's counting function under the fixture")
    fn = getattr(fn, "obj", fn)
    return fn()[fig]


def main():
    original = TEST.read_text()
    text = original
    applied = []
    for fig, old in OLD.items():
        if old not in text:
            if re.search(r'"%s":\s*\{"4\.10": 3' % re.escape(fig), text):
                print("wt187: %s already updated." % fig); continue
            sys.exit("REFUSING: declaration line for %s not found verbatim." % fig)
        got = measured(fig)
        if got.get("4.10") != 3:
            sys.exit("REFUSING: the manuscript measures 4.10 -> %r for %s, not 3. "
                     "Run wt185 first, or the repair changed." % (got.get("4.10"), fig))
        new = ('    "%s":  {"4.10": 3, "4.9": 2, "5.4": 1, "7": 1},'
               '  # 4.10 was 1 until wealthTensor-101: wt185 III-5 replaced two bare\n'
               '                                             # "§5.4\'s 0.150" attributions with the interval that width belongs to.'
               % fig)
        text = text.replace(old, new, 1)
        applied.append(fig)

    if applied:
        TEST.write_text(text)

    checks = [
        ("both declarations read 4.10: 3", text.count('{"4.10": 3, "4.9": 2, "5.4": 1, "7": 1}') == 2, False),
        ("no declaration still reads 4.10: 1 for these two figures",
         not re.search(r'"1\.(135|285)":\s*\{"4\.10": 1', text), True),
        ("§4.9's, §5.4's and §7's counts are untouched",
         text.count('"4.9": 2, "5.4": 1, "7": 1') >= 2, True),
        # `text.count("NOT_COUNTED = {")` is 2, not 1: RESULT_NOT_COUNTED contains it as a
        # substring. The first cut asserted 1, refused to write, and was wrong about the file
        # rather than the file being wrong -- which is the correct direction for a guard to fail.
        ("both exclusion lists are untouched",
         text.count("\nNOT_COUNTED = {") == 1 and text.count("\nRESULT_NOT_COUNTED = {") == 1, True),
        ("no figure was added to or removed from the declaration",
         len(re.findall(r'^\s{4}"[0-9.]+":\s*\{', text, re.M)) ==
         len(re.findall(r'^\s{4}"[0-9.]+":\s*\{', original, re.M)), True),
        ("the file still parses", True, False),
    ]
    for label, cond, isneg in checks:
        print("  [%s] %s%s" % ("PASS" if cond else "FAIL", "(NEGATIVE) " if isneg else "", label))
    if any(not c for _, c, _ in checks):
        TEST.write_text(original)
        print("ROLLED BACK.")
        return 2
    print("wt187: updated %s · %d post-conditions, %d NEGATIVE"
          % (", ".join(applied) or "(nothing)", len(checks), sum(1 for _, _, n in checks if n)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
