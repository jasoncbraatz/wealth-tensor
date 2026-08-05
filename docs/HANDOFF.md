---
project: wealth-tensor
gh_sha: 245649bad7e15eb7b2fb20acb7c6e2bd312302d0
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

**S2 never fought the bridge and neither should you.** Stand up darlish at Step 0 per Jason's
standing brief: one bridge call for the dsh-fire secret, then `/tmp/dx` for everything. S2's
bridge rotated mid-session and nothing noticed. If `darlish-up` fails at 1/6 it now **prints why**
and names `/tmp/darlish-deps.log` (fixed in S2); the unblock is
`pip install websockets asyncssh --break-system-packages`.

## 1 · IDENTITY + MISSION

You are Jason's co-author on **wealth-tensor** — an eleven-year, 210-paper patchwork being
tightened into a pre-print proposing an atomic unit of wealth (a thermodynamic-financial dual
tensor) at a genuine whitespace in economic thought.

**Two intentions, equally weighted.** (1) Get it pre-print ready. (2) **Have fun.** This is a
hobby; no tenure rides on it; he is not trying to be safe and says so. If it stops being
enjoyable that is a defect, not a mood.

**He invites criticism and means it.** S2's most useful moves were all disagreements — talking
him out of centring SMD, out of condensing the wrong section, out of the word "undeniable", and
out of a graph-neural-network dependency. Agreeing with him is not the job.

**The prose is disposable; the structure is precious.** He remasters every sentence in his own
voice, so LLM-register drafting is fine. What must NOT happen is laundering *his* insight into
your paraphrase. When he coins something — "force-fit, not form-fit" (WT-042) — it goes in
**verbatim** and it is credited to him in the ledger. If you cannot tell whose idea it is, ask.

**How he works on content:** his research notes are **on paper**. He reads one at a time and wants
to digest and discuss, not receive a report. Answer at the length the note earns. Read the note
back to him before building on it — paper → his hands → you is a lossy channel, and the loss this
project cannot absorb is a 2019 insight quietly becoming your paraphrase.

## 2 · ORIENT — run these, do not skim

```
git -C ~/repos/wealth-tensor pull --ff-only
python3 ~/repos/wealth-tensor/scripts/handoff_gate.py --check   # 0 pass · 1 blocker · 2 CANNOT VERIFY
cat  ~/repos/wealth-tensor/docs/LEDGER.md                        # 45 entries — READ THIS FIRST
python3 ~/repos/claude-blackbook/lessons.py search "google docs api" --scope global
python3 ~/repos/claude-blackbook/lessons.py doctrine
```

**`docs/LEDGER.md` is the project's brain** and in S2 it *earned that* — Jason proposed centring
SMD, and WT-012 and WT-020 had already forbidden exactly that, with a test enforcing it. The fence
held. Do not re-derive anything in it. Corroborate what you use: `lessons.py use <id> --task <tag>`
at orient, `lessons.py record-outcome <tag> pass` at wrap.

## 3 · STATE

- **Code** — **58 tests passing**, tree clean and pushed. Five modules: `cournot.py`,
  `excess_demand.py`, `lag.py`, `redistribution.py`, `lambda_sensitivity.py`. Reports regenerate
  from `scripts/wt030_report.py` and `scripts/wt002_lambda_report.py`.
- **Manuscript** (Google Doc `1RjAHJ7jHCX_N3ToHtstQvjlMb-BQz-iejBZ9Y4f58V8`, 63,283 chars) —
  three edits this session, all verified structurally (33 headings, 14 list lines byte-identical
  each time). Restore points, all verified: S1 `1fszgf295NGfvfQlT3VaCrRXrXA4K589tlS-bVsUIok4` ·
  S2a `1FeXUSbrFQQXDOaSxCoul13lE6LWicxMuJGL8xJKSLjs` ·
  S2b `12jJh93VhgfOe8EQ3J23G9heQekSCdzxHTm75ut8RL6g`.
- **Closed** — WT-002 entirely (and now *reframed*: Λ is an entailment, not a posit — WT-038),
  WT-030 (built and refined by WT-033).
- **The paper's real problem, now measured** — WT-040. The contribution begins at **76% of the
  body**, and the section defining the atomic unit is **1,893 chars**, one third the size of the
  Cournot/Bertrand history preceding it. Everything Jason raised in notes #3–#6 converges on one
  restructure.

## 4 · DOCTRINE / GUARDRAILS

