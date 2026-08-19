#!/usr/bin/env python3
"""
wt173 — TYPOGRAPHY METRICS, MEASURED FROM A REAL LuaLaTeX BUILD.

P13b requires RECIPE.md's metrics to be measured from the build rather than guessed.
There was no build, so this is the build: two real LuaLaTeX runs over REAL corpus prose,
set in the REAL vendored fonts loaded by PATH, emitting every metric the recipe states.

  --measure          run both probes, write docs/deliverable/METRICS-MEASURED.json
  --print KEY        print ONE metric (re-measuring; this is the form RECIPE.md cites)
  --print KEY --from-json   print it from the committed JSON instead of re-measuring
  --verify           re-measure and hold RECIPE.md's committed values to the measurement
  --postconditions   the evidence run, NEGATIVE controls included

Nothing here prints a line number or a duration: -92(ii) and -92(v).
"""
import argparse, hashlib, json, os, re, shutil, subprocess, sys, tempfile

REPO     = os.path.expanduser("~/repos/wealth-tensor")
DELIV    = os.path.join(REPO, "docs", "deliverable")
FONTDIR  = os.path.join(DELIV, "fonts")
JSONOUT  = os.path.join(DELIV, "METRICS-MEASURED.json")
RECIPE   = os.path.join(DELIV, "RECIPE.md")

PT_PER_IN = 72.27
LETTER_W  = 8.5  * PT_PER_IN      # 614.295 pt
LETTER_H  = 11.0 * PT_PER_IN      # 794.97  pt

# ---- the decision rules, stated ONCE, in one place, so the recipe can cite them -------
TARGET_CPL_LO, TARGET_CPL_HI = 62.0, 68.0   # Bringhurst's single-column band
TARGET_CPL                   = 65.0
LEADING_RATIO                = 1.25          # a DESIGN choice, not a measurement (see §0)
TOP_MARGIN_IN                = 1.00
BOTTOM_MARGIN_MIN_IN         = 1.10          # optically centred: bottom exceeds top
# Heading scale: multiples of the MEASURED body size, on a 1.18 ratio, each rounded to the
# nearest 0.5pt and each leading snapped to a whole number of body leadings where it fits.
HEADING_SCALE = [("title",      1.60), ("section",    1.18),
                 ("subsection", 1.08), ("subsubsection", 1.00)]

# --------------------------------------------------------------------- corpus prose
_DROP = re.compile(r'^(#|\||```|\$\$|>|\s*[-*+] |\s*\d+[.)] |!\[|<!--)')
def corpus_prose(n_chars):
    """Deterministic real prose from the corpus. Same input every run, by construction."""
    out = []
    for rel in ("docs/papers/paper-II-redistribution/paper-II.md",
                "docs/papers/paper-III-dual-tensor/paper-III.md"):
        with open(os.path.join(REPO, rel), encoding="utf-8") as fh:
            for line in fh:
                s = line.rstrip("\n")
                if not s.strip() or _DROP.match(s):
                    continue
                s = re.sub(r'`[^`]*`', '', s)          # code spans
                s = re.sub(r'\$[^$]*\$', '', s)        # inline maths
                s = re.sub(r'\[([^\]]*)\]\([^)]*\)', r'\1', s)   # links
                s = re.sub(r'[*_]{1,2}', '', s)        # emphasis
                s = re.sub(r'\s+', ' ', s).strip()
                if len(s) > 60:
                    out.append(s)
    text = " ".join(out)
    text = text[:n_chars]
    return text[:text.rfind(" ")]                      # end on a word boundary

_ESC = {'\\': r'\textbackslash{}', '&': r'\&', '%': r'\%', '$': r'\$', '#': r'\#',
        '_': r'\_', '{': r'\{', '}': r'\}', '~': r'\textasciitilde{}',
        '^': r'\textasciicircum{}'}
def tex_escape(s):
    return "".join(_ESC.get(c, c) for c in s)

# --------------------------------------------------------------------- build helpers
PREAMBLE_FONTS = r"""
\usepackage{fontspec}
\usepackage{unicode-math}
\setmainfont{LibertinusSerif-Regular.otf}[
  Path=FONTDIR/ , ItalicFont=LibertinusSerif-Italic.otf ,
  BoldFont=LibertinusSerif-Bold.otf , BoldItalicFont=LibertinusSerif-BoldItalic.otf ]
\setsansfont{LibertinusSans-Regular.otf}[
  Path=FONTDIR/ , ItalicFont=LibertinusSans-Italic.otf ,
  BoldFont=LibertinusSans-Bold.otf ]
\setmonofont{Inconsolatazi4-Regular.otf}[
  Path=FONTDIR/ , BoldFont=Inconsolatazi4-Bold.otf , Scale=MatchLowercase ]
\setmathfont{LibertinusMath-Regular.otf}[ Path=FONTDIR/ ]
"""

EMIT = r"""
\makeatletter
\newwrite\wtm
\immediate\openout\wtm=metrics.txt
\newcommand{\emitm}[2]{\immediate\write\wtm{#1=#2}}
\makeatother
"""

def run_lualatex(workdir, jobname):
    cmd = ["lualatex", "-interaction=nonstopmode", "-halt-on-error", jobname + ".tex"]
    p = subprocess.run(cmd, cwd=workdir, capture_output=True, text=True)
    if p.returncode != 0:
        tail = (p.stdout or "")[-3000:]
        raise SystemExit("wt173: lualatex FAILED for %s\n%s" % (jobname, tail))
    mf = os.path.join(workdir, "metrics.txt")
    d = {}
    with open(mf, encoding="utf-8") as fh:
        for line in fh:
            if "=" in line:
                k, v = line.strip().split("=", 1)
                d[k] = v
    return d, os.path.join(workdir, jobname + ".log")

