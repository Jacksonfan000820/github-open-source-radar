# GitHub Open Source Radar

一个完全运行在 GitHub 上的开源项目雷达。它使用 GitHub 官方仓库搜索 API 发现近期新晋或持续活跃的高关注项目，并通过相邻成功快照计算 Star 增量。

> 这里的“热门”是透明、可配置的代理指标，不等同于 GitHub Trending 的官方排名。脚本不会克隆或执行被扫描仓库的代码。

<!-- RADAR:START -->

## 最新雷达

- UTC：`2026-08-28T11:29:51Z`
- 北京时间：`2026-08-28T19:29:51+08:00`
- 数据源：GitHub REST Search repositories API
- 排除候选：45 个
- 说明：Star 增量按相邻两次成功快照计算。

### 新晋热门项目

查询规则：`created:>=2026-07-29 stars:>=100 fork:false archived:false`

| 项目 | Stars | 增量 | 语言 | 许可证 | 最近推送 | 简介 |
|---|---:|---:|---|---|---|---|
| [deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness) | 201,387 | +2187 | TypeScript | MIT | 2026-08-27 | DeepSeek Harness: Everything is a Plugin. |
| [anywhere-labs/dsh-desktop](https://github.com/anywhere-labs/dsh-desktop) | 21,412 | +387 | TypeScript | MIT | 2026-08-28 | 为 DeepSeek Harness (DSH) 插件生态打造的现代化桌面端解决方案。万物皆「插件」，桌面本身也是「插件」。 |
| [firecrawl/anydoc](https://github.com/firecrawl/anydoc) | 18,952 | +338 | Rust | MIT | 2026-08-28 | Convert Word, PowerPoint, Excel, OpenDocument, RTF, EPUB, CSV, and PDF to clean Markdown. Built in Rust, with Node.js a… |
| [guillaumemeyer/watermarks-remover](https://github.com/guillaumemeyer/watermarks-remover) | 18,944 | +312 | Python | MIT | 2026-08-28 | Strip multi-vendor AI provenance marks: Unicode text hygiene, statistical rewrite hooks, and C2PA/metadata from PNG/JPE… |
| [yc-software/qm](https://github.com/yc-software/qm) | 14,287 | +31 | TypeScript | MIT | 2026-08-28 | Multiplayer agent harness for work. |
| [awesome-dsh-plugin/awesome-dsh-plugin](https://github.com/awesome-dsh-plugin/awesome-dsh-plugin) | 13,325 | +223 | Python | CC0-1.0 | 2026-08-28 | A curated list of plugins for DeepSeek Harness (dsh) · DeepSeek Harness 插件精选列表 |
| [trycompai/crm](https://github.com/trycompai/crm) | 9,035 | +55 | TypeScript | MIT | 2026-08-21 | Comp AI CRM is an open source, CRM designed for AI agents. Agentic-first CRM. |
| [pathwaycom/arc-task-gen](https://github.com/pathwaycom/arc-task-gen) | 8,058 | +1144 | Python | MIT | 2026-08-11 | Generates original ARC-AGI-1-style tasks distribution-matched to the public eval set. |
| [yjh051108/dsh-routing-suite](https://github.com/yjh051108/dsh-routing-suite) | 6,922 | +45 | JavaScript | MIT | 2026-08-24 | dsh-routing-suite — injector + router-standard kit: install the runtime injector first, then the task-aware reasoning-m… |
| [FareedKhan-dev/kimi-k3-in-c](https://github.com/FareedKhan-dev/kimi-k3-in-c) | 6,637 | +91 | C | Apache-2.0 | 2026-08-26 | A 2.78-trillion-parameter Kimi K3 running inference on a single CPU in 8.24 GB of RAM. Portable C99: no BLAS, no framew… |
| [bashalarmistalt/decimen-optical-transfer](https://github.com/bashalarmistalt/decimen-optical-transfer) | 6,540 | +29 | TypeScript | AGPL-3.0 | 2026-08-26 | - |
| [zhu1090093659/dsh-web](https://github.com/zhu1090093659/dsh-web) | 6,354 | +106 | TypeScript | Apache-2.0 | 2026-08-28 | DeepSeek Harness（DSH）Web 插件聚合生态包 · 一切皆插件，创意工坊分发 |
| [arvids-unavailable/openGym](https://github.com/arvids-unavailable/openGym) | 6,181 | +49 | JavaScript | AGPL-3.0 | 2026-08-03 | https://github.com/DuarteSantos8/openGym |
| [s1dashu/ip-as-logo-skill](https://github.com/s1dashu/ip-as-logo-skill) | 4,485 | +70 | - | MIT | 2026-08-22 | A compact Agent Skill for highly simplified, rounded, subtly neo-skeuomorphic IP mascot logos. |
| [MengTo/threeui](https://github.com/MengTo/threeui) | 4,384 | +126 | HTML | MIT | 2026-08-28 | Open-source ThreeUI Community catalog with live interactive components and complete Community source. |
| [genspark-ai/genoffice](https://github.com/genspark-ai/genoffice) | 3,853 | +65 | TypeScript | Apache-2.0 | 2026-08-27 | Free, open-source AI office suite for macOS, Windows &amp; Linux — Word (.docx), Excel (.xlsx), PowerPoint (.pptx), PDF and… |
| [dmmulroy/anti-slop](https://github.com/dmmulroy/anti-slop) | 3,832 | +43 | TypeScript | MIT | 2026-08-18 | Opinionated Oxlint rules for rejecting low-evidence TypeScript and JavaScript patterns |
| [microsoft/skill-recorder](https://github.com/microsoft/skill-recorder) | 3,606 | +129 | TypeScript | MIT | 2026-08-24 | Desktop app that records your on-screen work session and uses the GitHub Copilot CLI to reconstruct it as an intent + o… |
| [CopilotKit/OpenBot](https://github.com/CopilotKit/OpenBot) | 3,240 | +144 | TypeScript | MIT | 2026-08-28 | Open-source AI coworkers that each get a computer of their own: a browser, files and tools, with every action decided b… |
| [KKKKhazix/human-writing](https://github.com/KKKKhazix/human-writing) | 3,233 | +54 | Python | MIT | 2026-08-11 | 让 AI 写的中文读起来像一个具体的人在说话。通用创作与改稿 Skill，开箱即用。 |

### 近期活跃项目

查询规则：`pushed:>=2026-08-21 stars:>=1000 fork:false archived:false`

| 项目 | Stars | 增量 | 语言 | 许可证 | 最近推送 | 简介 |
|---|---:|---:|---|---|---|---|
| [sindresorhus/awesome](https://github.com/sindresorhus/awesome) | 500,708 | +366 | - | CC0-1.0 | 2026-08-21 | 😎 Awesome lists about all kinds of interesting topics \[NOTE: Pull requests are temporarily disabled until I have a chan… |
| [public-apis/public-apis](https://github.com/public-apis/public-apis) | 472,020 | +697 | Python | MIT | 2026-08-26 | A collective list of free APIs |
| [freeCodeCamp/freeCodeCamp](https://github.com/freeCodeCamp/freeCodeCamp) | 454,722 | +58 | TypeScript | BSD-3-Clause | 2026-08-28 | freeCodeCamp.org's open-source codebase and curriculum. Learn math, programming, and computer science for free. |
| [practical-tutorials/project-based-learning](https://github.com/practical-tutorials/project-based-learning) | 281,149 | +117 | Python | MIT | 2026-08-24 | Curated list of project-based tutorials |
| [react/react](https://github.com/react/react) | 247,999 | +23 | JavaScript | MIT | 2026-08-28 | The library for web and native user interfaces. |
| [affaan-m/ECC](https://github.com/affaan-m/ECC) | 243,855 | +248 | JavaScript | MIT | 2026-08-28 | The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development… |
| [mattpocock/skills](https://github.com/mattpocock/skills) | 239,700 | +1248 | Shell | MIT | 2026-08-24 | Skills for Real Engineers. Straight from my .agents directory. |
| [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | 237,546 | +438 | Python | MIT | 2026-08-28 | The agent that grows with you |
| [TheAlgorithms/Python](https://github.com/TheAlgorithms/Python) | 224,072 | +18 | Python | MIT | 2026-08-28 | All Algorithms implemented in Python |
| [anomalyco/opencode](https://github.com/anomalyco/opencode) | 202,080 | +242 | TypeScript | MIT | 2026-08-28 | The open source coding agent. |
| [deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness) | 201,387 | +2187 | TypeScript | MIT | 2026-08-27 | DeepSeek Harness: Everything is a Plugin. |
| [tensorflow/tensorflow](https://github.com/tensorflow/tensorflow) | 197,759 | +40 | C++ | Apache-2.0 | 2026-08-28 | An Open Source Machine Learning Framework for Everyone |
| [microsoft/vscode](https://github.com/microsoft/vscode) | 189,748 | +40 | TypeScript | MIT | 2026-08-28 | Visual Studio Code |
| [ohmyzsh/ohmyzsh](https://github.com/ohmyzsh/ohmyzsh) | 189,418 | +12 | Shell | MIT | 2026-08-25 | 🙃   A delightful community-driven (with 2,500+ contributors) framework for managing your zsh configuration. Includes 30… |
| [yt-dlp/yt-dlp](https://github.com/yt-dlp/yt-dlp) | 187,482 | +225 | Python | Unlicense | 2026-08-27 | A feature-rich command-line audio/video downloader |
| [avelino/awesome-go](https://github.com/avelino/awesome-go) | 182,500 | +103 | Go | MIT | 2026-08-27 | A curated list of awesome Go frameworks, libraries and software |
| [ollama/ollama](https://github.com/ollama/ollama) | 179,621 | +80 | Go | MIT | 2026-08-28 | Get up and running with Kimi-K2.6, GLM-5.2, MiniMax, DeepSeek, gpt-oss, Qwen, Gemma and other models. |
| [flutter/flutter](https://github.com/flutter/flutter) | 178,688 | +20 | Dart | BSD-3-Clause | 2026-08-28 | Flutter makes it easy and fast to build beautiful apps for mobile and beyond |
| [github/gitignore](https://github.com/github/gitignore) | 175,478 | +8 | - | CC0-1.0 | 2026-08-25 | A collection of useful .gitignore templates |
| [twbs/bootstrap](https://github.com/twbs/bootstrap) | 174,666 | +4 | MDX | MIT | 2026-08-27 | The most popular HTML, CSS, and JavaScript framework for developing responsive, mobile first projects on the web. |

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

