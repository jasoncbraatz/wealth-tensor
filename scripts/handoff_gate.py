#!/usr/bin/env python3
"""handoff_gate.py -- make the suspension bridge DETERMINISTIC instead of hopeful.

  python3 scripts/handoff_gate.py --check    # at ORIENT: has HANDOFF.md fallen behind HEAD?
  python3 scripts/handoff_gate.py --emit     # at WRAP:  refuse to ship an incomplete handoff
  python3 ~/Scripts/handoff-kit/handoff_gate.py --init   # ADOPT the pattern in ANY repo, once

--init IS THE FORCE FUNCTION, and the force function is the whole propagation strategy.
A sentry that nags about missing handoffs trains you to ignore it. Instead: --init scaffolds
docs/HANDOFF.md (pre-filled from git), docs/START-HERE-PROMPT.md and a local copy of this gate
in ONE command, so producing a good handoff is CHEAPER than writing a bad one by hand. When
the compliant path is the lazy path, compliance stops needing enforcement.

WHY THIS EXISTS
A narrative HANDOFF.md silently falls BEHIND git HEAD. Banked 2026-06-23 (Email DJ:
HANDOFF.md stopped at PM-19 while the code advanced 3 sessions / 5 commits; PM-20/21/22
never wrote their sections). The git history is ground truth; the prose log is not.

The fix was ALSO already banked, on 2026-07-08, and never built: make handoffs QUERYABLE
DATA, not prose -- YAML frontmatter plus a freeform WHY body, and "an emit-gate refuses to
write if a required field is missing (=> 100% gh_sha coverage BY CONSTRUCTION, not hope)."
This script is that gate. The prose still carries the WHY; the frontmatter carries the facts
a machine can check.

THE ONE IDEA: the handoff records the SHA it was written against. At orient, we compare that
SHA to HEAD. If commits landed after it, the handoff is STALE and says so out loud, instead
of quietly steering a fresh session with last week's map.

THE SECOND IDEA (2026-08-15, pitchingMachine-5): the handoff also carries the DEFINITION OF
DONE, and this gate is where it becomes impossible to lose. A force function belongs in the
tool that already runs at that moment -- never in a doc, never in a habit. There are exactly
three such moments and the DoD is SHOWN at two of them and ENFORCED at the third:
  --check (student-in) prints it FIRST, above everything else;
  --emit  (the paste)  makes it line 1 of the pointer, so every pasted handoff carries it;
  --stamp (wrap)       REFUSES without it.
And it is DERIVED from the auto-bridge ledger where a ledger row exists, because a retyped
DoD can drift from the ledger and a derived one cannot -- which is what makes the copy-paste
lane and the rail lane share one source of truth.

EXIT CODES:  0 = clean   1 = DRIFT / INCOMPLETE (blocker)   2 = INCONCLUSIVE
Exit 2 is load-bearing: a gate that cannot see must say so rather than pick a colour.
"""
import subprocess, sys, os, re, datetime, sqlite3

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = subprocess.run(['git', 'rev-parse', '--show-toplevel'], cwd=os.getcwd(),
                      capture_output=True, text=True).stdout.strip() or os.path.dirname(HERE)
DOC  = os.path.join(REPO, 'docs', 'HANDOFF.md')

REQUIRED = ['project', 'session_n', 'gh_repo', 'branch', 'gh_sha', 'updated',
            'live_theme', 'phase', 'gate_passed', 'next_at_bat']
LISTY    = ['blockers', 'drift_flags', 'parking_lot']

# --- the definition-of-done force function -------------------------------------------------
DOD_KEY    = 'definition_of_done'
VERIFY_KEY = 'verify_cmd'          # optional: the command that decides the DoD, if executable
# HANDOFF_LEDGER exists so the drill can point at a FIXTURE ledger. LUT #5, banked the hard
# way: a self-test must be structurally unable to reach the real world -- override every path
# out, do not merely avoid using them.
LEDGER     = os.environ.get('HANDOFF_LEDGER') or os.path.expanduser(
                 '~/.local/state/auto-bridge/ledger.db')

