# Agent 周刊

下一代「个人电脑级」浪潮正在成型。本周刊不追逐热点，而是**记录和记载这股浪潮下逐渐成型的基础建设、共识、转型，以及值得注意的社会问题**。

每周一期，周六/日发表。

投稿方式：[提交 issue](https://github.com/lysandre001/agent-weekly/issues/new?template=clipping.md)。
投稿格式：**一个事实 + 一个出处链接 + 一句为什么值得放进周刊**。

## 目录

<!-- TOC:START -->
*尚无发表期数。*
<!-- TOC:END -->

## 仓库结构

```
agent-weekly/
├── README.md      # 本文件：定位 + 目录 + 投稿指引
├── docs/          # 定稿，一期一文件：issue-N.md（frontmatter 带 date，CI 自动维护上方目录）
├── docs-en/       # 英文版，与 docs/ 一一对应：issue-N.md（有对应文件时期数旁自动出现 EN 链接）
└── .github/       # workflows：新期或新英译合并后自动更新目录
```

素材投稿统一走 [issue](https://github.com/lysandre001/agent-weekly/issues)，不再设 inbox 目录。

## 分工

- **yilin**：选题决策、终审、声音定调。
- **Hermes**：资料员（剪藏+溯源）、结构编辑、初稿手。
- 导出工具（微信公众号 / 英文版 / Substack）：[agent-weekly-scripts](https://github.com/lysandre001/agent-weekly-scripts)。

## 调性

- 事实密度优先：引文 + 出处 + 时间坐标。
- 少下判断；观点必须可溯源到某人某文。
- 与热点保持距离：追问「这事一年后还重要吗」。
