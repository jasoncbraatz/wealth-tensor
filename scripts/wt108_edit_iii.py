#!/usr/bin/env python3
"""wealthTensor-108 -- paper-III-v1.md, one pass.

(1) 13 orphan reference entries deleted (the v1 rebuild cut the sections that cited them).
(2) 3 lost attributions restored in the body (Mayo, Nosek, Godley & Lavoie) and their entries kept.
(3) 4 stale "Cited in SSN.M" claims remapped to where the body actually names the work.
(4) Appendix A.4 added -- paper IV's SMD-as-boundary argument, landed on P3.
(5) 6 reference entries added for A.4, each verified against Crossref or the publisher's page.
(6) The reference preamble's crash-risk sentence removed with the crash-risk entries.
"""
import re, pathlib, sys

P = pathlib.Path("docs/papers/paper-III-dual-tensor/paper-III-v1.md")
src = P.read_text(encoding="utf-8")
orig = src

def once(old, new, label):
    global src
    n = src.count(old)
    if n != 1:
        sys.exit("ABORT %s: anchor occurs %d times, expected 1" % (label, n))
    src = src.replace(old, new, 1)
    print("  ok  %s" % label)

# ---------------------------------------------------------------- (2) Mayo + Nosek
once(
 "the instrument below measures a substitute.",
 "the instrument below measures a substitute. **\"Severe\" is Mayo's (1996) word and is used in her\n"
 "sense** -- a test that would very probably have caught the prediction being wrong had it been\n"
 "wrong -- and what makes this one severe rather than merely early is the registration discipline of\n"
 "Nosek, Ebersole, DeHaven and Mellor (2018): the prediction, the instrument and the falsifiers were\n"
 "committed and pushed before the data were touched.",
 "9-preamble: Mayo + Nosek")

# ---------------------------------------------------------------- (2) Godley & Lavoie
once(
 "**On stock-flow-consistent modelling.** The two-layer structure is not new as a structure; what is new is\n"
 "treating the wedge between the layers as an *information* quantity with a release rate, and proving what\n"
 "that structure does to identification.",
 "**On stock-flow-consistent modelling.** The two-layer structure is not new as a structure -- it is\n"
 "Godley and Lavoie's (2007), where every flow has a source and every stock a counterpart and the\n"
 "accounting closes by construction. What is new is treating the wedge *between* the layers as an\n"
 "*information* quantity with a release rate, and proving what that structure does to identification.",
 "12: Godley & Lavoie")

# ---------------------------------------------------------------- (3) cited-in remaps
assert src.count("(Cited in §5.2 for") == 3, src.count("(Cited in §5.2 for")
src = src.replace("(Cited in §5.2 for", "(Cited in §6 for")
print("  ok  cited-in: 5.2 -> 6 (Fisher, Kay, Long)")
once("(Cited in §7 for the", "(Cited in §7.3 for the", "cited-in: 7 -> 7.3 (Ryan 1995)")

# ---------------------------------------------------------------- (6) preamble sentence
once(" Bibliographic verification was carried out on 2026-08-10, and the\ncrash-risk entries were added on 2026-08-11.",
     " Bibliographic verification was carried out on 2026-08-10;\n"
     "the six aggregation entries §A.4 rests on were verified on 2026-08-26.",
     "refs preamble: crash-risk sentence retired")

# ---------------------------------------------------------------- (4) Appendix A.4
A4 = """## A.4 · The boundary on P3, and it is a fifty-year-old theorem

P3 is the proposition a competent economist attacks, and the attack has a name. Sonnenschein (1972,
1973), Mantel (1974) and Debreu (1974) proved that aggregate excess demand inherits from
individually rational agents only continuity, homogeneity of degree zero and Walras's Law -- not
downward slope, not uniqueness, not stability. Aggregate demand can take essentially arbitrary
shape. **The best-established result about aggregation in economics is that aggregation destroys
structure**, and a proposition asserting that measured aggregates are folds over units owes it an
answer rather than a citation.

The answer is one distinction, and it is not a hedge.

> **SMD is a theorem about maps. P3 is a claim about states.**

What SMD constrains is the aggregate excess demand *function* -- an object taking prices and
returning quantities, assembled from individual demand functions -- and what it establishes is that
essentially nothing about the individual functions survives the assembly. What P3 asserts folds is
the extensive **state**: how much physical stock is held, how much claim is recorded against it, and
at what rate each moves. Summing steel is not summing preferences. The two claims are therefore not
in tension. They are complementary halves of one statement, and the conjunction is sharper than
either half alone:

> **Aggregation preserves the extensive state and destroys the behavioural map.**

SMD is the second clause, proved fifty years ago inside the mainstream. P3 is the first. What makes
the pair worth having is that it sorts measurements by what they can carry. A discipline that
aggregates in order to recover behaviour -- a technology from a production function, a propensity
from a consumption function, an elasticity from a demand curve -- is estimating the object that does
not survive the sum. The standard response has been to impose enough distributional structure on the
population that the aggregate is well-behaved (Hildenbrand, 1994; Grandmont, 1992), which is a
legitimate research strategy and is also an admission that the structure is imposed rather than
inherited.

**Three limits on that answer, and the third is this paper's own result.**

1. **A state that folds is not thereby a state anyone can observe.** Folding is a property of the
   object; observability is a property of the measuring layer -- and §§2–9 are about a measuring layer
   failing to see something, as is Paper II. This framework's own results are the reason to doubt
   that the folded state is available to anyone.
2. **"Extensive" is doing real work, and rates are not extensive.** δ, φ and α do not fold by
   addition. They fold, where they fold at all, as weighted combinations whose weights are themselves
   state -- which is exactly why **§5's cross-class ladder reads the composite (1 − φ) ⊙ δ rather than
   φ**, and why ranking by the parameter can invert the ordering rather than blur it. §5 is what P3
   looks like when the rate is forgotten.
3. **Diagonality across classes within a firm-quarter is assumed, and §9.5 rejects it.** The fold is
   *degraded* at precisely the scale where the accounting is done -- degraded rather than severed,
   because what was rejected is a property of the reporting filter and not of the extensive state,
   and because the departure is now a measured quantity rather than an open exposure. What is not
   available is its cause: the design cannot say whether the coupling is economic or an artefact of
   the order the standards impose on the tests.

*This section is the surviving argument of a fourth manuscript, written and not carried forward;
`docs/papers/README-v1.md` records why, and `docs/papers/paper-IV-composition/paper-IV.md` carries
its own header saying where each of its three surviving parts went.*

---

"""
once("# Supplementary material", A4 + "# Supplementary material", "Appendix A.4 inserted")