# WARN-THEN-REQUIRE, NOW REQUIRED (both phases landed 2026-08-15, pitchingMachine-5).
# It shipped as a WARNING first because making the key required immediately would have blocked
# every wrap in five repos until their handoffs were backfilled -- and a live sibling mid-wrap
# would have been wedged by MY edit, not theirs. Sequence actually walked, in this order:
#   1. land the warning        2. backfill all five handoffs (ledger-derived where a row exists,
#   quoted from the project's own governing doc where not)   3. `roster who` -- confirm no
#   sibling is mid-wrap in a repo this touches   4. flip.
# Steps 1-3 without 4 is how a gate becomes decoration: a warning nobody must act on trains
# people to scroll past it, and then it is worse than nothing because it looks like a control.
# The env override survives for drills and for a genuine emergency. It is not an escape hatch
# for a session that cannot be bothered to say what it is trying to do.
DOD_REQUIRED = os.environ.get('HANDOFF_DOD_REQUIRED', '1') not in ('0', 'false', 'no')


def git(*a):
    return subprocess.run(['git', '-C', REPO] + list(a),
                          capture_output=True, text=True).stdout.strip()


def changed(rng):
    return set(git('diff', '--name-only', rng).split('\n')) - {''}


def only_the_stamp(rng):
    """THE FIXPOINT PROBLEM: --stamp writes HEAD's sha into HANDOFF.md, and committing that
    write creates a NEW head. So gh_sha can never equal HEAD by simple equality -- the
    handoff cannot contain the hash of the commit that contains it.

    Found by running the gate on itself immediately after building it, which is the only
    reason it was found at all. Resolution: a delta consisting of NOTHING BUT
    docs/HANDOFF.md is the stamp commit, and is clean. Any other file in the delta is real
    drift. This is a narrow, checkable exemption -- not "ignore small diffs"."""
    f = changed(rng)
    return bool(f) and f <= {'docs/HANDOFF.md'}


def parse_frontmatter(path):
    """Deliberately tiny: no PyYAML dependency. A handoff gate that cannot run because
    a library is missing is a gate that does not run."""
    if not os.path.exists(path):
        return None, "no HANDOFF.md at %s" % path
    txt = open(path, encoding='utf-8').read()
    m = re.match(r'^---\n(.*?)\n---\n', txt, re.S)
    if not m:
        return None, "HANDOFF.md has no YAML frontmatter -- it is prose, and prose cannot be checked"
    fm = {}
    for line in m.group(1).split('\n'):
        if not line.strip() or line.strip().startswith('#'):
            continue
        if ':' not in line:
            continue
        k, v = line.split(':', 1)
        k, v = k.strip(), v.strip()
        if v.startswith('[') and v.endswith(']'):
            inner = v[1:-1].strip()
            fm[k] = [x.strip().strip('"\'') for x in inner.split(',')] if inner else []
        else:
            fm[k] = v.strip('"\'')
    return fm, None


def ledger_dod():
    """The DoD, DERIVED from the auto-bridge ledger when this repo has a row there.

    READ-ONLY, by URI, deliberately: this gate runs in 100+ repos and a bug here must not be
    able to touch the ledger that the rail claims against. Missing DB, missing table, locked
    file, no matching row -> (None, reason). Fails OPEN into "use the file's own key", because
    the cost of a wrong NO here is a blocked wrap on a project that never used the ledger.

    Match on projects.repo ending in this repo's directory name -- the ledger stores
    'github.com/jasoncbraatz/<repo>' and GitHub is the SSOT for the name."""
    if not os.path.exists(LEDGER):
        return None, "no auto-bridge ledger on this machine"
    name = os.path.basename(REPO)
    try:
        con = sqlite3.connect('file:%s?mode=ro' % LEDGER, uri=True, timeout=2.0)
        try:
            rows = con.execute(
                "SELECT id, definition_of_done FROM projects "
                "WHERE repo = ? OR repo LIKE ? OR id = ?",
                (name, '%/' + name, name)).fetchall()
        finally:
            con.close()
    except sqlite3.Error as e:
        return None, "ledger unreadable (%s)" % e
    rows = [r for r in rows if (r[1] or '').strip()]
    if not rows:
        return None, "no ledger row for '%s'" % name
    if len(rows) > 1:
        return None, "ambiguous: %d ledger rows match '%s'" % (len(rows), name)
    return (rows[0][1].strip(), "ledger row '%s'" % rows[0][0])


