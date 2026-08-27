-- docs/deliverable/wt175_md2tex.lua
-- =========================================================================================
-- wt175 · THE PINNED MARKDOWN -> LATEX CONVERTER.
--
-- RECIPE.md step 2 pins the engine and step 1 pins the fonts by checksum, because a
-- dependency that drifts moves the reflow and costs the layout analysis a second time.
-- Until wealthTensor-94 NOTHING pinned the thing that turns four Markdown manuscripts into
-- the LaTeX the engine reads -- and that converter is where the layout silently changes.
-- build.sh pins pandoc's version; this filter pins its BEHAVIOUR on the two constructs the
-- corpus contains that a default conversion gets wrong.
--
-- (1) INLINE CODE. Pandoc's default is \texttt{}. RECIPE.md step 13 requires \url{}.
--     This is not cosmetic: \texttt cannot break, so the corpus's 64-character test
--     identifier overflows a 289.08pt measure in EVERY paper -- and LaTeX reports an
--     overfull box as a WARNING, so the build succeeds and the document is merely wrong.
--     \url breaks it at its underscores and inserts NO character, so the string a reader
--     copies out of the PDF still runs.
--     MEASURED over the four manuscripts: 155 spans contain no whitespace and become
--     \url{}; 18 contain whitespace and become \texttt{}, where the spaces are already
--     legal break points. Exactly ONE span contains a character \url could not carry
--     (a '%'), and it is in the whitespace set, so \url never sees an unsafe byte.
--
-- (2) SIX CHARACTERS NO VENDORED FACE CARRIES. See preamble.tex, block wt175. Two are
--     mathematics and go to math mode out of LibertinusMath; four are the References
--     sections' own verification notation and go to the vendored, checksummed FreeSerif.
--     Left alone they emit "Missing character:" to the log and set NOTHING -- 126 marks
--     silently absent from a build that exited 0.
--
-- Both defects share one shape, and it is the shape to remember: THE TOOLCHAIN REPORTS
-- BEING WRONG AT A SEVERITY BELOW THE ONE THAT STOPS IT. build.sh promotes both to fatal.
-- =========================================================================================

-- U+2299 CIRCLED DOT OPERATOR and U+1D4A9 SCRIPT CAPITAL N are mathematics; LibertinusMath
-- has both, so they are set in math mode rather than vendored around.
-- U+2713 U+29D7 U+270E U+26A0 are the verification marks; \wtmark selects vendored FreeSerif.
local REPL = {
  ["\226\138\153"]     = "\\ensuremath{\\odot}",           -- U+2299  ⊙
  ["\240\157\146\169"] = "\\ensuremath{\\mathcal{N}}",     -- U+1D4A9 𝒩
  ["\226\156\147"]     = "\\wtmark{✓}",                    -- U+2713  ✓
  ["\226\167\151"]     = "\\wtmark{⧗}",                    -- U+29D7  ⧗
  ["\226\156\142"]     = "\\wtmark{✎}",                    -- U+270E  ✎
  ["\226\154\160"]     = "\\wtmark{⚠}",                    -- U+26A0  ⚠
}
-- Longest byte-sequence first, so a 4-byte character can never be split by a 3-byte probe.
local ORDER = { "\240\157\146\169", "\226\138\153", "\226\156\147",
                "\226\167\151", "\226\156\142", "\226\154\160" }

-- U+1D62 SUBSCRIPT SMALL I IS THE ONE THAT TEACHES SOMETHING. It is present in
-- LibertinusSerif-Regular and -Bold and ABSENT from -Italic and -BoldItalic, and the corpus
-- writes it as an index on an emphasised variable ("*mᵢ*"), which is exactly the italic
-- case. A coverage probe run against the DEFAULT face reports it present. It disappears
-- only where the prose happens to be italic -- 40 times, silently, in a build that exits 0.
-- THE RULE THAT FALLS OUT: a glyph-coverage probe must test every face the document can
-- SELECT, not the face it happens to start in. The first probe this session ran tested one
-- face and reported six missing characters; the true answer for the body text is seven.
--
-- The repair routes the whole super/subscript family to mathematics rather than patching
-- the one broken character, because that is what these are: mᵢ, δᵢ, E₀, 10⁻¹⁵, η⁺, Λ⁻¹ are
-- indices and exponents, and setting some of them as text glyphs and one of them as maths
-- would be visibly inconsistent on the page. Runs are GROUPED -- "10⁻¹⁵" becomes
-- 10\ensuremath{^{-15}} and not three separate scripts.
local SUP = { ["\226\129\176"]="0", ["\194\185"]="1", ["\194\178"]="2", ["\194\179"]="3",
              ["\226\129\180"]="4", ["\226\129\181"]="5", ["\226\129\182"]="6",
              ["\226\129\183"]="7", ["\226\129\184"]="8", ["\226\129\185"]="9",
              ["\226\129\186"]="+", ["\226\129\187"]="-",
              ["\225\181\151"]="t", ["\225\181\131"]="a" }
