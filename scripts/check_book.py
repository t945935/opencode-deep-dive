#!/usr/bin/env python3
"""Small, dependency-free release checks for the manuscript."""
from pathlib import Path
import zipfile

root = Path(__file__).resolve().parents[1]
required = [root / "BOOK.md", root / "EDITORIAL_PLAN.md", root / "book/manuscript.md"]
required += [root / f"book/chapters/{n:02d}-chapter.md" for n in range(1, 23)]
required += [root / "book/chapters/appendix-a.md", root / "book/chapters/appendix-b.md"]
missing = [str(p.relative_to(root)) for p in required if not p.exists()]
if missing:
    raise SystemExit("Missing: " + ", ".join(missing))

text = (root / "book/manuscript.md").read_text()
for phrase in ("Provider", "Session", "MCP", "JSONL RPC", "API Key"):
    if phrase not in text:
        raise SystemExit(f"Missing required topic: {phrase}")

epub = root / "OpenCode-深入解析.epub"
with zipfile.ZipFile(epub) as z:
    if z.namelist()[0] != "mimetype" or z.read("mimetype") != b"application/epub+zip":
        raise SystemExit("Invalid EPUB mimetype placement")
    if any(any(ord(c) > 127 for c in n) for n in z.namelist() if n.lower().endswith(".css")):
        raise SystemExit("EPUB contains a non-ASCII CSS filename")
print(f"OK: {len(required)} manuscript files, {len(z.namelist())} EPUB entries")
