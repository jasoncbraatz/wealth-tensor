# REFERENCE-POLICY · what this project does when it cites something

*Portable by design. Nothing below is specific to `wealth-tensor` — it is written to be copied into
the next project unchanged. Written 2026-08-11, session `wealthTensor-10`, prompted by a question
the author asked out loud: **"is there a way to cite what's publicly available online?"***

*The short answer is yes, it is the norm, and the long answer is this document.*

---

## 0 · Why this exists

The author reads papers the way most people in economics and finance read papers: on preprint
servers, in working-paper archives, in institutional repositories, and — sometimes — as a quotation
in a forum thread that led to the paper in the first place. He is not an academic, holds no
institutional subscription, and has correctly observed that paying $39.95 for the privilege of
*correctly crediting somebody else's work* is a strange arrangement.

None of that is a defect. **Reading the preprint is not the offence. Calling the preprint the
journal is.** This document draws that line precisely enough to work from, and then gives the
machinery that enforces it.

It also exists because this project keeps finding the same animal in new costumes. See
`METHOD-001-the-phantom-tag.md` §5 for the family portrait.

---

## 1 · The three acts, and their evidentiary requirements

Most citation confusion dissolves once you notice that "citing a paper" is three different acts with
three different requirements. Almost every real citation failure is one act performed with the
evidence for a weaker one.

| act | what you are doing | what you must have |
|---|---|---|
| **CITE** | pointing at a work so a reader can find it | **nothing but a correct bibliographic record.** You may cite a work you have never opened. A citation is a signpost, not an affidavit. |
| **CHARACTERIZE** | saying what a work found, argued, assumed or concluded | **evidence that reaches the claim.** An abstract fully licenses abstract-level claims. It licenses nothing about mechanism, sample, design, or what the paper considered and set aside. |
| **QUOTE** | reproducing its words | **the text itself, and the identity of the version you read.** |

### The rule that follows

> **An abstract is a legitimate source for what an abstract contains.**
> The failure is never *using* one. The failure is letting one carry weight it cannot hold.

Concretely, from this project's own reading:

- ✅ *"Kim & Zhang (2016) find that conditional conservatism is associated with a lower likelihood of
  future crashes."* — the abstract says exactly this.
- ❌ *"Kim & Zhang's mechanism is contemporaneous rather than accumulative."* — true, verified, and
  **only** knowable from the body. Claiming it from the abstract would have been luck, not method.
- ✅ *"Zhu (2016) explains the accrual–crash relation by bad-news hoarding reaching a tipping point."*
  — the author's own abstract, verbatim, in his own words.
- ❌ *"Zhu (2016) does not consider a no-informed-party mechanism."* — the abstract cannot establish
  an absence. Absences require the body.

**Absence claims are the sharpest case and deserve their own line: an abstract can never establish
that something is *not* in a paper.** Every zero-hit table this project has published came from
`grep` over an extracted full text, and that is the only thing that licenses one.

### Honest secondhand

When you are relying on someone else's description of a work you have not read, say so. The
machinery is old and standard:

> Ryan (1995), as cited in Beaver & Ryan (2000).

It is mildly unglamorous and entirely correct, which is the right trade every time. A reader who
knows your chain of custody can evaluate it. A reader who doesn't, can't.

---

## 2 · The forum lead

A quotation found in a forum thread, a blog post, a Substack, a Reddit comment or a
ResearchGate discussion is **a lead, not a source.**

Not because those places are disreputable — several of the best pointers in this project came from
exactly there, and the open discussion of research in public is a genuine improvement on 1993. But a
quotation in the wild has passed through an unknown number of hands, and each one may have
truncated it, paraphrased it inside quotation marks, silently modernised its spelling, or taken it
from a different version than the one it names.

> **A forum find tells you where to look. It never tells you what is there.**

Treat it exactly as you treat a handwritten note in the everything folder: **read it back against the
source before building on it.** Same rule, same reason, and this project has burned itself on both.

---

## 3 · The five passes

