#!/usr/bin/env python3
"""wt111 — add the RECOGNISABILITY column to CONSTRAINT-INVENTORY-001, and grade the
`machine` column by whether the named machine actually BINDS its constraint.

WHY THIS SCRIPT EXISTS
----------------------
`-42` built the inventory and wrote a `machine` column. `-43` read that column as
coverage — "nine of the fifty already had a machine, all of them incidental" — and
concluded that the cell *"a machine could recognise this and nobody wrote one"* was
EMPTY. `-44` audited the column instead of reading it, one named test at a time, against
one question:

    if the constraint were violated, would this named test necessarily go RED?

Sixteen of the eighteen incidental entries answer NO or NOT-QUITE. So the `machine`
column was never a coverage column; it was an ADJACENCY column wearing a coverage
column's clothes, and the emptiness of the third cell was an artifact of reading it.

WHAT THIS SCRIPT CHANGES
------------------------
Two mechanical edits to `docs/preregistration/CONSTRAINT-INVENTORY-001.md` §1's table:

  1. a new `recog` column, between `verdict` and `machine`, carrying one of
     MECH / PROXY / READER / n/a — a property of the CONSTRAINT. (It sits beside the
     machine grade because that pairing is the whole point. The first cut of this
     script announced the column in the header one position to the LEFT of where it
     inserted the cells, and every row was silently misaligned — caught by recomputing
     the counts, not by reading the table. `-35`'s tell, on this pass: the defect you
     are about to introduce. `tests/test_constraint_inventory_selfconsistent.py`
     asserts header-and-cell agreement so the next one cannot be silent.)
  2. a grade prefix on the `machine` cell — FOR / BINDS / PARTIAL / ADJACENT —
     a property of the ESTATE.

Keeping them in two columns is the point of the pass. `-43`'s three cells fused them:
"has a machine" is not a recognisability grade, and the fusion is what made a column of
adjacencies read as a column of guards.

Three pointer corrections ride along, all found by the same audit:
  * C40's machine was the wrong test entirely. `test_term002_count.py` is about §8's
    free-parameter refusal numeral and never opens §4.7. The real binder is
    `test_reg012_sec6_sec47_frozen.py`, whose §4.7 freeze span contains the clause.
  * C42's two named tests pin three of its fifteen numbers. `test_reg009_ladder_inputs.py`
    pins four more and is not named.
  * C47 and C50 cite the wrong section (`REG-012` §4, not §5; `SOURCE-001` §3, not §5).

REVERSIBILITY: a `.bak-pre-wt111` copy is written first. Note that `*.bak*` is ignored by
`~/.gitignore_global` and is therefore NOT the evidence — `tests/test_constraint_inventory_selfconsistent.py`
is (the `-42` bug-spray tell, applied to this pass).

IDEMPOTENCE: re-running is a no-op. The script refuses if the table has already been
graded, so the record of the edit stays honest.
"""
from __future__ import annotations

import pathlib
import re
import shutil
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
DOC = ROOT / "docs" / "preregistration" / "CONSTRAINT-INVENTORY-001.md"

