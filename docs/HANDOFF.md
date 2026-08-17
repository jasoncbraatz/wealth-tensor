---
project: wealth-tensor
gh_sha: 25a0b70
updated: 2026-08-17
session: wealthTensor-62
gate_passed: false
gate_version: "2.59"
definition_of_done: "CLEARED FOR LIFTOFF (Jason's ruling, 2026-08-16): Papers II, III and IV done with their coaching and editing, the corpus audited as ONE thing, the python scripts done with every number regenerating from a committed one, and ONE well-designed deliverable that visualises the work — then Jason reads it, does whatever minor re-arranging document design reveals, and clears it. At that moment Claude is finished on wealth-tensor. POSTING IS NOT IN SCOPE: Voice Box Jasonizing, Jason's own-hand rewrite, the endorsement ask and submission are SUCCESSOR projects. A session driving toward 'posted' is driving past the end of the road. The deliverable is a PDF **and a recipe**: RECIPE.md paint-by-numbers (every font, size, leading, margin, package version), a preflight that FAILS on a substituted font rather than approximating, vendored/checksummed fonts, and a rebuild that reproduces the committed page count and per-page text hash — because Jason does the layout and visualisation analysis exactly ONCE."
---
# wealth-tensor — HANDOFF

## `-62` IN ONE LINE
**`P7` HAS A FIRST PASS AND IT IS A DOCUMENT.** `docs/REVIEW-005-P7-pass-1.md` — **32 items scored,
11 LIVE, 8 REPAIRED, 21 dismissed with reasons.** The backlog that three legs read and nobody scored
is drained. **And the cheapest unrun check in the repository was run**: `RESULT-REG-013.md` §4.3's
defence of its seed choice is false in both directions, `LEDGER WT-090`. Board still **52/66** —
`P7` is one boolean and cannot move on a pass (§5 of the review, carded). Commits `15c1d02`,
`25a0b70`.

> ⚠ **`gate_passed: false`, SIXTH CONSECUTIVE SESSION, SAME TWO FILES. IT IS PERMANENT AND YOU WILL
> INHERIT IT TOO.** `G-A`→`G-AL` green, all repos committed and pushed. The single `FAIL` is
> `~/Scripts DIRTY(2)`: `braatz-crawl-check.py`, `serve-braatz-archive.py`. **DO NOT COMMIT THEM.**
> `-61` measured it: mtimes **Aug 16 13:37 / 13:35**, against roster joins hours later — they cannot
> be ours, and that is arithmetic. `big_worker-braatzArchive` has been reaped, so route three's
> *"inside a LIVE sibling's window"* can never be satisfied again. Numbers, three drill cases and
> the safety argument: card `1217526943288480`. `-59`→`-62` all declined to implement it, for the
> same still-correct reason — a judgement change to a safety guard wants its own at-bat. **Say it
> out loud anyway: a session that EXPECTS a red gate will not notice a real one.**

---
## 0 · READ THIS BEFORE YOU READ ANYTHING ELSE — the tell `-62` inherited and the one it adds

`-61`'s, still the most expensive lesson on this project: **A CORPUS UNDER REPAIR HAS A MOVING
REFERENT, AND ONLY THE FILESYSTEM KNOWS.** `ls -la` and a `.bak` diff before you build anything on a
passage. It paid again this session, in the *opposite* direction: the single sharpest finding in
`P7` pass 1 (`IV-1`) exists **because** the passage was four hours old — `-59` inserted it closing a
hole and opened a worse one. Fresh text is not automatically a mirage; it is automatically
**unreviewed**.

**`-62` adds the corollary that nearly cost it a finding, and it generalises further than the first:**
**THE LINE-WRAP GREP TRAP RUNS IN TWO DIRECTIONS, AND THE SECOND IS THE EXPENSIVE ONE.** `-61` met
it as a false *fabrication* charge — grep a wrapped phrase, get zero, conclude the quote was
invented. Run the identical zero against an older `.bak` and it reads as **freshly inserted text** —
a false *novelty* charge. In a corpus being repaired while it is audited, that is the error that
destroys a verdict. This session almost filed one: Paper II's abstract phrase *"order of magnitude
in compression"* returns nothing from `bak-wt54-preP3` on a line grep, and is in fact the **oldest**
live item found. **Normalise before asserting presence OR absence:**
`tr '\n' ' ' < f | tr -s ' ' | grep -o '…'`.
**And never `grep -oc`** — `-c` overrides `-o` and counts *lines*, so a normalised single-line file
returns `1` for every nonzero count. That bug produced "diagonal occurs once" when it occurs eight
times, and was caught only by recounting with `grep -o | wc -l`.

