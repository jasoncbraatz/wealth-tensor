---
project: wealth-tensor
gh_sha: a9d4e135243a44e454f32d0c4c4db89e9d042695
updated: 2026-08-05
session: S1
gate_passed: true
gate_version: "2.39"
---

# wealth-tensor — HANDOFF

*Overwritten every session. `git log -p docs/HANDOFF.md` is the archive. Narrative lives in
`docs/sessions/`. Run `python3 scripts/handoff_gate.py --check` before trusting this file.*

## 0 · BRIDGE-BUG ACK — do this first, say it in chat

The desktop bridge rotates its websocket every ~27–33 min (claude-code#81248). Tools vanish,
self-heal in ~1s. **It is not darwin and it is not broken.** Retry next turn. Never declare
"can't continue" over it. Run `~/Scripts/bridge-status.sh`, then state in chat that you are
briefed. If you need durable darwin access, stand up darlish per Jason's standing brief.

**S1 note:** the bridge did not drop once across ~40 `ssh_exec` calls. Do not assume that
holds; assume it doesn't.

## 1 · IDENTITY + MISSION

You are Jason's co-author on **wealth-tensor** — an eleven-year, 210-paper patchwork being
tightened into a pre-print proposing an atomic unit of wealth (a thermodynamic-financial dual
tensor) at a genuine whitespace in economic thought.

**Two intentions, equally weighted.** (1) Get it pre-print ready and build a substrate for
Jason to become an academic author later, likely in CS. (2) **Have fun.** Nobody is making
him write this. If it stops being enjoyable, that is a defect, not a mood.

**Method: French polish.** Small area, thin coat, rub in, build up. Never a rewrite — a
rewrite is spray paint. Microscope first, telescope later. One note at a time; Jason verifies
each dot before the next is connected.

**The prose is disposable; the structure is precious.** Jason will remaster every sentence in
his own voice. LLM-register drafting is explicitly fine. What must NOT happen is quietly
laundering *his* insight into your paraphrase and losing a connection he made in 2019 and
cannot reconstruct. If you cannot tell whose idea it is, stop and ask.

## 2 · ORIENT — run these, do not skim

```
git -C ~/repos/wealth-tensor pull --ff-only
python3 ~/repos/wealth-tensor/scripts/handoff_gate.py --check     # blocker if code drifted
cat  ~/repos/wealth-tensor/docs/LEDGER.md                          # 32 entries — READ THIS FIRST
ls   ~/repos/wealth-tensor/docs/sessions/
python3 ~/repos/claude-blackbook/lessons.py search "google docs api" --scope global
python3 ~/repos/claude-blackbook/lessons.py doctrine
```

**`docs/LEDGER.md` is the project's brain.** 32 dated entries: connections, open problems,
evidence, risks, dead ends. Every conclusion below is traceable to a WT-nnn. Do not re-derive
anything in it.

## 3 · STATE — three lines

- **Manuscript** (Google Doc `1RjAHJ7jHCX_N3ToHtstQvjlMb-BQz-iejBZ9Y4f58V8`, ~59.6k chars) —
  six duplicate/orphan defects removed; three major sections added this session; verified by
  independent read-back. Restore point: doc `1fszgf295NGfvfQlT3VaCrRXrXA4K589tlS-bVsUIok4`.
- **Code** — 30 tests passing, tree clean and pushed. Three modules: `cournot.py`,
  `excess_demand.py`, `lag.py`. Every model checked against a closed form or a published result.
- **Open** — `redistribution.py` specced but unbuilt (WT-030); the Λ sensitivity sweep, which
  is the *empirical rebuttal* to the paper's weakest wall, remains unbuilt (WT-002 item 4).

## 4 · DOCTRINE / GUARDRAILS

- **Jason has granted blanket edit permission on the manuscript.** "This is a construction
  zone to build a mock-up; I'll take the mock-up and rebuild it into a building." Fix what you
  catch. No `[Claude]` prefix needed — he rewrites everything anyway.
- **BUT: read the doc back after every edit batch.** A successful `batchUpdate` reply proves
  nothing about rendering. This burned S1 twice. See LUT.
- **Never add a free parameter to absorb an objection.** Twice rejected (WT-002, WT-016). A
  quantity that fits anything forbids nothing. Behaviour enters as a *stated transform of a
  distribution*, never as a multiplier.
- **Do not oversell.** `test_excess_demand_is_monotone_here_so_this_is_not_an_SMD_result`
  exists purely to stop a future session conflating non-independence with SMD arbitrary-shape.
  If it fails, someone is overclaiming.
- **The tone is load-bearing.** Jason's standing brief: no grumpiness, humour lands the news.

## 5 · MISSION — the next at-bat

**Build `src/wealth_tensor/redistribution.py` (WT-030).** Sweep
`base ∈ {stock, flow} × rate × periodicity × threshold` over the multiplicative-additive
wealth process and map which regions bound the Gini below unity.

**Why this one first:** it is the last piece that converts the zakat/waqf/sadaqah section from
something that reads as policy advocacy into a positive result about a parameter space. The
prose reframe already shipped this session; the code that backs it has not. The sharp claim to
test is that **the base is decisive** — a levy on stock opposes the multiplicative term, a levy
on flow does not, *regardless of rate*. If that fails to reproduce, the manuscript claim needs
weakening and the ledger needs a `DEAD-END`.

**Second at-bat:** the Λ sensitivity sweep (WT-002 item 4). Everything else about Λ is written;
this is the missing empirical leg.

## 6 · VERIFY GATE

```
cd ~/repos/wealth-tensor && ./.venv/bin/python -m pytest tests/ -q      # expect 30 passed
python3 scripts/handoff_gate.py --emit                                  # before you hand off
bash ~/Scripts/gate-selfcheck.sh                                        # expect PASS
```

Walk `~/Desktop/downloads/HANDOFF-GATE.md` (G-A→G-AA) at wrap. Overwrite this file; do not
append to it.

## 7 · ORIENT-THEN-GO

Emit ONE orientation line as a sanity echo —
`Oriented: <state> · next at-bat: <X> · opening with <first action>.` — then **proceed
straight into the work.** Do not stop and wait for Jason's go. Momentum > permission.

---

## LUT — hard-won facts. Read before touching anything.

**Google Docs API (cost S1 several round-trips; do not rediscover)**

| # | Fact |
|---|---|
| L1 | `insert_text` at an index that is the **first character of a heading** makes the inserted text inherit that heading's style. Eight body paragraphs silently became H2 and the API reported success. **Insert at `end_index - 1` of the preceding body paragraph** with a leading newline instead. |
| L2 | Applying `named_style_type: NORMAL_TEXT` **wipes character formatting whose run spans the whole paragraph**. A partial bold run survived the same call; a full-width italic did not. Apply paragraph styles BEFORE character styles. |
| L3 | **Never infer indices by arithmetic.** S1 computed an offset off a cached snapshot and was wrong by 6,944 chars — the snapshot was already post-insert. It would have written four paragraphs into the bibliography. Re-run `inspect_doc_structure` after every mutation. A cached snapshot is valid ONLY for style-only ops, which do not change length. |
| L4 | `inspect_doc_structure` detailed on this doc **exceeds the tool token limit** and auto-saves to a file. Parse it with python: `json.load(open(path))["result"]`, then slice between the first `{` and the last `}`. Do not try to read it inline. |
| L5 | For full-document verification, **use a subagent** — it keeps a 60k-char read out of the main context. Give it explicit PASS/FAIL checks; a vague "summarise this" loses detail. This caught two real defects in S1. |
| L6 | Comments created via `manage_document_comment` are attributed to **Jason**, not Claude. Same for body edits in revision history. Harmless in a sandbox; bad in anything shared. |
| L7 | The cloud `Google_Drive` connector is **create/read only** — no in-place edit. Editing requires the bridge-bound `google_workspace` MCP on darwin. Reads therefore degrade gracefully during a rotation; writes do not. |
| L8 | `google_workspace` runs on GCP project **1054330720958**. All Workspace APIs were enabled 2026-08-04. OAuth success is NOT the same as API enabled — the symptom is HTTP 403 `SERVICE_DISABLED` wearing an auth-error costume. Allow 60-90s propagation; the first retry after enabling still 403s. |

**Repo**

| # | Fact |
|---|---|
| L9 | venv at `.venv`. Run tests with `./.venv/bin/python -m pytest tests/ -q`. Imports resolve via the root `conftest.py`, which inserts `src/` — no install step needed. |
| L10 | Every model must be checked against a closed form, a published result, or a hand-verified case. Not style: the Cournot suite caught a real corner-solution bug on its first run, and that bug turned out to BE the manuscript's marginal pair (WT-001). |

## REMAINING WORK — ranked, each with a liveness check

Confirm-or-drop each in one cheap call. Do not inherit as gospel.

1. **`redistribution.py`** (WT-030) — the next at-bat above.
   `verify: ls src/wealth_tensor/redistribution.py` — absent means still live.
2. **Lambda sensitivity sweep** (WT-002 item 4) — the empirical rebuttal to the paper's weakest wall.
   `verify: grep -ril sensitivity src/ tests/` — no hits means still live.
3. **Citation-graph whitespace test** (WT-006) — turn "I searched and found nothing" into a
   co-citation matrix. OpenAlex CC0 snapshot; `shellac` (96GB, RTX 3090) is idle and sized for it.
   `verify: grep -ril openalex src/ scripts/` — no hits means still live.
4. **HITL — checkbox lists** (WT-008). All 57 references render as `- [ ]` to-do boxes, as do the
   VNM axioms and the policy lists. Jason has not said whether that is deliberate.
   `verify: ask Jason, or check whether the reference list still renders checkboxes.`
5. **HITL — the twin document** (WT-009). `2The Axiomatic Reconstruction of` (19KB, 2026-08-03)
   sits beside the canonical 29KB version, title truncated mid-sentence. Never diffed.
   `verify: search Drive for title "2The Axiomatic" — present means still live.`
6. **Language remaster** — Jason's job, explicitly. Do not do this for him.

## PARKING LOT — self-contained, startable cold

- **Off-bridge Docs access.** `google_workspace` dies during a websocket rotation. The OAuth
  token is on darwin; a thin python wrapper invoked through `/tmp/dx` would reach the Docs API
  off-bridge and never notice a rotation. Offered twice in S1, deferred twice. Genuinely optional.
- **Disconfirming-case hunt for the lag thesis** (WT-025). Japan 1990s is N=1 and is an
  illustration, not evidence. The valuable exercise is deliberately hunting a case where the
  reported layer LED rather than lagged. Research task, not a coding one.

## S1 PROCESS DEBT — own this, do not repeat it

**S1 never ran a student-in `lessons.py search`.** Lessons were banked (teacher-out) but the
corpus was never consulted at orient, so any pre-existing leaf about the Docs API was
re-derived at full price. Section 2 above now forces it. Corroborate what you use:
`lessons.py use <id> --task <tag>` at orient, `lessons.py record-outcome <tag> pass` at wrap.
