#!/usr/bin/env python3
"""wt170 - adjudicate ALL FIFTEEN promises Paper II emits, the pass that widened its scope.

WHY THIS FILE EXISTS
--------------------
`docs/promises-adjudicated.tsv` has gated Papers III and IV since `-81` and has never gated
Paper II, which is one of the three manuscripts in this project's definition of done. Nine
consecutive passes parked the widening. `wealthTensor-91` widened `#scope` to `paper-II` in a
commit containing that ONE line and nothing else (`f5691b3`), so the set of promises this script
adjudicates is a git object that no later edit in this pass can quietly reshape.

WHAT AN ADJUDICATION HAS TO BE HERE
-----------------------------------
The TSV's header states it: a row is a CLAIM that a human RAN OR READ the artefact and found the
sentence borne out. Three lessons this repository paid for are built into the shape below.

  * `-84`: AN ADJUDICATION THAT LOCATES AN ARTEFACT HAS NOT CHECKED ANY SENTENCE ABOUT IT.
    Every evidence command here prints CONTENT - assert bodies, collector counts, git subjects,
    command stdout - and none of them is an `ls`.
  * `-88` (v): a command run over several paths at once yields output you cannot attribute.
    Each command names its own operands and labels each printed line.
  * `-89`/`wt168` H14: a note that paraphrases its own evidence is a note nobody has checked.
    `G1..G15` below assert `stdout.strip() == QUOTED[pid]` for all fifteen rows, character for
    character. Three of these commands were WRONG on their first probe - two substring tests used
    a typographic apostrophe where the file has a straight one, and a rounding-tolerant number
    scan silently credited 0.103 to an unrelated kappa. The equality guard is what caught them.

WHAT WAS FOUND, SAID HERE SO A GREEN RUN IS NOT READ AS A CLEAN PAPER
--------------------------------------------------------------------
Thirteen H, one N, one C. The C is `c9a565b3fe`: section 7 claims the two named commands
regenerate every number in section 3 "except section 3.4's Gini ceiling", and FOUR numbers in
section 3 are printed by neither command in any precision. It is carded rather than repaired
because a manuscript edit re-keys `promise_id` and moves the emitted set underneath the pass
measuring it. The N is `54c1c5fb27`, whose artefact `0002374` is not an artefact at all: wt148's
sha rule matched the numeric half of the arXiv identifier `cond-mat/0002374`.

EXIT CODES: 0 = fifteen rows added and every post-condition holds - 2 = refused, or a
post-condition failed and the TSV was rolled back to its pre-run bytes.

USAGE
    python3 scripts/wt170_paperII_promises.py            # write the fifteen rows (one-shot)
    python3 scripts/wt170_paperII_promises.py --verify   # re-run all fifteen COMMITTED evidence
                                                         # cells and hold them to their quotations

WHY `--verify` EXISTS. The writing path refuses on a second invocation - it will not write a
twin - so without this mode the fifteen evidence commands would have been checked once, on the
day they were written, and never again. That is the defect this whole file exists to attack, one
level up. `--verify` reads the evidence column OUT OF THE COMMITTED TSV (not out of `EV` below),
runs it, and requires the stdout to equal the note's quotation character for character. It is
re-runnable forever and it is what REVIEW-031 falsifier 2 names.
"""
from __future__ import annotations

import hashlib
import json
import os
import shutil
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
TSV = "docs/promises-adjudicated.tsv"
TAG = "wt170"
PII = "docs/papers/paper-II-redistribution/paper-II.md"

# The scope commit. Paper II's prose must be byte-identical to its state here: this pass
# adjudicates a fixed set and does not move it.
SCOPE_COMMIT = "f5691b3"

CARD_NUMBERS = "1217630566080722"      # section 7 excepts one unregenerated number, there are four
CARD_ARXIV = "1217630566080626"        # wt148's sha pattern mis-parses an arXiv identifier

IN_SCOPE = ("paper-II", "paper-III", "paper-IV")

# --------------------------------------------------------------------------------------------
# the fifteen evidence commands - one per row, each printing CONTENT and labelling every line
# --------------------------------------------------------------------------------------------
EV: dict[str, str] = {}
QUOTED: dict[str, str] = {}
CLS: dict[str, str] = {}
NOTE: dict[str, str] = {}

EV["dfd41f5263"] = (
    "python3 -c \"import re;src=open('tests/test_redistribution.py').read();"
    "ns=re.findall(r'^def (test_\\w+)',src,re.M);print('tests:',len(ns));"
    "print('overclaim guard present:','test_a_flat_gini_does_not_mean_a_bounded_one' in ns)\""
)
QUOTED["dfd41f5263"] = "tests: 18\noverclaim guard present: True"
CLS["dfd41f5263"] = "H"
NOTE["dfd41f5263"] = (
    "prints 'tests: 18' and 'overclaim guard present: True'. The file defines exactly eighteen "
    "test functions and one of them is test_a_flat_gini_does_not_mean_a_bounded_one, whose three "
    "asserts (read at row c138f0078e) fail if section 3.4's criterion is ever simplified back to a "
    "drift test -- which is what 'the claims are held in place by the 18 tests in "
    "tests/test_redistribution.py, one of which exists specifically to make overclaiming fail "
    "loudly' asserts about THIS artefact. WHAT THIS ROW DOES NOT CLEAR: the same sentence's first "
    "clause, 'every number below is regenerated ... by the two commands section 7 names', is the "
    "claim CARDED at row c9a565b3fe, where four decimals in section 3 are printed by neither "
    "command. This row is keyed on the test file and clears the test-file clause only."
)

