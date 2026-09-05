---
project: "smDrainTensor3"
session_n: 0
gh_repo: "jasoncbraatz/wealth-tensor"
branch: "main"
gh_sha: ""
updated: "2026-09-05"
definition_of_done: "Every one of the 2 card(s) in the frozen manifest lane-tensor3.json is closed on the State Machine with a bb-close.py receipt (or PARKED by a CEO ruling via smdrain-lane.py park), and `bash /Users/jasoncbraatz/repos/claude-blackbook/scripts/verify-smdrain.sh tensor3` exits 0."
verify_cmd: "bash /Users/jasoncbraatz/repos/claude-blackbook/scripts/verify-smdrain.sh tensor3"
ruler_files: ["/Users/jasoncbraatz/repos/claude-blackbook/state/smdrain/lane-tensor3.json", "/Users/jasoncbraatz/repos/claude-blackbook/scripts/verify-smdrain.sh", "/Users/jasoncbraatz/repos/claude-blackbook/scripts/smdrain-lane.py"]
lessons_consulted: ["2026-09-03-fraction-target-work-board-unreachable-only", "2026-09-04-freezing-acceptance-command-freezing-acceptance-criteria", "2026-09-04-rewriting-handoff-every-inning-can-silently", "2026-09-04-roster-claim-authorship-roster-brake-s", "2026-09-02-state-machine-backlog-precedence-jason-s"]
live_theme: "session 0: lane armed by the CEO desk from the 2026-09-05 freeze; no work yet."
phase: "0/2 closed. RULER RED (expected before any work)."
gate_passed: false
next_at_bat: "Run the verify_cmd; take the first OPEN gid in the table below; read the card on Asana (the body carries prior sessions' measurements), fix it reversibly, verify it yourself, bb-close.py with a receipt. One card per inning is fine; two is better; a card you cannot close is a finding (park needs a ruling \u2014 open a decision)."
blockers: []
drift_flags: []
parking_lot: []
---

# smDrainTensor3 — LIVING HANDOFF

## Read first
Run the `verify_cmd` in the frontmatter above FIRST. Its OPEN lines are the at-bat and its
closed lines are the guard rails. Then `docs/NORTH-STAR.md` if this repo has one.

## What this lane is

Jason asked the CEO desk to attack the State Machine backlog (target: 95% of the frozen workable
board). The board was FROZEN at **2026-09-05T08:15:12+00:00** (rule 1 of the `backlog.work` bat: never
count against a live board — an honest session FILES cards, so a live denominator makes good work
look like failure). 81 cards were workable at the freeze (NOW+NEXT; SOMEDAY is memory, not debt).

This lane is ONE CLUSTER of that freeze — **wealth-tensor: wealth-tensor: a v1.0 preprint is tagged and Jason is its successor — every edit here is a NON-DESTRUCTIVE copy beside the shipped one** — because a cluster is
one system, which is one repo, which is one claim. The cards were scoped by the repo they are
CLOSED IN, not the topic they share.

## The ruler is DECLARED, not shimmed

`verify_cmd` is the blackbook verifier and `ruler_files:` in the frontmatter names the manifest,
the verifier and its engine. rail.py (ff86a5b, `ruler_files:` DECLARED never inferred) digests
every one of them at rail-on, so narrowing the manifest is a LOUD `RULER MOVED` (exit 2), not a
silent pass — the smDrainWisdom false complete (48327fb1) cannot recur here.