local SUB = { ["\226\130\128"]="0", ["\226\130\129"]="1", ["\226\130\130"]="2",
              ["\226\130\131"]="3", ["\225\181\162"]="i" }
local SUPK, SUBK = {}, {}
for k in pairs(SUP) do SUPK[#SUPK+1] = k end
for k in pairs(SUB) do SUBK[#SUBK+1] = k end

-- Escape a literal string for \texttt{}. \url{} needs no escaping (it is verbatim) and is
-- only ever handed whitespace-free spans, which the corpus measurement shows are safe.
local function texttt_escape(s)
  s = s:gsub("\\", "\\textbackslash{}")
  s = s:gsub("([%%%$&#_{}])", "\\%1")
  s = s:gsub("%^", "\\textasciicircum{}")
  s = s:gsub("~", "\\textasciitilde{}")
  return s
end

local function code_to_texttt(el)
  return pandoc.RawInline("latex", "\\texttt{" .. texttt_escape(el.text) .. "}")
end

-- A snake_case IDENTIFIER is a different typographic object from a URL or a SHA, and
-- wealthTensor-109b is where that stopped being a distinction without a difference. Both were
-- routed to \url; xurl then broke both at any character, so an identifier was cut mid-word
-- sixteen times across the capture. An identifier has seams -- its underscores -- and a reader
-- expects the break there. A URL's slashes and a SHA's undifferentiated hex do not, which is
-- why those keep the break-anywhere behaviour that fixed -94's two measured overflows.
-- The test is SEAM PRESENCE, not shape. The first version of this asked whether the token was
-- `^[%w_]+$` with an underscore, which is true of a bare identifier and false of the same
-- identifier inside a path -- so `scripts/wt083_tier_ladder_antialignment.py` fell through to
-- \url and was still cut at `wt083_ti`. Measured: that narrow test fixed 9 of 16 mid-word
-- breaks and left 7, every one of them a path. A path's seams are `/` and `.` where an
-- identifier's are `_`; both are places a reader's eye accepts a break. Only a token carrying
-- no seam whatsoever -- a 64-character hex SHA -- has nowhere to break and still needs xurl's
-- break-anywhere rule, which is the case -94 added xurl for in the first place.
local function has_seam(s)
  return s:find("[_/%.%-:]") ~= nil
end

local function code_span(tok)
  if has_seam(tok) then return "\\wtident{" .. tok .. "}" end
  return "\\url{" .. tok .. "}"
end

local function code_inline(el)
  -- Whitespace-free spans are identifiers or URLs; code_span decides which (step 13).
  if not el.text:find("%s") then
    return pandoc.RawInline("latex", code_span(el.text))
  end
  -- A span WITH whitespace is a command line, and "it can break at its spaces" is not
  -- enough: measured on the real build, `python3 scripts/wt089_recognition_and_offdiagonal.py`
  -- has a 44-character TOKEN, and \texttt cannot break inside one. Two of these overflowed
  -- the measure, the worse by 88.98pt. So each token is sent through \url on its own -- same
  -- mechanism, same guarantee that nothing is inserted -- and the tokens are separated by
  -- real spaces inside a \ttfamily group, so the interword space is the monospace one and
  -- not the serif one it would otherwise inherit.
  -- \url carries %, #, &, ~, < and > safely; it cannot carry a brace or a backslash, and
  -- MEASURED over the four manuscripts no code span contains either.
  local parts = {}
  for tok in el.text:gmatch("%S+") do parts[#parts + 1] = code_span(tok) end
  return pandoc.RawInline("latex", "{\\ttfamily " .. table.concat(parts, " ") .. "}")
end

local function match_at(t, i, keys)
  for _, k in ipairs(keys) do
    if t:sub(i, i + #k - 1) == k then return k end
  end
  return nil
end

local function str_marks(el)
  local t = el.text
  local hit = false
  for _, set in ipairs({ ORDER, SUPK, SUBK }) do
    for _, k in ipairs(set) do
      if t:find(k, 1, true) then hit = true break end
    end
    if hit then break end
  end
  if not hit then return nil end

  local out, buf, i, n = {}, {}, 1, #t
  local function flush()
    if #buf > 0 then out[#out + 1] = pandoc.Str(table.concat(buf)); buf = {} end
  end
  -- Consume a maximal run of one script family and emit it as ONE ensuremath group.
  local function run(keys, map, op)
    local acc = {}
    local k = match_at(t, i, keys)
    while k do
      acc[#acc + 1] = map[k]
      i = i + #k
      k = match_at(t, i, keys)
    end
    flush()
    out[#out + 1] = pandoc.RawInline("latex",
      "\\ensuremath{" .. op .. "{" .. table.concat(acc) .. "}}")
  end

  while i <= n do
    local m = match_at(t, i, ORDER)
    if m then
      flush()
      out[#out + 1] = pandoc.RawInline("latex", REPL[m])
      i = i + #m
    elseif match_at(t, i, SUPK) then
      run(SUPK, SUP, "^")
    elseif match_at(t, i, SUBK) then
      run(SUBK, SUB, "_")
    else
      buf[#buf + 1] = t:sub(i, i)
      i = i + 1
    end
  end
  flush()
  return out
end

-- TWO PASSES, AND THE ORDER IS THE POINT.
--
-- \url is fragile: inside a heading it is a MOVING ARGUMENT (\section writes its argument to
-- the .toc whether or not anybody calls \tableofcontents) and the build dies with "Undefined
-- control sequence". Pass 1 therefore rewrites code spans INSIDE HEADINGS to \texttt, before
-- the general rule can send them to \url. Headings are short and the longest code span in one
-- measures 30 characters, well inside the 55 that fit inline, so nothing is lost.
--
-- That case was MISSED by the survey that preceded this filter: "no heading contains a code
-- span" was measured with a regex anchored at '^#', and the one heading that does contain one
-- sits inside a blockquote ('> ## ... `REVIEW-002-internal-referee.md` ...'). The build caught
-- what the measurement could not see -- the same shape as the ADR-002 finding one directory
-- over: AN INSTRUMENT THAT CANNOT SEE A CASE REPORTS ZERO OF THEM, and zero reads as absence.

-- Table ids are (paper slug, ordinal within that paper). The slug arrives by environment
-- variable because build.sh runs one pandoc invocation per manuscript.
local wt_slug = os.getenv("WT_SLUG") or "doc"
local wt_table_n = 0

return {
  { Header = function(el)
      el.content = el.content:walk({ Code = code_to_texttt })
      return el
    end },

  { Code = code_inline,
    Str  = str_marks,

    -- Every table is wrapped in \begin{wttable}{<id>}, which gives it ITS OWN measure --
    -- defaulting to the body measure and widened only where the build proved it necessary,
    -- from the committed docs/deliverable/TABLE-WIDTHS.tsv. Six of the corpus's thirty
    -- tables overflow a 289.08pt measure, the worst by 143.65pt; a nine-column table simply
    -- is not a four-inch object. A UNIFORM wide measure was tried first and is wrong: it
    -- stretches narrow tables to the same width and opens a canyon down the middle of them.
    -- See preamble.tex, block "wide tables", for the glue, and for why the overfull count
    -- alone could not have caught getting that glue wrong.
    Table = function(el)
      wt_table_n = wt_table_n + 1
      local id = wt_slug .. "-t" .. wt_table_n
      -- The COLUMN COUNT travels with the table because the tuner needs it: a cell that
      -- overflows its p-column by x needs the TABLE widened by roughly x times the number
      -- of columns, since pandoc's column widths are fractions of the table's measure.
      local ncols = #el.colspecs
      return { pandoc.RawBlock("latex", "\\begin{wttable}{" .. id .. "}{" .. ncols .. "}"), el,
               pandoc.RawBlock("latex", "\\end{wttable}") }
    end },
}
