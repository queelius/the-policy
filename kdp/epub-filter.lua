-- Lua filter for EPUB: clean up front matter and fix math rendering
--
-- Pandoc's --epub-title-page=true generates its own title page from metadata.
-- The LaTeX \titlepage also gets converted to a Div.titlepage in the AST.
-- Without an explicit header, pandoc's EPUB writer generates an h1 from the
-- document title for orphan front matter blocks. This filter removes the
-- LaTeX titlepage, adds an unlisted header (invisible, not in TOC) to prevent
-- the auto-generated one, and assigns CSS classes to front matter divs.
--
-- Also converts complex math expressions that pandoc can't render to MathML
-- into readable Unicode text fallbacks.

-- Fix math expressions that pandoc leaves as raw TeX
local math_fallbacks = {
  ["R_{\\text{specified}} \\xrightarrow{\\text{Outer Alignment}} R_{\\text{actual}} \\xrightarrow{\\text{Inner Alignment}} \\pi_{\\text{learned}}"]
    = "R(specified) \u{2192} R(actual) \u{2192} \u{03C0}(learned)",
  ["\\max E[\\sum_{t=0}^{\\infty} \\gamma^t R_t]"]
    = "max E[\u{03A3} \u{03B3}\u{1D57}R\u{209C}]",
  ["\\max E[\\sum_{t=0}^{\\infty} \\gamma^t R(s_t, a_t, u_t; \\phi_t)]"]
    = "max E[\u{03A3} \u{03B3}\u{1D57}R(s\u{209C}, a\u{209C}, u\u{209C}; \u{03C6}\u{209C})]",
}

-- Scene breaks: \scenebreak expands to a centered "* * *" asterism, which
-- pandoc reads as a center Div. Convert it to a horizontal rule, which
-- kindle.css renders as a spaced asterism (hr::after).
function Div(el)
  if el.classes:includes("center") and #el.content == 1
     and el.content[1].t == "Para"
     and pandoc.utils.stringify(el.content[1]) == "* * *" then
    return pandoc.HorizontalRule()
  end
  return el
end

function Math(el)
  local fallback = math_fallbacks[el.text]
  if fallback then
    return pandoc.Emph({pandoc.Str(fallback)})
  end
  return el
end

function Pandoc(doc)
  local new_blocks = {}
  local front_matter_index = 0
  local inserted_header = false

  for _, block in ipairs(doc.blocks) do
    -- Remove the LaTeX titlepage div (pandoc's auto title page handles this)
    if block.t == "Div" and block.classes:includes("titlepage") then
      -- skip it

    elseif front_matter_index < 3 and block.t == "Div" and block.classes:includes("center") then
      -- Before the first front matter div, insert an unlisted header
      -- This prevents pandoc from auto-generating an h1 from the doc title
      if not inserted_header then
        local header = pandoc.Header(1, {},
          pandoc.Attr("front-matter", {"unnumbered", "unlisted"}))
        table.insert(new_blocks, header)
        inserted_header = true
      end

      -- Reclassify front matter center divs with proper CSS classes
      front_matter_index = front_matter_index + 1
      local class_map = {
        [1] = "copyright-page",
        [2] = "dedication-page",
        [3] = "epigraph-page"
      }
      block.classes = {class_map[front_matter_index]}
      table.insert(new_blocks, block)

    else
      front_matter_index = 3
      table.insert(new_blocks, block)
    end
  end

  doc.blocks = new_blocks
  return doc
end
