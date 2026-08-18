#!/usr/bin/env python3
"""wt151b · adjudicate the three promises wt151's repairs emitted, and retire the
row its rewrite made STALE. wealthTensor-83 / REVIEW-023."""
import json, pathlib, subprocess, shutil, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
TSV = ROOT / "docs/promises-adjudicated.tsv"
STALE = "93662b4195"

j = json.loads(subprocess.run(
    ["python3", "scripts/wt148_promise_sweep.py", "paper-III", "--json"],
    cwd=ROOT, capture_output=True, text=True).stdout)
by_pid = {r["pid"]: r for r in j}

ADJ = {
 "9696c13d6a": (
   "python3 on darwin, wealthTensor-83: union of `cik` across both universes of data/pre-002-events.json",
   "pilot 247 events / 122 firms, replication 448 / 191 -- 313 summed, 307 as a union. "
   "RESULT-REG-003 §1 states 'the pooled firm count is 307, not 313' and names the six dual-SIC "
   "registrants (Live Ventures, Ubiquity, Right On Brands, Fortune Valley Treasures, IAC, Match Group); "
   "REG-003 §2's one-event-per-firm sensitivity -- the 0.413 §5.4 quotes -- is computed on n=307. "
   "REPLACES STALE 93662b4195, which read 313 out of wt089's reconciliation block (122+191) rather "
   "than out of the file the sentence names, and called 307 an erratum"),
 "5f35388d48": (
   "read docs/preregistration/RESULT-002-wt026.md §4 end to end, wealthTensor-83",
   "§4 'Where the conjunction may have broken -- post-hoc, and it does not count as evidence' carries "
   "exactly three, lettered: (a) the theory may simply be wrong, (b) the bridge assumption may be wrong, "
   "(c) the unit mismatch. Its preamble is the one §6.1 paraphrases. docs/notes/, the repository's actual "
   "working-notes directory, holds two files and carries none of the three"),
 "7090dac01e": (
   "read docs/papers/paper-III-dual-tensor/POSITIONING-002-second-pass.md §6, wealthTensor-83",
   "§6 is titled 'UNDISCHARGED -- the reading list, with read-status attached to every entry' and opens "
   "'WT-059 applies and is NOT discharged'; Ryan (1995) STILL NOT READ, Zhu (2016) ABSTRACT ONLY, "
   "Bushman & Williams BIBLIOGRAPHIC ONLY. The file's top-level sections run 1-9.6 with no §10, and "
   "§10 of the manuscript is 'Relation to existing work' and holds no queue"),
}

missing = [p for p in ADJ if p not in by_pid]
if missing:
    sys.exit(f"REFUSE: wt148 does not emit {missing}")

lines = TSV.read_text().split("\n")
kept = [l for l in lines if not l.startswith(f"paper-III\t{STALE}\t")]
if len(kept) != len(lines) - 1:
    sys.exit(f"REFUSE: expected exactly 1 stale row {STALE}, removed {len(lines)-len(kept)}")

while kept and kept[-1] == "":
    kept.pop()
for pid, (ev, note) in ADJ.items():
    r = by_pid[pid]
    kept.append("\t".join(["paper-III", pid, r["artefact"], "H", ev, note, r["sentence"]]))
kept.append("")

shutil.copyfile(TSV, TSV.with_name(TSV.name + ".bak-wt151"))
TSV.write_text("\n".join(kept))
print(f"retired STALE {STALE}; added {len(ADJ)} rows")