---
## ORIENT — in this order
1. **`docs/REVIEW-005-P7-pass-1.md`** — `-62`'s, **NEW, and it is the at-bat you are continuing.**
   §1 the eight repairs, §2 the three live-and-unrepaired with reasons, §3 the twenty-one dismissed
   (**read §3 — it is what makes the eleven mean something**), §4 what this pass's own instrument got
   wrong, §5 why the board cannot show `P7`'s state.
2. **`docs/preregistration/RESULT-REG-013.md`** — read the **appended CORRECTION note** before §4.3,
   or §4.3 will read as settled. `LEDGER WT-090` is the same finding with the transferable half.
3. **`docs/DECISION-001-A2-and-road-one.md`** — **STILL UNTICKED as of 2026-08-17 08:24.**
   `-60`, `-61` and `-62` all checked the file and did not block. **If a box is ticked, that is your
   at-bat and it outranks the board.** Two of `P7` pass 1's three unrepaired items (`II-2`, `II-3`)
   are edits of whichever option is chosen — do not repair them separately.
4. **`docs/RESULT-END-TO-END-001.md`** and **`-E6.md` §2 before §3** — the pass is CLOSED, `T = 2`,
   `A = 0`, THE SYSTEM FAILS. §2 is a warning, not a result.
5. **`docs/CHECKLIST.md`** — 66 criteria, **52 met**. `./scripts/regen-board.sh`, never `board.py`.
   First open lane still reads `P13`; **`P13` IS LAST by ruling**, so the board is not your
   instruction. See §3.
6. **`docs/CO-AUTHOR-CHARTER.md`** — the constitution. **THE CHARTER WINS.**
   `~/Scripts/charter-read.sh wealthTensor-<NN>` — POSITIONAL slug, **re-stamp IMMEDIATELY BEFORE
   THE GATE.**

---
## 1 · WHAT HAPPENED

### `P7` CONVERGENCE PASS 1 — the first one that exists
Twenty-eight rows of `RESULT-…-E2-blind-pass.md` §§3–4 had been read by three legs, each asking its
own question, and **scored as `P7` by nobody.** Four more sat on card `1217538797952709`. A
convergence counter cannot start over an unscored backlog — a "zero-finding pass" across rows nobody
adjudicated is an omission, not a zero. So pass 1 drained it. **Three independent single-paper
scorers, then every surviving quote and count re-verified by hand against the bytes.**

**The eight repaired**, each with a `.bak-wt62-p7` written *before* the anchor assertion:
- **`IV-1`, and it is the sharpest thing in the corpus this week.** Paper IV §3 *Household* read
  *"its claim layer recognises at α = 0.05"* — **the one number Paper III measures as wrong.**
  Paper III §5.4: **α̂ = 0.408/yr, 95% CI [0.383, 0.432]**, *"low by an order of magnitude"*,
  *"the calibrated 0.05 is outside the interval of all of them."* Paper IV carried `0.05` once and
  `0.408`, `calibrat*`, `hazard` **zero** times — **while disclosing diagonality, rejected by the
  SAME §5.4 run on the same events, eight times.** One rejection flagged three sections deep, its
  sibling silent. The clause was `-59`'s, inserted 19:58→21:27 on 08-16 to close Builder B rank 1's
  *"household leg with no paper at all"*. `-58`'s precedent needed a third session; `-62` was it.
- **`IV-2`** §2.1 promises domains and carries none (`domain` occurs **once in 715 lines**). Pointer
  added plus P1's domain in full — the one that bites, since IV lists *"a claim on a pension"* and
  `contractual` occurs zero times.
- **`IV-3`** §1.1's three constraints had two lapses and a decoration. *"all three have lapsed"* →
  two; the firm-level-energy claim, denied by Paper IV in **four** of its own places, withdrawn in
  terms. **Closes `E2` Builder B #5, circled by three sessions and never repaired.**
- **`IV-4`** §7 asserted Λ⁻¹ *"already published"*; Paper III §A.2.2 denies exactly that
  *"emphatically"*. Narrowed to the dimensional claim, with §A.2.2's bound cited in the sentence.
- **`III-1`** the abstract states a **ratio as a multiple**: 2.58 is the ladder's leverage-to-budget
  ratio, not 2.58× the 0.61 failure level. The multiple is **4.2×**, and it recomputes from §4.4's
  own printed rungs (1.193 / 0.463 = 2.576). A referee finds this with the printed table and a
  calculator.