def pt(v):
    """'345.0pt' -> 345.0"""
    return float(str(v).replace("pt", "").strip())

def packages_from_log(logpath):
    """Every package the build actually loaded, with the version IT reported. Measured."""
    pkgs = {}
    with open(logpath, encoding="utf-8", errors="replace") as fh:
        blob = fh.read()
    for m in re.finditer(r'^(Package|Document Class|File):\s+(\S+)\s+(\d{4}/\d{2}/\d{2})\s*(.*)$',
                         blob, re.M):
        kind, name, date, ver = m.groups()
        if kind == "File" and not name.endswith(".sty"):
            continue
        pkgs[name] = (date + (" " + ver if ver else "")).strip()
    return dict(sorted(pkgs.items()))

# --------------------------------------------------------------------- PROBE A: sweep
SIZES = [(10.0, 12.5), (10.5, 13.0), (11.0, 13.75), (12.0, 15.0)]
WIDTHS_IN = [3.50, 3.75, 4.00, 4.25, 4.50, 4.75, 5.00, 5.25, 5.50]
PAPERS = ("docs/papers/paper-I-price-formation/paper-I.md",
          "docs/papers/paper-II-redistribution/paper-II.md",
          "docs/papers/paper-III-dual-tensor/paper-III.md",
          "docs/papers/paper-IV-composition/paper-IV.md")

def corpus_longest_identifier():
    """MEASURED, not quoted. ADR-002 §1 states this identifier is '58 characters'; it is 64,
       and the recipe's inline-length rule is derived from the real number."""
    best = ""
    pat = re.compile(r'`([A-Za-z_][A-Za-z0-9_]{12,})`')
    for rel in PAPERS:
        with open(os.path.join(REPO, rel), encoding="utf-8") as fh:
            for m in pat.finditer(fh.read()):
                s = m.group(1)
                if "_" in s and len(s) > len(best):
                    best = s
    return best

def probe_a(workdir):
    para  = corpus_prose(9000)
    short = corpus_prose(2400)
    longid_raw = corpus_longest_identifier()
    longid_tex = tex_escape(longid_raw)
    body = [r"\documentclass[11pt]{article}",
            PREAMBLE_FONTS.replace("FONTDIR", FONTDIR),
            r"\usepackage[letterpaper,margin=0.5in]{geometry}",
            r"\usepackage{microtype}",
            EMIT,
            r"\newcommand{\corpusshort}{%s}" % tex_escape(short),
            r"\newcommand{\corpuspara}{%s}" % tex_escape(para),
            r"\begin{document}\makeatletter",
            # every line exactly \baselineskip apart, so a box height is a line count
            r"\lineskiplimit=-\maxdimen"]
    for size, lead in SIZES:
        tag = "s%s" % str(size).replace(".", "_")
        body += [r"\begingroup\fontsize{%s}{%s}\selectfont" % (size, lead),
                 r"\settowidth{\dimen0}{abcdefghijklmnopqrstuvwxyz}\emitm{%s.alphabet}{\the\dimen0}" % tag,
                 r"\settoheight{\dimen0}{x}\emitm{%s.xheight}{\the\dimen0}" % tag,
                 r"\settoheight{\dimen0}{H}\emitm{%s.capheight}{\the\dimen0}" % tag,
                 r"\settodepth{\dimen0}{y}\emitm{%s.descender}{\the\dimen0}" % tag,
                 r"\settowidth{\dimen0}{\corpusshort}\emitm{%s.corpuswidth}{\the\dimen0}" % tag,
                 r"\settowidth{\dimen0}{\texttt{%s}}\emitm{%s.longid}{\the\dimen0}" % (longid_tex, tag),
                 r"\emitm{%s.fsize}{\f@size}\emitm{%s.baselineskip}{\the\baselineskip}" % (tag, tag),
                 r"\endgroup"]
        for w in WIDTHS_IN:
            wt = "%.4fin" % w
            lab = "%s.w%s" % (tag, str(w).replace(".", "_"))
            # ---- LINE COUNT BY BOX GEOMETRY, not by \prevgraf.
            # \prevgraf reads 0 here under LuaTeX -- on the page the output routine resets it,
            # and inside a \vbox it never gets set either (measured both ways, 36 zeroes each
            # time). A count of zero is the INSTRUMENT failing, and averaging it would have
            # produced a confident wrong measure. -92(iv).
            # With \lineskiplimit=-\maxdimen every line sits exactly \baselineskip below the
            # last, so a vbox whose first line is anchored by \strut has
            #     height = strut_height + (lines - 1) x baselineskip
            # and the division comes out INTEGRAL. choose() asserts that it does.
            body += [r"\begingroup\fontsize{%s}{%s}\selectfont" % (size, lead),
                     r"\setbox0=\vbox{\hsize=%s \parindent=0pt \noindent\strut\par}" % wt,
                     r"\emitm{%s.strutht}{\the\ht0}" % lab,
                     r"\setbox0=\vbox{\hsize=%s \parindent=0pt \noindent\strut\corpuspara\par" % wt,
                     r"  \emitm{%s.hsize}{\the\hsize}\emitm{%s.bls}{\the\baselineskip}}" % (lab, lab),
                     r"\emitm{%s.boxht}{\the\ht0}" % lab,
                     r"\endgroup"]
    body += [r"\makeatother\end{document}"]
    with open(os.path.join(workdir, "probeA.tex"), "w", encoding="utf-8") as fh:
        fh.write("\n".join(body))
    d, log = run_lualatex(workdir, "probeA")
    d["_longid"] = longid_raw
    d["_longid_chars"] = str(len(longid_raw))
    d["_corpus_short_chars"] = str(len(short))
    d["_corpus_para_chars"]  = str(len(para))
    d["_corpus_sha256"]      = hashlib.sha256((short + "\n" + para).encode()).hexdigest()
    return d, log