- **Blanket edit permission on the manuscript.** "A construction zone to build a mock-up."
- **Fresh restore point before every edit session, and VERIFY it** — `Google_Drive__copy_file`
  (works without the bridge), then read the copy back and assert byte-identity with the original.
  S2 did this twice at one call each. A restore point you never read is not a restore point.
- **Read back after every edit batch** — structurally, per L12. Cheaper and stricter than a
  subagent.
- **Never add a free parameter to absorb an objection.** Rejected four times now: WT-002, WT-016,
  the temptation in WT-033 to define "flow" so the claim came out right, and WT-043's warning that
  a freely-varying Λ forbids nothing. `realization` survives only because it is a stated structural
  property *and* it is swept rather than chosen.
- **Do not oversell.** Two standing guard-tests exist to stop a future session overclaiming:
  `test_excess_demand_is_monotone_here_so_this_is_not_an_SMD_result` and
  `test_a_flat_gini_does_not_mean_a_bounded_one`. If either fails, someone is overclaiming.
- **When a sharp claim half-survives, the refinement is the prize** (WT-033). Do not weaken to
  mush and do not defend the original.
- **The tone is load-bearing.** No grumpiness; humour lands the news.

## 4b · THE DECISION THAT FRAMES EVERYTHING BELOW

**`docs/adr/ADR-001-paper-decomposition.md` — read it before planning anything.** The manuscript
is not one paper, it is four, and that was decided with Jason in S2 with evidence allocated
exhaustively and without overlap. Do not re-litigate it; bring a reason the ADR does not already
answer, or proceed.

**I** price formation without independent curves · **II** redistribution as a parameter space ·
**III** the dual tensor and the reporting layer (*the flagship*, carries the axioms, needs WT-026)
· **IV** the atomic theory. Order: **II → III → I → IV**, and II is the rehearsal.

**Audience: Jason's three children, 8, 11 and 17.** He said so at the close of S2 and it is not
decoration — it decided two things. `docs/` stays public, and `Abandoned Approaches` is promoted
to a load-bearing section in every paper. When the reader is someone learning how to think, the
method is the message. Behave accordingly: the ledger is part of the deliverable now.

## 5 · MISSION — ranked, with reasons

### START HERE — **WT-026: the severe test.** Build it.

`verify: grep -ril "10-K\|edgar\|unobserv" src/ scripts/` — no hits means still live.

The claim: **lag magnitude scales with the *unobservability* of the degradation**, and accounting
standards themselves identify the unobservable categories — they are precisely the ones GAAP
declines to capitalise. Neoclassical finance predicts no such gradient. EDGAR is public and
machine-readable.

**Why this is first, ahead of the manuscript work.** It surfaced three times independently in one
session as the highest-value unbuilt item, and the third time settled it: WT-043 shows that what
saves this framework from the Odum trap is *not prose*. Emergy died of (a) coefficients that were
not independently measurable and (b) no risky prediction. This framework passes (a) decisively —
Λ⁻¹ is UN SDG indicator 7.3.1. (b) is unbuilt, and (b) is the whole difference between a theory
and an accounting scheme. It is also fully self-contained: no judgement calls from Jason, no
manuscript risk, and its result slots straight into §3 of the restructure below.

**Scope honestly.** This is a data project, not an afternoon. Prefer a scoped pilot — one sector,
a defined firm set, a stated pre-registered prediction — over a study that never lands. Say in the
handoff what you sampled and what you dropped.

### 2 — **The restructure (WT-040).** Flip the paper: contribution first, literature second.

The spine, made entirely of material that already exists:

1. **The constraint expired.** *Force-fit, not form-fit* (WT-042) with dates and numbers, plus the
   n≥3 / central-bank / COVID motivation. Answers *why now*, which the paper never answers. This
   is the one genuinely new page.
2. **What wealth is.** P1/P2/P3 as propositions with stated domains (WT-038). Should be the
   largest section; is currently the smallest.
3. **What follows.** The five verified results — WT-037. Currently in the repo and nowhere in the
   paper.
4. **Relation to existing frameworks.** The relocation method run as a section (WT-039). Absorbs
   most of the current history at half the length, re-genred from narration to assertion.
5. **What this does not settle.** Quine–Duhem stated honestly, architecture left open, WT-026
   named.

**Why second, not first:** it is mostly *moving*, but moving sections is exactly where the Docs
index minefield bites (L11 does not help you relocate structure, only replace text), and each
section's placement is a judgement call that is better made with Jason present and with WT-026's
result in hand.