- **`III-2`** α overloaded at exactly one sentence → *"the significance level tightened to 0.025."*
- **`II-1`** §7 states a provenance rule and breaks it eleven lines later: the `src/` pin claimed
  *"every number in §3"* while two producers live in `scripts/`. **Same shape as `IV-1`, one paper
  over** — a repair session named a second producer outside the pinned path and left the pin's
  *"therefore"* standing.

### The seed-provenance check — `-61` named it, `-62` ran it, and the answer is at a different site
`RESULT-REG-013.md` §4.3 names the one judgement no pre-registration can retire — *"Seed choice is a
judgement"* — and then retires it with a claim about the repository: *"The seeds … **are the works
this corpus actually cites**."* **False in both directions.** Five of nineteen target seeds are
cited nowhere in Papers I–IV (Ayres & Warr 2009 · Kümmel 2011 · Godley 1999 · Lavoie 2014 · Dos
Santos 2005; by cluster **K 6/6 · T 5/7 · S 3/6**, and **S is the denominator cluster** in two of
three target pairs). And Paper II cites *Econophysics of Income and Wealth Distributions* (2013) —
kinetic exchange by three of cluster `K`'s own seed authors — which is **not** a seed. The card's
guessed form of the check ("a cited work in both seed sets") returns **nothing**; the "six works"
count is not contradicted. **It moves no number and may not** (`REG-013` §6). It removes a defence.

---
## 2 · RULINGS — DO NOT REOPEN
- **All of `-31`'s through `-61`'s stand verbatim.** `END-TO-END-001` IS FIXED AND COMPLETE AND ITS
  STOPPING RULE HAS FIRED; `E1`–`E6` ARE SPENT; A LEG MAY NOT COUNT A FINDING MADE BEFORE IT EXISTED;
  TEST AND AUDIT COUNTS SEPARATE, NEVER COMBINED; THE ADMISSION CRITERION IS NOT ADVISORY;
  `P2`/`P3`/`P5` STAY MANUAL; **DO NOT EDIT `src/`**; **`P13` IS LAST**; ROW IDS NEVER RENUMBERED;
  `P7` DOES NOT CLOSE THE CORPUS; DONE IS "CLEARED FOR LIFTOFF"; `R5` UNSPENT; **`T = 2`, THE SYSTEM
  FAILS, `T` CAN RISE AND CANNOT FALL**; THE REGISTRATION IS **0-for-8** AND `N` STAYS EARNED.
- **NEW · `P7` PASS 1 IS RUN AND IS A DOCUMENT.** `REVIEW-005-P7-pass-1.md`. **The consecutive-zero
  count is 0 for all three papers** and a pass that finds anything resets it. A pass is a document or
  it did not happen.
- **NEW · `-58`'s PRECEDENT NOW BINDS `-62`.** The session which rewrites a passage may not grade it.
  **`-62` repaired eight passages and may not score them in pass 2.** `-63` can, and should — they
  are the first eight items on its list.
- **NEW · `REG-013` §4.3's SEED-PROVENANCE DEFENCE IS RETIRED; THE SEED LISTS STAND.** §6 forbids
  re-choosing a seed list in response to anything, this finding included. **Do not propose a re-run
  to "fix" the seeds.** A correction note is appended and that is the whole remedy.
- **NEW · THE `P2`-AT-THREE-STRENGTHS LEAD IS WITHDRAWN.** It reads a modelling stipulation
  (*"**Model** … as"*) and a conditional antecedent (*"**If** … then"*) as unqualified assertions,
  and compares a *recording* qualifier against a *maintenance* qualifier — where maintenance is an
  explicit parameter, `E(t+1) = E(t)·(1 − d·(1 − m))`, `m = 0.6`. One proposition, correctly
  qualified once. **Do not re-derive.**
- **NEW · TWENTY-ONE BLIND-PASS ROWS ARE SCORED AND DISMISSED** (`REVIEW-005` §3). Nine were the
  builders finding the paper's own disclosure and reporting it as concealment; two were right about
  a fact and wrong about the jurisdiction. **The blind pass is mined. Do not re-mine it.**

---
## 3 · THE AT-BAT for `-63`
**`P7` is still the critical path** — `P8` waits on it, `P13` waits on `P8`, `P11` is done, and the
board's first open lane is still `P13`, which is last by ruling. **Take one, in this order:**

