#!/usr/bin/env python3
from pathlib import Path
import re

root = Path(__file__).resolve().parents[1]
out = root / "book/manuscript.md"
main_chapters = [
    ("基礎與啟動 OpenCode", range(1, 4)),
    ("設定與模型選擇", range(4, 6)),
    ("工作階段與上下文", range(6, 8)),
    ("Prompt、Skills 與 Tools", range(8, 11)),
    ("MCP、事件與 Extension", range(11, 16)),
    ("應用程式整合與發佈", range(16, 19)),
    ("完整實戰與工具選擇", range(19, 21)),
    ("安全性與設計哲學", range(21, 23)),
]

def as_subchapter(text, sub_number):
    lines = text.splitlines()
    title_index = None
    for i, line in enumerate(lines):
        if line.startswith("# 第 "):
            title = re.sub(r"^# 第 \d+ 章　?", "", line)
            lines[i] = f"## {title}"
            title_index = i
            break
    # Headings inside a former chapter become topic-level paragraphs.
    for i, line in enumerate(lines):
        if i != title_index and line.startswith("## "):
            topic = line[3:]
            # Old source files used global chapter numbers (e.g. 8.2).
            # In the new hierarchy these are topic paragraphs, so remove
            # the obsolete number and use local semantic headings.
            topic = re.sub(r"^\d+\.\d+\s+", "", topic)
            topic = topic.replace("本章目標", "本節目標")
            topic = topic.replace("本章實作", "本節實作")
            topic = topic.replace("章末練習", "本節練習")
            topic = topic.replace("章末小結", "本節小結")
            lines[i] = "### " + topic
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