EV["4eae009313"] = (
    "python3 -c \"import re,subprocess;"
    "t=re.sub(r'\\s+',' ',open('docs/RESULT-END-TO-END-001-E1.md').read());"
    "g=lambda p: subprocess.check_output(['git','log','--diff-filter=A','--format=%cI %h','--',p]).decode().strip();"
    "print('thresholds:', chr(167)+'5 fixes E1'+chr(39)+'s thresholds, its VOID rule, its ordering' in t);"
    "print('before any leg was run:', 'before any leg was run' in t);"
    "print('named in advance:', 'The design named its candidate difference in advance' in t);"
    "print('design added:', g('docs/END-TO-END-001.md'));"
    "print('result added:', g('docs/RESULT-END-TO-END-001-E1.md'))\""
)
QUOTED["4eae009313"] = (
    "thresholds: True\nbefore any leg was run: True\nnamed in advance: True\n"
    "design added: 2026-08-16T12:22:30-05:00 4ea6361\n"
    "result added: 2026-08-16T13:20:36-05:00 91e26cd"
)
CLS["4eae009313"] = "H"
NOTE["4eae009313"] = (
    "prints 'thresholds: True', 'before any leg was run: True', 'named in advance: True', 'design "
    "added: 2026-08-16T12:22:30-05:00 4ea6361' and 'result added: 2026-08-16T13:20:36-05:00 "
    "91e26cd'. E1 records the CHECK (its section 2, the E1a symbol table and type check); it "
    "records the THRESHOLDS by name -- 'section 5 fixes E1's thresholds, its VOID rule, its "
    "ordering (E1a precedes E1b) and the corpus's response to every outcome', registered in "
    "docs/END-TO-END-001.md 'before any leg was run'; and at section 2.2 it records that 'The "
    "design named its candidate difference in advance', the rho-versus-phi difference in kind that "
    "produced this withdrawal. The two add-dates, taken PER FILE, put the design in the repository "
    "58 minutes before the result, so 'written down before the check was run' is a git fact rather "
    "than a recollection."
)

EV["c138f0078e"] = (
    "python3 -c \"import re;src=open('tests/test_redistribution.py').read();"
    "m=re.search(r'^def test_a_flat_gini_does_not_mean_a_bounded_one\\(.*?(?=^def |\\Z)',src,re.M|re.S).group(0);"
    "print([l.strip() for l in m.split(chr(10)) if l.strip().startswith('assert')])\""
)
QUOTED["c138f0078e"] = (
    "['assert drift < 0.02                     # flat by a drift test...', "
    "'assert top_share(res) > 0.95            # ...and completely condensed', "
    "'assert not is_bounded(res)']"
)
CLS["c138f0078e"] = "H"
NOTE["c138f0078e"] = (
    "prints \"['assert drift < 0.02                     # flat by a drift test...', 'assert "
    "top_share(res) > 0.95            # ...and completely condensed', 'assert not "
    "is_bounded(res)']\" -- the test's three asserts, read out of the function body rather than "
    "located by name. The third is the one the sentence promises. A criterion simplified back to a drift test alone "
    "returns True for the unopposed run, and 'assert not is_bounded(res)' then FAILS -- so the "
    "simplification 'fails loudly' instead of 'quietly re-scoring condensation as success'. The "
    "first two are what make the third discriminating: they establish that the run it is asserted "
    "over is flat by a drift test AND completely condensed, which is the trap the guard exists for."
)

EV["f6956d83f0"] = (
    "python3 -c \"import re;src=open('tests/test_redistribution.py').read();"
    "m=re.search(r'^def test_the_result_is_not_a_lucky_seed\\(.*?(?=^def |\\Z)',src,re.M|re.S).group(0);"
    "print('T =', re.search(r'^T = (\\d+)',src,re.M).group(1));"
    "print('configurations:', len(re.findall(r'\\(\\\"(?:stock|flow)\\\", ',m)));"
    "print('horizons:', re.search(r'for horizon in \\(([^)]*)\\)',m).group(1));"
    "print('seeds:', re.search(r'for s in (range\\(\\d+\\))',m).group(1))\""
)
QUOTED["f6956d83f0"] = "T = 600\nconfigurations: 2\nhorizons: T, 1200\nseeds: range(5)"
CLS["f6956d83f0"] = "H"
NOTE["f6956d83f0"] = (
    "prints 'T = 600', 'configurations: 2', 'horizons: T, 1200' and 'seeds: range(5)' -- every "
    "quantity the sentence names, read out of the function body and the module constant rather "
    "than asserted. Two configurations, each with its own band; five seeds; and BOTH horizons, the "
    "suite's T = 600 and the reported T = 1200, which is the whole point of the sentence: a band "
    "checked only at half the reported horizon would not reach the numbers it is offered for. "
    "wt170's post-condition P16 RUNS this test and it passes, so the bands hold rather than merely "
    "being written down."
)