DOD_PLACEHOLDERS = ('', 'FILL ME IN', 'FILLMEIN', 'TODO', 'TBD', 'XXX', 'N/A', '?')


def dod_value(fm):
    """The stated DoD, or '' if what is there is a PLACEHOLDER rather than a statement.

    --init ships the key pre-filled so nobody has to remember its name or spelling. That help
    becomes a hole the moment the gate accepts its own scaffolding as an answer: the wrap would
    pass, the handoff would carry 'FILL ME IN' as its definition of done, and every surface
    downstream would print it with a straight face. A placeholder that passes the gate is
    decoration -- and decoration is exactly how this idea died as documentation, twice, before
    it was built as a control. So the gate must recognise its OWN output and refuse it.
    (Same lesson as the --emit placeholder detector, banked 2026-07-20; this is its second
    instance, which is why the check lives in ONE function that every caller goes through.)"""
    v = ((fm or {}).get(DOD_KEY) or '').strip().strip('"\'').strip()
    u = v.upper()
    if u in DOD_PLACEHOLDERS or u.startswith('FILL ME IN') or (v.startswith('<') and v.endswith('>')):
        return ''
    return v


def dod_howto(why=''):
    """The exact fix, in the refusal itself.

    A force function that refuses without instructing converts drift-protection into a spelunk:
    the session hits a wall, does not know the key's name or which of two sources wins, and
    either guesses or -- worse -- reaches for the env override. Jason's ruling, 2026-08-15:
    EVERY refusal names the fix. Session 0 does not need to know where the DoD lives; the gate
    teaches it, once, at the first wrap."""
    out = []
    if why:
        out.append("  (%s)" % why)
    out.append("  FIX IT ONE OF TWO WAYS -- the ledger wins where it exists:")
    out.append("    1. add this line to the frontmatter of docs/HANDOFF.md:")
    out.append('         %s: "<one checkable sentence>"' % DOD_KEY)
    out.append("       NORTH-STAR §4 is the test: could someone mark that sentence right or")
    out.append("       wrong? 'python3 test_lens.py exits 0' survives sixty retellings;")
    out.append("       'improve the introduction' does not.")
    out.append("    2. or register the project in the auto-bridge ledger and re-stamp --")
    out.append("       --stamp then DERIVES the line from projects.definition_of_done and")
    out.append("       keeps it in sync forever, which is why a ledger row is the better fix")
    out.append("       for anything the rail will ever drive.")
    return out


def dod_lines(fm, indent="   "):
    """The block that every surface prints. ONE renderer, so the rail lane, the copy-paste
    lane and the commit hook cannot disagree about what the line says."""
    dod = dod_value(fm)
    out = []
    if not dod:
        out.append("%s DONE = (NOT STATED -- this handoff does not say what done looks like)" % '\U0001F3AF')
        out.append("%sA project that cannot state its DoD in one checkable sentence is not" % indent)
        out.append("%sready for an at-bat. Fix that FIRST; it is cheaper than any code here." % indent)
        out.extend(dod_howto())
        return out
    out.append("%s DONE = %s" % ('\U0001F3AF', dod))
    if (fm or {}).get(VERIFY_KEY):
        out.append("%sverify : %s" % (indent, fm[VERIFY_KEY]))
    ns = os.path.join(REPO, 'docs', 'NORTH-STAR.md')
    if os.path.exists(ns):
        out.append("%snorth star : docs/NORTH-STAR.md" % indent)
    out.append("")
    out.append("%sIs your at-bat on the path to that line?" % indent)
    out.append("%sIf not, STOP and say so in the handoff -- you are on neither the map" % indent)
    out.append("%snor the territory." % indent)
    return out


