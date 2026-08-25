import pathlib
t = pathlib.Path("docs/done-criteria.tsv"); s = t.read_text(encoding="utf-8")
old = "v1.0-preprint >/dev/null   # "
new = ("v1.0-preprint >/dev/null   # P7 closes on the ship conditions of "
       "docs/DEFINITION-OF-DONE-SHIP.md section 4, and reopens if any of the four regresses. ")
assert s.count(old) == 1, s.count(old)
t.write_text(s.replace(old, new, 1), encoding="utf-8"); print("P7 check now names its SSOT")
h = pathlib.Path("docs/HANDOFF.md"); hs = h.read_text(encoding="utf-8")
oldc = "    cmd: python3 scripts/wt170_paperII_promises.py --verify\n    rc: 0\n    count: 11"
newc = "    cmd: python3 scripts/wt170_paperII_promises.py --verify\n    rc: 0\n    count: 7"
assert hs.count(oldc) == 1, hs.count(oldc)
h.write_text(hs.replace(oldc, newc, 1), encoding="utf-8"); print("wt170 claim count 11 -> 7")