# --- the two grades, per constraint -----------------------------------------------
#
# recog  — can a MACHINE decide compliance from artifacts committed to this repo?
#   MECH   : yes. every fact the constraint turns on is in a file a test can open.
#   PROXY  : only a necessary condition is decidable. the constraint's core is a
#            judgement about what a sentence is DOING (attributing, headlining,
#            reopening, choosing) and a machine can only check a shadow of it.
#   READER : no. only a reader.
#   n/a    : not live — the antecedent did not fire, so there is nothing to recognise.
#
# binding — does the named machine go RED when the constraint is violated?
#   FOR      : a guard written FOR this constraint.
#   BINDS    : incidental, but a violation necessarily reddens it.
#   PARTIAL  : one limb binds; at least one limb of the constraint escapes.
#   ADJACENT : named in the column, and a violation can leave it green.
#   ""       : no machine named.
#
# every PARTIAL and ADJACENT below was established by reading the named test in full and
# constructing a concrete violation that survives it. those constructions are recorded in
# §3 of the inventory, not here.
GRADES: dict[str, tuple[str, str]] = {
    "C01": ("MECH", ""),
    "C02": ("MECH", ""),
    "C03": ("MECH", ""),
    "C04": ("MECH", ""),
    "C05": ("READER", ""),
    "C06": ("MECH", ""),
    "C07": ("MECH", "ADJACENT"),
    "C08": ("n/a", ""),
    "C09": ("PROXY", ""),
    "C10": ("MECH", ""),
    "C11": ("PROXY", "ADJACENT"),
    "C12": ("MECH", "FOR"),
    "C13": ("n/a", ""),
    "C14": ("MECH", ""),
    "C15": ("MECH", "FOR"),
    "C16": ("MECH", ""),
    "C17": ("PROXY", ""),
    "C18": ("READER", ""),
    "C19": ("MECH", "FOR"),
    "C20": ("MECH", ""),
    "C21": ("MECH", "FOR"),
    "C22": ("MECH", ""),
    "C23": ("MECH", ""),
    "C24": ("MECH", "FOR"),
    "C25": ("MECH", ""),
    "C26": ("MECH", ""),
    "C27": ("MECH", ""),
    "C28": ("n/a", ""),
    "C29": ("n/a", ""),
    "C30": ("MECH", ""),
    "C31": ("PROXY", ""),
    "C32": ("MECH", "ADJACENT"),
    "C33": ("MECH", ""),
    "C34": ("MECH", "ADJACENT"),
    "C35": ("MECH", "BINDS"),
    "C36": ("READER", ""),
    "C37": ("PROXY", "ADJACENT"),
    "C38": ("MECH", "PARTIAL"),
    "C39": ("PROXY", "ADJACENT"),
    "C40": ("MECH", "BINDS"),
    "C41": ("PROXY", "PARTIAL"),
    "C42": ("MECH", "PARTIAL"),
    "C43": ("MECH", "PARTIAL"),
    "C44": ("MECH", "PARTIAL"),
    "C45": ("MECH", "ADJACENT"),
    "C46": ("PROXY", "PARTIAL"),
    "C47": ("MECH", "BINDS"),
    "C48": ("MECH", "FOR"),
    "C49": ("MECH", "FOR"),
    "C50": ("MECH", "ADJACENT"),
}

# --- pointer corrections ----------------------------------------------------------
# (constraint, exact old substring, new substring). all three are wrong-pointer defects
# found by the audit; none of them changes a verdict about the manuscript.
POINTER_FIXES: list[tuple[str, str, str]] = [
    (
        "C40",
        "`test_term002_count.py`",
        "`test_reg012_sec6_sec47_frozen.py` — **not** `test_term002_count.py`, "
        "which is about §8's free-parameter numeral and never opens §4.7",
    ),
    (
        "C42",
        "`test_reg009_band_count.py`, `test_reg010_half_integer_banding.py`",
        "`test_reg009_ladder_inputs.py` (four numbers), `test_reg009_band_count.py` "
        "(three), `test_reg010_half_integer_banding.py`",
    ),
    ("C47", "`REG-012` §5", "`REG-012` §4"),
    ("C50", "`SOURCE-001` §5", "`SOURCE-001` §3"),
    (
        "C49",
        "`test_reg012_band_edge_phase.py`",
        "**`test_reg012_sec7_refusal_is_asserted.py`** (new, `-44`, the *presence* "
        "limb) + `test_reg012_band_edge_phase.py` (the *absence* limb)",
    ),
]