EV["95e60baa81"] = (
    "python3 -c \"import re;print('regenerating command imports it:',"
    "'from wealth_tensor.redistribution import' in open('scripts/wt030_report.py').read());"
    "print('paper suite imports it:', 'from wealth_tensor.redistribution import' in open('tests/test_redistribution.py').read());"
    "print('module defines:', re.findall(r'^(?:class|def) (\\w+)',open('src/wealth_tensor/redistribution.py').read(),re.M))\""
)
QUOTED["95e60baa81"] = (
    "regenerating command imports it: True\npaper suite imports it: True\n"
    "module defines: ['gini', 'RedistributiveEconomy', 'stationary_gini', 'top_share', "
    "'is_bounded', 'reachable_frontier', 'sweep']"
)
CLS["95e60baa81"] = "H"
NOTE["95e60baa81"] = (
    "prints 'regenerating command imports it: True', 'paper suite imports it: True' and "
    "\"module defines: ['gini', 'RedistributiveEconomy', 'stationary_gini', 'top_share', "
    "'is_bounded', 'reachable_frontier', 'sweep']\". The bullet is a provenance claim -- "
    "that THIS module is the paper's -- and it is checked by reading what depends on it rather "
    "than by finding the file: scripts/wt030_report.py, the command the next bullet names for "
    "regenerating section 3, imports from wealth_tensor.redistribution, and so does "
    "tests/test_redistribution.py, the module holding the paper's claims. Every name section 3 "
    "reports through (stationary_gini, top_share, is_bounded, reachable_frontier, sweep) is "
    "defined here. Locating the file would not discriminate: a module nothing imports would pass "
    "that (wealthTensor-84, REVIEW-024 section 1)."
)

EV["c9a565b3fe"] = (
    "python3 -c \"import re,subprocess;"
    "L=open('" + PII + "').read().split(chr(10));"
    "a=next(i for i,l in enumerate(L) if l.startswith('## 3 '));"
    "b=next(i for i,l in enumerate(L) if i>a and l.startswith('## '));"
    "o=''.join(subprocess.check_output(['python3','scripts/'+c],text=True) for c in ('wt030_report.py','wt077_tail_index.py'));"
    "n=set();"
    "[n.add(m.group(1)) for i in range(a,b) if not L[i].startswith('#') "
    "for m in re.finditer(r'(\\d+[.]\\d+)',L[i]) if L[i][max(0,m.start()-1)] != chr(167)];"
    "print('decimals in section 3:', len(n));"
    "print('printed by neither command:', sorted(x for x in n if x not in o))\""
)
QUOTED["c9a565b3fe"] = (
    "decimals in section 3: 49\n"
    "printed by neither command: ['0.035', '0.039', '0.103', '0.1073', '0.90', '0.99875', '4.6']"
)
CLS["c9a565b3fe"] = "C"
NOTE["c9a565b3fe"] = (
    "FAILS AS WRITTEN. prints 'decimals in section 3: 49' and \"printed by neither command: "
    "['0.035', '0.039', '0.103', '0.1073', '0.90', '0.99875', '4.6']\". Of the seven, 0.1073 and "
    "4.6 ARE regenerated -- they are printed quantities at the paper's own precision (0.107269 and "
    "-4.568 %) -- and 0.99875 is the ONE exception the sentence names. The remaining FOUR are "
    "numbers in section 3 that neither command prints in any precision and that the sentence does "
    "not except: three quantities quoted as differences of printed values, 0.035 (L294, the "
    "periodicity span, 0.486-0.451), 0.103 (L324, the Gini gap, 0.994-0.891) and 0.039 (L327, the "
    "top-decile margin, 0.90-0.861); and one criterion constant, 0.90 (L321, section 3.4's "
    "top-decile threshold). The clause is internally inconsistent: it excepts the Gini ceiling "
    "BECAUSE it 'is printed by neither', and (N-1)/N is one step of arithmetic from the N=800 that "
    "wt030_report.py prints in its own header. NAMED FALSIFIER: re-run the command above; if its "
    "second line reads ['0.1073', '0.99875', '4.6'] the defect does not exist and this row is "
    "FALSE -- delete it and wt148 goes red. WHY C AND NOT R: the repair is a manuscript edit, "
    "which re-keys promise_id and moves the emitted set underneath the pass measuring it. Carded "
    + CARD_NUMBERS + " with the proposed one-sentence replacement."
)