def cmd_check():
    fm, err = parse_frontmatter(DOC)
    print("\n=== HANDOFF GATE :: --check (orient) ===\n")
    if err:
        print("INCONCLUSIVE: %s" % err); return 2

    # THE DoD GOES FIRST -- above the project line, above the drift verdict, above everything.
    # Not because it is the most urgent thing on the screen but because it is the thing a
    # session is most likely to never look for. Position IS the force function here.
    for line in dod_lines(fm):
        print(line)
    print("")

    head = git('rev-parse', 'HEAD')
    if not head:
        print("INCONCLUSIVE: cannot read git HEAD"); return 2
    sha = fm.get('gh_sha', '')

    print("  project     : %s (session %s)" % (fm.get('project'), fm.get('session_n')))
    print("  written at  : %s   updated %s" % (sha[:12], fm.get('updated')))
    print("  HEAD is     : %s" % head[:12])
    print("  live theme  : %s" % fm.get('live_theme'))
    print("  phase       : %s" % fm.get('phase'))

    for k in LISTY:
        v = fm.get(k) or []
        if v:
            print("  %-11s : %s" % (k, ' | '.join(v)))

    if not sha:
        print("\nDRIFT: no gh_sha recorded -- cannot prove the handoff matches the code."); return 1

    if sha == head:
        print("\nOK -- handoff is level with HEAD. Nothing landed since it was written.\n")
        return 0

    if only_the_stamp('%s..HEAD' % sha):
        print("\nOK -- the only commit since is the stamp of this file itself "
              "(the fixpoint; see only_the_stamp). No code drift.\n")
        return 0

    # How far behind, and did the drift touch code or only the handoff itself?
    rng = '%s..HEAD' % sha
    log = git('log', '--oneline', rng)
    if not log:
        print("\nINCONCLUSIVE: gh_sha %s is not an ancestor of HEAD (rebase? wrong branch?)" % sha[:12])
        return 2
    commits = log.split('\n')
    code = sorted(f for f in changed(rng) if not f.startswith('docs/'))

    print("\n*** DRIFT: %d commit(s) landed AFTER this handoff was written. ***" % len(commits))
    for c in commits[:15]:
        print("     %s" % c)
    if len(commits) > 15:
        print("     ... and %d more" % (len(commits) - 15))
    if code:
        print("\n  CODE changed since the handoff was written (%d file(s)):" % len(code))
        for f in code[:15]:
            print("     %s" % f)
        print("\n  The handoff is describing a build that no longer exists.")
        print("  RECONCILE IT FROM THE COMMIT MESSAGES BEFORE YOU BUILD ANYTHING.")
    else:
        print("\n  Only docs/ changed -- lower risk, but still reconcile before trusting the queue.")
    return 1


