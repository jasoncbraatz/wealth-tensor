"""The preflight must REFUSE, not approximate — proved, not asserted.

wealthTensor-54. `docs/deliverable/preflight.sh` exists because LaTeX substitutes a missing
font instead of failing: the build succeeds, the metrics shift, the reflow moves, and the
document comes out "close". A preflight that has only ever been seen to PASS is exactly as
useful as no preflight at all, so these tests break it on purpose and require a non-zero exit.

Both tests restore the tree byte-for-byte and assert the restore, in a finally: block.
"""
import hashlib
import pathlib
import shutil
import subprocess

import pytest

REPO = pathlib.Path(__file__).resolve().parent.parent
DEL = REPO / "docs" / "deliverable"
PRE = DEL / "preflight.sh"
FONTS = DEL / "fonts"


def _run(*args, env=None):
    import os
    e = dict(os.environ)
    e.update(env or {})
    return subprocess.run(["bash", str(PRE), *args], cwd=str(DEL), env=e,
                          stdout=subprocess.PIPE, stderr=subprocess.STDOUT)


def _a_font():
    fonts = sorted(FONTS.glob("*.otf"))
    assert fonts, "no vendored fonts — P13d cannot be true"
    return fonts[0]


def test_preflight_passes_on_the_tree_as_committed():
    r = _run("--fonts-only")
    assert r.returncode == 0, r.stdout.decode("utf-8", "replace")


def test_preflight_refuses_a_font_whose_bytes_changed():
    """The catastrophe: a font file that is present but is NOT the one the layout was
    measured against. Name-based checks cannot see this; a checksum can."""
    f = _a_font()
    original = f.read_bytes()
    digest = hashlib.sha256(original).hexdigest()
    try:
        f.write_bytes(original + b"\x00")
        r = _run("--fonts-only")
        out = r.stdout.decode("utf-8", "replace")
        assert r.returncode != 0, "preflight ACCEPTED a modified font:\n" + out
        assert "CHECKSUM MISMATCH" in out, out
    finally:
        f.write_bytes(original)
        assert hashlib.sha256(f.read_bytes()).hexdigest() == digest


def test_preflight_refuses_a_missing_font_rather_than_carrying_on():
    f = _a_font()
    original = f.read_bytes()
    digest = hashlib.sha256(original).hexdigest()
    aside = f.with_suffix(f.suffix + ".redproof")
    try:
        shutil.move(str(f), str(aside))
        r = _run("--fonts-only")
        out = r.stdout.decode("utf-8", "replace")
        assert r.returncode != 0, "preflight ACCEPTED a missing font:\n" + out
        assert "MISSING" in out.upper(), out
    finally:
        if aside.exists():
            shutil.move(str(aside), str(f))
        assert hashlib.sha256(f.read_bytes()).hexdigest() == digest


def test_preflight_refuses_an_unpinned_tex_live_year():
    """A distribution bump can move metrics, so it is a refusal with a documented deliberate
    override -- not a warning anyone would skim past."""
    r = _run(env={"WT_TEXLIVE_PIN": "1999"})
    out = r.stdout.decode("utf-8", "replace")
    assert r.returncode != 0, out
    assert "1999" in out and "LAYOUT-MANIFEST" in out, out


@pytest.mark.parametrize("required", ["FONTS.tsv"])
def test_the_font_manifest_is_present_and_carries_checksums(required):
    m = FONTS / required
    assert m.is_file(), "%s is the thing P13d checks" % required
    rows = [l for l in m.read_text(encoding="utf-8").split("\n")
            if l and not l.startswith("#") and not l.startswith("file\t")]
    assert rows, "manifest lists no fonts"
    for r in rows:
        f = r.split("\t")
        assert len(f) >= 3 and len(f[2]) == 64, "row has no sha256: %r" % r
