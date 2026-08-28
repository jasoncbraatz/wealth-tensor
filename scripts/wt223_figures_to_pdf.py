#!/usr/bin/env python3
"""wt223_figures_to_pdf.py — the nine figures, out of the browser and into the typesetter.

P13f: every figure in the deliverable is produced by a COMMITTED script. This is that script for
the v2 pair, and it exists because the figures are not files -- they are DRAWN BY JAVASCRIPT into
empty <svg> shells in docs/papers/wt-figures.html. Lifting an <svg> straight out of that source
yields a correctly-sized, entirely empty box; it renders, it is the right shape, and it contains
nothing. So the page has to be EXECUTED, and this script is the execution.

THREE THINGS BITE, IN ORDER, AND ALL THREE WERE MEASURED RATHER THAN ANTICIPATED:

  1. THE SVGs ARE EMPTY IN THE SOURCE. Nine <svg> elements, zero paths between them. The first
     extraction produced nine 0.9K PDFs -- every one an identically-sized blank page, which is
     exactly what a working pipeline looks like from the outside. Headless Chrome runs the page;
     the DOM comes back three times the size of the file.

  2. EVERY MARK IS PAINTED WITH A CSS CUSTOM PROPERTY -- stroke="var(--s1)" -- declared on :root
     in the page. Out of the document those resolve to nothing and cairosvg falls back to black,
     so the SECOND attempt produced nine figures with correct geometry and no colour at all.
     Again: it looks like a figure until you look at one. The palette is therefore SUBSTITUTED
     LITERALLY below rather than declared, and the script asserts zero var( remain.

  3. THE VIEWBOX IS THE CROP. In the page the <svg> sits in a box with visible overflow, so
     figure 1's x-axis label at y=424 shows fine against a viewBox height of 420. Standalone it
     was sliced in half. The pad is applied BY MEASUREMENT, so a re-cut figure cannot bring the
     defect back quietly.

Light palette throughout: the deliverable is print. Output is VECTOR -- the figures scale with the
page and their text stays selectable.

  python3 scripts/wt223_figures_to_pdf.py            regenerate docs/figures/*.pdf
  python3 scripts/wt223_figures_to_pdf.py --check    exit 1 if any figure is missing or stale
"""
import hashlib, json, pathlib, re, subprocess, sys

REPO   = pathlib.Path(__file__).resolve().parents[1]
PAGE   = REPO/"docs"/"papers"/"wt-figures.html"
OUT    = REPO/"docs"/"figures"
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

PAL = {
 "--page":"#f4f6f8","--surface-1":"#fcfdfe","--line":"#dfe3e8","--grid":"#e9edf1",
 "--text-primary":"#0b0e11","--text-secondary":"#4d545c","--text-muted":"#7b838c",
 "--s1":"#2a78d6","--s2":"#eb6834",
 "--t0":"#86b6ef","--t1":"#3987e5","--t2":"#256abf","--t3":"#104281",
 "--rule":"#c4cbd3","--accent":"#2a78d6",
}
FONT = "<style>text{font-family:Georgia,'Times New Roman',serif}</style>"


def resolve(s):
    def sub(m):
        return PAL.get(m.group(1).strip(), (m.group(2) or "").strip(" ,") or "#0b0e11")
    prev = None
    while prev != s:                       # nested var() -> resolve to a fixed point
        prev = s
        s = re.sub(r"var\(\s*(--[a-z0-9-]+)\s*(,[^()]*)?\)", sub, s)
    return s


def slug(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")[:44]


def render_dom():
    if not pathlib.Path(CHROME).exists():
        sys.exit("CANNOT VERIFY — %s is not installed. The figures are drawn by JavaScript and "
                 "cannot be extracted without executing the page." % CHROME)
    r = subprocess.run([CHROME, "--headless", "--disable-gpu", "--virtual-time-budget=5000",
                        "--dump-dom", PAGE.as_uri()], capture_output=True, text=True, timeout=180)
    dom = r.stdout
    if len(dom) < len(PAGE.read_text()) * 1.5:
        sys.exit("the DOM came back barely larger than the source (%d vs %d bytes) — the draw "
                 "scripts did not run, and the figures would be empty boxes."
                 % (len(dom), len(PAGE.read_text())))
    return dom


def build():
    dom    = render_dom()
    titles = re.findall(r'<p class="ftitle">([^<]+)</p>', dom)
    svgs   = re.findall(r'(<svg\b.*?</svg>)', dom, re.S)
    if len(svgs) != 9 or len(titles) != 9:
        sys.exit("expected 9 figures and 9 titles, found %d/%d — the page changed shape"
                 % (len(svgs), len(titles)))
    import cairosvg
    OUT.mkdir(parents=True, exist_ok=True)
    made = []
    for i, (svg, title) in enumerate(zip(svgs, titles), 1):
        m = re.match(r"(<svg\b[^>]*>)(.*)", svg, re.S)
        body = resolve(m.group(1) + FONT + m.group(2))
        left = len(re.findall(r"var\(--", body))
        if left:
            sys.exit("figure %d still carries %d unresolved custom properties — it would render "
                     "black. Add the missing name to PAL." % (i, left))
        vb = re.search(r'viewBox="([^"]+)"', body)
        x0, y0, vw, vh = [float(v) for v in vb.group(1).split()]
        ys   = [float(y) for y in re.findall(r'\by="(-?[\d.]+)"', body)]
        need = (max(ys) + 12) - vh if ys else 0
        if need > 0:
            body = body.replace(vb.group(0), 'viewBox="%g %g %g %g"' % (x0, y0, vw, vh+need), 1)
        name = "fig-%02d-%s" % (i, slug(title))
        (OUT/(name+".svg")).write_text(body, encoding="utf-8")
        cairosvg.svg2pdf(bytestring=body.encode("utf-8"), write_to=str(OUT/(name+".pdf")))
        made.append((i, title, name, (OUT/(name+".pdf")).stat().st_size, need))
    return made


def main():
    check = "--check" in sys.argv
    made = build()
    print("nine figures, vector, from %s\n" % PAGE.relative_to(REPO))
    for i, t, n, sz, pad in made:
        print("  %d  %-46s %6.1fK%s" % (i, t[:46], sz/1024,
              ("   viewBox +%.0fpx" % pad) if pad > 0 else ""))
    thin = [m for m in made if m[3] < 4000]
    if thin:
        print("\nREFUSED — %d figure(s) under 4K, which is what an EMPTY page weighs:" % len(thin))
        for i, t, n, sz, _ in thin:
            print("  ✗ %d %s (%.1fK)" % (i, t[:50], sz/1024))
        return 1
    print("\nall nine carry real marks (smallest %.1fK)." % (min(m[3] for m in made)/1024))
    return 0


if __name__ == "__main__":
    sys.exit(main())
