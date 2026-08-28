#!/usr/bin/env python3
"""wealthTensor-110 · build the v2 review pair — voice pass + the figures, matched by name.

WHAT THIS MAKES
---------------
    docs/papers-v2/paper-II-redistribution/paper-II.md
    docs/papers-v2/paper-III-dual-tensor/paper-III.md

each of which is the corresponding **v1** manuscript (the cut whose arguments the author
kept) with two things done to it:

  1. `scripts/wt224_voice_pass.py` run over it -- the em-dash conversion voice-box's
     VOICE-SELF-REPORT.md prescribes, imported rather than re-implemented so there is one
     copy of those rules;
  2. an image embed inserted immediately above every "Figure N -- ..." caption, pointing at
     the vector PDF `scripts/wt223_figures_to_pdf.py` produced in `docs/figures/`.

WHY docs/papers-v2/ AND NOT docs/papers/
----------------------------------------
`docs/papers/*/` is the canonical corpus, and several registries walk it assuming ONE
manuscript per directory. More to the point, `docs/deliverable/LAYOUT-MANIFEST.json` is a
per-page, per-hash statement about the capture built from those four files, and P13e holds
it. A review pair that shares the directory is a review pair that can silently become the
thing under verification. So the v2 lives in its own root, build.sh takes WT_PAPERS_ROOT,
and the canonical capture is untouched by anything here.

HOW A FIGURE FINDS ITS CAPTION
------------------------------
By NAME, not by ordinal. The manuscripts number their figures per paper (paper II has a
Figure 1 and so does paper III) while `docs/figures/` numbers them once across both, so an
ordinal match would be a silent off-by-six. Instead the caption's title is slugified and
matched against the filename's slug, and either may be the shorter -- the generator truncates
long titles at 50 characters, and a caption may carry a subtitle the filename does not:

    > **Figure 2 — The identified set.**      ->  fig-02-the-identified-set-is-a-continuum

A prefix match in either direction counts, ANY OTHER OUTCOME IS A REFUSAL. Zero matches,
two matches, or a figure file nothing claims all stop the build, because the failure this
guards against is a paper that ships with the wrong picture under a caption -- which reads
as correct to everyone who is not holding both files open.

USAGE
    wt225_build_v2.py            build both, refuse on any unmatched figure or caption
    wt225_build_v2.py --check    match and report only; write nothing
"""
from __future__ import annotations

import argparse
import importlib.util
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
FIGDIR = ROOT / "docs" / "figures"
OUTROOT = ROOT / "docs" / "papers-v2"

PAIRS = [
    ("paper-II-redistribution", "paper-II-v1.md", "paper-II.md"),
    ("paper-III-dual-tensor", "paper-III-v1.md", "paper-III.md"),
]

CAPTION = re.compile(r"^\s*>?\s*\*\*Figure\s+(\d+)\s*[—-]\s*(.+?)\*\*")


def _load_voice_pass():
    spec = importlib.util.spec_from_file_location(
        "wt224", ROOT / "scripts" / "wt224_voice_pass.py"
    )
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def slug(text: str) -> str:
    text = re.sub(r"\*+|`|\$", "", text)
    text = text.replace("’", "").replace("'", "")
    return re.sub(r"-+", "-", re.sub(r"[^a-z0-9]+", "-", text.lower())).strip("-")


def figure_slugs() -> dict[str, str]:
    """filename -> its slug, for every vector figure on disk."""
    out = {}
    for f in sorted(FIGDIR.glob("fig-*.pdf")):
        m = re.match(r"fig-\d+-(.*)\.pdf$", f.name)
        if not m:
            raise SystemExit(f"REFUSED: {f.name} is not fig-NN-<slug>.pdf")
        out[f.name] = m.group(1)
    if not out:
        raise SystemExit(f"REFUSED: no figures in {FIGDIR} -- run scripts/wt223_figures_to_pdf.py")
    return out


def match_one(cap_slug: str, figs: dict[str, str], claimed: set[str]) -> str:
    hits = [
        name
        for name, fs in figs.items()
        if name not in claimed and (cap_slug.startswith(fs) or fs.startswith(cap_slug))
    ]
    if len(hits) == 1:
        return hits[0]
    if not hits:
        raise SystemExit(
            f"REFUSED: no figure file matches caption slug {cap_slug!r}.\n"
            f"         available: {sorted(set(figs.values()) )}"
        )
    raise SystemExit(f"REFUSED: caption slug {cap_slug!r} matches {len(hits)}: {hits}")


def build(check: bool) -> int:
    vp = _load_voice_pass()
    figs = figure_slugs()
    claimed: set[str] = set()
    total_caps = 0

    for d, src_name, dst_name in PAIRS:
        src = ROOT / "docs" / "papers" / d / src_name
        text = src.read_text(encoding="utf-8")
        log: list = []
        text = vp.convert_text(text, log, src.name)
        kinds: dict[str, int] = {}
        for k, *_ in log:
            kinds[k] = kinds.get(k, 0) + 1

        lines = text.split("\n")
        out: list[str] = []
        n_here = 0
        for ln in lines:
            m = CAPTION.match(ln)
            if m:
                cap_slug = slug(m.group(2).rstrip("."))
                fname = match_one(cap_slug, figs, claimed)
                claimed.add(fname)
                n_here += 1
                total_caps += 1
                print(f"  {src.name}  Figure {m.group(1)}  {cap_slug[:44]:<44} -> {fname}")
                # the embed sits in its OWN paragraph, with empty alt text: see the Para rule
                # in docs/deliverable/wt175_md2tex.lua for why the alt text must be empty
                if out and out[-1].strip():
                    out.append("")
                out.append(f"![]({fname})")
                out.append("")
            out.append(ln)

        b, a = vp.measure(src.read_text(encoding="utf-8")), vp.measure("\n".join(out))
        print(
            f"  {src.name}: {n_here} figure(s); em-dash "
            f"{b['em_dash']} ({b['em_dash_per_1k']}/1k) -> {a['em_dash']} ({a['em_dash_per_1k']}/1k); "
            f"paired {kinds.get('paired', 0)} single {kinds.get('single', 0)} "
            f"deferred {kinds.get('defer', 0)}\n"
        )
        if not check:
            dst = OUTROOT / d / dst_name
            dst.parent.mkdir(parents=True, exist_ok=True)
            dst.write_text("\n".join(out), encoding="utf-8")
            print(f"  wrote {dst.relative_to(ROOT)}\n")

    unclaimed = sorted(set(figs) - claimed)
    if unclaimed:
        raise SystemExit(
            "REFUSED: %d figure file(s) no caption claims -- a picture nobody prints is a\n"
            "         picture nobody proof-reads:\n           %s"
            % (len(unclaimed), "\n           ".join(unclaimed))
        )
    print(f"OK — {total_caps} caption(s), {len(figs)} figure file(s), every one claimed exactly once")
    return 0


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    sys.exit(build(ap.parse_args().check))