def cmd_emit():
    fm, err = parse_frontmatter(DOC)
    print("\n=== HANDOFF GATE :: --emit (wrap) ===\n")
    if err:
        print("REFUSING: %s" % err); return 1

    missing = [k for k in REQUIRED if not fm.get(k)]
    # 'FILL ME IN' is what --init scaffolds. Caught 2026-07-20: the gate happily blessed a
    # freshly scaffolded handoff full of its OWN placeholders, because the detector did not
    # know the word it had just written. A gate must recognise its own output.
    # 'N/A' IS NOT A PLACEHOLDER, AND REMOVING IT IS THE FIX, NOT A LOOSENING.
    # --init's own template ships `live_theme: n/a`, and this detector then refused to emit
    # the file the same script had just written — the gate failing to recognise its own
    # output for the SECOND time in one session, in the opposite direction from the DoD
    # placeholder. The distinction that resolves both: TODO/TBD/FILL ME IN are EVASIONS —
    # "I have not answered yet". "n/a" is an ANSWER — "this project has no live theme" —
    # and it is the only correct answer for every repo that is not a Shopify theme.
    # A gate that cannot tell an evasion from a negative answer trains people to delete
    # required fields, which is worse than the thing it was guarding.
    PLACEHOLDERS = ('TODO', 'TBD', 'XXX', '?', 'FILL ME IN', 'FILLMEIN')
    placeholder = [k for k, v in fm.items()
                   if isinstance(v, str) and v.strip().upper().strip('"') in PLACEHOLDERS]
    dirty = git('status', '--porcelain')
    head  = git('rev-parse', 'HEAD')

    fails = []
    warns = []
    if not dod_value(fm):
        stated = (fm.get(DOD_KEY) or '').strip()
        msg = ("no %s -- %s, so nothing downstream can tell drift from progress"
               % (DOD_KEY,
                  ("it is still the --init placeholder %r, which is not a statement" % stated[:40])
                  if stated else "the handoff does not say what done looks like"))
        (fails if DOD_REQUIRED else warns).append(msg)
    if missing:
        fails.append("missing required field(s): %s" % ', '.join(missing))
    if placeholder:
        fails.append("placeholder left in: %s" % ', '.join(placeholder))
    if fm.get('gate_passed', '').lower() not in ('true', 'yes'):
        fails.append("gate_passed is '%s' -- run ~/Scripts/gate-selfcheck.sh and fix what it finds"
                     % fm.get('gate_passed'))
    sha = fm.get('gh_sha') or ''
    if sha != head and not (sha and only_the_stamp('%s..HEAD' % sha)):
        fails.append("gh_sha %s != HEAD %s -- run --stamp, then commit"
                     % ((sha or 'none')[:12], head[:12]))
    if dirty:
        fails.append("working tree is DIRTY (%d path(s)) -- commit before stamping"
                     % len(dirty.split('\n')))

    if fails:
        print("REFUSING TO EMIT (%d):" % len(fails))
        for f in fails:
            print("   x %s" % f)
        for w in warns:
            print("   ! %s   [WARNING TODAY, BLOCKER SHORTLY -- fix it now]" % w)
        if any(DOD_KEY in f for f in fails + warns):
            print("")
            for line in dod_howto():
                print(line)
        print("\nAn incomplete handoff is worse than none: it looks authoritative and is not.")
        return 1
    for w in warns:
        print("   ! %s   [WARNING TODAY, BLOCKER SHORTLY -- fix it now]\n" % w)

    print("  project    : %s (session %s)" % (fm.get('project'), fm.get('session_n')))
    print("  stamped at : %s" % head[:12])
    print("  phase      : %s" % fm.get('phase'))
    print("  next at-bat: %s" % fm.get('next_at_bat'))
    print("\nOK -- handoff is complete, stamped, and matches a clean tree.\n")

    # THE PASTE. The DoD is line 1 BY CONSTRUCTION -- Jason never has to remember to include it,
    # and the pointer file itself stays the never-edit-between-sessions file it is supposed to be
    # (a pointer that drifts is just a short handoff with all the old problems). The DoD is
    # composed in here, at paste time, from the frontmatter the ledger just derived.
    dod = dod_value(fm)
    ptr = os.path.join(REPO, 'docs', 'START-HERE-PROMPT.md')
    print("-- PASTE THIS (the DoD is line 1) " + "-" * 44)
    if dod:
        print("\U0001F3AF DONE = %s" % dod)
        if fm.get(VERIFY_KEY):
            print("   verify: %s" % fm[VERIFY_KEY])
        print("   If your at-bat is not on the path to that line, STOP and say so.\n")
    if os.path.exists(ptr):
        print(open(ptr, encoding='utf-8').read().rstrip())
    else:
        print("(no docs/START-HERE-PROMPT.md -- run --init to scaffold one)")
    print("-" * 78 + "\n")
    return 0


