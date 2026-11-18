-- connected.lua: Lua helper for connected.cls (v2.4.0). Loaded by the class, not by chapters.
--
-- connected.snippet(file, opts, out)
--   Cuts the lines firstline..lastline (taken from `opts`) out of a source file and writes them to
--   `out`. The listings package otherwise reads and tokenizes the whole file before cutting the
--   range, and under LuaLaTeX Hebrew text from the SKIPPED lines (the module docstring) leaked into
--   the first displayed line (CODE-01). It also sets two macros:
--     \connected@snipfirst  the real number of the first line (so the box shows real line numbers)
--     \connected@snipopts   `opts` without firstline/lastline
--   Hebrew runs inside the code are followed by U+200E (LRM), so that the quote mark and comma that
--   come after a Hebrew string stay in the left-to-right code order and do not jump into the
--   Hebrew run (CODE-02). The text is not reversed or retyped, only the direction is marked.

connected = connected or {}

local LRM = utf8.char(0x200E)
local RLM = utf8.char(0x200F)

local function is_hebrew(cp)
  return cp >= 0x0590 and cp <= 0x05FF
end

-- characters that may sit inside a Hebrew phrase: space ( ) ' - : , .
local inside = { [32] = true, [40] = true, [41] = true, [39] = true,
                 [45] = true, [58] = true, [44] = true, [46] = true }

local function mark_hebrew(line)
  local cps = {}
  for _, c in utf8.codes(line) do cps[#cps + 1] = c end
  local out, i, n = {}, 1, #cps
  while i <= n do
    if is_hebrew(cps[i]) then
      local j, last = i, i
      while j <= n and (is_hebrew(cps[j]) or inside[cps[j]]) do
        if is_hebrew(cps[j]) or cps[j] == 41 then last = j end
        j = j + 1
      end
      out[#out + 1] = LRM
      for k = i, last do out[#out + 1] = utf8.char(cps[k]) end
      out[#out + 1] = RLM  -- keeps a closing parenthesis inside the Hebrew run
      out[#out + 1] = LRM
      i = last + 1
    else
      out[#out + 1] = utf8.char(cps[i])
      i = i + 1
    end
  end
  return table.concat(out)
end

function connected.snippet(file, opts, outname)
  local first = tonumber(opts:match("firstline[ \t]*=[ \t]*([0-9]+)")) or 1
  local last = tonumber(opts:match("lastline[ \t]*=[ \t]*([0-9]+)"))
  local fh = assert(io.open(file, "rb"), "connected.snippet: cannot open " .. file)
  local lines, n = {}, 0
  for l in fh:lines() do
    n = n + 1
    if n >= first and ((not last) or n <= last) then
      l = l:gsub("\r$", "")
      lines[#lines + 1] = mark_hebrew(l)
    end
  end
  fh:close()
  local oh = assert(io.open(outname, "wb"))
  oh:write(table.concat(lines, "\n"), "\n")
  oh:close()
  local cleaned = opts:gsub("firstline[ \t]*=[ \t]*[0-9]+[ \t]*,?", "")
  cleaned = cleaned:gsub("lastline[ \t]*=[ \t]*[0-9]+[ \t]*,?", "")
  token.set_macro("connected@snipfirst", tostring(first))
  token.set_macro("connected@snipopts", cleaned)
end
