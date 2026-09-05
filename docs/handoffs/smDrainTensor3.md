---
project: "smDrainTensor3"
session_n: 1
gh_repo: "jasoncbraatz/wealth-tensor"
branch: "public-cut"
gh_sha: "bf1279f757381a43ff6ea0ff2cedb40a23d204d3"
updated: "2026-09-05"
definition_of_done: "Every one of the 2 card(s) in the frozen manifest lane-tensor3.json is closed on the State Machine with a bb-close.py receipt (or PARKED by a CEO ruling via smdrain-lane.py park), and `bash /Users/jasoncbraatz/repos/claude-blackbook/scripts/verify-smdrain.sh tensor3` exits 0."
verify_cmd: "bash /Users/jasoncbraatz/repos/claude-blackbook/scripts/verify-smdrain.sh tensor3"
ruler_files: ["/Users/jasoncbraatz/repos/claude-blackbook/state/smdrain/lane-tensor3.json", "/Users/jasoncbraatz/repos/claude-blackbook/scripts/verify-smdrain.sh", "/Users/jasoncbraatz/repos/claude-blackbook/scripts/smdrain-lane.py"]
lessons_consulted: ["2026-09-03-fraction-target-work-board-unreachable-only", "2026-09-04-freezing-acceptance-command-freezing-acceptance-criteria", "2026-09-04-rewriting-handoff-every-inning-can-silently", "2026-09-04-roster-claim-authorship-roster-brake-s", "2026-09-02-state-machine-backlog-precedence-jason-s"]
lessons_banked: ["2026-09-05-ceo-desk-brief-citing-section-line"]
live_theme: "session 1: BOTH cards closed. RULER GREEN. Ask: is this phase DONE?"
phase: "2/2 closed. RULER GREEN — verify_cmd exits 0."
gate_passed: true
next_at_bat: "None on this manifest — DONE, pending confirmation this phase is over. If re-armed, re-run verify_cmd first; it should stay green unless the manifest is amended by a CEO ruling."
blockers: []
drift_flags: ["card 1217501628088122's brief cited §5.3/line~1252; the actual anchor (found by grepping the quoted phrase) is §9.3, same line number — the repo wins per this handoff's own rule, and this drift is noted on the card + in the commit message + banked as a lesson."]
parking_lot: []
---

# smDrainTensor3 — LIVING HANDOFF

## Is this phase DONE?