EV["1cbe31f16c"] = (
    "python3 -c \"import subprocess;"
    "o=subprocess.check_output(['python3','scripts/wt077_tail_index.py'],text=True).split(chr(10));"
    "print([l.strip() for l in o if 'closed form' in l]);"
    "print([l.strip() for l in o if 'Var[log a] =' in l])\""
)
QUOTED["1cbe31f16c"] = (
    "['E[eta+] closed form = 0.107269   quadrature = 0.107269']\n"
    "['unlevied Var[log a] = 0.076542', 'stock r=0.10: Var[log a] = 0.076536   (kappa=0.10000)', "
    "'flow  r=0.10: Var[log a] = 0.073276   (kappa=0.01022)', "
    "'flow  r=1.00: Var[log a] = 0.051189   (kappa=0.10216)']"
)
CLS["1cbe31f16c"] = "H"
NOTE["1cbe31f16c"] = (
    "prints \"['E[eta+] closed form = 0.107269   quadrature = 0.107269']\" and \"['unlevied "
    "Var[log a] = 0.076542', 'stock r=0.10: Var[log a] = 0.076536   (kappa=0.10000)', 'flow  "
    "r=0.10: Var[log a] = 0.073276   (kappa=0.01022)', 'flow  r=1.00: Var[log a] = 0.051189   "
    "(kappa=0.10216)']\". The clause this row carries is that section 3.1's closed-form "
    "quantities 'come from python3 scripts/wt077_tail_index.py', and they do: the command prints "
    "E[eta+] = 0.107269, which is section 3.1's 0.1073 at the paper's precision, and it prints the "
    "three values section 3.1 quotes -- unlevied 0.076542, stock 0.076536 and flow 0.051189. It "
    "prints a FOURTH, flow r=0.10 Var[log a] = 0.073276, which the paper does not quote; 'the "
    "three Var[log a] values' is a claim about what section 3.1 uses, not about what the script "
    "prints, and both are shown here so a later reader can tell the two apart rather than reading "
    "'three' against an output that has four. The OTHER half of the same sentence -- 'regenerate "
    "every number in section 3' -- is CARDED at c9a565b3fe."
)

EV["5a47d4caef"] = (
    "python3 -c \"import subprocess;"
    "f=lambda p: len([l for l in subprocess.run(['python3','-m','pytest',p,'-q','--collect-only'],"
    "capture_output=True,text=True).stdout.split(chr(10)) if '::' in l]);"
    "print('whole repository:', f('tests/'));"
    "print('tests/test_redistribution.py:', f('tests/test_redistribution.py'));"
    "print('18 quoted at lines:', [i for i,l in enumerate(open('" + PII + "'),1) if '18 tests' in l or '**18** tests' in l])\""
)
QUOTED["5a47d4caef"] = (
    "whole repository: 1095\ntests/test_redistribution.py: 18\n18 quoted at lines: [38, 90, 459]"
)
CLS["5a47d4caef"] = "H"
NOTE["5a47d4caef"] = (
    "prints 'whole repository: 1095', 'tests/test_redistribution.py: 18' and '18 quoted at lines: "
    "[38, 90, 459]'. pytest's OWN collector is what counts here, not a grep for 'def test_', so "
    "'python3 -m pytest tests/ -q runs the whole repository' is measured at 1095 collected tests "
    "and the paper-scoped count at 18. The third line settles the sentence's last clause: line 38 "
    "falls inside the abstract (L21-47) and line 90 inside section 1 (L48-104), so the count IS "
    "the one quoted in the abstract and in section 1; line 459 is the sentence itself. A count "
    "asserted in three places and derived in none is the defect this checks for."
)

EV["a14c44b2ef"] = (
    "python3 -c \"import re;src=open('tests/test_redistribution.py').read();"
    "ns=re.findall(r'^def (test_\\w+)',src,re.M);print('tests:',len(ns));"
    "print('first:',ns[0]);print('last:',ns[-1]);"
    "print('imports the paper module:','from wealth_tensor.redistribution import' in src)\""
)
QUOTED["a14c44b2ef"] = (
    "tests: 18\nfirst: test_gini_matches_hand_computed_values\n"
    "last: test_parameter_validation\nimports the paper module: True"
)
CLS["a14c44b2ef"] = "H"
NOTE["a14c44b2ef"] = (
    "prints 'tests: 18', 'first: test_gini_matches_hand_computed_values', 'last: "
    "test_parameter_validation' and 'imports the paper module: True'. This row carries the "
    "sentence's claim about the FILE rather than about the pytest command (which is row "
    "5a47d4caef): that the tests holding this paper's claims in place are the ones in "
    "tests/test_redistribution.py. Eighteen test functions are defined in it, the count agrees "
    "with pytest's collector at row 5a47d4caef, and the file imports from "
    "wealth_tensor.redistribution -- the module section 7's previous bullet pins -- so the tests "
    "exercise this paper's code and not a neighbour's."
)

EV["cd94f1a9bc"] = (
    "python3 -c \"import re;"
    "a=open('tests/test_redistribution.py').read();b=open('tests/test_excess_demand.py').read();"
    "f=lambda s,t: bool(re.search(r'^def '+t+r'\\(',s,re.M));"
    "print('test_a_flat_gini_does_not_mean_a_bounded_one in tests/test_redistribution.py:',"
    "f(a,'test_a_flat_gini_does_not_mean_a_bounded_one'));"
    "print('same name in tests/test_excess_demand.py:', f(b,'test_a_flat_gini_does_not_mean_a_bounded_one'));"
    "print('its asserts:', [l.strip() for l in re.search(r'^def test_a_flat_gini_does_not_mean_a_bounded_one\\(.*?(?=^def |\\Z)',a,re.M|re.S).group(0).split(chr(10)) if l.strip().startswith('assert')])\""
)
QUOTED["cd94f1a9bc"] = (
    "test_a_flat_gini_does_not_mean_a_bounded_one in tests/test_redistribution.py: True\n"
    "same name in tests/test_excess_demand.py: False\n"
    "its asserts: ['assert drift < 0.02                     # flat by a drift test...', "
    "'assert top_share(res) > 0.95            # ...and completely condensed', "
    "'assert not is_bounded(res)']"
)
CLS["cd94f1a9bc"] = "H"
NOTE["cd94f1a9bc"] = (
    "prints 'test_a_flat_gini_does_not_mean_a_bounded_one in tests/test_redistribution.py: True', "
    "'same name in tests/test_excess_demand.py: False' and \"its asserts: ['assert drift < 0.02  "
    "                   # flat by a drift test...', 'assert top_share(res) > 0.95            # "
    "...and completely condensed', 'assert not is_bounded(res)']\". The NEGATIVE "
    "line is the discriminating one: the bullet places this test in the paper's own module and the "
    "second of the pair 'in a companion module of the same suite', so a reading that found the "
    "same name in both files would falsify the contrast the bullet draws. It is in one and not the "
    "other. The asserts are read rather than located, and the third, 'assert not is_bounded(res)', "
    "is what makes a future simplification of section 3.4's criterion fail instead of quietly "
    "re-scoring condensation as success."
)

