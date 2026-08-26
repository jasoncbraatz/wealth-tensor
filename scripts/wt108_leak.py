import pathlib, sys, re
P = pathlib.Path("docs/papers/paper-IV-composition/paper-IV.md")
s = P.read_text(encoding="utf-8")
old = "> **Decided at wealthTensor-107, executed at wealthTensor-108 (2026-08-26).** This manuscript's"
new = "> **Decided and executed in the `paper-rebuild` pass of 2026-08-26.** This manuscript's"
if s.count(old) != 1:
    sys.exit("ABORT decided-at: %d" % s.count(old))
P.write_text(s.replace(old, new, 1), encoding="utf-8")
pat = re.compile(r"wealthTensor-[0-9]+|REVIEW-[0-9]{3}|LEDGER\.md|WT-[0-9]{3}")
for f in ("docs/papers/paper-II-redistribution/paper-II.md",
          "docs/papers/paper-III-dual-tensor/paper-III.md",
          "docs/papers/paper-IV-composition/paper-IV.md"):
    hits = pat.findall(pathlib.Path(f).read_text(encoding="utf-8"))
    print(f, "leaks:", hits if hits else "none")