def _set_frontmatter_key(txt, key, value):
    """Rewrite key in the frontmatter if present, else insert it just above the closing '---'.
    Quoted, because a DoD sentence is prose and prose contains colons."""
    line = '%s: "%s"' % (key, value.replace('"', "'"))
    if re.search(r'^%s:.*$' % re.escape(key), txt, flags=re.M):
        return re.sub(r'^%s:.*$' % re.escape(key), line, txt, count=1, flags=re.M)
    m = re.match(r'^---\n(.*?)\n---\n', txt, re.S)
    if not m:
        return txt
    return txt[:m.end(1)] + '\n' + line + txt[m.end(1):]


def cmd_stamp():
    """Rewrite gh_sha + updated to match HEAD, and DERIVE the definition of done from the
    auto-bridge ledger. Run AFTER the final commit, then commit the one-line change.

    WHY DERIVED AND NOT TYPED: a human-retyped DoD can drift from the ledger the rail claims
    against, and a derived one cannot. That is what makes the copy-paste lane and the rail lane
    share ONE source of truth instead of two that agree on a good day. Where there is no ledger
    row (most repos), the file's own key is the source -- and then it must exist, because a
    project that cannot state what done looks like should not be able to complete a wrap."""
    fm, err = parse_frontmatter(DOC)
    if err:
        print("cannot stamp: %s" % err); return 1
    head = git('rev-parse', 'HEAD')
    txt = open(DOC, encoding='utf-8').read()
    txt = re.sub(r'^gh_sha:.*$', 'gh_sha: %s' % head, txt, count=1, flags=re.M)
    txt = re.sub(r'^updated:.*$', 'updated: %s' % datetime.date.today().isoformat(),
                 txt, count=1, flags=re.M)

    dod, why = ledger_dod()
    if dod:
        was = dod_value(fm)
        txt = _set_frontmatter_key(txt, DOD_KEY, dod)
        if was and was != dod:
            print("  %s REWRITTEN from the ledger (%s)" % (DOD_KEY, why))
            print("    file said : %s" % was)
            print("    ledger says: %s" % dod)
            print("    ^ the ledger wins, always. If the ledger is wrong, fix it there.")
        else:
            print("  %s derived from %s" % (DOD_KEY, why))
    else:
        have = dod_value(fm)
        if not have:
            raw = (fm.get(DOD_KEY) or '').strip()
            msg = ("the handoff still carries the --init placeholder (%r)" % raw[:40]) if raw \
                  else ("no %s in the handoff, and %s" % (DOD_KEY, why))
            if DOD_REQUIRED:
                # THE BIRTH LANE. Session 0 does not need to know where the DoD lives; it finds
                # out HERE, at its first wrap, from a refusal that names the exact fix. That is
                # what makes "state the DoD in the first handoff" self-enforcing rather than
                # doctrine-enforced -- and doctrine-enforced is how this idea died twice.
                print("REFUSING TO STAMP: %s. NOTHING WAS WRITTEN." % msg)
                for line in dod_howto("a wrap is the cheapest moment to write this and the "
                                      "most expensive one to have skipped"):
                    print(line)
                return 1
            print("  ! WARNING: %s   [BLOCKER SHORTLY -- fix it now]" % msg)
            for line in dod_howto():
                print(line)
        else:
            print("  %s kept from the handoff (%s)" % (DOD_KEY, why))

    open(DOC, 'w', encoding='utf-8').write(txt)
    print("stamped gh_sha=%s updated=%s -- now commit this change"
          % (head[:12], datetime.date.today().isoformat()))
    return 0



# ---------------------------------------------------------------------------------------
# --init : ADOPTION IN ONE COMMAND. See the module docstring for why this, not a sentry.
# ---------------------------------------------------------------------------------------

