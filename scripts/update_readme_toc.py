#!/usr/bin/env python3
"""扫描 docs/issue-*.md，重建 README 目录（TOC:START 与 TOC:END 之间）。

issue 文件约定：
- 文件名 issue-N.md，N 为期号
- 可选 YAML frontmatter：date: YYYY-MM-DD
- 正文第一个 # 标题 = 期标题
"""
import re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
README = ROOT / "README.md"
START, END = "<!-- TOC:START -->", "<!-- TOC:END -->"


def parse_issue(path: Path):
    n = int(re.match(r"issue-(\d+)\.md", path.name).group(1))
    text = path.read_text(encoding="utf-8")
    date = None
    m = re.match(r"^---\s*\n(.*?)\n---", text, re.S)
    if m:
        dm = re.search(r"^date:\s*(\d{4}-\d{2}-\d{2})", m.group(1), re.M)
        if dm:
            date = dm.group(1)
    tm = re.search(r"^#\s+(.+)$", text, re.M)
    title = tm.group(1).strip() if tm else path.stem
    return n, title, date


def main():
    issues = [parse_issue(p) for p in sorted(DOCS.glob("issue-*.md"),
                                             key=lambda p: int(re.match(r"issue-(\d+)", p.name).group(1)))]
    lines = []
    current_ym = None
    for n, title, date in issues:
        ym = date[:7] if date else "未标注日期"
        if ym != current_ym:
            current_ym = ym
            lines += [f"**{ym}**", ""]
        suffix = f"（{date}）" if date else ""
        lines.append(f"- 第 {n} 期：[{title}](docs/issue-{n}.md){suffix}")
    toc = "\n".join(lines) if lines else "*尚无发表期数。*"

    readme = README.read_text(encoding="utf-8")
    new = re.sub(re.escape(START) + r".*?" + re.escape(END),
                 f"{START}\n{toc}\n{END}", readme, flags=re.S)
    if new != readme:
        README.write_text(new, encoding="utf-8")
        print("TOC updated")
    else:
        print("TOC unchanged")


if __name__ == "__main__":
    sys.exit(main())