Each pass asks a question the previous ones structurally *cannot* answer. That is why they are
ordered, and why a clean earlier pass is not evidence for a later one.

| # | pass | the question it asks | what it cannot see |
|---|---|---|---|
| 1 | **Bibliographic** | *Does this work exist with these details?* | whether the reference does any work |
| 2 | **Cited-in-text** | *Does this reference do any work in the body?* | whether it points at the object read |
| 3 | **Provenance** | *Is this the object the claim is about, and the one that was read?* | whether the text read is the text of record |
| 4 | **Version** | *Is the text I quoted the text of record?* | whether it was read at all |
| 5 | **Read-status** | *Was this work read at source — and if not, does every claim made of it stay inside what was?* | — |

**Pass 5 is new, added 2026-08-11, and it exists because passes 1–4 are all silently satisfied by a
work nobody ever opened.** Such a work exists (pass 1 ✅), is cited in the body (pass 2 ✅), is
trivially "the object" since no other object is in play (pass 3 ✅), and raises no version question
because nothing was quoted (pass 4 ✅). It sails through the whole apparatus. Pass 5 is the only one
that asks the obvious question, which is exactly the pattern METHOD-001 documents: **the defect hides
in the question nobody thought to ask, not in the answers.**

### The order is the lesson

A clean bibliographic pass is not evidence of a correct citation; it is evidence of a correct
*bibliography*. Those are two different documents that happen to share a page. Each subsequent pass
is that same observation, one step further in.

---

## 4 · The marks

Every reference entry carries one. The mark is a **read-status disclosure**, not a quality grade.

| mark | meaning |
|---|---|
| **✓** | Checked against a publisher page, library catalogue, Crossref record or the issuing body's own documentation. Not recalled. |
| **✓✎** | Additionally checked against **the author's own copy**, by reading that copy's title page and colophon. |
| **✓⧗** | Bibliographically verified, but the **text** consulted is a pre-publication version. Any quotation is attributed to the version read and may not appear in the article of record. Dual-dated `consulted/published`. |
| **✓◐** | *(new, 2026-08-11)* Bibliographically verified; **the work has not been read at source.** Every claim the paper makes of it is one the author's own abstract states, in the author's own words, and nothing more. No quotation from the body. No absence claim. |

**✓◐ is the direct answer to the question that prompted this document.** Yes, you may cite from an
abstract — and this is the mark that says so out loud, in the reference list, where a reader can see
it and discount accordingly. It converts a silent weakness into a disclosed one.

Note the symmetry, because it is the reusable part: the author's last question about his own reading
habits produced the **fourth pass**. This one produced the **fifth mark**. *A researcher who
interrogates his own method is a better instrument than any checklist written for him.*

### The pre-publication rule, stated once

Where the copy read was a working paper or accepted manuscript rather than the typeset article:

1. **Cite the RESULT to the published article.** That is the article of record; that is what was
   refereed; that is what a reader should go get. Volume, issue, pages, DOI.
2. **Attribute the QUOTATION to the version actually read.** Not the journal.
3. **Dual-date** `consulted/published`.
4. **Say the sentence may not appear in the article of record**, because you do not know that it does.

### Pagination

**A green-OA or accepted-manuscript PDF may carry the publisher's own typesetting and still have the
wrong page numbers.** This project has hit it twice. If the copy's pagination does not match the
issue's:

- cite the **issue's** pagination in the reference entry,
- quote **without page numbers**, and
- **say why**, in the entry.

An invented page number is worse than no page number, because it is checkable and wrong.

---

## 5 · The access playbook — free, legal, ranked by time saved

Run these before concluding a work is unreachable. This project has recovered full texts through
routes 1, 3 and 5 that four commercial aggregators reported as "closed."

1. **The author's institutional repository.** Green OA, legitimate, usually the accepted manuscript.
   SMU InK, CityU Scholars, university `eprints`/`IDEALS`/Pure instances. *This is the single highest
   hit rate for post-2000 work in accounting and finance.*