### 2b — **Draft Paper II** (redistribution). It is the rehearsal, and it can run alongside WT-026.

`redistribution.py`, 18 tests, WT-033/034/035, a sharp counterintuitive result, no philosophical
scaffolding, and the friendliest venue. Jason's self-identified gap is preprint machinery, not
science — so learn abstracts, keywords, JEL codes, code-availability statements and the
endorsement process on the paper where a mistake costs least. Per WT-047 the manuscript currently
has **none** of that apparatus; Paper II is where the template gets built for the other three.

`verify: ls docs/papers/` — absent means still live.

### 3 — **Attribution pass (WT-044).** Cheapest fix-to-value ratio in the document.

Zero occurrences in the body of: **Mises**, **malinvestment**, **Godley**, **Lavoie**, **Farmer**,
**Lillo**, **Sraffa**, **Robinson**, **Samuelson**. Each supports an argument the paper already
makes. Citations, not rewrites. Sraffa/Robinson/Samuelson matter most now that scalar capital is
the live target (WT-041).

*Name audit is already done and came back clean* — do not redo it. Carnot is correct;
Chakrabarti/Chakraborti/Chakravarty are three real people.

### 4 — **Citation-graph whitespace test (WT-006).** Demoted from S2's ranking, deliberately.

It defends the paper's *novelty*; WT-026 defends its *theory*. `shellac` is idle and sized for it.
`verify: grep -ril openalex src/ scripts/` — no hits means still live.

### 5 — **HITL, both cheap, both need Jason.** Checkbox lists (WT-008): all 57 references render as
`- [ ]` to-do boxes and he has never said whether that is deliberate — it is the first thing a
reader sees. The twin document (WT-009): `2The Axiomatic Reconstruction of`, 19KB, never diffed,
may hold content the canonical copy lost.

### 6 — **Language remaster.** His job, explicitly. Do not do it for him.

**No open ASKs.** The `docs/`-stays-public question is **decided** (ADR-001) — keep it, add one
README line framing `docs/` as a working lab notebook. Previously-open framing: `docs/` is world-readable (the repo is
public at `github.com/jasoncbraatz/wealth-tensor`) and contains candid internal assessments.
Recommendation: leave it and add one README line framing `docs/` as a working lab notebook — a
paper whose method insists dead ends be recorded with equal weight is strengthened by a ledger
that visibly does it. His call.

## 6 · VERIFY GATE

```
cd ~/repos/wealth-tensor && ./.venv/bin/python -m pytest tests/ -q   # expect 58 passed
git commit ...                                                       # the LAST content commit
python3 scripts/handoff_gate.py --stamp                              # writes gh_sha = HEAD
git commit -am "docs: stamp handoff gh_sha to HEAD"
python3 scripts/handoff_gate.py --emit                               # blesses it
bash ~/Scripts/gate-selfcheck.sh                                     # expect PASS
```

**`--emit` does not stamp.** S2 assumed it did and the gate reported "sha matches HEAD" over a
literal `PENDING` — `sh()` swallowed git's error and a bad sha resolved to an empty diff, which
looks exactly like no drift. Fixed the same session: tri-state exit codes, a placeholder sha is a
blocker, a well-formed sha absent from the clone is a 2. Walk
`~/Desktop/downloads/HANDOFF-GATE.md` (G-A→G-AB, v2.40 — trust the file header, not this line).

## 7 · ORIENT-THEN-GO

Emit ONE orientation line — `Oriented: <state> · next at-bat: <X> · opening with <first action>.`
— then proceed. Do not wait for Jason's go.

---

## LUT — hard-won facts. Read before touching anything.

**Google Docs API**