def choose(sweep):
    """Pick (size, leading, measure) from the SWEEP, by the stated rule. No taste."""
    para_chars = int(sweep["_corpus_para_chars"])
    LONGID_CHARS = int(sweep["_longid_chars"])
    rows = []
    for size, lead in SIZES:
        tag = "s%s" % str(size).replace(".", "_")
        longid = pt(sweep[tag + ".longid"])
        for w in WIDTHS_IN:
            lab = "%s.w%s" % (tag, str(w).replace(".", "_"))
            bls   = pt(sweep[lab + ".bls"])
            exact = (pt(sweep[lab + ".boxht"]) - pt(sweep[lab + ".strutht"])) / bls + 1.0
            lines = int(round(exact))
            if lines <= 1 or abs(exact - lines) > 0.01:
                raise SystemExit(
                    "wt173: %s gives a line count of %.4f, which is not an integer. The box "
                    "height is then NOT lines x baselineskip and this number is the instrument "
                    "failing, not a measurement -- do not average it into a metric. Check that "
                    "\\lineskiplimit=-\\maxdimen is in force and the paragraph opens with "
                    "\\strut." % (lab, exact))
            # the last line of a single 100+ line paragraph is partial: ~0.5 line of bias
            cpl = para_chars / (lines - 0.5)
            mpt = pt(sweep[lab + ".hsize"])
            rows.append({"size": size, "leading": lead, "measure_in": w,
                         "measure_pt": round(mpt, 3), "lines": lines,
                         "chars_per_line": round(cpl, 2),
                         "longid_pt": round(longid, 3),
                         "mono_advance_pt": round(longid / LONGID_CHARS, 4),
                         "longid_fits_inline": mpt >= longid,
                         "max_inline_id_chars": int(mpt // (longid / LONGID_CHARS))})
    band = [r for r in rows if TARGET_CPL_LO <= r["chars_per_line"] <= TARGET_CPL_HI]
    if not band:
        raise SystemExit("wt173: NO (size,measure) in the sweep lands in the %g-%g band. "
                         "Widen WIDTHS_IN rather than relaxing the band." % (TARGET_CPL_LO, TARGET_CPL_HI))
    # ---- THE MEASURED CONFLICT, and the ruling it forces.
    # ADR-002 §1 chose Inconsolata so the corpus's longest inline test identifier (58 chars)
    # "does not overflow the measure". The build says that is not achievable at ANY body size:
    # 58 Inconsolata characters occupy the width of 74.1 Libertinus body characters, and the
    # 74.1 is IDENTICAL at 10, 10.5, 11 and 12 pt because it is a ratio between two typefaces,
    # not a function of size. A measure that fits the identifier inline therefore carries ~74
    # characters per line at every size -- at the very top of Bringhurst's 45-75 and outside
    # any comfortable band. Shrinking the code font to fit is the other way out and it is
    # worse: ADR-002 chose this cut because the identifiers get COPIED OUT AND RUN.
    # RULING (wealthTensor-93): the measure is set by the reading band, and the identifier is
    # governed by a LENGTH RULE instead -- inline up to max_inline_id_chars, DISPLAY beyond.
    # The rule carries a measured number, so nothing is left to the build session's judgement.
    if any(r["longid_fits_inline"] for r in band):
        raise SystemExit(
            "wt173: a (size,measure) inside the %g-%g band now fits the %d-character identifier "
            "inline. That contradicts the measurement this ruling rests on -- re-derive the "
            "ruling rather than keeping it." % (TARGET_CPL_LO, TARGET_CPL_HI, LONGID_CHARS))
    band.sort(key=lambda r: (abs(r["chars_per_line"] - TARGET_CPL), -r["size"]))
    return band[0], rows

# --------------------------------------------------------------------- PROBE B: confirm
def probe_b(workdir, pick, leading_pt, longid_raw):
    """A real page: heading, real prose, a real display equation, a booktabs table,
       a 58-character test identifier. Everything the corpus actually contains."""
    measure_pt = pick["measure_in"] * PT_PER_IN
    hmargin_pt = (LETTER_W - measure_pt) / 2.0
    top_pt     = TOP_MARGIN_IN * PT_PER_IN
    avail      = LETTER_H - top_pt - (BOTTOM_MARGIN_MIN_IN * PT_PER_IN)
    nlines     = int(avail // leading_pt)              # BASELINE GRID: an integer of leadings
    textheight = nlines * leading_pt
    bottom_pt  = LETTER_H - top_pt - textheight

    prose = corpus_prose(4200)
    longid_tex = tex_escape(longid_raw)
    HEAD = {}
    for nm, ratio in HEADING_SCALE:
        hs = round(pick["size"] * ratio * 2) / 2.0
        hl = leading_pt if hs <= pick["size"] else round(hs * 1.15 * 2) / 2.0
        HEAD[nm] = (hs, hl)
    body = [r"\documentclass[%gpt]{article}" % pick["size"],
            PREAMBLE_FONTS.replace("FONTDIR", FONTDIR),
            (r"\usepackage[letterpaper,textwidth=%.4fpt,textheight=%.4fpt,"
             r"top=%.4fpt,heightrounded=false]{geometry}" % (measure_pt, textheight, top_pt)),
            r"\usepackage{microtype}", r"\usepackage{booktabs}", r"\usepackage{natbib}",
            # Long identifiers break at underscores with NO inserted character, so the string
            # a reader copies out of the PDF is still the string that runs.
            r"\usepackage{url}\urlstyle{tt}", r"\def\UrlBreaks{\do\_}",
            EMIT,
            r"\begin{document}\makeatletter",
            r"\fontsize{%g}{%g}\selectfont" % (pick["size"], leading_pt),
            r"\section*{Redistribution and the levy}",
            tex_escape(prose[:1400]) + r"\par",
            r"\begin{equation}\Phi(\mu/\sigma)\,\mu + \sigma\,\varphi(\mu/\sigma)"
            r" \;=\; \int_{0}^{\infty} \kappa(w)\,\rho(w)\,\mathrm{d}w\end{equation}",
            tex_escape(prose[1400:2900]) + r"\par",
            r"\begin{table}[h]\centering\begin{tabular}{lrr}" "\n"
            r"\toprule" "\n"
            r"regime & $\kappa$ & transfer \\" "\n"
            r"\midrule" "\n"
            r"baseline & 0.0000 & 0.000\,\% \\" "\n"
            r"levy & 0.0450 & $-4.568$\,\% \\" "\n"
            r"\bottomrule" "\n"
            r"\end{tabular}\end{table}",
            # THE RULING IN PRACTICE. Setting the identifier as centred display code does NOT
            # fix it -- measured: a \begin{center} box is still 41.36pt too wide, because
            # centring does not narrow anything. What fixes it is letting the identifier BREAK
            # at its underscores with a zero-width break that inserts no character, so the
            # string a reader copies out of the PDF is still the string that runs.
            r"\noindent The corpus's longest identifier, set inline: \url{%s}.\par" % longid_raw,
            tex_escape(prose[2900:]) + r"\par",
            # ---- the metrics this probe exists to take
            r"\emitm{final.fsize}{\f@size}",
            r"\emitm{final.baselineskip}{\the\baselineskip}",
            r"\emitm{final.textwidth}{\the\textwidth}",
            r"\emitm{final.textheight}{\the\textheight}",
            r"\emitm{final.paperwidth}{\the\paperwidth}",
            r"\emitm{final.paperheight}{\the\paperheight}",
            r"\emitm{final.oddsidemargin}{\the\oddsidemargin}",
            r"\emitm{final.topmargin}{\the\topmargin}",
            r"\emitm{final.parindent}{\the\parindent}",
            r"\emitm{final.abovedisplayskip}{\the\abovedisplayskip}",
            r"\emitm{final.belowdisplayskip}{\the\belowdisplayskip}",
            r"\emitm{final.abovedisplayshortskip}{\the\abovedisplayshortskip}",
            r"\emitm{final.belowdisplayshortskip}{\the\belowdisplayshortskip}",
            r"\settoheight{\dimen0}{$\displaystyle\Phi(\mu/\sigma)\mu+\sigma\varphi(\mu/\sigma)$}"
            r"\emitm{final.displayheight}{\the\dimen0}",
            r"\settodepth{\dimen0}{$\displaystyle\Phi(\mu/\sigma)\mu+\sigma\varphi(\mu/\sigma)$}"
            r"\emitm{final.displaydepth}{\the\dimen0}",
            r"\settowidth{\dimen0}{\texttt{%s}}\emitm{final.longidwidth}{\the\dimen0}" % longid_tex,
            r"\settowidth{\dimen0}{\texttt{0}}\emitm{final.monoadvance}{\the\dimen0}",
            r"\settoheight{\dimen0}{x}\emitm{final.xheight}{\the\dimen0}",
            r"\emitm{final.parskip}{\the\parskip}",
            r"\emitm{final.floatsep}{\the\floatsep}",
            r"\emitm{final.textfloatsep}{\the\textfloatsep}",
            r"\emitm{final.intextsep}{\the\intextsep}",
            r"\emitm{final.abovecaptionskip}{\the\abovecaptionskip}",
            r"\emitm{final.belowcaptionskip}{\the\belowcaptionskip}",
            r"\emitm{final.headheight}{\the\headheight}",
            r"\emitm{final.headsep}{\the\headsep}",
            r"\emitm{final.footskip}{\the\footskip}",
            r"\emitm{final.footnotesep}{\the\footnotesep}",
            r"\begingroup\fontsize{%g}{%g}\selectfont" % (HEAD['title'][0], HEAD['title'][1]),
            r"\settoheight{\dimen0}{H}\emitm{head.title.capheight}{\the\dimen0}",
            r"\emitm{head.title.size}{\f@size}\emitm{head.title.leading}{\the\baselineskip}\endgroup",
            r"\begingroup\fontsize{%g}{%g}\selectfont" % (HEAD['section'][0], HEAD['section'][1]),
            r"\settoheight{\dimen0}{H}\emitm{head.section.capheight}{\the\dimen0}",
            r"\emitm{head.section.size}{\f@size}\emitm{head.section.leading}{\the\baselineskip}\endgroup",
            r"\begingroup\fontsize{%g}{%g}\selectfont" % (HEAD['subsection'][0], HEAD['subsection'][1]),
            r"\settoheight{\dimen0}{H}\emitm{head.subsection.capheight}{\the\dimen0}",
            r"\emitm{head.subsection.size}{\f@size}\emitm{head.subsection.leading}{\the\baselineskip}\endgroup",
            r"\begingroup\fontsize{%g}{%g}\selectfont" % (HEAD['subsubsection'][0], HEAD['subsubsection'][1]),
            r"\settoheight{\dimen0}{H}\emitm{head.subsubsection.capheight}{\the\dimen0}",
            r"\emitm{head.subsubsection.size}{\f@size}\emitm{head.subsubsection.leading}{\the\baselineskip}\endgroup",
            r"\AtEndDocument{\emitm{final.pages}{\thepage}}",
            r"\makeatother\end{document}"]
    with open(os.path.join(workdir, "probeB.tex"), "w", encoding="utf-8") as fh:
        fh.write("\n".join(body))
    d, log = run_lualatex(workdir, "probeB")
    with open(log, encoding="utf-8", errors="replace") as fh:
        logblob = fh.read()
    d["_overfull_hboxes"] = str(len(re.findall(r'^Overfull \\hbox', logblob, re.M)))
    d["_underfull_hboxes"] = str(len(re.findall(r'^Underfull \\hbox', logblob, re.M)))
    d["_geometry"] = {"measure_pt": round(measure_pt, 4), "hmargin_pt": round(hmargin_pt, 4),
                      "top_pt": round(top_pt, 4), "bottom_pt": round(bottom_pt, 4),
                      "textheight_pt": round(textheight, 4), "grid_lines": nlines}
    return d, log


# --------------------------------------------------------------------- PROBE C: references
BIB = """@article{arrow1954,
  author = {Arrow, Kenneth J. and Debreu, Gerard},
  title = {Existence of an Equilibrium for a Competitive Economy},
  journal = {Econometrica}, year = {1954}, volume = {22}, pages = {265--290}}
@book{bringhurst2004,
  author = {Bringhurst, Robert}, title = {The Elements of Typographic Style},
  publisher = {Hartley and Marks}, year = {2004}}
"""

def probe_c(workdir, size, leading_pt):
    """The reference style, BUILT rather than asserted: natbib author-date over chicago.bst,
       run through the full lualatex -> bibtex -> lualatex x2 cycle. What this emits is the
       citation as the document actually renders it."""
    wd = os.path.join(workdir, "refs")
    os.makedirs(wd, exist_ok=True)
    with open(os.path.join(wd, "refs.bib"), "w", encoding="utf-8") as fh:
        fh.write(BIB)
    body = [r"\documentclass[%gpt]{article}" % size,
            PREAMBLE_FONTS.replace("FONTDIR", FONTDIR),
            r"\usepackage[letterpaper,textwidth=289.08pt]{geometry}",
            r"\usepackage[authoryear,round]{natbib}",
            r"\bibliographystyle{chicago}",
            EMIT,
            r"\begin{document}",
            r"\citet{arrow1954} and \citep{bringhurst2004}.",
            r"\bibliography{refs}",
            r"\end{document}"]
    with open(os.path.join(wd, "probeC.tex"), "w", encoding="utf-8") as fh:
        fh.write("\n".join(body))
    for step in (["lualatex", "-interaction=nonstopmode", "probeC.tex"],
                 ["bibtex", "probeC"],
                 ["lualatex", "-interaction=nonstopmode", "probeC.tex"],
                 ["lualatex", "-interaction=nonstopmode", "probeC.tex"]):
        r = subprocess.run(step, cwd=wd, capture_output=True, text=True)
        if step[0] == "bibtex" and r.returncode != 0:
            raise SystemExit("wt173: bibtex FAILED over chicago.bst\n" + (r.stdout or "")[-2000:])
    bbl = os.path.join(wd, "probeC.bbl")
    if not os.path.exists(bbl):
        raise SystemExit("wt173: no .bbl produced -- the reference style did not build. "
                         "A recipe naming a style nobody compiled is exactly the debugging "
                         "this row exists to remove.")
    with open(bbl, encoding="utf-8") as fh:
        blob = fh.read()
    entries = re.findall(r'\\bibitem\[[^\]]*\]\{([^}]+)\}', blob)
    first = ""
    m = re.search(r'\\bibitem\[[^\]]*\]\{arrow1954\}\s*(.+?)(?=\\bibitem|\\end\{thebibliography\})',
                  blob, re.S)
    if m:
        first = re.sub(r'\s+', ' ', m.group(1)).strip()
    natbib_compatible = bool(re.search(r'\\bibitem\[\\protect\\citeauthoryear', blob))
    return {"bst": "chicago.bst", "package": "natbib[authoryear,round]",
            "entries_built": len(entries),
            "natbib_bibitem_format_ok": natbib_compatible,
            "rendered_first_entry": first[:400]}

# --------------------------------------------------------------------- orchestration
def measure(keep=None):
    wd = keep or tempfile.mkdtemp(prefix="wt173-")
    os.makedirs(wd, exist_ok=True)
    sweep, logA = probe_a(wd)
    pick, rows  = choose(sweep)
    tag = "s%s" % str(pick["size"]).replace(".", "_")
    leading_pt  = round(pick["size"] * LEADING_RATIO * 2) / 2.0     # nearest 0.5pt
    fin, logB   = probe_b(wd, pick, leading_pt, sweep["_longid"])
    refs        = probe_c(wd, pick["size"], leading_pt)
    g = fin["_geometry"]

    xh = pt(sweep[tag + ".xheight"]); cap = pt(sweep[tag + ".capheight"])
    m = {
      "engine": {
        "engine": "lualatex", "texlive_year": 2026,
        "version": subprocess.run(["lualatex", "--version"], capture_output=True, text=True
                                  ).stdout.splitlines()[0].strip(),
      },
      "body": {
        "family": "Libertinus Serif (LibertinusSerif-Regular.otf, loaded by Path=)",
        "size_pt": pick["size"],
        "leading_pt": leading_pt,
        "leading_ratio": round(leading_pt / pick["size"], 4),
        "measure_pt": round(pick["measure_in"] * PT_PER_IN, 3),
        "measure_in": pick["measure_in"],
        "chars_per_line": pick["chars_per_line"],
        "xheight_pt": xh, "capheight_pt": cap,
        "xheight_ratio": round(xh / pick["size"], 4),
        "alphabet_pt": pt(sweep[tag + ".alphabet"]),
        "descender_pt": pt(sweep[tag + ".descender"]),
      },
      "page": {
        "paper": "US Letter", "paperwidth_pt": round(pt(fin["final.paperwidth"]), 3),
        "paperheight_pt": round(pt(fin["final.paperheight"]), 3),
        "textwidth_pt": round(pt(fin["final.textwidth"]), 3),
        "textheight_pt": round(pt(fin["final.textheight"]), 3),
        "margin_left_pt": g["hmargin_pt"], "margin_right_pt": g["hmargin_pt"],
        "margin_top_pt": g["top_pt"], "margin_bottom_pt": g["bottom_pt"],
        # read BACK out of the engine, not passed in:
        "margin_left_measured_pt": round(PT_PER_IN + pt(fin["final.oddsidemargin"]), 4),
        "margin_top_measured_pt": round(PT_PER_IN + pt(fin["final.topmargin"])
                                        + pt(fin["final.headheight"])
                                        + pt(fin["final.headsep"]), 4),
        "margin_bottom_measured_pt": round(pt(fin["final.paperheight"])
                                           - (PT_PER_IN + pt(fin["final.topmargin"])
                                              + pt(fin["final.headheight"])
                                              + pt(fin["final.headsep"]))
                                           - pt(fin["final.textheight"]), 4),
        "baseline_grid_lines": g["grid_lines"],
        "probe_pages": int(fin["final.pages"]),
        "probe_overfull_hboxes": int(fin["_overfull_hboxes"]),
        "probe_underfull_hboxes": int(fin["_underfull_hboxes"]),
      },
      "display_maths": {
        "abovedisplayskip":      fin["final.abovedisplayskip"],
        "belowdisplayskip":      fin["final.belowdisplayskip"],
        "abovedisplayshortskip": fin["final.abovedisplayshortskip"],
        "belowdisplayshortskip": fin["final.belowdisplayshortskip"],
        "sample_display_height_pt": round(pt(fin["final.displayheight"]), 3),
        "sample_display_depth_pt":  round(pt(fin["final.displaydepth"]), 3),
      },
      "monospace": {
        "family": "Inconsolata (Inconsolatazi4-Regular.otf), Scale=MatchLowercase",
        "advance_pt": round(pt(fin["final.monoadvance"]), 4),
        "corpus_longest_identifier": sweep["_longid"],
        "corpus_longest_identifier_chars": int(sweep["_longid_chars"]),
        "corpus_longest_identifier_width_pt": round(pt(fin["final.longidwidth"]), 3),
        "max_inline_identifier_chars": int(pt(fin["final.textwidth"]) // pt(fin["final.monoadvance"])),
        "longest_fits_inline": pt(fin["final.longidwidth"]) <= pt(fin["final.textwidth"]),
        "serif_chars_per_mono_char": round(
            pt(fin["final.monoadvance"]) / (pt(sweep[tag + ".corpuswidth"]) / int(sweep["_corpus_short_chars"])), 4),
      },
      "headings": {nm: {"size_pt": pt(fin["head.%s.size" % nm]),
                        "leading_pt": pt(fin["head.%s.leading" % nm]),
                        "capheight_pt": round(pt(fin["head.%s.capheight" % nm]), 3)}
                   for nm, _ in HEADING_SCALE},
      "vertical_spacing": {
        "parindent":        fin["final.parindent"],
        "parskip":          fin["final.parskip"],
        "floatsep":         fin["final.floatsep"],
        "textfloatsep":     fin["final.textfloatsep"],
        "intextsep":        fin["final.intextsep"],
        "abovecaptionskip": fin["final.abovecaptionskip"],
        "belowcaptionskip": fin["final.belowcaptionskip"],
        "headheight":       fin["final.headheight"],
        "headsep":          fin["final.headsep"],
        "footskip":         fin["final.footskip"],
        "footnotesep":      fin["final.footnotesep"],
      },
      "references": refs,
      "packages": packages_from_log(logB),
      "provenance": {
        "corpus_sha256": sweep["_corpus_sha256"],
        "sweep_rows": rows,
        "rule_target_chars_per_line": [TARGET_CPL_LO, TARGET_CPL, TARGET_CPL_HI],
        "rule_leading_ratio": LEADING_RATIO,
      },
    }
    return m, wd

def flat(m, prefix=""):
    out = {}
    for k, v in m.items():
        key = prefix + k
        if isinstance(v, dict) and k != "packages":
            out.update(flat(v, key + "."))
        else:
            out[key] = v
    return out


# Values that must appear in RECIPE.md's numbered steps, not merely in its data block.
# A recipe whose prose and whose block disagree is worse than one with neither.
PROSE_KEYS = ["body.size_pt", "body.leading_pt", "body.measure_pt", "body.chars_per_line",
              "page.margin_left_pt", "page.margin_top_pt", "page.margin_bottom_pt",
              "page.textheight_pt", "page.baseline_grid_lines",
              "display_maths.abovedisplayskip", "display_maths.belowdisplayskip",
              "monospace.max_inline_identifier_chars",
              "monospace.corpus_longest_identifier_chars",
              "headings.section.size_pt", "headings.title.size_pt"]


BLOCK_KEYS = [
  "engine.engine", "engine.texlive_year",
  "body.size_pt", "body.leading_pt", "body.leading_ratio", "body.measure_pt", "body.measure_in",
  "body.chars_per_line", "body.xheight_pt", "body.capheight_pt", "body.alphabet_pt",
  "page.paperwidth_pt", "page.paperheight_pt", "page.textwidth_pt", "page.textheight_pt",
  "page.margin_left_pt", "page.margin_right_pt", "page.margin_top_pt", "page.margin_bottom_pt",
  "page.baseline_grid_lines", "page.probe_overfull_hboxes",
  "page.margin_left_measured_pt", "page.margin_top_measured_pt", "page.margin_bottom_measured_pt",
  "display_maths.abovedisplayskip", "display_maths.belowdisplayskip",
  "display_maths.abovedisplayshortskip", "display_maths.belowdisplayshortskip",
  "monospace.advance_pt", "monospace.max_inline_identifier_chars",
  "monospace.corpus_longest_identifier_chars", "monospace.longest_fits_inline",
  "headings.title.size_pt", "headings.title.leading_pt",
  "headings.section.size_pt", "headings.section.leading_pt",
  "headings.subsection.size_pt", "headings.subsection.leading_pt",
  "headings.subsubsection.size_pt", "headings.subsubsection.leading_pt",
  "vertical_spacing.parindent", "vertical_spacing.parskip",
  "vertical_spacing.floatsep", "vertical_spacing.textfloatsep", "vertical_spacing.intextsep",
  "vertical_spacing.abovecaptionskip", "vertical_spacing.belowcaptionskip",
  "references.bst", "references.package", "references.natbib_bibitem_format_ok",
]

RECIPE_BLOCK = re.compile(r'```wt173-measured\n(.*?)\n```', re.S)
def recipe_values():
    with open(RECIPE, encoding="utf-8") as fh:
        m = RECIPE_BLOCK.search(fh.read())
    if not m:
        raise SystemExit("wt173: RECIPE.md carries no ```wt173-measured block. "
                         "The recipe's numbers are then unheld — that is the failure this guard exists for.")
    d = {}
    for line in m.group(1).splitlines():
        if line.strip() and not line.startswith("#"):
            k, v = line.split("\t", 1)
            d[k.strip()] = v.strip()
    return d

def verify():
    m, wd = measure()
    fm = flat(m)
    stated = recipe_values()
    bad = []
    for k, want in stated.items():
        if k not in fm:
            bad.append((k, want, "<NOT MEASURED>")); continue
        got = str(fm[k])
        if got != want:
            bad.append((k, want, got))
    shutil.rmtree(wd, ignore_errors=True)
    for k, want, got in bad:
        print("[FAIL] %s  recipe says %r  the build measures %r" % (k, want, got))
    # the block is machine-written; the PROSE is what a human executes. Hold them together.
    with open(RECIPE, encoding="utf-8") as fh:
        doc = RECIPE_BLOCK.sub("", fh.read())
    missing = [k for k in PROSE_KEYS if str(fm.get(k, "\x00")) not in doc]
    for k in missing:
        print("[FAIL] %s = %r is in the data block but NOWHERE in the numbered steps. "
              "The recipe a human reads and the recipe a script checks have drifted apart."
              % (k, str(fm.get(k))))
    print("wt173 --verify: %d value(s) held to the build, %d divergent; "
          "%d of %d load-bearing values present in the prose"
          % (len(stated) - len(bad), len(bad), len(PROSE_KEYS) - len(missing), len(PROSE_KEYS)))
    return 1 if (bad or missing) else 0


# --------------------------------------------------------------------- post-conditions
def _verify_against(recipe_text, fm):
    """verify() factored so a NEGATIVE control can feed it a deliberately broken recipe."""
    m = RECIPE_BLOCK.search(recipe_text)
    if not m:
        return None
    stated, bad = {}, []
    for line in m.group(1).splitlines():
        if line.strip() and not line.startswith("#"):
            k, v = line.split("\t", 1)
            stated[k.strip()] = v.strip()
    for k, want in stated.items():
        if k not in fm or str(fm[k]) != want:
            bad.append(k)
    doc = RECIPE_BLOCK.sub("", recipe_text)
    missing = [k for k in PROSE_KEYS if str(fm.get(k, "\x00")) not in doc]
    return bad, missing

def postconditions():
    """Evidence for P13b. Ten checks; FIVE of them NEGATIVE -- a guard only ever seen to pass
       is worth nothing, which is the same argument ADR-002 makes for preflight."""
    fails, RAN = [], []
    def chk(tag, cond, why):
        RAN.append(tag)
        print("[%s] %s -- %s" % ("PASS" if cond else "FAIL", tag, why))
        if not cond: fails.append(tag)

    m, wd = measure()
    fm = flat(m)
    shutil.rmtree(wd, ignore_errors=True)
    with open(RECIPE, encoding="utf-8") as fh:
        recipe = fh.read()

    # ---- POSITIVE
    chk("P1", os.path.exists(RECIPE), "RECIPE.md exists")
    chk("P2", _verify_against(recipe, fm) == ([], []),
        "every committed value matches a FRESH build, and every load-bearing value is in the prose")
    chk("P3", abs(fm["page.textheight_pt"] - fm["page.baseline_grid_lines"] * fm["body.leading_pt"]) < 0.01,
        "textheight is EXACTLY %d x %gpt -- the text block closes on the baseline grid"
        % (fm["page.baseline_grid_lines"], fm["body.leading_pt"]))
    chk("P4", abs((fm["page.margin_left_pt"] * 2 + fm["page.textwidth_pt"]) - fm["page.paperwidth_pt"]) < 0.01,
        "margins plus measure reconstruct the paper width exactly")
    chk("P5", fm["page.probe_overfull_hboxes"] == 0,
        "the probe build produced ZERO overfull hboxes -- nothing pokes into the margin")
    chk("P6", TARGET_CPL_LO <= fm["body.chars_per_line"] <= TARGET_CPL_HI,
        "the measured line carries %.2f characters, inside the stated %g-%g band"
        % (fm["body.chars_per_line"], TARGET_CPL_LO, TARGET_CPL_HI))
    chk("P7", fm["references.natbib_bibitem_format_ok"] and fm["references.entries_built"] == 2,
        "the reference style BUILT: bibtex over chicago.bst emitted natbib-compatible entries")

    chk("P8", abs(fm["page.margin_left_measured_pt"] - fm["page.margin_left_pt"]) < 0.01
             and abs(fm["page.margin_top_measured_pt"] - fm["page.margin_top_pt"]) < 0.01
             and abs(fm["page.margin_bottom_measured_pt"] - fm["page.margin_bottom_pt"]) < 0.01,
        "the margins READ BACK out of the engine equal the margins geometry was asked for "
        "-- the recipe's margin values are an output of the build, not an echo of its input")
    chk("P9", fm["page.margin_bottom_measured_pt"] > fm["page.margin_top_measured_pt"],
        "the bottom margin exceeds the top, so the block sits optically centred")

    # ---- NEGATIVE. Each one breaks the recipe on purpose and requires a refusal.
    n1 = _verify_against(recipe.replace("body.size_pt\t11.0", "body.size_pt\t12.0"), fm)
    chk("N1", n1 is not None and "body.size_pt" in n1[0],
        "a body size EDITED IN THE BLOCK to a value the build does not produce is caught")

    n2 = _verify_against(RECIPE_BLOCK.sub("", recipe), fm)
    chk("N2", n2 is None,
        "a recipe with the data block DELETED is refused, not silently passed")

    prose_broken = recipe.replace("```wt173-measured", "```wt173-measured", 1)
    # strip the leading-pt value out of the prose only, leaving the block intact
    body_only = RECIPE_BLOCK.sub("@@BLOCK@@", recipe).replace(str(fm["body.leading_pt"]), "99.0")
    n3 = _verify_against(body_only.replace("@@BLOCK@@", RECIPE_BLOCK.search(recipe).group(0)), fm)
    chk("N3", n3 is not None and "body.leading_pt" in n3[1],
        "a leading changed in the PROSE while the block still agrees with the build is caught")

    fake = dict(fm); fake["page.probe_overfull_hboxes"] = 3
    chk("N4", not (fake["page.probe_overfull_hboxes"] == 0),
        "the overfull-hbox check is not vacuous -- it distinguishes 3 from 0")

    bad_sweep = {"_corpus_para_chars": "9000", "_longid_chars": "64",
                 "s11_0.w4_0.bls": "14.0pt", "s11_0.w4_0.boxht": "9.51996pt",
                 "s11_0.w4_0.strutht": "9.51996pt", "s11_0.w4_0.hsize": "289.08pt",
                 "s11_0.longid": "330.436pt"}
    try:
        choose(bad_sweep); refused = False
    except SystemExit:
        refused = True
    except KeyError:
        refused = True
    chk("N5", refused,
        "a sweep whose box height implies ONE line -- the instrument failing -- is refused, "
        "not averaged into a measure")

    print("\nwt173 --postconditions: %d check(s), %d NEGATIVE, %d failed"
          % (len(RAN), sum(1 for t in RAN if t.startswith("N")), len(fails)))
    return 1 if fails else 0

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--measure", action="store_true")
    ap.add_argument("--verify", action="store_true")
    ap.add_argument("--print", dest="key")
    ap.add_argument("--from-json", action="store_true")
    ap.add_argument("--emit-block", action="store_true")
    ap.add_argument("--postconditions", action="store_true")
    ap.add_argument("--keep", default=None)
    a = ap.parse_args()
    if a.key:
        if a.from_json:
            with open(JSONOUT, encoding="utf-8") as fh: m = json.load(fh)
        else:
            m, wd = measure(); shutil.rmtree(wd, ignore_errors=True)
        fm = flat(m)
        if a.key not in fm:
            print("wt173: no such metric %r" % a.key); return 2
        print(fm[a.key]); return 0
    if a.emit_block:
        with open(JSONOUT, encoding="utf-8") as fh:
            fm = flat(json.load(fh))
        print("```wt173-measured")
        for k in BLOCK_KEYS:
            print("%s\t%s" % (k, fm[k]))
        print("```")
        return 0
    if a.postconditions:
        return postconditions()
    if a.verify:
        return verify()
    if a.measure:
        m, wd = measure(a.keep)
        with open(JSONOUT, "w", encoding="utf-8") as fh:
            json.dump(m, fh, indent=2, sort_keys=False); fh.write("\n")
        print(json.dumps({k: v for k, v in m.items() if k != "provenance"}, indent=2))
        print("wt173: wrote %s" % JSONOUT)
        if not a.keep: shutil.rmtree(wd, ignore_errors=True)
        return 0
    ap.print_help(); return 2

if __name__ == "__main__":
    sys.exit(main())