EV["5a442cbbf3"] = (
    "python3 -c \"import re;src=open('tests/test_excess_demand.py').read();"
    "m=re.search(r'^def test_excess_demand_is_monotone_here_so_this_is_not_an_SMD_result\\(.*?(?=^def |\\Z)',src,re.M|re.S).group(0);"
    "print('present:', True);"
    "print('constrains the manuscript:', 'must not be conflated in the manuscript' in m);"
    "print('asserts:', [l.strip() for l in m.split(chr(10)) if l.strip().startswith('assert')])\""
)
QUOTED["5a442cbbf3"] = (
    "present: True\nconstrains the manuscript: True\n"
    "asserts: ['assert all(a >= b for a, b in zip(zs, zs[1:]))']"
)
CLS["5a442cbbf3"] = "H"
NOTE["5a442cbbf3"] = (
    "prints 'present: True', 'constrains the manuscript: True' and \"asserts: ['assert all(a >= b "
    "for a, b in zip(zs, zs[1:]))']\". test_excess_demand_is_monotone_here_so_this_is_not_an_SMD_"
    "result is defined in tests/test_excess_demand.py -- a companion module of the same suite, as "
    "the bullet says -- and the constraint is not inferred: its docstring carries the sentence "
    "'This module shows invariance of the curves' difference to the allocation; it does NOT show "
    "arbitrary shape, and the two must not be conflated in the manuscript.' Its single assert "
    "holds excess demand monotone across 500 prices, which is the fact that licenses the limit. So "
    "the test does CONSTRAIN the price-formation manuscript, which is what 'a test suite that "
    "constrains its author is a different object from one that flatters him' asserts about it."
)

EV["0d95afb089"] = (
    "python3 -c \"import subprocess;"
    "r=lambda a: subprocess.run(a,capture_output=True,text=True);"
    "print('object type:', r(['git','cat-file','-t','3b11f23']).stdout.strip());"
    "print('subject:', r(['git','log','-1','--format=%h %cI %s','3b11f23']).stdout.strip());"
    "print('last commit touching the module:', r(['git','log','-1','--format=%h','--','src/wealth_tensor/redistribution.py']).stdout.strip())\""
)
QUOTED["0d95afb089"] = (
    "object type: commit\n"
    "subject: 3b11f23 2026-08-05T09:15:30-05:00 redistribution: WT-030 sweep - the base caps the "
    "reachable region, realisation is the crux\n"
    "last commit touching the module: 3b11f23"
)
CLS["0d95afb089"] = "H"
NOTE["0d95afb089"] = (
    "prints 'object type: commit', 'subject: 3b11f23 2026-08-05T09:15:30-05:00 redistribution: "
    "WT-030 sweep - the base caps the reachable region, realisation is the crux' and 'last commit "
    "touching the module: 3b11f23'. 3b11f23 resolves to a commit, its subject is the "
    "redistribution sweep this paper reports, and the third line is the sentence's OWN "
    "verification -- git log -1 --format=%h -- src/wealth_tensor/redistribution.py -- run at HEAD "
    "and returning the sha the sentence pins. So 'the last commit touching "
    "src/wealth_tensor/redistribution.py' is true NOW, not merely on the day it was typed, which "
    "is the property a per-file pin was chosen for."
)

EV["3b3c126c47"] = (
    "python3 -c \"import subprocess;"
    "h=subprocess.check_output(['git','log','--format=%h','--','src/wealth_tensor/redistribution.py'],text=True).split();"
    "print('every commit touching the module:', h);"
    "print('files in that commit:', subprocess.check_output(['git','show','--name-only','--format=','3b11f23'],text=True).split())\""
)
QUOTED["3b3c126c47"] = (
    "every commit touching the module: ['3b11f23']\n"
    "files in that commit: ['src/wealth_tensor/redistribution.py', 'tests/test_redistribution.py']"
)
CLS["3b3c126c47"] = "H"
NOTE["3b3c126c47"] = (
    "prints \"every commit touching the module: ['3b11f23']\" and \"files in that commit: "
    "['src/wealth_tensor/redistribution.py', 'tests/test_redistribution.py']\". The log over that "
    "path returns ONE sha, so 3b11f23 is not merely the last commit touching the module but its "
    "only one -- which is what makes 'and therefore the state of the module that produced section "
    "3's simulation output' hold: there is no later state for the pin to be distinguished from. "
    "The commit carries tests/test_redistribution.py alongside it, so the module and the eighteen "
    "tests that hold this paper's claims entered the repository together. Compare paper-III row "
    "9add6ff45d, where the same style of pin DID need a disclosure because src/ moved afterwards."
)

