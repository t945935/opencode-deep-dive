#!/usr/bin/env python3
from pathlib import Path
import re

root = Path(__file__).resolve().parents[1]
out = root / "book/manuscript.md"
main_chapters = [
    ("第一章　基礎與啟動 OpenCode", range(1, 4)),
    ("第二章　設定與模型選擇", range(4, 6)),
    ("第三章　工作階段與上下文", range(6, 8)),
    ("第四章　Prompt、Skills 與 Tools", range(8, 11)),
    ("第五章　MCP、事件與 Extension", range(11, 16)),
    ("第六章　應用程式整合與發佈", range(16, 19)),
    ("第七章　完整實戰與工具選擇", range(19, 21)),
    ("第八章　安全性與設計哲學", range(21, 23)),
]

def as_subchapter(text, sub_number):
    lines = text.splitlines()
    for i, line in enumerate(lines):
        if line.startswith("# 第 "):
            title = re.sub(r"^# 第 \d+ 章　?", "", line)
            lines[i] = f"## {sub_number}　{title}"
            break
    # Headings inside a former chapter become topic-level paragraphs.
    for i, line in enumerate(lines):
        if i and line.startswith("## "):
            lines[i] = "### " + line[3:]
    return "\n".join(lines)

with out.open("w") as f:
    f.write((root / "book/frontmatter.md").read_text())
    for main_number, (title, numbers) in enumerate(main_chapters, 1):
        f.write(f"\n\n# {title}\n\n")
        for offset, n in enumerate(numbers, 1):
            block = (root / f"book/chapters/{n:02d}-chapter.md").read_text()
            f.write(as_subchapter(block, f"{main_number}.{offset}"))
            f.write("\n\n")
    for p in sorted((root / "book/chapters").glob("appendix-*.md")):
        f.write(p.read_text())
        f.write("\n\n")
print(out)
