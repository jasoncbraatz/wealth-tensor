# -*- coding: utf-8 -*-

_LEGEND_NEW = """***How to read this list.* The edition cited is the edition *consulted* — the copy in the author's
possession — not the earliest printing a catalogue happens to list. Where the original's date does
argumentative work, because the entry is a translation or because a claim about priority rests on
it, the entry is **dual-dated** `original/consulted`. A reprint that changes no pagination is a
*printing*, not an edition, and is not dual-dated. Where the copy read was a working paper or an
accepted manuscript rather than the typeset article of record, the entry is dual-dated in the other
direction — `consulted/published`.**

*Each entry carries a mark recording how far verification reached, because a bibliographic record
and a text are different objects: a work can exist exactly as cited and still not contain the
sentence attributed to it. Bibliographic verification was carried out on 2026-08-10, and the
crash-risk entries were added on 2026-08-11. Per-entry findings are in the note attached to the
entry they describe.*

**✓** — checked against a publisher page, a library-catalogue record, a Crossref record or the
issuing body's own documentation, not recalled. **✓✎** — additionally checked against **the
author's own copy**, by reading that copy's title page and colophon. The ✓✎ entries are the ones
where doing so changed the citation. **✓⧗** — bibliographically verified, but the **text**
consulted is a pre-publication version; any quotation is attributed to the version read and may not
appear in the article of record; three entries carry it. **⧗** *alone* — the bibliographic record
is verified and the **text was not read**; the characterisation rests on named secondary sources,
and the entry says so in its own note. Three entries carry it. Two entries carry **no mark at
all**, each stating in its own note why it is unmarked, and those two are the only unmarked entries
in the list."""
EDITS = [
('IIIb-e01', 'C-e', 'for the same reason this paper ships\nwith `REVIEW-001`: an argument is easier to judge when its objections are in the room.', 'for the same reason this paper ships with an adversarial\nreferee report on itself (§11): an argument is easier to judge when its objections are in the room.'),
('IIIb-e02', 'C-e', ' Until wealthTensor-80 six of them were printed by none,\n  and this bullet said "three tables" of a command that printed four.', ''),
('IIIb-e03', 'C-e', ' Until wealthTensor-101 this section named no\n  command for §4.10 and the manuscript named that script only as the bare token `wt091`.', ''),
('IIIb-e04', 'C-e', 'committed data, and this bullet implied otherwise until wealthTensor-80.', 'committed data.'),
('IIIb-e05', 'C-e', ' This bullet\n  promised a per-tier breakdown until wealthTensor-82.', ''),
('IIIb-b01', 'C-b', '**That command reproduces the instrument and not the\n  sample, and the distinction is the whole of this bullet.**', '**That command reproduces the instrument and not the\n  sample.**'),
('IIIb-b03', 'C-b', '\n  This sentence read "three" from the day it was written, which was two days after the last three\n  landed.', ''),
('IIIb-b04', 'C-b', 'A submission-time head-of-repository SHA will be pinned when this paper is posted; the per-file\n  pins are what a replicator needs and are verifiable now.', 'No head-of-repository SHA is pinned; the per-file\n  pins above are what a replicator needs, and each is verifiable now.'),
('IIIb-b05', 'C-b', 'This material\nmotivated the filter and is retained in full: it states', 'This material\nmotivated the filter: it states'),
('IIIb-b06', 'C-b', 'The earlier drafts of this work appealed to "first principles" repeatedly and defined the term\nzero times. The gap was not a wording problem, and several attempts to fix it by rewording failed\nfor a reason worth stating, because it is a type error and type errors do not respond to prose:', 'An appeal to "first principles" is worthless without a definition of the term, and the gap is not\na wording problem — it is a type error, and type errors do not respond to prose:'),
('IIIb-b08', 'C-b', 'An earlier version of this aside added that\nthe mechanism was **the same**. That identification is withdrawn. Put to a cross-scale check it\ndoes not hold:', 'The identification of the two mechanisms that the\nshared theme invites is withdrawn. Put to a cross-scale check it does not hold:'),
('IIIb-b09', 'C-b', '; that this appendix still carried the withdrawn\nidentification after the check had run is recorded in `docs/RESULT-END-TO-END-001-E3.md`.*', '.*'),
('IIIb-b10', 'C-b', '*This section is where Λ is defended. It is defended here, at full strength, on three independent\nlegs, and then it is used for the rest of the paper without further apology. That is a deliberate\nposture and it is worth naming: a defence that recurs is a tell. Five defences of one quantity\ninform a referee that there are five soft places, and recruit attention to precisely the ground an\nauthor would rather they walked over.*', '*This section defends Λ, at full strength and on three independent legs; the rest of the paper\nthen uses it without re-arguing it.*'),
('IIIb-b11', 'C-b', "**Notation, stated before the argument because two different objects have been sharing one symbol\nin this programme's working notes.** Write", '**Notation, stated before the argument because two different objects are easily conflated under\none symbol.** Write'),
('IIIb-b12', 'C-b', 'Conflating them is easy and this paper has done it before. Everything below', 'Conflating them is easy. Everything below'),
('IIIb-b14', 'C-b', 'and the difference is exactly the kind of thing §6.2 will show this programme has previously\nglossed over at its cost.', 'and the difference is exactly the kind §6.2 is about.'),
('IIIb-b17', 'C-b', '**And it is a weaker leg than §A.2.3, which should be said plainly rather than left to a referee.**', "**This leg is weaker than §A.2.3's.**"),
('IIIb-b18', 'C-b', '(The shorter horizon is inherited from the\nverifier this figure comes from and is stated because it changes the values:', '(The shorter horizon is stated because it changes the values:'),
('IIIb-b19', 'C-b', 'is the free parameter this programme has refused three times in other costumes. So the claim is not', 'is a free parameter. So the claim is not'),
('IIIb-b24', 'C-b', 'article, which earlier revisions of this entry could not obtain. Nothing is quoted from it.)*', 'article. Nothing is quoted from it.)*'),
('IIIb-b25', 'C-b', '**Read at\nsource** in this revision and the characterisation held:', '**Read at\nsource**, and the characterisation held:'),
('IIIb-b26', 'C-b', " A session with\nlibrary access should read the monograph, and Askari and Cummings's 1977 survey of the Nerlove\nliterature, before this is upgraded.", ''),
('IIIb-b27', 'C-b', '; an earlier revision of this entry recorded it as checked only\nagainst NBER Working Paper 10453 and flagged the risk that the referee process had altered it. It\nhad not.', ', and unchanged from NBER Working Paper 10453.'),
('IIIb-b28', 'C-b', 'An earlier draft of\nthis list cited Mayo (2018),* Statistical Inference as Severe Testing *— a later restatement the author\nhas not read.', 'Mayo (2018),* Statistical Inference as Severe Testing *— a later restatement — has not been\nread.'),
('IIIb-e07', 'C-e', ' This entry\nwas re-pointed away to* Environment, Power, and Society *(Columbia, 2007) when the first library sweep\ndid not find the 1996 book, then restored when it did. The sweep, not the citation, was wrong — see\nWT-062.', ' This entry\nwas re-pointed away to* Environment, Power, and Society *(Columbia, 2007) when the first library sweep\ndid not find the 1996 book, then restored when it did. The sweep, not the citation, was wrong.'),
]