EV["50503d9ee7"] = (
    "python3 -c \"import re;t=re.sub(r'\\s+',' ',open('docs/papers/PREPRINT-CHECKLIST.md').read());"
    "print('carries a reference-verification item:', 'Every reference entry' + chr(39) + 's bibliographic details verified against a publisher page, a library catalogue or a Crossref record' in t);"
    "print('quotes paper II' + chr(39) + 's own deferral:', 'The remainder are standard works whose details are to be re-checked at submission per' in t)\""
)
QUOTED["50503d9ee7"] = (
    "carries a reference-verification item: True\nquotes paper II's own deferral: True"
)
CLS["50503d9ee7"] = "H"
NOTE["50503d9ee7"] = (
    "prints 'carries a reference-verification item: True' and \"quotes paper II's own deferral: "
    "True\". docs/papers/PREPRINT-CHECKLIST.md carries the checkbox 'Every reference entry's "
    "bibliographic details verified against a publisher page, a library catalogue or a Crossref "
    "record', so the deferral has a target that actually holds the work -- which is the whole "
    "content of 'to be re-checked at submission per docs/papers/PREPRINT-CHECKLIST.md'. The second "
    "line is the row's history rather than its verdict, and it is worth a successor's attention: "
    "the checklist itself records that this item was added 2026-08-18 (wealthTensor-79) after a "
    "measured gap in which 'ten of its sixteen entries were deferred to a document that was not "
    "holding them'. The sentence is TRUE now and was FALSE when it was written, and the artefact "
    "it points at is the document that says so."
)

EV["54c1c5fb27"] = (
    "python3 -c \"import subprocess;"
    "r=subprocess.run(['git','cat-file','-t','0002374'],capture_output=True,text=True);"
    "print('git cat-file -t 0002374 ->', (r.stdout+r.stderr).strip());"
    "print('the token as it stands in the manuscript:',"
    "[l.strip() for l in open('" + PII + "') if 'cond-mat/0002374' in l])\""
)
QUOTED["54c1c5fb27"] = (
    "git cat-file -t 0002374 -> fatal: Not a valid object name 0002374\n"
    "the token as it stands in the manuscript: ['issue as 282(3). Text consulted: arXiv "
    "`cond-mat/0002374`, read in full. The quotations in §3.1 are']"
)
CLS["54c1c5fb27"] = "N"
NOTE["54c1c5fb27"] = (
    "prints 'git cat-file -t 0002374 -> fatal: Not a valid object name 0002374' and \"the token "
    "as it stands in the manuscript: ['issue as 282(3). Text consulted: arXiv `cond-mat/0002374`, "
    "read in full. The quotations in \u00a73.1 are']\". THE ARTEFACT IS AN INSTRUMENT MIS-PARSE, NOT A REPOSITORY OBJECT. "
    "wt148's sha rule matches any 7-40 character hex run containing a digit, and '0002374' is the "
    "numeric half of the arXiv identifier cond-mat/0002374; git refuses it. The sentence therefore "
    "asserts nothing about any artefact of this repository that could fail: 'read in full' is a "
    "claim about a human act on an external preprint, and the bibliographic half of it is held by "
    "the PREPRINT-CHECKLIST item adjudicated at row 50503d9ee7. Classed N by the file's own "
    "definition, with the mis-parse stated rather than ticked over -- an adjudicator who did not "
    "run cat-file could write a true-sounding note about a commit that does not exist, which is "
    "wealthTensor-83's failure mode with the artefact removed altogether. Instrument gap carded "
    + CARD_ARXIV + "."
)

PIDS = tuple(EV)


# --------------------------------------------------------------------------------------------
def sh(cmd, shell=False):
    return subprocess.run(cmd, cwd=REPO, capture_output=True, text=True, shell=shell)


def die(msg):
    print(f"{TAG}: REFUSED - {msg}", file=sys.stderr)
    return 2


def emitted():
    r = sh([sys.executable, "scripts/wt148_promise_sweep.py", "--json"])
    if r.returncode == 2:
        raise RuntimeError(r.stderr)
    return json.loads(r.stdout)


def adjudicated_ids(lines):
    return {ln.split("\t")[1] for ln in lines if ln and not ln.startswith("#") and "\t" in ln}


def pending_now(lines):
    have = adjudicated_ids(lines)
    return {p["pid"]: p for p in emitted()
            if p["paper"] in IN_SCOPE and p["pid"] not in have}


