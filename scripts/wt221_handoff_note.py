import pathlib
p = pathlib.Path("docs/HANDOFF.md"); lines = p.read_text(encoding="utf-8").split("\n")
OLD_HEAD = "* **149 C-class repairs** landed across the three manuscripts"
i = [n for n, l in enumerate(lines) if l.startswith(OLD_HEAD)]
assert len(i) == 1, i
ADD = [
"",
"## 🩹 ONE CORRECTION LANDED AFTER THE FIRST TAG, AND IT IS THE MOST INSTRUCTIVE THING HERE",
"",
"**The corpus shipped with a broken sentence in it.** paper-IV § 3 read *\"a confiscatory levy on",
"flow **is / leaves** the wealth vector exactly unchanged\"* — a stranded copula, left behind when a",
"late correction replaced the predicate and not the verb before it.",
"",
"**It passed 1,168 tests, thirty green guards, forty-one re-run claims, a page-for-page layout",
"reproduction, and two adversarial verifiers.** A third verifier, reading for something else",
"entirely, happened on it.",
"",
"**THE GAP IS NOT THAT THE APPARATUS IS WEAK — IT IS THAT A LATE CORRECTION ROUND INHERITS NONE OF",
"THE VERIFICATION OF THE ROUND IT CORRECTS.** Both adversarial sweeps and the mechanical stitch",
"check were run over the first 166 repairs and none over the corrections that followed them. If you",
"take one process lesson from this session, take that one: **the last edits are the least checked",
"edits, and they are the ones that ship.**",
"",
"Repaired at `wt220`, with a second milder instance beside it; the tag was moved onto the repair and",
"the move is recorded in the tag's own message. `SHIP-STATEMENT.md` § 6.6 carries it as the sharpest",
"instance of **nothing in this repository reads English**.",
"",
]
lines[i[0]:i[0]] = ADD
p.write_text("\n".join(lines), encoding="utf-8"); print("handoff: correction note inserted")
