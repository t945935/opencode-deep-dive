#!/usr/bin/env python3
from pathlib import Path

root = Path(__file__).resolve().parents[1]
out = root / "book/manuscript.md"
parts = {
    1: ("第一篇　認識與啟動 OpenCode", range(1, 4)),
    2: ("第二篇　設定與模型選擇", range(4, 6)),
    3: ("第三篇　工作階段與上下文", range(6, 8)),
    4: ("第四篇　Prompt、Skills 與 Tools", range(8, 11)),
    5: ("第五篇　MCP、事件與 Extension", range(11, 16)),
    6: ("第六篇　應用程式整合與發佈", range(16, 19)),
    7: ("第七篇　完整實戰與工具選擇", range(19, 21)),
    8: ("第八篇　安全性與設計哲學", range(21, 23)),
}
with out.open("w") as f:
    f.write((root / "book/frontmatter.md").read_text())
    for _, (title, numbers) in parts.items():
        f.write(f"\n\n# {title}\n\n")
        for n in numbers:
            f.write((root / f"book/chapters/{n:02d}-chapter.md").read_text())
            f.write("\n\n")
    for p in sorted((root / "book/chapters").glob("appendix-*.md")):
        f.write(p.read_text())
        f.write("\n\n")
print(out)