def verify():
    """Re-run every committed evidence cell for the fifteen rows and hold it to its quotation."""
    full_tsv = os.path.join(REPO, TSV)
    rows = {}
    for ln in open(full_tsv, encoding="utf-8").read().splitlines():
        if ln.startswith("#") or "\t" not in ln:
            continue
        f = ln.split("\t")
        if len(f) >= 6 and f[1] in EV:
            rows[f[1]] = f
    missing = sorted(set(EV) - set(rows))
    if missing:
        return die(f"{len(missing)} of the fifteen rows are not in {TSV}: {missing}")

    ok_all = True
    print(f"=== {TAG} --verify: fifteen committed evidence cells, re-run ===")
    for pid in PIDS:
        f = rows[pid]
        cell_matches_source = f[4] == EV[pid]
        cls_ok = f[3] == CLS[pid]
        r = sh(f[4], shell=True)
        out_ok = r.returncode == 0 and r.stdout.strip() == QUOTED[pid]
        quoted_in_note = all(l in f[5] for l in QUOTED[pid].split("\n") if l.strip())
        ok = cell_matches_source and cls_ok and out_ok and quoted_in_note
        ok_all &= ok
        detail = ("stdout matches its quotation" if ok else
                  f"cell==source:{cell_matches_source} class:{f[3]}=={CLS[pid]} "
                  f"rc:{r.returncode} got:{r.stdout.strip()[:100]!r}")
        print(f"  [{'ok  ' if ok else 'FAIL'}] {pid} {f[3]}  {detail}")
    print(f"\n{len(PIDS)} rows verified against their committed evidence.")
    if not ok_all:
        print(f"{TAG}: a committed row no longer shows what its note says it shows.",
              file=sys.stderr)
        return 2
    return 0