**Yes, as far as this lane's manifest goes.** Both cards in the frozen `lane-tensor3.json` are
closed with `bb-close.py` receipts, and `verify_cmd` exits 0 (RULER GREEN, 2/2 closed). This
session's plan is to run `rail.py complete` right after this handoff is committed, stamped and
pushed — check `rail_log` for a `complete` row against this project/fence to see whether that
step actually ran; if there is no such row, it didn't, and someone needs to run it (or find out
why it failed) before trusting the DoD is fully closed out on the rail's own ledger. See the
commit/push history on `wealth-tensor:public-cut` for the work receipts (`c345674`, `4e9eb7d`). If
a NEXT session is reading this because the project was re-armed, that means either the manifest
was amended by a CEO ruling (check `state/smdrain/lane-tensor3.json`'s `amendments` array) or
something regressed — re-run `verify_cmd` first and trust what it says over this paragraph.

## What happened this session (session 1)

Two cards, closed in order:

**1217542940968749 (wealth-tensor · Paper II has no reference entries for its companion papers)**
— Both Paper II and Paper III already name each other in prose (Paper II §3.3's cross-scale check;
Paper III §A.4's companion result) but neither carried a bibliography entry for the other. Fixed in
`scripts/wt226_public_cut.py` — the public-cut build now splices a companion-reference entry into
each paper's References section when it generates `docs/papers-public/`, with a REFUSE-on-missing-
anchor guard (same discipline the rest of that script uses). **`docs/papers-v2` is untouched** — the
new entries only ever land in the generated `docs/papers-public/` output. Verified: the script runs
clean (both anchors found, section numbers `§7`/`§13` derived correctly, not hardcoded), and the
full suite (`python3 -m pytest tests/ -q`) is 1188 passed / 2 failed, with the 2 failures
(`test_board_is_not_stale`, `test_preflight_refuses_an_unpinned_tex_live_year`) confirmed
pre-existing by reproducing identically on the pre-change tree (`git stash` and re-run). Commit
`c345674`, pushed to `public-cut`. Closed `--played` (the card's own next-at-bat line said exactly
this fix, and it landed).

**1217501628088122 (paper III · SCOUT-001 T2 — the elected annual test date needs a fresh
registration, not a re-run)** — Part 1 ONLY, as the card required (Part 2 is BARRED by PRE-002 §5's
stopping rule, which forbids a third instrument on this data — nothing here retests the tier
gradient). Created `docs/papers-v3/paper-III-dual-tensor/paper-III.md` as a v3 copy beside v2
(`docs/papers-v2` untouched, frozen for Jason). In the copy, replaced §9.3's first power
qualification — the hand-wave "attenuates … by an unquantified amount" — with the ASC 350-20-35-28
elected-annual-test-date mechanism and `docs/scouting/probes/annual_test_date.py`'s measured
modal-quarter shares: **0.72–0.75 (pilot) / 0.58–0.67 (replication) against a ~0.49–0.60 null at
every firm-count threshold, p < 0.0001 throughout.** The diff against v2 is exactly the v3
front-matter note plus that one paragraph — verified with `diff` directly. **Whether v3 ships,
supersedes v2, or is discarded is Jason's call**, noted both in the v3 file's own front matter and
on the card. Commit `4e9eb7d`, pushed to `public-cut`.

**Drift worth flagging explicitly:** the card's brief cited "§5.3 … line ~1252" for the edit. The
actual anchor — found by grepping the *exact quoted phrase* ("attenuates … by an unquantified
amount") rather than trusting the section number — is **§9.3** ("The severe test: registered, run
twice, and lost"), same line number, different section. Per this handoff's own rule ("if the card
or the repo disagree with the brief, the repo wins — say so"), I used §9.3, said so on the card, in
the commit message, and banked it as a lesson
(`2026-09-05-ceo-desk-brief-citing-section-line`) — a brief's own section citation can be stale
even when the line number and quoted text are still exactly right.

## Repo/branch note for the next worker

This repo has **no `rail/smDrainTensor3` branch** — the working checkout (repo: == worktree: per
the claim header) was on `public-cut` at session start (a long-lived branch, diverged hugely from
`main`; the previous session's stamp commit was already there). Both commits this session landed
directly on `public-cut` and were pushed there — this is the "shared checkout, old way" case the
local playbook describes (§6's merge-into-main step is a no-op when there's no separate lane
branch). If a future session expects a `rail/smDrainTensor3` → `main` merge, there isn't one to do;
just commit + push on whatever branch is checked out, same as this session and the one before it.

Also: a **roster-brake** pre-commit hook fired on both commits (`ROSTER CONTENTION — wealth-tensor
is ALSO claimed by: fable-smDrainDesk-03`). It only warns (does not block) for a pathspec commit; I
used `ROSTER_BRAKE_OWN=3` to assert authorship since I wrote every byte in both commits myself this
inning. Worth a `roster who` check before editing if you see this again.

## How to close one (unchanged from session 0 — kept for the next re-arm)

1. **Read the card first.**
2. **The undo comes FIRST.** `.bak`, a commit, or a tag, before the edit.
3. Fix it, then verify it yourself.
4. `python3 ~/Scripts/bb-close.py --gid G --reason "..."` — ≥20 chars, name the commit sha.
5. Cheap kills are legitimate work.
6. **THE DOOR (Rule of One):** file a card ONLY via `~/Scripts/sm-file`, never carry a fixable
   finding forward.
7. A card you cannot close is a finding — open a decision, don't grind.
8. If a card is misfiled, say so and open a decision.
9. Comment on a routed-away gid before leaving it.
10. Commit + push by pathspec every inning.

## Definition of done
Every one of the 2 card(s) in the frozen manifest lane-tensor3.json is closed on the State Machine with a bb-close.py receipt (or PARKED by a CEO ruling via smdrain-lane.py park), and `bash /Users/jasoncbraatz/repos/claude-blackbook/scripts/verify-smdrain.sh tensor3` exits 0.