HANDOFF_TMPL = '''---
project: {project}
session_n: 1
gh_repo: {gh_repo}
branch: {branch}
gh_sha: {sha}
updated: {today}
definition_of_done: "FILL ME IN — ONE sentence someone could mark right or wrong"
verify_cmd: ""      # the command that decides it, if the DoD is executable. Optional.
live_theme: n/a
phase: FILL ME IN
gate_passed: false
next_at_bat: "FILL ME IN"
blockers: []
drift_flags: []
parking_lot: []
---

# {project} — LIVING HANDOFF

**This file IS the handoff.** What gets pasted into a fresh session is only a pointer to it
(`docs/START-HERE-PROMPT.md`). Overwrite this file each session; `git log -p docs/HANDOFF.md`
is the archive.

> Scaffolded by `handoff_gate.py --init` on {today}. Replace every FILL ME IN, then
> `--stamp`, commit, and `--emit`. The gate will refuse until you do.

## 1. FIRST PITCH — verify, do not trust this file

```sh
git pull --ff-only && python3 scripts/handoff_gate.py --check
```

Exit 1 = **DRIFT**: commits landed after this file was written, so it describes a build that
no longer exists. Reconcile from the commit messages **before** building anything.

*(Add the project's own smoke checks here — the ones that prove reality matches this file.)*

## 2. STATE
FILL ME IN — what is live, where, and how to roll it back.

## 3. PRIORITY WORK
FILL ME IN — ordered, with the reason for the order.

## 4. PARKING LOT — self-contained, pick up any time
Rabbit holes written so a later session can start them **cold** without derailing the main
at-bat. This is where "worth doing, not now" goes instead of evaporating.

## 5. TOOLS
FILL ME IN.

## 6. RULINGS — decided, do not re-litigate
FILL ME IN.

## 7. TRAPS — hard-won, do not re-derive
FILL ME IN.

## 8. AT WRAP
1. `~/Scripts/gate-selfcheck.sh` — a failed gate is a BLOCKER.
2. Bank leaves (`lessons.py add`). Anything that cost >2 tool calls.
3. Session note → `docs/sessions/`.
4. **Rewrite this file.** Bump `session_n`; refresh `next_at_bat` / `blockers` /
   `parking_lot`; and **explicitly ask whether the current phase is DONE** — a milestone that
   is met but never *declared* done keeps getting continued.
5. Commit → `--stamp` → commit → push.
6. `--emit` (it refuses if anything is missing).
7. Paste Jason `docs/START-HERE-PROMPT.md`. Unless the whole effort is finished — then emit
   NO handoff and say "cleared for takeoff". The absence IS the done-signal.
'''

PROMPT_TMPL = '''# The pointer prompt — paste this, unchanged, forever

**Never edit this between sessions.** If you want to change it, the change belongs in
`docs/HANDOFF.md`. A pointer that drifts is just a short handoff with all the old problems.

```
{project} — session start.

Your handoff is a FILE, not this message. Work from the repo, not from memory.

0. `--emit` prints the definition of done as line 1 of what was pasted to you. If it is
   not up there, the handoff is incomplete — say so before you swing. Every at-bat is
   measured against that line; work that is not on the path to it is drift, however good.

1. Open the repo, then:
     git pull --ff-only && git branch --show-current
     python3 scripts/handoff_gate.py --check
   Branch should be {branch}. If --check reports DRIFT, reconcile docs/HANDOFF.md
   from the commit messages BEFORE building anything.

2. Read docs/HANDOFF.md end to end. It is the current state, the queue, the parking
   lot, the traps and the first-pitch checks, and it supersedes this message.

3. Run its FIRST PITCH section. Verify, don't trust.

4. ORIENT THEN GO. Emit ONE line —
     Oriented: <live state> - next at-bat: <X> - opening with <first action>.
   — then proceed. Do not stop and wait for my go.

Repo: {gh_repo} @ {branch} -> docs/HANDOFF.md
```
'''