def main():
    if "--verify" in sys.argv[1:]:
        return verify()
    full_tsv = os.path.join(REPO, TSV)
    before_lines = open(full_tsv, encoding="utf-8").read().splitlines()
    before_hash = hashlib.sha256("\n".join(before_lines).encode()).hexdigest()

    # ---- guards, before a byte is written -----------------------------------------------
    scope_line = [ln for ln in before_lines if ln.lstrip().startswith("#scope")]
    if len(scope_line) != 1:
        return die(f"expected exactly one #scope line, found {len(scope_line)}")
    scope = [f.strip() for f in scope_line[0].split("\t")[1:] if f.strip()]
    if scope != ["paper-II", "paper-III", "paper-IV"]:
        return die(f"#scope is {scope}; wt170 is written for "
                   f"['paper-II', 'paper-III', 'paper-IV'] and paper-I is deliberately NOT in it")

    try:
        pending = pending_now(before_lines)
    except Exception as exc:                                       # noqa: BLE001
        return die(f"wt148 --json unusable: {exc!r}")
    if set(pending) != set(PIDS):
        missing = sorted(set(PIDS) - set(pending))
        extra = sorted(set(pending) - set(PIDS))
        return die(f"wt148's unadjudicated set has come apart from this script's: "
                   f"missing {missing}, unexpected {extra}")
    if any(ln.split("\t")[1:2] and ln.split("\t")[1] in PIDS
           for ln in before_lines if not ln.startswith("#") and "\t" in ln):
        return die("one of the fifteen already has a row; refusing to write a twin")

    prose = sh(["git", "diff", "--name-only", SCOPE_COMMIT, "--", PII])
    if prose.returncode != 0:
        return die(f"git diff against {SCOPE_COMMIT} failed: {prose.stderr.strip()}")
    if prose.stdout.strip():
        return die(f"{PII} has changed since {SCOPE_COMMIT}; this pass adjudicates a fixed "
                   f"emitted set and a manuscript edit moves it underneath the measurement")
    print(f"{TAG}: guards passed - wt148 reports exactly the fifteen expected ids, "
          f"#scope names paper-II, and {PII} is byte-identical to {SCOPE_COMMIT}.")

    # ---- run every evidence command and hold it to its quoted output ---------------------
    ran = {}
    for pid in PIDS:
        ran[pid] = sh(EV[pid], shell=True)

    # ---- write ---------------------------------------------------------------------------
    rows = []
    for pid in PIDS:
        p = pending[pid]
        row = "\t".join([p["paper"], pid, p["artefact"], CLS[pid], EV[pid], NOTE[pid],
                         p["sentence"]])
        if "\n" in row or row.count("\t") != 6:
            return die(f"row for {pid} is malformed ({row.count(chr(9))} tabs)")
        rows.append(row)

    shutil.copyfile(full_tsv, f"{full_tsv}.bak-{TAG}")
    with open(full_tsv, "a", encoding="utf-8") as fh:
        fh.write("\n".join(rows) + "\n")
    print(f"{TAG}: appended {len(rows)} rows.")

    after_lines = open(full_tsv, encoding="utf-8").read().splitlines()
    unchanged_hash = hashlib.sha256(
        "\n".join(after_lines[:len(before_lines)]).encode()).hexdigest()

    def rc(script, *a):
        return sh([sys.executable, f"scripts/{script}", *a]).returncode

    rc148 = rc("wt148_promise_sweep.py")
    pending_after = pending_now(after_lines)
    sweeps = {s: rc(s) for s in (
        "wt133_crossref_sweep.py", "wt154_evidence_discrimination_sweep.py",
        "wt156_reproducibility_sweep.py", "wt160_bare_pointer_sweep.py",
        "wt163_pointer_vocabulary.py", "wt166_pointer_groundtruth.py",
        "wt169_pointer_groundtruth_heldout.py")}
    named_tests = sh([sys.executable, "-m", "pytest",
                      "tests/test_redistribution.py::test_the_result_is_not_a_lucky_seed",
                      "tests/test_redistribution.py::test_a_flat_gini_does_not_mean_a_bounded_one",
                      "tests/test_excess_demand.py::"
                      "test_excess_demand_is_monotone_here_so_this_is_not_an_SMD_result",
                      "-q"])
    new_rows = after_lines[len(before_lines):]
    ev_cells = [r.split("\t")[4] for r in new_rows]
    note_cells = [r.split("\t")[5] for r in new_rows]

    checks = []
    for i, pid in enumerate(PIDS, 1):
        r = ran[pid]
        checks.append((f"G{i}", "POSITIVE",
                       f"{pid}: the evidence command exits 0 and its stdout matches the note's "
                       f"quotation character for character",
                       r.returncode == 0 and r.stdout.strip() == QUOTED[pid],
                       "matches" if r.stdout.strip() == QUOTED[pid]
                       else f"rc {r.returncode}; got {r.stdout.strip()[:120]!r}"))

    checks += [
        ("P16", "POSITIVE", "the three tests the manuscript names by name are RUN and pass",
         named_tests.returncode == 0, named_tests.stdout.strip().split("\n")[-1][:80]),
        ("P17", "POSITIVE", "wt148 RC 0 after the rows land", rc148 == 0, f"RC {rc148}"),
        ("P18", "POSITIVE", "no in-scope promise is left unadjudicated on ANY of the three papers",
         not pending_after, f"{len(pending_after)} pending"),
        ("P19", "POSITIVE", "every adjudicated row count is said out loud",
         len(adjudicated_ids(after_lines)) == len(adjudicated_ids(before_lines)) + 15,
         f"{len(adjudicated_ids(after_lines))} adjudicated"),
        ("P20", "POSITIVE",
         "the seven sibling sweeps still RC 0 - wt133, wt154, wt156, wt160, wt163, wt166, wt169",
         all(v == 0 for v in sweeps.values()),
         ", ".join(f"{k.split('_')[0]}={v}" for k, v in sweeps.items())),
        ("N21", "NEGATIVE", "no pre-existing TSV row changed",
         unchanged_hash == before_hash, "prefix hash identical"),
        ("N22", "NEGATIVE", "the file grew by exactly fifteen lines",
         len(after_lines) - len(before_lines) == 15,
         f"+{len(after_lines) - len(before_lines)}"),
        ("N23", "NEGATIVE",
         "no new evidence cell records its result in a vanished session - no 'on darwin', no "
         "session id, no 'session log' (the wt156 D1 defect, checked here rather than trusted)",
         not any(t in c.lower() for c in ev_cells
                 for t in ("on darwin", "session log", "wealthtensor-")),
         "every cell is re-executable"),
        ("N24", "NEGATIVE",
         "no new evidence cell is locate-only - none is an ls, a git ls-files or a grep -l with "
         "no content-printing operation beside it (the wt154 D1 defect)",
         all(c.startswith("python3 -c") for c in ev_cells), "all fifteen print content"),
        ("N25", "NEGATIVE",
         "the pass did NOT come out clean - exactly one C and one N are recorded, so a later "
         "session that quietly upgrades either to H fails this script",
         sum(1 for r in new_rows if r.split("\t")[3] == "C") == 1
         and sum(1 for r in new_rows if r.split("\t")[3] == "N") == 1,
         "1 C, 1 N, 13 H"),
        ("N26", "NEGATIVE", "the carded row carries a NAMED FALSIFIER and its card gid",
         all(k in NOTE["c9a565b3fe"] for k in ("NAMED FALSIFIER", CARD_NUMBERS)),
         "falsifier + " + CARD_NUMBERS),
        ("N27", "NEGATIVE",
         "paper-I is NOT in scope - the brief narrowed this pass to the three shipping papers and "
         "widening further would double the work for a manuscript nobody is submitting",
         "paper-I" not in scope, f"scope = {scope}"),
        ("N28b", "NEGATIVE",
         "every note quotes EVERY line of its command's stdout verbatim - a note that quotes the "
         "first line and paraphrases the rest reads as checked and is not (this fired on five of "
         "the fifteen notes when --verify was first written, in this same pass)",
         all(all(l in NOTE[pid] for l in QUOTED[pid].split("\n") if l.strip())
             for pid in PIDS), "fifteen for fifteen"),
        ("N28", "NEGATIVE",
         "no new note is a bare locate - none says only that the artefact is present",
         not any(c.strip().lower().startswith(("present", "exists", "the file exists"))
                 for c in note_cells), "every note quotes a value"),
    ]

    ok_all = True
    print(f"\n=== {TAG} post-conditions ===")
    for cid, kind, desc, ok, detail in checks:
        ok_all &= bool(ok)
        print(f"  [{'ok  ' if ok else 'FAIL'}] {cid} {kind:8s} {desc} - {detail}")
    print(f"\n{len(checks)} post-conditions, "
          f"{sum(1 for c in checks if c[1] == 'NEGATIVE')} NEGATIVE.")

    if not ok_all:
        print(f"{TAG}: POST-CONDITIONS FAILED - rolling back.", file=sys.stderr)
        shutil.copyfile(f"{full_tsv}.bak-{TAG}", full_tsv)
        return 2

    print(f"\n{TAG}: paper-II adjudicated - 13 H, 1 N, 1 C. "
          f"{len(adjudicated_ids(after_lines))} rows adjudicated across three manuscripts.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
