#!/usr/bin/env python3
"""wt198 — Pass B repair of SHIP-LIST SL-8: paper-II's nine uncited reference entries.

paper-II carried 16 entries, 7 cited, 9 not, in a corpus where paper-III is 49/49 and
paper-IV 28/28.  This is IV-7's shape, and IV-7's repair is the one being copied here
rather than a new form invented: CITE IT AT THE SENTENCE THAT RELIES ON IT, OR CUT THE
ENTRY.  Padding the body to justify an entry is not permitted, so the one entry no
sentence relies on is cut rather than given a sentence to sit in.

  §1's *"the kinetic-exchange literature has established this repeatedly"*  ->  the three
      kinetic-exchange entries that establish it
  §6's tail-index clause                                                    ->  Gabaix
  §6's public-finance paragraph                                             ->  Kaldor on the
      choice of base; Auerbach, Toder and Viard, Saez and Zucman on realisation vs mark-to-market
  Piketty (2014)                                                            ->  CUT.  The paper is
      positive throughout, is silent about optimal taxation by design, and no sentence in it
      relies on that work.

Checkable after this runs: `python3 scripts/wt133_crossref_sweep.py` reports paper-II
`n of n cited, 0 not`.  Idempotent: NO-OP on a second run, exit 0.
"""
import sys, pathlib

P = pathlib.Path.home() / "repos/wealth-tensor/docs/papers/paper-II-redistribution/paper-II.md"

EDITS = [
    ("SL-8a · §1 kinetic exchange",
     "wealth share of the top holder tends to one. The kinetic-exchange literature has established\nthis repeatedly and by several routes.",
     "wealth share of the top holder tends to one. The kinetic-exchange literature has established\nthis repeatedly and by several routes (Drăgulescu and Yakovenko, 2000; Patriarca, Chakraborti and\nKaski, 2004; Yakovenko and Rosser, 2009)."),
    ("SL-8b · §6 tail indices",
     "but the first one any extension of §3.1 toward tail indices would meet.",
     "but the first one any extension of §3.1 toward tail indices, the object Gabaix (2009) surveys,\nwould meet."),
    ("SL-8c · §6 public finance",
     "The realisation result touches the public-finance literature on realisation-based versus\nmark-to-market taxation from an unfamiliar angle:",
     "The realisation result touches the public-finance literature on the choice of base (Kaldor, 1955)\nand on realisation-based versus mark-to-market taxation (Auerbach, 1991; Toder and Viard, 2016;\nSaez and Zucman, 2019) from an unfamiliar angle:"),
    ("SL-8d · cut Piketty",
     "Gini, C. (1912). *Variabilità e Mutabilità*. Tipografia di P. Cuppini.\n\nPiketty, T. (2014). *Capital in the Twenty-First Century*. Harvard University Press.\n",
     "Gini, C. (1912). *Variabilità e Mutabilità*. Tipografia di P. Cuppini.\n"),
]

def main():
    text = P.read_text(encoding="utf-8")
    orig, rc = text, 0
    for tag, old, new in EDITS:
        if old in text:
            if text.count(old) != 1:
                print(f"{tag}: old text is not unique ({text.count(old)}x)"); return 2
            text = text.replace(old, new); print(f"{tag}: APPLIED")
        elif new in text:
            print(f"{tag}: NO-OP (already repaired)")
        else:
            print(f"{tag}: NOT FOUND — neither old nor new text present"); rc = 2
    if rc: return rc
    if text != orig:
        P.write_text(text, encoding="utf-8"); print("wrote", P.name)
    else:
        print("no write needed")
    return 0

sys.exit(main())