#: One verdict cell changes, because one audit finding was repaired in the same session
#: rather than recorded: C49's guard could not distinguish a refusal from a silence, and
#: `tests/test_reg012_sec7_refusal_is_asserted.py` is the presence limb that can.
#: Keeping it here rather than as a hand-edit is what lets this script reproduce the
#: committed file byte-for-byte from the `.bak`.
VERDICT_REWRITES: dict[str, tuple[str, str]] = {
    "C49": (
        "**compliant**; the distinction is load-bearing and named in `HANDOFF` §2",
        "**compliant** — but `-44` found the guard could not tell a refusal from a "
        "silence: both states have zero band counts and "
        "`test_reg012_band_edge_phase.py`'s assertion is an **absence**. Paired guard "
        "added",
    ),
}

HEADER_OLD = (
    "| # | source | the constraint | governed quantity | resolution | scope | live? "
    "| verdict | machine |"
)
HEADER_NEW = (
    "| # | source | the constraint | governed quantity | resolution | scope | live? "
    "| verdict | recog | machine |"
)
RULE_OLD = "|---|---|---|---|---|---|---|---|---|"
RULE_NEW = "|---|---|---|---|---|---|---|---|---|---|"

ROW = re.compile(r"^\| (C\d\d) \|")


def main() -> int:
    text = DOC.read_text(encoding="utf-8")

    if "| recog |" in text:
        print("wt111: already applied (the table carries a `recog` column) — no-op.")
        return 0
    if HEADER_OLD not in text:
        print("wt111: REFUSING — §1's header is not the one this script was written "
              "against. Re-read the table before editing it.", file=sys.stderr)
        return 2

    shutil.copy2(DOC, DOC.with_suffix(".md.bak-pre-wt111"))

    lines = text.split("\n")
    out: list[str] = []
    seen: set[str] = set()

    for line in lines:
        if line.strip() == HEADER_OLD:
            out.append(HEADER_NEW)
            continue
        if line.strip() == RULE_OLD:
            out.append(RULE_NEW)
            continue

        m = ROW.match(line)
        if not m:
            out.append(line)
            continue

        cid = m.group(1)
        if cid not in GRADES:
            print(f"wt111: REFUSING — {cid} has no grade.", file=sys.stderr)
            return 2
        seen.add(cid)
        recog, binding = GRADES[cid]

        # cells: trailing "|" makes a final empty field; keep the shape exactly.
        cells = line.split(" | ")
        if len(cells) != 9:
            print(f"wt111: REFUSING — {cid} has {len(cells)} cells, expected 9.",
                  file=sys.stderr)
            return 2

        if cid in VERDICT_REWRITES:
            was, now = VERDICT_REWRITES[cid]
            if was not in cells[7]:
                print(f"wt111: REFUSING — {cid}'s verdict is not the one this script "
                      f"was written against.", file=sys.stderr)
                return 2
            cells[7] = cells[7].replace(was, now)

        machine = cells[8].rstrip().rstrip("|").strip()
        for fix_cid, old, new in POINTER_FIXES:
            if fix_cid != cid:
                continue
            target = 1 if old in machine else (2 if old in cells[1] else 0)
            if target == 1:
                machine = machine.replace(old, new)
            elif target == 2:
                cells[1] = cells[1].replace(old, new)
            else:
                print(f"wt111: REFUSING — {cid}'s pointer fix did not match: {old!r}",
                      file=sys.stderr)
                return 2

        if binding:
            if machine.lower().startswith("none"):
                print(f"wt111: REFUSING — {cid} graded {binding} with no machine.",
                      file=sys.stderr)
                return 2
            machine = f"**{binding}** · {machine}"
        elif not machine.lower().startswith("none"):
            print(f"wt111: REFUSING — {cid} names a machine and carries no grade.",
                  file=sys.stderr)
            return 2

        cells[8] = machine
        out.append(" | ".join(cells[:8] + [recog] + cells[8:]) + " |")

    missing = sorted(set(GRADES) - seen)
    if missing:
        print(f"wt111: REFUSING — graded but not found in the table: {missing}",
              file=sys.stderr)
        return 2

    DOC.write_text("\n".join(out), encoding="utf-8")
    print(f"wt111: graded {len(seen)} rows; `recog` column added; "
          f"{len(POINTER_FIXES)} pointer corrections applied.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
