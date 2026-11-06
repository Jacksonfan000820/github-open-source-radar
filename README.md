# GitHub Open Source Radar

一个完全运行在 GitHub 上的开源项目雷达。它使用 GitHub 官方仓库搜索 API 发现近期新晋或持续活跃的高关注项目，并通过相邻成功快照计算 Star 增量。

> 这里的“热门”是透明、可配置的代理指标，不等同于 GitHub Trending 的官方排名。脚本不会克隆或执行被扫描仓库的代码。

<!-- RADAR:START -->

## 最新雷达

- UTC：`2026-11-06T06:56:48Z`
- 北京时间：`2026-11-06T14:56:48+08:00`
- 数据源：GitHub REST Search repositories API
- 排除候选：40 个
- 说明：Star 增量按相邻两次成功快照计算。

### 新晋热门项目

查询规则：`created:>=2026-10-07 stars:>=100 fork:false archived:false`

| 项目 | Stars | 增量 | 语言 | 许可证 | 最近推送 | 简介 |
|---|---:|---:|---|---|---|---|
| [deepseek-ai/DeepInfer](https://github.com/deepseek-ai/DeepInfer) | 25,501 | +89 | Python | Apache-2.0 | 2026-11-03 | DeepInfer: High-performance, large-scale inference framework for DeepSeek models |
| [wheresryan22/anatomy](https://github.com/wheresryan22/anatomy) | 25,347 | +348 | JavaScript | MIT | 2026-10-18 | An agent skill for creating detailed, interactive isometric illustrations of real-world machines and complex systems. G… |
| [deepseek-ai/dsh-superagent-prototype](https://github.com/deepseek-ai/dsh-superagent-prototype) | 19,777 | +875 | TypeScript | MIT | 2026-11-03 | Towards a More Autonomous Agent System |
| [storytold/wordcraft](https://github.com/storytold/wordcraft) | 17,423 | +98 | Rust | Apache-2.0 | 2026-11-06 | An open-source, clean-room reimplementation of Microsoft Word in pure Rust |
| [storytold/craft-anything](https://github.com/storytold/craft-anything) | 15,904 | +2934 | Rust | Apache-2.0 | 2026-11-06 | Craft Anything: understand how any software works, and craft your own. |
| [tangency-labs/solidcraft](https://github.com/tangency-labs/solidcraft) | 14,275 | +472 | Rust | Apache-2.0 | 2026-11-06 | SolidCraft: an open-source parametric 3D CAD application built in pure Rust. Desktop, web, and automation through MCP. |
| [seedds/nxnative](https://github.com/seedds/nxnative) | 12,640 | +378 | Python | MIT | 2026-11-06 | Switch games running natively on iPhone, iPad and Mac: an NSP folder becomes an unsigned IPA (NSO rewriter, Horizon HLE… |
| [ccch1mneyyy/dsh-Go](https://github.com/ccch1mneyyy/dsh-Go) | 12,006 | +1794 | Dart | AGPL-3.0 | 2026-11-06 | dsh-go — DeepSeek Harness 装进口袋：手机本机运行，也能遥控你的电脑。 |
| [pengchujin/aerial-tv](https://github.com/pengchujin/aerial-tv) | 10,125 | +397 | Kotlin | MIT | 2026-11-06 | 给国产电视的一块干净桌面：参照 tvOS 设计的开源 Android TV 桌面，没有广告，开机自动接管。A tvOS-style launcher for Xiaomi, TCL and other China-market TVs. |
| [heydamir/unslop](https://github.com/heydamir/unslop) | 10,089 | +1165 | JavaScript | CC-BY-4.0 | 2026-11-01 | A Claude skill that turns vibecoded, AI-looking UI into a designed interface |
| [storytold/cadcraft](https://github.com/storytold/cadcraft) | 7,721 | +61 | Rust | Apache-2.0 | 2026-11-06 | CADCraft: computer-aided design and drafting — an open-source, clean-room AutoCAD-style app in pure Rust |
| [HeyPuter/everything](https://github.com/HeyPuter/everything) | 7,357 | +160 | JavaScript | MIT | 2026-11-06 | We're rebuilding and open-sourcing the world’s software from scratch. |
| [wangzan101/Mika](https://github.com/wangzan101/Mika) | 7,234 | +424 | Kotlin | Apache-2.0 | 2026-11-05 | An on-device AI agent for Android that operates apps and the web to get things done for you. |
| [storytold/gridcraft](https://github.com/storytold/gridcraft) | 7,218 | +47 | Rust | Apache-2.0 | 2026-11-05 | GridCraft: an open-source, clean-room spreadsheet (Microsoft Excel-style) in pure Rust. By ArtCraft. |
| [unclebob/ub-mode](https://github.com/unclebob/ub-mode) | 7,146 | +133 | - | MIT | 2026-11-02 | - |
| [ly05010419/MacNativeGames](https://github.com/ly05010419/MacNativeGames) | 7,124 | +70 | C | MIT | 2026-11-05 | Play your own Tears of the Kingdom and Breath of the Wild natively on Apple silicon Mac, iPhone and iPad. Not an emulat… |
| [l0ng-ai/openidea](https://github.com/l0ng-ai/openidea) | 6,984 | +619 | TypeScript | Apache-2.0 | 2026-11-06 | The IDE you know, rebuilt in Rust. IntelliJ IDEA–style keymap, tool windows and search-everywhere in a fast native app:… |
| [rddmwmddr/android-ad-cleaner](https://github.com/rddmwmddr/android-ad-cleaner) | 6,613 | +216 | Python | MIT | 2026-11-06 | 关掉国产安卓手机系统里的广告、热搜、资讯推荐和营销推送。不 root，可还原，支持 AI 智能体一键执行。 |
| [ARahim3/DigUp](https://github.com/ARahim3/DigUp) | 6,273 | +26 | Swift | MIT | 2026-10-26 | Search your computer by what's in your files: photos, PDFs, documents, recordings, videos and code. On-device on Mac, W… |
| [simbasjungles/free-my-tv](https://github.com/simbasjungles/free-my-tv) | 5,936 | +43 | Java | MIT | 2026-10-31 | A fast, ad-free home screen for Google TV, LG webOS and Samsung Tizen. One button to undo. |

### 近期活跃项目

查询规则：`pushed:>=2026-10-30 stars:>=1000 fork:false archived:false`

| 项目 | Stars | 增量 | 语言 | 许可证 | 最近推送 | 简介 |
|---|---:|---:|---|---|---|---|
| [public-apis/public-apis](https://github.com/public-apis/public-apis) | 496,496 | +310 | Python | MIT | 2026-11-05 | A collective list of free APIs |
| [freeCodeCamp/freeCodeCamp](https://github.com/freeCodeCamp/freeCodeCamp) | 458,629 | +63 | TypeScript | BSD-3-Clause | 2026-11-06 | freeCodeCamp.org's open-source codebase and curriculum. Learn math, programming, and computer science for free. |
| [morluto/rea](https://github.com/morluto/rea) | 435,387 | +3454 | TypeScript | MIT | 2026-11-06 | Reverse engineer anything with agents, from app behavior down to native binaries. |
| [EbookFoundation/free-programming-books](https://github.com/EbookFoundation/free-programming-books) | 401,016 | +127 | Python | CC-BY-4.0 | 2026-11-01 | :books: Freely available programming books |
| [openclaw/openclaw](https://github.com/openclaw/openclaw) | 394,012 | +79 | TypeScript | MIT | 2026-11-06 | The AI that really does things. Any OS. Any Platform. The lobster way. 🦞 |
| [jwasham/coding-interview-university](https://github.com/jwasham/coding-interview-university) | 364,011 | 基线 | - | CC-BY-SA-4.0 | 2026-11-06 | A complete computer science study plan to become a software engineer. |
| [mattpocock/skills](https://github.com/mattpocock/skills) | 315,711 | +1983 | Shell | MIT | 2026-11-05 | Skills for Real Engineers. Straight from my .agents directory. |
| [obra/superpowers](https://github.com/obra/superpowers) | 313,168 | +583 | Shell | MIT | 2026-11-03 | An agentic skills framework &amp; software development methodology that works. |
| [affaan-m/ECC](https://github.com/affaan-m/ECC) | 298,020 | +608 | JavaScript | MIT | 2026-11-06 | The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development… |
| [practical-tutorials/project-based-learning](https://github.com/practical-tutorials/project-based-learning) | 289,157 | +91 | Python | MIT | 2026-11-02 | Curated list of project-based tutorials |
| [deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness) | 274,183 | +1166 | TypeScript | MIT | 2026-11-04 | DeepSeek Harness: Everything is a Plugin. |
| [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | 260,971 | +300 | Python | MIT | 2026-11-06 | The agent that grows with you |
| [react/react](https://github.com/react/react) | 252,016 | +40 | JavaScript | MIT | 2026-11-05 | The library for web and native user interfaces. |
| [TheAlgorithms/Python](https://github.com/TheAlgorithms/Python) | 225,915 | +29 | Python | MIT | 2026-11-02 | All Algorithms implemented in Python |
| [anomalyco/opencode](https://github.com/anomalyco/opencode) | 224,872 | +218 | TypeScript | MIT | 2026-11-06 | The open source coding agent. |
| [yt-dlp/yt-dlp](https://github.com/yt-dlp/yt-dlp) | 205,616 | +288 | Python | Unlicense | 2026-11-04 | A feature-rich command-line audio/video downloader |
| [tensorflow/tensorflow](https://github.com/tensorflow/tensorflow) | 201,311 | -3 | C++ | Apache-2.0 | 2026-11-06 | An Open Source Machine Learning Framework for Everyone |
| [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | 199,032 | +295 | TypeScript | AGPL-3.0 | 2026-11-06 | Supercharge your AI agents with data from the web and beyond. Building the library for superintelligence. 🔥 |
| [ultraworkers/claw-code](https://github.com/ultraworkers/claw-code) | 194,947 | -14 | Rust | MIT | 2026-11-04 | An agent-managed museum exhibit, built in Rust with Gajae-Code / LazyCodex — developed and maintained with no human int… |
| [microsoft/vscode](https://github.com/microsoft/vscode) | 194,760 | +108 | TypeScript | MIT | 2026-11-06 | Visual Studio Code |

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