| # | Fact |
|---|---|
| **L11** | **To CHANGE existing text use `find_and_replace_doc`. It needs no indices**, so L1/L3/WT-032 — the index minefield that nearly wrote four paragraphs into the bibliography — cannot bite. S2 made three manuscript edits this way with zero index calculations. Anchor on a long verbatim span; the API reports the occurrence count, which is itself a check that your anchor was as unique as you believed. Indices remain unavoidable for inserting or **relocating** structure — which is why the restructure is real work. |
| **L12** | **Verify a doc edit structurally.** Export via the *cloud* `Google_Drive__read_file_content` (rotation-immune, auto-persists to a file so it costs almost no context), then in python compare the array of `#`-prefixed lines and the array of list-item lines against the pre-edit export. Identical arrays are positive proof no style corruption occurred; a paragraph diff shows how many changed. Expect 1 for a one-paragraph edit — S2 saw 4 once and it was a paragraph boundary shifting, confirmed by eye rather than assumed. |
| L1 | `insert_text` at a heading's first character makes the inserted text inherit that heading's style. Insert at `end_index - 1` of the preceding body paragraph. |
| L2 | `named_style_type: NORMAL_TEXT` wipes character formatting spanning a whole paragraph. Paragraph styles BEFORE character styles. |
| L3 | **Never infer indices by arithmetic.** S1 was wrong by 6,944 chars off a stale snapshot. |
| L4 | `inspect_doc_structure` detailed exceeds the tool token limit and auto-saves to a file. Parse with python. |
| L5 | For *semantic* whole-document verification use a subagent. For *structural*, use L12. |
| L6 | Comments and body edits are attributed to **Jason**, not Claude. |
| L7 | Cloud `Google_Drive` is create/read only — but `copy_file` **is** a create, so **restore points need no bridge**. Editing still needs `google_workspace` on darwin. |
| L8 | `google_workspace` runs on GCP project **1054330720958**. A `SERVICE_DISABLED` 403 is an API-not-enabled error in an auth-error costume. |

**Repo and tooling**

| # | Fact |
|---|---|
| L9 | venv at `.venv`. Tests: `./.venv/bin/python -m pytest tests/ -q`. Root `conftest.py` inserts `src/`. |
| L10 | Every model checked against a closed form, a published result, or a hand-verified case. The Cournot suite caught a real bug on its first run and that bug turned out to BE the manuscript's marginal pair (WT-001). |
| **L13** | **A multi-line commit message will not survive `dx`'s quoting** — exit 2 is dx's refusal, meaning nothing ran and retry is safe. `dx --put` it to **`.git/COMMIT_DRAFT`**, then `git commit -F`. Inside `.git/` specifically: a draft in the working tree gets swept up by `git add -A` and committed, which S2 did. Also: `$HOME` in the cloud shell is `/root`, not darwin's home — use literal `~` in dx paths. |
| **L14** | `conftest.py` only fires under pytest; `scripts/` needs its own shim: `sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "src"))`. |
| **L15** | **Mutation-test any result you intend to publish**, and confirm the *right* test screams. S2 ran eight mutations across two modules; all eight caught. Watch the anchor: a literal `\n` in a heredoc argument does not match, the replacement silently no-ops, and you get a **spurious pass** that reads like a weak test. Assert the anchor exists, and always run an unmutated control. |
| **L16** | **Measure the manuscript, don't opine about it.** Jason asked whether a section was too long; counting sections showed it was 8.9% of the document while the contribution was 3.0% and arrived at 76% of the body. That turned an editorial opinion into WT-040. `manuscript_after.md` parsing is three lines of python and it has been right every time. |

## WHAT S2 DID

Two at-bats and six of Jason's paper notes.

Built `redistribution.py` (WT-030→033/034/035): the sharp claim half-survived — at matched rates
the bases are an order of magnitude apart as predicted, but "regardless of rate" is false. The
surviving, sharper claim is **realisation**: at ρ = 0 a 100% flow levy is indistinguishable from
no levy. Caught `is_bounded` scoring total condensation as *bounded* because the Gini saturates at
the (N−1)/N ceiling (WT-034, now a standing guard test). Built `lambda_sensitivity.py` (WT-036),
closing WT-002 entirely: the numeraire cancels, spread exactly 0.0 across twelve orders of
magnitude, dimensional outputs at slope 1.000000000000.

Then notes #3–#6 with Jason, which produced more than the code did: **WT-038** (a first principle
is an invariant with a stated domain, not an undeniable truth — and on that footing Λ is an
*entailment*, which retires three sessions of defending WT-002), **WT-039** (his relocation
method, named), **WT-040** (the 76% measurement and the restructure), **WT-041** (SMD is the
shield; scalar capital is the sword), **WT-042** (*force-fit, not form-fit* — his phrase, and the
constraint-expiry argument), **WT-043** (defend Λ once, and WT-026 is what escapes the Odum trap),
**WT-044** (names audit clean; attribution absent), **WT-045** (GNN demoted, KAN added).

Also fixed, outside this repo: `darlish-up` now logs why its dependency step failed;
`handoff_gate.py` exit codes went tri-state after blessing a handoff carrying `gh_sha: PENDING`;
and `gate-selfcheck.sh`'s range-ref detector learned to count past Z, which immediately surfaced
four stale references it had been hiding.
