# GitHub Open Source Radar

一个完全运行在 GitHub 上的开源项目雷达。它使用 GitHub 官方仓库搜索 API 发现近期新晋或持续活跃的高关注项目，并通过相邻成功快照计算 Star 增量。

> 这里的“热门”是透明、可配置的代理指标，不等同于 GitHub Trending 的官方排名。脚本不会克隆或执行被扫描仓库的代码。

<!-- RADAR:START -->

## 最新雷达

- UTC：`2026-10-10T06:00:05Z`
- 北京时间：`2026-10-10T14:00:05+08:00`
- 数据源：GitHub REST Search repositories API
- 排除候选：31 个
- 说明：Star 增量按相邻两次成功快照计算。

### 新晋热门项目

查询规则：`created:>=2026-09-10 stars:>=100 fork:false archived:false`

| 项目 | Stars | 增量 | 语言 | 许可证 | 最近推送 | 简介 |
|---|---:|---:|---|---|---|---|
| [storytold/photocraft](https://github.com/storytold/photocraft) | 36,824 | +7932 | Rust | Apache-2.0 | 2026-10-10 | An open-source, clean-room reimplementation of Adobe Photoshop in pure Rust |
| [NandhaKishorM/laya](https://github.com/NandhaKishorM/laya) | 32,024 | +223 | Python | Apache-2.0 | 2026-10-08 | Non-autoregressive System 1 decision engine. Typed choice, score and yes/no decisions over any text in a single forward… |
| [browser-use/jev-ultrafast](https://github.com/browser-use/jev-ultrafast) | 22,493 | +73 | Python | MIT | 2026-09-30 | Fastest and cheapest web agent |
| [Niko1221/Strata](https://github.com/Niko1221/Strata) | 19,831 | +1057 | C++ | MIT | 2026-10-08 | Qwen3.8-Flash-Next on any consumer hardware: one-click install for Windows / Linux. Strata inference engine, OpenAI/Ant… |
| [robbietilton/Compositor](https://github.com/robbietilton/Compositor) | 15,052 | +1147 | Swift | MIT | 2026-10-10 | The Photoshop alternative for Mac |
| [openai/math](https://github.com/openai/math) | 13,259 | +847 | Lean | Apache-2.0 | 2026-10-08 | - |
| [jaredpalmer/kev](https://github.com/jaredpalmer/kev) | 8,854 | +96 | Python | Apache-2.0 | 2026-10-09 | Jev-like family of decision models built on top of Qwen3.5/3.8 you can train and run on your own |
| [shihabal3amri/DiPlay](https://github.com/shihabal3amri/DiPlay) | 8,505 | +850 | Kotlin | GPL-3.0 | 2026-10-09 | Independent CarPlay receiver for compatible Android head units. Wired and wireless public preview. |
| [storytold/lightcraft](https://github.com/storytold/lightcraft) | 7,974 | +1807 | Rust | Apache-2.0 | 2026-10-10 | An open-source, clean-room reimplementation of Adobe Lightroom in pure Rust. |
| [yetone/magpie](https://github.com/yetone/magpie) | 7,672 | +727 | Go | MIT | 2026-10-10 | Every agent's model. One place. Codex on DeepSeek, Claude Code on Kimi, from the menu bar. |
| [zai-org/ZCode](https://github.com/zai-org/ZCode) | 7,619 | +54 | TypeScript | Apache-2.0 | 2026-09-29 | Z.ai's coding agent harness. Powerful, intelligent, extensible. |
| [tamaratran/fast-jev-compaction](https://github.com/tamaratran/fast-jev-compaction) | 7,559 | +24 | TypeScript | MIT | 2026-09-18 | Claude Code plugin that replaces the compaction summary with Jev decisions: every tool call and result is scored in one… |
| [jev-chat/jev-chat-jarvis](https://github.com/jev-chat/jev-chat-jarvis) | 7,531 | +36 | Kotlin | MIT | 2026-10-08 | The chat decision assistant: before you reply, Jev reads the chat, judges intent and risk, and drafts replies you fill… |
| [storytold/filmcraft](https://github.com/storytold/filmcraft) | 7,420 | +1710 | Rust | Apache-2.0 | 2026-10-10 | An open-source, clean-room reimplementation of Adobe Premiere Pro built in pure Rust. |
| [KKKKhazix/AIHOT](https://github.com/KKKKhazix/AIHOT) | 6,971 | +166 | TypeScript | MIT | 2026-10-10 | 一个自己找热点、自己写日报的网站框架。把信源和精选标准换成你的，它就是你的行业热点站。 |
| [mizorewww/laya-mlx](https://github.com/mizorewww/laya-mlx) | 6,857 | +15 | Python | Apache-2.0 | 2026-10-10 | Native MLX runtime for Laya typed decision models — 7–14 ms short decisions on M3 Max. No text generation, PyTorch, or… |
| [storytold/pdfcraft](https://github.com/storytold/pdfcraft) | 6,709 | +1768 | Rust | Apache-2.0 | 2026-10-10 | An open-source, clean-room reimplementation of Adobe Acrobat built in pure Rust |
| [Mak5er/AirCard](https://github.com/Mak5er/AirCard) | 6,427 | +42 | Swift | MIT | 2026-10-05 | Apple Wallet Card Skinner for iOS 18+ (No Jailbreak Required) |
| [rehan-remade/universal-modder](https://github.com/rehan-remade/universal-modder) | 6,101 | +370 | Python | MIT | 2026-10-10 | Point Claude at any game. Skills, tools and the fal MCP that let Claude Code mod almost any PC game you own: recon, rev… |
| [Ebony-Vinyl/dsh-our-free-model](https://github.com/Ebony-Vinyl/dsh-our-free-model) | 5,998 | +1279 | JavaScript | MIT | 2026-10-10 | 在 dsh 里装上这个插件即可，无需登录、注册或填 API Key，就能使用包括 DeepSeek V4.1 Flash、Kimi K3 在内的前沿模型——完全免费，不限量。 All you do is install this plug… |

### 近期活跃项目

查询规则：`pushed:>=2026-10-03 stars:>=1000 fork:false archived:false`

| 项目 | Stars | 增量 | 语言 | 许可证 | 最近推送 | 简介 |
|---|---:|---:|---|---|---|---|
| [public-apis/public-apis](https://github.com/public-apis/public-apis) | 487,042 | +201 | Python | MIT | 2026-10-05 | A collective list of free APIs |
| [freeCodeCamp/freeCodeCamp](https://github.com/freeCodeCamp/freeCodeCamp) | 456,784 | +43 | TypeScript | BSD-3-Clause | 2026-10-09 | freeCodeCamp.org's open-source codebase and curriculum. Learn math, programming, and computer science for free. |
| [EbookFoundation/free-programming-books](https://github.com/EbookFoundation/free-programming-books) | 398,609 | +89 | Python | CC-BY-4.0 | 2026-10-09 | :books: Freely available programming books |
| [openclaw/openclaw](https://github.com/openclaw/openclaw) | 391,556 | +52 | TypeScript | MIT | 2026-10-10 | The AI that really does things. Any OS. Any Platform. The lobster way. 🦞 |
| [obra/superpowers](https://github.com/obra/superpowers) | 296,947 | +300 | Shell | MIT | 2026-10-10 | An agentic skills framework &amp; software development methodology that works. |
| [practical-tutorials/project-based-learning](https://github.com/practical-tutorials/project-based-learning) | 286,234 | +99 | Python | MIT | 2026-10-05 | Curated list of project-based tutorials |
| [mattpocock/skills](https://github.com/mattpocock/skills) | 283,107 | +1643 | Shell | MIT | 2026-10-09 | Skills for Real Engineers. Straight from my .agents directory. |
| [affaan-m/ECC](https://github.com/affaan-m/ECC) | 276,081 | +562 | JavaScript | MIT | 2026-10-10 | The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development… |
| [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | 252,337 | +241 | Python | MIT | 2026-10-10 | The agent that grows with you |
| [react/react](https://github.com/react/react) | 250,808 | +52 | JavaScript | MIT | 2026-10-09 | The library for web and native user interfaces. |
| [deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness) | 246,545 | +636 | TypeScript | MIT | 2026-10-09 | DeepSeek Harness: Everything is a Plugin. |
| [TheAlgorithms/Python](https://github.com/TheAlgorithms/Python) | 225,127 | +15 | Python | MIT | 2026-10-06 | All Algorithms implemented in Python |
| [anomalyco/opencode](https://github.com/anomalyco/opencode) | 212,434 | +183 | TypeScript | MIT | 2026-10-10 | The open source coding agent. |
| [tensorflow/tensorflow](https://github.com/tensorflow/tensorflow) | 200,578 | +17 | C++ | Apache-2.0 | 2026-10-10 | An Open Source Machine Learning Framework for Everyone |
| [microsoft/vscode](https://github.com/microsoft/vscode) | 193,503 | +46 | TypeScript | MIT | 2026-10-10 | Visual Studio Code |
| [ohmyzsh/ohmyzsh](https://github.com/ohmyzsh/ohmyzsh) | 190,059 | +16 | Shell | MIT | 2026-10-09 | 🙃   A delightful community-driven (with 2,500+ contributors) framework for managing your zsh configuration. Includes 30… |
| [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | 190,001 | +317 | TypeScript | AGPL-3.0 | 2026-10-10 | Supercharge your AI agents with data from the web and beyond. Building the library for superintelligence. 🔥 |
| [microsoft/markitdown](https://github.com/microsoft/markitdown) | 189,257 | +141 | Python | MIT | 2026-10-04 | Python tool for converting files and office documents to Markdown. |
| [avelino/awesome-go](https://github.com/avelino/awesome-go) | 187,614 | +174 | Go | MIT | 2026-10-10 | A curated list of awesome Go frameworks, libraries and software |
| [ollama/ollama](https://github.com/ollama/ollama) | 182,569 | +133 | Go | MIT | 2026-10-10 | Get up and running with Kimi, GLM, MiniMax, DeepSeek, gpt-oss, Qwen, Gemma and other models. |

---

“热门”由仓库搜索条件与 Star 增量共同定义，不代表 GitHub 官方 Trending 排名。

<!-- RADAR:END -->

## 默认规则

- 新晋热门：近 30 天创建且至少 100 Stars。
- 近期活跃：近 7 天有推送且至少 1,000 Stars。
- 排除 Fork、归档、禁用和无明确开源许可证的仓库。
- 每类读取最多 100 个候选，在首页展示前 20 个。
- 首次运行建立基线；后续运行按仓库数字 ID 计算 Star 增量，仓库改名不会丢失历史。

规则可在 [`config.json`](config.json) 中调整。

## 运行方式

只依赖 Python 3.11+ 标准库：

```bash
python src/radar.py --config config.json --data-dir data --readme README.md
```

可选环境变量 `GITHUB_TOKEN` 用于提高 API 限额。本仓库的定时任务使用 GitHub 自动生成、仅限本仓库的 Token，不需要个人访问令牌。

## 自动化

- 每天北京时间 08:17 自动扫描。
- 支持从 Actions 页面手动运行。
- 测试通过且报告发生变化后，由 `github-actions[bot]` 更新 `README.md` 和 `data/`。
- API 或数据校验失败时任务失败，不覆盖上一份成功报告。

## 测试

```bash
python -m unittest discover -s tests -v
```

## 数据

- `data/latest.json`：最近一次成功快照。
- `data/history/YYYY-MM-DD.json`：按 UTC 日期保存的历史快照；同日重复运行覆盖当日文件。

## 许可证

[MIT](LICENSE)

