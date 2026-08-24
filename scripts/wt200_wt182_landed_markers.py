import pathlib, shutil
p = pathlib.Path("scripts/wt182_paperIV_p7pass3.py")
bak = pathlib.Path("scripts/wt182_paperIV_p7pass3.py.bak-wt105")
if not bak.exists():
    shutil.copy2(p, bak)
t = p.read_text(encoding="utf-8")

if "LANDED = {" in t:
    print("  already patched (idempotent no-op)")
else:
    marker = "def _flat(s: str) -> str:"
    block = (
        "# The DISTINCTIVE CLAIM each repair introduced, one per tag. A repair is LANDED when its own\n"
        "# claim is present -- not when the whole surrounding paragraph still matches the wrapped\n"
        "# string this file wrote. Those are different questions, and only the first is about THIS\n"
        "# repair. wealthTensor-104 flattened whitespace here after SL-9 reflowed a paragraph, which\n"
        "# fixed the REFLOW case and left the REWORD case -- teed up there, and hit head-on at\n"
        "# wealthTensor-105 when a Pass C C-d repair gave 'the fourth paper' its antecedent inside\n"
        "# IV-12a's own sentence, leaving every edit intact and this file red. Each marker below is\n"
        "# also a postcondition subject, so 'applied' and 'passes' cannot disagree.\n"
        "# A FALSE-POSITIVE REDUCTION under DoD 1.1's narrow exception: it looks at nothing new.\n"
        "LANDED = {\n"
        "    \"IV-12a\": \"their record named in \\u00a710, one for each\",\n"
        "    \"IV-12b\": \"roughly 7,500 words\",\n"
        "    \"IV-13\":  \"Had the route worked, \\u00a75 would indict the Marshallian cross\",\n"
        "    \"IV-11\":  \"for \\u00a71.1's reading of \\u00a74.3 as\",\n"
        "    \"IV-12c\": \"have their record named here, which\",\n"
        "    \"IV-10\":  \"`python3 scripts/wt018_report.py` prints \\u00a75's table\",\n"
        "}\n\n\n"
    )
    assert t.count(marker) == 1
    t = t.replace(marker, block + marker, 1)

    old = ("        if _flat(new) in _flat(txt) and old not in txt:\n"
           "            print(f\"  {tag}: already applied (idempotent no-op)\")\n"
           "            continue")
    new = ("        mark = LANDED.get(tag)\n"
           "        if old not in txt and (\n"
           "                _flat(new) in _flat(txt) or (mark and _flat(mark) in _flat(txt))):\n"
           "            print(f\"  {tag}: already applied (idempotent no-op)\")\n"
           "            continue")
    assert t.count(old) == 1, t.count(old)
    t = t.replace(old, new, 1)
    p.write_text(t, encoding="utf-8")
    print("  wt182 patched")

# every marker must actually be present in the manuscript right now, or the marker is wrong
paper = pathlib.Path("docs/papers/paper-IV-composition/paper-IV.md").read_text(encoding="utf-8")
flat = " ".join(paper.split())
import re
for tag, mark in re.findall(r'"(IV-[0-9a-c]+)":\s+"((?:[^"\\]|\\.)*)"', p.read_text(encoding="utf-8")):
    m = mark.encode().decode("unicode_escape")
    print("   marker", tag, "present:", " ".join(m.split()) in flat)