**1 · `P7` PASS 2, and you are the only session that can start it.** Two halves, both required:
  - **(a) Re-grade `-62`'s eight repairs.** They are listed in `REVIEW-005` §1 with the exact new
    wording. `-62` is disqualified from scoring them by `-58`'s precedent; you are not. **If all
    eight hold and you find nothing else in that paper, that paper has its FIRST zero pass** — and
    two consecutive zeros closes `P7` for it. That is the shortest live path to a closed criterion
    anywhere on this project.
  - **(b) Read what pass 1 did not.** Pass 1 was a *backlog drain* — it scored what two blind
    builders and one card had already surfaced. **It was not an independent read of the manuscripts.**
    Paper III §A.2.3–A.2.4 (numeraire cancellation, Λ sawtooth) has still been read only for the α
    and SDG threads, by anybody, ever. `REVIEW-004` C6 (ASC 410) and C10 (IAS 36 reversal asymmetry)
    are still re-served by nobody.

**2 · `III-3`, the cheapest substantive item on the board, and it needs ONE answer.** Paper III §4.7
says *"For three of the four classes, the standards already supply that outside determination"* and
then names **two** — finite-lived intangibles and depreciable property. The abstract inherits the
count as *"restoring φ for every class but goodwill."* The missing third can only be indefinite-lived
intangibles, which the same paper says are *"tested for impairment rather than amortised"*.
**`-62` deliberately did not repair it**: weakening a headline claim on a guess is worse than
flagging it. **What settles it is one GAAP fact** (do indefinite-lived intangibles carry any
disclosed outside determination of δ?) **plus one question about intent** (did §4.7 mean something
else by "three"?). The first half a Claude can settle in ten minutes; if the answer is no, **both
§4.7 and the abstract are one class too generous** and the abstract is the one that matters.

**3 · `P6`'s remaining two thirds** (`P1n`/`P5n` are `P3n` repointed, ~30 min, mechanical).

**FORCING LINE, `-59`'s ruling, kept: a session that takes none of the three must say why in ONE
LINE at the top of its handoff.** `-62` took #1 and #2 of its own list and reports the line costs
nothing.

**JASON-SIZED, NOT A CLAUDE'S — unchanged and still waiting:**
- **`DECISION-001`: A, B or C.** Unticked. `-60` recommends **B**. **Two `P7` items are riding on
  it** (`II-2` the abstract's *"order of magnitude in compression"* against §3.1's *"in κ"*;
  `II-3` the ρ = 0 result reported as *"statistically indistinguishable"* when it is an identity by
  construction). Whichever option is ticked, those are two of its edits.
- **Paper IV's title and abstract leading clause still read *"from the household to the sovereign."***
  §3's remedy named that phrase for narrowing, `E3` certified it narrowed, it is not. Narrow it, or
  ratify the appended demotion as sufficient. `E2` ruled the title Jason-sized.

---
## 4 · TEED UP, IN ORDER
- **`P7` CANNOT BE REPRESENTED ON THE BOARD** — one row, `0/1`, for a per-paper two-consecutive-zero
  criterion. True state after pass 1: II 3 findings, III 3, IV 5, counter **0/0/0**, none of it
  visible. **`-56`'s `P11` finding in a new costume**, same repair shape (per-paper rows from one
  template, check as a derivation not a constant). Card `1217540043232039`. Not done: adding criteria
  moves the 66 and wants its own at-bat. **Take it together with card `1217529210807546`** — the
  board also has zero rows for A2, `REVIEW-004`, `ROADS-001`, Road One or Road Two.
- **`END-TO-END-002` inherits four registration defects**, recorded, none repaired: `E5`'s clause-pair
  mismatch · `E4`'s two reachable gaps · `E4`'s unconditional remedy · `E6`/`E4`/`E5` declaring no
  UNDECIDED region.
- **`G-H#22c`** — card `1217526943288480`, with `-61`'s measured mtimes and three drill cases.
- Paper I was never compared against Paper IV's account of it (out of scope; the corpus is II/III/IV).
- `REG-013` re-run: the biophysical audience was capped at 4 000 of 7 801. **And note §3.1's fourth
  `T` seed names two works separated by a slash under one date; the script chose Hall & Klitgaard
  after the registration. §6's "fixed" guarantee is one seed weaker than it reads.**
- **`~/Scripts/gate-selfcheck.sh` IS A SYMLINK INTO `~/code/darwin-mac-ops`** — `git add` in
  `~/Scripts` stages nothing **and reports success.**
- Infra siblings, carded: Caddy `1217488447555628` · capability path `1217488117177482` ·
  card-lint `1217483699706758` · gate `1217465036940491`.

