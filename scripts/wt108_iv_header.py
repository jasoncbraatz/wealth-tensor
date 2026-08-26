import pathlib, sys
P = pathlib.Path("docs/papers/paper-IV-composition/paper-IV.md")
s = P.read_text(encoding="utf-8")
anchor = "# The tensor composes, the behaviour does not: one atomic unit at the household, firm and sovereign scales\n"
if s.count(anchor) != 1:
    sys.exit("ABORT: title anchor count %d" % s.count(anchor))
hdr = """> ## ⛔ STOOD DOWN — do not cite, do not edit. This paper is not carried forward.
>
> **Decided at wealthTensor-107, executed at wealthTensor-108 (2026-08-26).** This manuscript's
> thesis is that the three scales are one structure. The corpus's own end-to-end check,
> `docs/RESULT-END-TO-END-001-E1.md`, demoted that to *"one question asked three times."* The
> paper is left here intact, at v0.2, as the record of an argument that was made and withdrawn —
> which `docs/ADR-001-paper-decomposition.md` and `docs/METHOD-001-the-phantom-tag.md` are the
> house precedent for keeping in public.
>
> **Its three surviving parts went here:**
>
> | part | was | is now |
> |---|---|---|
> | The SMD-as-boundary argument | §4 (4.1–4.4) | **Paper III, Appendix §A.4** — *"The boundary on P3, and it is a fifty-year-old theorem."* Landed on P3 (atomism), where the objection actually bites. Limit 2 is remapped to Paper III's own §5; limit 3 to its §9.5. The six aggregation references travelled with it and were re-verified against Crossref on 2026-08-26. |
> | The crossing-height instance | §5 | **`docs/RESULT-CROSSING-HEIGHT-001.md`** — retired from the papers, kept whole. It was *not* folded into Paper III §5.6: the two crossings share the word and no operator, and §0 of that file argues the refusal. |
> | The pre-registered citation-whitespace instrument | §6 | **`docs/METHOD-002-citation-whitespace.md`** — a standalone method note beside `METHOD-001`. Not Paper III §13, which enumerates only the registrations producing Paper III's numbers; REG-013 produces none of them. |
>
> Nothing else here was moved. `test_excess_demand_is_monotone_here_so_this_is_not_an_SMD_result`
> outlives this manuscript and Paper II §7 says so. Sections numbered below are **this paper's own**
> and do not correspond to Paper III's post-rebuild numbering.

---

"""
P.write_text(hdr + s, encoding="utf-8")
print("header prepended;", len((hdr+s).split("\n")), "lines")
