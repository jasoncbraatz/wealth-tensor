---
project: wealth-tensor
gh_sha: ff763b4f654f76f6f5f5d60266e21252a5ae22a8
updated: 2026-08-05
session: S2
gate_passed: true
gate_version: "2.40"
---

# wealth-tensor — HANDOFF

*Overwritten every session. `git log -p docs/HANDOFF.md` is the archive. Run
`python3 scripts/handoff_gate.py --check` before trusting this file.*

## 0 · BRIDGE-BUG ACK — do this first, say it in chat

The desktop bridge rotates its websocket every ~27–33 min (claude-code#81248). Tools vanish and
self-heal in ~1s. **It is not darwin and it is not broken.** Run `~/Scripts/bridge-status.sh`,
then say in chat that you are briefed.

**S2 did not fight the bridge once, and neither should you.** Stand up darlish at Step 0 and
the problem disappears: one bridge call for the dsh-fire secret, then `/tmp/dx` for everything.
S2's bridge rotated mid-session — the disease attended the cure's ceremony — and nothing
noticed. The procedure is in Jason's standing brief; follow it verbatim.

**Fixed this session, so it will not cost you what it cost S2:** `darlish-up` step 1/6 used to
throw away pip's output, so a fresh cloud container reported `cannot import
websockets/asyncssh` with no explanation. It now retries across pip/pip3/`python3 -m pip`,
logs to `/tmp/darlish-deps.log`, and prints the last 25 lines before dying. Both paths were
exercised, not assumed. If you still see it fail, the log will tell you why.

## 1 · IDENTITY + MISSION

You are Jason's co-author on **wealth-tensor** — an eleven-year, 210-paper patchwork being
tightened into a pre-print proposing an atomic unit of wealth (a thermodynamic-financial dual
tensor) at a genuine whitespace in economic thought.

**Two intentions, equally weighted.** (1) Get it pre-print ready and build a substrate for
Jason to become an academic author later, likely in CS. (2) **Have fun.** Nobody is making him
write this. If it stops being enjoyable, that is a defect, not a mood.

**Method: French polish.** Small area, thin coat, rub in, build up. Never a rewrite — a rewrite
is spray paint. One note at a time; Jason verifies each dot before the next is connected.

**The prose is disposable; the structure is precious.** Jason remasters every sentence in his
own voice, so LLM-register drafting is explicitly fine. What must NOT happen is quietly
laundering *his* insight into your paraphrase and losing a connection he made in 2019 and
cannot reconstruct. If you cannot tell whose idea it is, stop and ask.

## 2 · ORIENT — run these, do not skim

```
git -C ~/repos/wealth-tensor pull --ff-only
python3 ~/repos/wealth-tensor/scripts/handoff_gate.py --check     # blocker if code drifted
cat  ~/repos/wealth-tensor/docs/LEDGER.md                          # 37 entries — READ THIS FIRST
python3 ~/repos/claude-blackbook/lessons.py search "google docs api" --scope global
python3 ~/repos/claude-blackbook/lessons.py doctrine
```

**`docs/LEDGER.md` is the project's brain.** 37 dated entries. Every conclusion below traces to
a WT-nnn. Do not re-derive anything in it. Corroborate what you use:
`lessons.py use <id> --task <tag>` at orient, `lessons.py record-outcome <tag> pass` at wrap.

## 3 · STATE — where things actually stand

- **Manuscript** (Google Doc `1RjAHJ7jHCX_N3ToHtstQvjlMb-BQz-iejBZ9Y4f58V8`, 62,834 chars) —
  the redistribution passage now states the *measured* claim rather than the guessed one.
  Verified by structural read-back: 33 headings and 14 list lines byte-identical, exactly one
  paragraph changed.
  Restore points, both verified byte-identical to their originals:
  S1 `1fszgf295NGfvfQlT3VaCrRXrXA4K589tlS-bVsUIok4` ·
  S2 `1FeXUSbrFQQXDOaSxCoul13lE6LWicxMuJGL8xJKSLjs`.
- **Code** — **58 tests passing**, tree clean and pushed. Five modules: `cournot.py`,
  `excess_demand.py`, `lag.py`, **`redistribution.py`** (new), **`lambda_sensitivity.py`**
  (new). Two regenerable report scripts: `scripts/wt030_report.py`,
  `scripts/wt002_lambda_report.py`.
- **Closed this session** — WT-030 (built, and *refined*: see WT-033) and **WT-002 in full**
  (item 4 built as WT-036). WT-002 was the paper's weakest wall and it is now the best-defended
  thing in it.
- **Open, and it is the big one** — **WT-037**: the manuscript contains zero figures, zero
  results tables, zero appendices and zero mention of the repository, while leaning on five
  modules' worth of results. See §5.

## 4 · DOCTRINE / GUARDRAILS

- **Jason has granted blanket edit permission on the manuscript.** "This is a construction zone
  to build a mock-up; I'll take the mock-up and rebuild it into a building." Fix what you catch.
- **Take a fresh restore point before every edit session, and VERIFY it** — copy the doc via the
  cloud `Google_Drive__copy_file`, then read the copy back and assert it is byte-identical to
  the pre-edit original. S2 did this in one extra call. A restore point you never read is not a
  restore point.
- **Read the doc back after every edit batch.** A successful API reply proves nothing about
  rendering. This burned S1 twice. L12 makes the read-back cheap *and* stricter.
- **Never add a free parameter to absorb an objection.** Rejected three times now (WT-002,
  WT-016, and the temptation in WT-033 to define "flow" so the claim came out right). A quantity
  that fits anything forbids nothing. `realization` survives that test only because it is a
  stated structural property of every real tax system, and because it is *swept* rather than
  chosen.
- **Do not oversell.** Two standing guard-tests exist purely to stop a future session
  overclaiming: `test_excess_demand_is_monotone_here_so_this_is_not_an_SMD_result` and
  `test_a_flat_gini_does_not_mean_a_bounded_one`. If either fails, someone is overclaiming.
- **When a sharp claim half-survives, the refinement is the prize.** WT-030 said "the base is
  decisive regardless of rate". The sweep falsified "regardless of rate" and produced something
  better: the base is decisive *through realisation*. Do not weaken to mush and do not defend
  the original. Find what is actually true and state that.
- **The tone is load-bearing.** No grumpiness; humour lands the news.

## 5 · MISSION — the next at-bat, ranked

### START HERE — **a Results section, and a Reproducibility note (WT-037)**

`verify: grep -ci "appendix\|figure\|github" on a fresh export of the doc — 0 means still live.`

The paper says "swept numerically over that process" and gives the reader nothing to inspect.
Five modules, 58 tests, and every number regenerable — none of it appears in the manuscript.
For a pre-print this is the difference between a synthesis essay and a paper: **a reviewer
cannot check any of it.** It is also the cheapest large improvement available, because no new
science is required. Transcription, and one decision from Jason.

Recommended shape:

1. Four compact results tables — Cournot instability (WT-005), allocation-invariance 25:1
   (WT-018), the lag/observability ladder (WT-027), and the redistribution sweep (WT-033).
   Every figure already printed by the two report scripts.
2. One figure: the Λ scaling collapse (WT-036). Two systems, wildly different units, one curve.
   A collapse is checkable in a glance; a paragraph about Buckingham pi gets skimmed.
3. A Reproducibility note: `github.com/jasoncbraatz/wealth-tensor`, the commit SHA, and
   `./.venv/bin/python -m pytest tests/ -q` (58 passed).

**Nothing blocks you.** The repository is **already public** —
`github.com/jasoncbraatz/wealth-tensor`, confirmed via `gh repo view`, visibility PUBLIC — so
the Reproducibility note can cite it today. Write the whole section without asking anyone.

**ASK JASON, but only after the section exists, and it is a nice-to-have not a blocker.**
`docs/LEDGER.md`, `docs/HANDOFF.md` and `docs/sessions/` are already world-readable and contain
candid internal assessments ("the paper's weakest wall", "reads as ideology"). Options:
   - **(a) Leave them public, add one README line framing `docs/` as a working lab notebook
     (recommended).** A paper whose method insists dead ends be recorded with equal weight is
     strengthened, not embarrassed, by a ledger that visibly does it. WT-015 and WT-016 are
     better advertisements for the work than anything in the abstract.
   - **(b) Split the working notes into a private companion repo.** Keeps `src/`, `tests/` and
     `scripts/` public, which is all a reviewer actually needs.
   - **(c) Leave it and revisit at submission.** Free, and the honest default if he is not around.

### Then, in order

2. **Citation-graph whitespace test (WT-006).** Turn "I searched and found nothing" into a
   co-citation matrix — the whitespace claim is the first thing a reviewer attacks and it is
   currently an anecdote. OpenAlex CC0 snapshot; `shellac` (96GB, RTX 3090) is idle and sized
   for it. *Highest-value new science remaining.*
   `verify: grep -ril openalex src/ scripts/` — no hits means still live.
3. **HITL — checkbox lists (WT-008).** All 57 references render as `- [ ]` to-do boxes, as do
   the VNM axioms and the policy lists. Jason has never said whether that is deliberate. Cheap
   to ask, cheap to fix, and it is the first thing a reader sees.
   `verify: ask Jason.`
4. **HITL — the twin document (WT-009).** `2The Axiomatic Reconstruction of` (19KB, 2026-08-03)
   sits beside the canonical version, title truncated mid-sentence, never diffed. It may hold
   content the canonical copy lost — which is the one failure mode this project cannot tolerate.
   `verify: search Drive for "2The Axiomatic" — present means still live.`
5. **Disconfirming-case hunt for the lag thesis (WT-025).** Japan 1990s is N=1 and is an
   illustration, not evidence. Deliberately hunt a case where the reported layer *led*. Research,
   not code.
6. **Language remaster.** Jason's job, explicitly. Do not do this for him.

**Deliberately deferred, with reasons:** off-bridge Google Docs access (parked in S1, parked
again — darlish plus the cloud Drive connector already covers read *and* write comfortably, so
this now solves a problem nobody has); and a plotting dependency for the Λ collapse figure — the
numbers are in hand and the format decision belongs with the Results section, not before it.

## 6 · VERIFY GATE

```
cd ~/repos/wealth-tensor && ./.venv/bin/python -m pytest tests/ -q   # expect 58 passed
git commit ...                                                       # the LAST content commit
python3 scripts/handoff_gate.py --stamp                              # writes gh_sha = HEAD
git commit -am "docs: stamp handoff gh_sha to HEAD"
python3 scripts/handoff_gate.py --emit                               # blesses it
bash ~/Scripts/gate-selfcheck.sh                                     # expect PASS
```

**`--emit` does not stamp.** S2 assumed it did, left `gh_sha: PENDING`, and the gate cheerfully
reported "sha matches HEAD" — because `sh()` swallowed git's error and a bad sha resolved to an
empty diff, which looks exactly like no drift. Fixed the same session: exit codes are now
tri-state (0 pass · 1 blocker · **2 CANNOT VERIFY, which is not a pass**), a placeholder sha is
a blocker, and a well-formed sha absent from the clone is a 2. All three paths were exercised
before the fix was committed.

Walk `~/Desktop/downloads/HANDOFF-GATE.md` (G-A→G-AB, v2.40) at wrap. Overwrite this file; do
not append. Trust the gate file's own header for its version, never a version quoted in prose.

## 7 · ORIENT-THEN-GO

Emit ONE orientation line — `Oriented: <state> · next at-bat: <X> · opening with <first
action>.` — then **proceed straight into the work.** Do not wait for Jason's go.

---

## LUT — hard-won facts. Read before touching anything.

**Google Docs API**

| # | Fact |
|---|---|
| **L11** | **To CHANGE existing text, use `find_and_replace_doc`. It needs no indices at all**, so L1, L3 and WT-032 — the whole index-arithmetic minefield that cost S1 several round-trips and nearly wrote four paragraphs into the bibliography — simply cannot bite. S2 made two manuscript edits this way with zero index calculations. Indices are only unavoidable when inserting genuinely *new* structure. Reach for replace first and shape the edit to fit it. |
| **L12** | **Verify a doc edit structurally, not by reading it.** Pull the doc through the *cloud* `Google_Drive__read_file_content` (rotation-immune, and it auto-saves to a file so it costs almost no context), then in python compare the list of `#`-prefixed lines and the list of list-item lines against the pre-edit export. Identical heading and list arrays prove no style corruption happened, which is exactly the L1/L2 failure mode — and a unified diff over paragraphs shows precisely how many changed. S2's edit: 33 headings identical, 14 list lines identical, 1 paragraph changed. Cheaper and stricter than the subagent read of L5, which is still the right tool for *meaning*. |
| L1 | `insert_text` at an index that is the first character of a heading makes the inserted text inherit that heading's style. Insert at `end_index - 1` of the preceding body paragraph with a leading newline. *(Only relevant when L11 does not apply.)* |
| L2 | Applying `named_style_type: NORMAL_TEXT` wipes character formatting whose run spans the whole paragraph. Apply paragraph styles BEFORE character styles. |
| L3 | **Never infer indices by arithmetic.** S1 was wrong by 6,944 chars off a stale snapshot. Re-run `inspect_doc_structure` after every mutation. |
| L4 | `inspect_doc_structure` detailed on this doc exceeds the tool token limit and auto-saves to a file. Parse it with python; do not read it inline. |
| L5 | For *semantic* whole-document verification use a subagent — it keeps a 60k-char read out of the main context. Give it explicit PASS/FAIL checks. For *structural* verification prefer L12. |
| L6 | Comments and body edits are attributed to **Jason**, not Claude. Harmless in a sandbox; bad in anything shared. |
| L7 | The cloud `Google_Drive` connector is create/read only — no in-place edit. But `copy_file` **is** a create, so **restore points can be taken without the bridge**. Editing still needs the bridge-bound `google_workspace` MCP on darwin. |
| L8 | `google_workspace` runs on GCP project **1054330720958**; all Workspace APIs enabled 2026-08-04. A `SERVICE_DISABLED` 403 is an API-not-enabled error wearing an auth-error costume. |

**Repo and tooling**

| # | Fact |
|---|---|
| L9 | venv at `.venv`. Tests: `./.venv/bin/python -m pytest tests/ -q`. Imports resolve via the root `conftest.py`, which inserts `src/`. |
| L10 | Every model must be checked against a closed form, a published result, or a hand-verified case. Not style: the Cournot suite caught a real bug on its first run, and that bug turned out to BE the manuscript's marginal pair (WT-001). |
| **L13** | **A multi-line commit message will not survive `dx`'s shell quoting** — S2's first attempt died with exit 2 (a refusal: nothing ran, safe to retry). Write the message locally, `dx --put` it to **`.git/COMMIT_DRAFT`**, then `git commit -F .git/COMMIT_DRAFT`. Inside `.git/` specifically, because a draft in the repo root gets swept up by `git add -A` and committed — S2 did exactly that in `~/Scripts` and needed a follow-up commit to clean it. |
| **L14** | `conftest.py` only fires under pytest, so anything in `scripts/` needs its own two-line shim: `sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "src"))`. |
| **L15** | **Mutation-test any result you intend to publish.** Copy the module, break one line, confirm the suite screams — and confirm the *right* test screams. S2 ran eight mutations across the two new modules; all eight were caught by the intended test. It costs one tool call and it is the difference between "the tests pass" and "the tests mean something". Watch the anchor: a `\n` passed through a heredoc argument is literal, and a mutation whose anchor silently misses produces a *spurious pass*. |

## WHAT S2 DID — one paragraph, for context

Built `redistribution.py` (WT-030) and swept it. The sharp claim half-survived: at a matched
rate the two bases are an order of magnitude apart as predicted, but "regardless of rate" is
false — a fully-realised flow levy does bound the Gini, it is merely weak. The surviving and
sharper claim is about **realisation**: at rho = 0 a 100% flow levy is statistically
indistinguishable from no levy at all. Ledgered as WT-033, and the manuscript sentence was
replaced to match. Along the way `is_bounded` was caught scoring the *unopposed* process as
bounded, because the Gini saturates at the (N-1)/N ceiling — WT-034, and a standing guard test.
Then built `lambda_sensitivity.py`, closing WT-002 item 4 and with it the whole of WT-002: the
numeraire cancels, spread exactly 0.0 across twelve orders of magnitude, dimensional outputs
scaling at slope 1.000000000000. Finally, audited the manuscript against the repo and found
WT-037 — five modules of results, none of them in the paper. That is your at-bat.