---
## 5 · TOOLING — what `-62` measured, on top of `-61`'s list which all still holds
- **`STEP 0` went READY on the first try again, enrollment to `roster join` in under four minutes.**
  Budget four. The `darlish-up` → Asana attestation → `darlish-up` → `dx` sequence needed no retries.
- **`tar czf /tmp/wt-docs.tgz docs` + ONE `dx --get`** is still the single biggest speedup here.
  4.5 MB, every `.bak` included. `mkdir -p` the destination first — `$HOME` is `/root` in the cloud
  container and a `--get` into a missing directory fails with **exit 3**.
- **`| tail` MASKS `$?` ON EVERY `dx` CALL** — `cmd; echo rc=$?`, no pipe. Still true.
- **The `COMMITMSG.txt` → `dx --put` → `git commit -F` recipe worked cleanly twice.** Never inline a
  multi-line message in `dx '...'`.
- **`NEVER grep -oc`.** `-c` overrides `-o` and counts LINES. On a whitespace-normalised file — which
  is one line — every nonzero count returns `1`. This produced a wrong token count that survived into
  a draft finding and was caught only by recounting. Use `grep -o … | wc -l`.
- **A batched patch script beats eight edits.** One python file holding `(path, label, old, new)`
  tuples: `.bak` for every touched file **first**, then `assert src.count(old) == 1` for every anchor
  **before** any write, then write. Dry-run it against a copy of the tarball in the cloud container,
  diff the copy, *then* `dx --put` the identical script and run it on darwin. Eight anchors, zero
  misses, and the dry run caught two line-wrap scars before they reached the repo.
- **When you extend an anchor to rewrap a paragraph, extend it to a sentence boundary**, not to the
  end of your replacement — otherwise the following clause lands with a leading space.
- `roster claim` needs `--who` AND `--resource`. `lessons.py use <id> --task <tag>` — id positional.
- `gate-selfcheck.sh` takes 5–6 min; the cloud `Bash` tool caps at 2 min and a foreground call dies
  at 8m20s. **Detach, then poll with two `sleep`s** — and this is new and it matters:
  **`GATE_ROSTER_WHO=big-wealthTensor-<NN> nohup ~/Scripts/gate-selfcheck.sh > /tmp/gate.log 2>&1 &`.**
  A detached run has no session tag, so `G-AL` returns `CANNOT VERIFY` **and `G-AL#board` never
  runs.** `-62`'s first gate showed one FAIL (the permanent `~/Scripts` red) and looked normal; the
  same gate with `GATE_ROSTER_WHO` set showed **two**, and the second was a stale board caused by
  this session's own edit. Six sessions of handoffs prescribe detaching and none mentions the
  variable. `charter-read.sh` stamping is **not** sufficient — the gate reads `GATE_ROSTER_WHO` or
  `$SESSION_STATE/current`, and a detached `dx` shell has neither.
- **ANY EDIT TO ANY ABSTRACT: run `python3 scripts/check_abstract_size.py <paper> --print` in the
  same breath.** All three abstracts sit within three words of the hard 250-word ceiling — II 249,
  IV 248, III 248 after this session (247 before it). `-62`'s first `III-1` wording hit **268** and
  took `P1a` and `P1l` red without a word of warning; the checker is silent on success and on
  failure, so `echo rc=$?` or pass `--print`.

---
## 6 · ORIENT-THEN-GO
Nothing is perishable. Emit one line — `Oriented: <state> · at-bat: <X> · opening with <first
action>.` — and start. Do not open by asking Jason anything **except** whether he has ticked
`DECISION-001`, and **check the file before you ask.**

**Coffee status:** ☕ **TWENTY-EIGHT SESSIONS, AND THE AUDIT IS OVER — THE EDITING HAS STARTED.**
`-56` found the fact that killed `E1` four days stale in a dossier. `-57` found the sentence that
killed `E3` four words long in an appendix. `-58` and `-59` built findings and watched refuters take
them apart. `-60` was told the answer in advance and found it wrong. `-61` built the best finding of
six legs and it was a mirror. **`-62` found the corpus arguing with itself in three places at once —
a paper importing the one number its companion measured as false, an abstract reporting a ratio as a
multiple, and a provenance rule broken eleven lines after it was stated — and every one of them was
put there by somebody trying to be careful.** The `E2` blind pass wrote 28 rows and 21 of them were
the papers' own disclosures being read as concealments, which is the corpus's real defence: **it
already says the awkward part out loud, usually two sections further down than anyone looked.**
Twenty-one clean bills and eleven live defects is a good day's box score, and the eleventh was found
by grepping a sentence whose entire job was to say the grepping was already done. 🥎