# ---------------------------------------------------------------- (1) + (5) references
r0 = src.index("\n## References\n")
head, refs = src[:r0], src[r0:]

DROP_PREFIXES = [
 "Andreou, P. C., Lambertides",
 "Elbers, C., & Ridder, G. (1982)",
 "Fama, E. F. (1970)",
 "Hayek, F. A. (1945)",
 "Little, J. D. C. (1961)",
 "Hutton, A. P., Marcus, A. J.",
 "Jin, L., & Myers, S. C. (2006)",
 "Mann, H. B., & Whitney, D. R. (1947)",
 "Mayo, D. G., & Spanos, A.",
 "Mises, L. von (1949/1998)",
 "Piketty, T. (2013/2014)",
 "Popper, K. R. (1935/2002)",
 "Zhu, W. (2016)",
]

NEW = {
 "Bushman, R. M., & Williams, C. D. (2015)":
   "Debreu, G. (1974). Excess demand functions. *Journal of Mathematical Economics*, 1(1), 15–21. ✓\n"
   "*(§A.4 cites it as one of the three SMD papers, for the theorem and not for a passage. Crossref\n"
   "record verified; nothing is quoted.)*",
 "Georgescu-Roegen, N. (1971)":
   "Grandmont, J.-M. (1992). Transformations of the commodity space, behavioral heterogeneity, and the\n"
   "aggregation problem. *Journal of Economic Theory*, 57(1), 1–35. ✓ *(§A.4 cites it, with\n"
   "Hildenbrand (1994), for the strategy of restoring aggregate regularity by restricting the\n"
   "population's heterogeneity. Crossref record verified; the **text was not read**, and the\n"
   "characterisation claims no more than the title states.)*",
 "Godley, W., & Lavoie, M. (2007)":
   "Hildenbrand, W. (1994). *Market Demand: Theory and Empirical Evidence*. Princeton University Press.\n"
   "✓ *(Frontiers of Economic Research series; verified against the publisher's own page. §A.4 cites it\n"
   "for the dispersion-of-characteristics route to a well-behaved aggregate. The **text was not\n"
   "read**.)*",
 "Marshall, A. W., & Proschan, F. (1972)":
   "Mantel, R. R. (1974). On the characterization of aggregate excess demand. *Journal of Economic\n"
   "Theory*, 7(3), 348–353. ✓ *(§A.4; Crossref record verified, nothing quoted.)*",
 "Soddy, F. (1926/1961)":
   "Sonnenschein, H. (1972). Market excess demand functions. *Econometrica*, 40(3), 549–563. ✓\n"
   "*(§A.4; Crossref record verified, nothing quoted.)*\n\n"
   "Sonnenschein, H. (1973). Do Walras' identity and continuity characterize the class of community\n"
   "excess demand functions? *Journal of Economic Theory*, 6(4), 345–354. ✓ *(§A.4; Crossref record\n"
   "verified, nothing quoted.)*",
}

paras = refs.split("\n\n")
out, dropped, added = [], [], []
for pa in paras:
    s = pa.strip()
    if any(s.startswith(pref) for pref in DROP_PREFIXES):
        dropped.append(s.split(".")[0])
        continue
    out.append(pa)
    for anchor, entry in NEW.items():
        if s.startswith(anchor):
            out.append(entry)
            added.append(entry.split(".")[0])
refs = "\n\n".join(out)
src = head + refs

print("  dropped %d entries: %s" % (len(dropped), ", ".join(dropped)))
print("  added   %d anchors: %s" % (len(added), ", ".join(added)))
if len(dropped) != 13:
    sys.exit("ABORT: expected 13 drops, got %d" % len(dropped))
if len(added) != 5:
    sys.exit("ABORT: expected 5 insertion anchors, got %d" % len(added))

P.write_text(src, encoding="utf-8")
print("written: %s  (%d -> %d lines)" % (P, orig.count("\n"), src.count("\n")))