2. **CORE (`core.ac.uk`).** Harvests those repositories and serves them at
   `https://core.ac.uk/download/<id>.pdf` — **which `curl` can fetch even when the origin repository
   is behind a bot wall.** Note: the CORE *web UI* may 403 while the `/download/` endpoint works.
   Neighbouring IDs are often neighbouring deposits from the same repository, which is a legitimate
   and very fast way to find a companion paper.
3. **Unpaywall** (`api.unpaywall.org/v2/{DOI}?email=…`). Free, fast, authoritative when it says yes.
   **Not authoritative when it says no** — this project has twice downloaded a legitimate repository
   copy of a work Unpaywall reported as `closed` with zero locations.
4. **SSRN / NBER / arXiv / RePEc.** The preprint layer. Free. Frequently Cloudflare-gated against
   `curl`, and fine in a browser.
5. **JSTOR, free personal account.** 100 articles per 30 days, **read online in the browser** — no
   PDF download (that is JPASS, paid). This is the route for pre-1997 journal content that predates
   the preprint era and has no repository copy anywhere. It is often the *only* route.
6. **Email the author.** Legal, free, and it works. Authors may share their own work for scholarly
   purposes and are generally pleased to be asked. An independent researcher writing to say *"I am
   building on your model and I want to get it right"* is the best email an academic gets that week.
7. **Public library card.** Many systems include JSTOR or EBSCO, and most will do interlibrary loan
   on a journal article for free.
8. **Alumni library privileges**, if applicable.

**Not used, ever:** sci-hub, libgen, and unauthorized re-uploads of publisher PDFs to commercial
academic social networks. Not primarily a legal position — a practical one. A copy of unknown
provenance cannot discharge pass 3 or pass 4, so it fails this project's own apparatus before it
fails anyone else's rules.

### When a work is genuinely unreachable

It happens, and the honest handling is short:

- **Do not cite it from a summary.** Not from an agent, not from a citing paper's characterization,
  not from an indexer's abstract.
- **Either** cite it ✓◐ with a claim its own abstract carries, **or** leave it out.
- **Never** let it support an absence claim, a priority claim, or a distinction.
- **Record the attempt.** A reader benefits from knowing a source was sought and not reached; that is
  information about the state of the field, not an admission.

---

## 6 · Two hazards specific to machine-assisted reading

**An adversarial or research agent is a retrieval pipeline in a better suit.** Its most damaging
claim gets verified by hand, mechanically, against a source, before it enters any document.
Demand a *"WHAT I COULD NOT ACCESS"* section and read it first — it is reliably the most honest part
of the report.

**An indexer-supplied abstract may be a fabrication of the index, not of the author.** Many journals
did not print abstracts before the late 1990s. Aggregators synthesize one anyway, sometimes by
welding the opening paragraph onto whatever front matter exists. If a pre-1997 paper has an
"abstract" that visibly restarts its own framing mid-way, that is what happened. **An abstract
credited to a paper that never had one is the phantom tag in a fourth medium** — see METHOD-001 §5.

---

## 7 · The checklist

Before any work enters a reference list:

- [ ] **Pass 1** — record verified against a publisher page, catalogue, Crossref or issuing body.
- [ ] **Pass 2** — the entry does actual work in the body. If not, remove it; do not retro-fit.
- [ ] **Pass 3** — the copy consulted is the object the claim is about.
- [ ] **Pass 4** — if quoted, the version quoted is named; `consulted/published` if pre-publication.
- [ ] **Pass 5** — read-status is honest, and every claim stays inside the evidence that reaches it.
- [ ] **Mark assigned** — ✓ / ✓✎ / ✓⧗ / ✓◐.
- [ ] **No absence claim** rests on anything but an extracted full text.
- [ ] **No page number** that was not seen on a page.
- [ ] **No quotation** sourced from a forum, a summary, or an agent without verification at source.

Nine boxes. Most entries tick all nine in under a minute. The ones that don't are the ones worth the
time.

---

*This document is public for the same reason the rest of `docs/` is: a reader who can see how the
citations were checked can decide how much to trust them. A reference list that silently improves
teaches nobody anything.*