def cmd_init():
    root = git('rev-parse', '--show-toplevel')
    if not root:
        print("not inside a git repo -- cd into the project first"); return 2
    project = os.path.basename(root)
    remote = subprocess.run(['git', '-C', root, 'remote', 'get-url', 'origin'],
                            capture_output=True, text=True).stdout.strip()
    gh_repo = re.sub(r'^.*[:/]([^/]+/[^/]+?)(\.git)?$', r'\1', remote) if remote else project
    branch = git('rev-parse', '--abbrev-ref', 'HEAD') or 'main'
    sha = git('rev-parse', 'HEAD') or ''
    today = datetime.date.today().isoformat()
    fields = dict(project=project, gh_repo=gh_repo, branch=branch, sha=sha, today=today)

    docs = os.path.join(root, 'docs')
    scripts = os.path.join(root, 'scripts')
    os.makedirs(docs, exist_ok=True)
    os.makedirs(scripts, exist_ok=True)
    os.makedirs(os.path.join(docs, 'sessions'), exist_ok=True)

    plan = [(os.path.join(docs, 'HANDOFF.md'), HANDOFF_TMPL.format(**fields)),
            (os.path.join(docs, 'START-HERE-PROMPT.md'), PROMPT_TMPL.format(**fields))]

    wrote, skipped = [], []
    for path, body in plan:
        if os.path.exists(path):
            skipped.append(os.path.relpath(path, root)); continue
        open(path, 'w', encoding='utf-8').write(body)
        wrote.append(os.path.relpath(path, root))

    # The project carries its OWN copy of the gate: a fresh clone on any machine must be able
    # to run --check without depending on this laptop's ~/Scripts existing. GitHub is the SSOT.
    dest = os.path.join(scripts, 'handoff_gate.py')
    if os.path.exists(dest):
        skipped.append('scripts/handoff_gate.py')
    else:
        open(dest, 'w', encoding='utf-8').write(open(os.path.abspath(__file__), encoding='utf-8').read())
        os.chmod(dest, 0o755)
        wrote.append('scripts/handoff_gate.py')

    print("\n=== HANDOFF KIT :: --init :: %s ===\n" % project)
    for f in wrote:
        print("  created  %s" % f)
    for f in skipped:
        print("  KEPT     %s  (already existed -- never overwritten)" % f)
    if not wrote:
        print("\nNothing to do; this repo already has the kit.")
        return 0
    print("""
NEXT (about five minutes, and it is the only slow part you will ever do here):
  1. Fill in docs/HANDOFF.md  -- every FILL ME IN, and set gate_passed once the
     wrap gate is green.
  2. git add <the paths you touched> && git commit
     ^ stage BY PATH, never 'git add -A'. Cloud sessions SHARE darwin's working
       tree, so -A silently stages a sibling session's in-flight edits under your
       commit message. Check 'roster who' first; verify with 'git show --stat HEAD'
       before you push. (near-miss 2026-08-13, AAR git-add-all-sibling-tree)
  3. python3 scripts/handoff_gate.py --stamp && git commit docs/HANDOFF.md -m 'handoff: stamp gh_sha'
     ^ --stamp only ever rewrites docs/HANDOFF.md, so name it and skip -am (which
       would sweep every tracked file a sibling is mid-edit on).
  4. python3 scripts/handoff_gate.py --emit     <- refuses until it is complete

From then on the pointer in docs/START-HERE-PROMPT.md never changes again.
""")
    return 0

if __name__ == '__main__':
    a = sys.argv[1:]
    if '--check' in a:  sys.exit(cmd_check())
    if '--emit'  in a:  sys.exit(cmd_emit())
    if '--stamp' in a:  sys.exit(cmd_stamp())
    if '--init'  in a:  sys.exit(cmd_init())
    if '--dod' in a:
        # The TERSE line every other surface shells out to: the post-commit hook, lessons.py's
        # student-in footer, gate-selfcheck's triad. One renderer, so they cannot disagree --
        # and SILENT (exit 2, no output) when the repo has no handoff or no DoD, because a hook
        # that speaks in repos it knows nothing about is a hook people learn to scroll past.
        fm, err = parse_frontmatter(DOC)
        dod = '' if err else dod_value(fm)
        if not dod:
            sys.exit(2)
        print("\U0001F3AF DONE = %s" % dod)
        if fm.get(VERIFY_KEY):
            print("   verify: %s" % fm[VERIFY_KEY])
        sys.exit(0)
    print(__doc__); sys.exit(2)