**You may not edit the manifest.** A card you cannot close is a FINDING, not a failure:
open a decision (`python3 ~/repos/auto-bridge/abridge.py decision open --proj smDrainTensor3 --needs-ceo -q "..."`),
say so on the card, move on. After the CEO rules, the park is
`python3 /Users/jasoncbraatz/repos/claude-blackbook/scripts/smdrain-lane.py park --lane tensor3 --gid G --why "<cite the ruling>"`
— it appends to a sibling file and never touches the ruler. Commit `state/smdrain/parked-tensor3.json`
in claude-blackbook by pathspec (that repo is NOT this lane's claim — commit only that file, say so in the message).

## The cards (FROZEN — do not add, do not remove)

BRIEF is the CEO desk's measured fix surface from the campfire (read on 2026-09-05 with the repo open).
It is a head start, not an order: if the card or the repo disagree with the brief, the repo wins — say so.

| gid | bin | card | BRIEF (fix surface · Q1 done? · who) |
|---|---|---|---|
| `1217501628088122` | NOW | paper III · SCOUT-001 T2 — the elected annual test date (ASC 350-20-35-28) needs a fresh r | Part 1 ONLY: in a v3 COPY of paper-III.md beside v2 (docs/papers-v3/… — create it; never edit papers-v2 or papers-public), replace §5.3 qualification 1's 'attenuates … by an unquantified amount' (line ~1252) with the ASC 350-20-35-28 elected-annual-test-date mechanism and the probe's measured modal-quarter shares (docs/scouting/probes/annual_test_date.py); narrowing, not lengthening; G-COACH/prosody unchanged. Part 2 is BARRED (PRE-002 §5) — say so. Whether v3 ships is Jason's: note it on the card and close on the copy. CLAUDE S-M. |
| `1217542940968749` | NEXT | wealth-tensor · Paper II has no reference entries for its companion papers, against the co | Reciprocal reference entries for the companion preprint in Papers II and III in the public-cut build (scripts/wt226_public_cut.py, last 9cb4c30 — READ its output first: it may already emit citations) or in the v3 copies; superseded Paper I gets no entry; the §7 guard sentence says only what the test constrains. Do NOT overwrite docs/papers-v2. Close. CLAUDE S-M. |

## How to close one

1. **Read the card first** — several carry a prior session's measurements in the body. That is
   free context you would otherwise pay to rediscover.
2. **The undo comes FIRST.** `.bak`, a commit, or a tag, before the edit.
3. Fix it, then **verify it yourself** — run the thing, read the log, hit the route. A green
   claim you did not witness is what MANAGEMENT BY WALKING AROUND exists for.
4. `python3 ~/Scripts/bb-close.py --gid G --reason "<what you did, what proves it, how to undo>"`
   — the reason is the receipt a stranger reads in a fortnight; ≥20 chars, name the commit sha.
5. **Cheap kills are legitimate work** (divide ADR Q1/Q2): a card that is already done, or no
   longer necessary, closes on MEASURED evidence — cite the sha / the grep / the date in the reason.
6. **THE DOOR (Rule of One):** a finding that is one repo + ≤3 files + no missing secret + a commit
   undoes it is FIXED THIS INNING, not carded. File a card ONLY via `~/Scripts/sm-file file --repo R --kind K --reason CODE`.
7. **A card you cannot close is a finding.** Open a decision (`--needs-ceo` if it needs the desk),
   say so on the card, move on. Do NOT grind. The desk rules promptly.
8. **If a card is MISFILED — the fix surface is not this repo — say so and open a decision.**
   If a lane says a card is misfiled it is probably right; the desk will rule it promptly.
9. **The card you route away from must say where the work went** (smDrainDesk-02, 2026-09-05):
   "routed" and "abandoned" look identical from the source gid. Comment on THIS gid before you leave it.
10. **Commit + push by pathspec every inning** (`git add <exact paths>`; never `-A`). If a fix lands
    in a SIBLING repo, claim it on the roster first (`~/Scripts/roster claim --repo R --why ...`).

## Lane-specific notes from the desk

Jason reads docs/papers-v2 — it is frozen for him. All work in copies. The repo's own build (docs/deliverable/) is the paper-build kit a future card wants extracted; do not restructure it.

CONTAINER CARD 1218065539722208 (owned by kills3, NOT in your manifest): CONTAINER owned by kills3 — kills3 does item (12) here with a sibling claim; coordinate: if you see docs/HANDOFF.md already re-stamped when you arrive, leave it. Nothing else of yours on that card.

## Definition of done
Every one of the 2 card(s) in the frozen manifest lane-tensor3.json is closed on the State Machine with a bb-close.py receipt (or PARKED by a CEO ruling via smdrain-lane.py park), and `bash /Users/jasoncbraatz/repos/claude-blackbook/scripts/verify-smdrain.sh tensor3` exits 0.
