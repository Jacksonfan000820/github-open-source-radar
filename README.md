# GitHub Open Source Radar

一个完全运行在 GitHub 上的开源项目雷达。它使用 GitHub 官方仓库搜索 API 发现近期新晋或持续活跃的高关注项目，并通过相邻成功快照计算 Star 增量。

> 这里的“热门”是透明、可配置的代理指标，不等同于 GitHub Trending 的官方排名。脚本不会克隆或执行被扫描仓库的代码。

<!-- RADAR:START -->

## 最新雷达

- UTC：`2026-11-23T07:50:05Z`
- 北京时间：`2026-11-23T15:50:05+08:00`
- 数据源：GitHub REST Search repositories API
- 排除候选：34 个
- 说明：Star 增量按相邻两次成功快照计算。

### 新晋热门项目

查询规则：`created:>=2026-10-24 stars:>=100 fork:false archived:false`

| 项目 | Stars | 增量 | 语言 | 许可证 | 最近推送 | 简介 |
|---|---:|---:|---|---|---|---|
| [storytold/craft-anything](https://github.com/storytold/craft-anything) | 41,554 | +984 | Rust | Apache-2.0 | 2026-11-23 | Craft Anything: understand how any software works, and craft your own. |
| [ccch1mneyyy/dsh-Go](https://github.com/ccch1mneyyy/dsh-Go) | 30,415 | +625 | Dart | AGPL-3.0 | 2026-11-23 | dsh-go — DeepSeek Harness 装进口袋：手机本机运行，也能遥控你的电脑。 |
| [deepseek-ai/dsh-superagent-prototype](https://github.com/deepseek-ai/dsh-superagent-prototype) | 24,299 | +114 | TypeScript | MIT | 2026-11-03 | Towards a More Autonomous Agent System |
| [heydamir/unslop](https://github.com/heydamir/unslop) | 20,454 | +584 | JavaScript | CC-BY-4.0 | 2026-11-15 | A Claude skill that turns vibecoded, AI-looking UI into a designed interface |
| [ItsNotRexed/Leonida](https://github.com/ItsNotRexed/Leonida) | 17,306 | +9668 | Python | GPL-3.0 | 2026-11-23 | Leonida Is A Native PC Recompilation Of The Xbox Version Of Grand Theft Auto 6 |
| [anefzaoui/misterdownloadmanager](https://github.com/anefzaoui/misterdownloadmanager) | 16,910 | +911 | Rust | GPL-3.0 | 2026-11-23 | misterdownloadmanager: The ultimate open-source, clean-room download manager written from scratch in pure Rust for Wind… |
| [libracoder/kiri](https://github.com/libracoder/kiri) | 12,445 | +334 | Rust | Apache-2.0 | 2026-11-22 | A small, fast container runtime for macOS, Windows and Linux with free Ngrok alternative |
| [JuneYaooo/rea-video](https://github.com/JuneYaooo/rea-video) | 12,367 | +433 | Python | Apache-2.0 | 2026-11-23 | Reverse-engineer any video, shot by shot: filmed, AI-generated or coded, and how to remake it. Breakdowns in the open V… |
| [janestreet/agent\_skills](https://github.com/janestreet/agent_skills) | 10,902 | +315 | - | MIT | 2026-11-17 | Agent skills |
| [zortos293/Lichii](https://github.com/zortos293/Lichii) | 10,097 | +83 | C++ | GPL-3.0 | 2026-11-23 | VERY experimental Nintendo Switch 2 emulator |
| [wangzan101/Mika](https://github.com/wangzan101/Mika) | 9,700 | +175 | Kotlin | Apache-2.0 | 2026-11-23 | An on-device AI agent for Android that operates apps and the web to get things done for you. |
| [RoutineMiku/apkstart](https://github.com/RoutineMiku/apkstart) | 9,326 | +252 | JavaScript | MIT | 2026-11-22 | Windows 上的安卓应用运行器：双击 APK 即装，应用以独立窗口与桌面图标运行，自持 QEMU 运行时 |
| [huami1314/GestaltX](https://github.com/huami1314/GestaltX) | 8,827 | +68 | Swift | GPL-3.0 | 2026-11-17 | An MobileGestalt editor for iOS 27.x, featuring region-code tweaks, device presets, backups. |
| [patch-gg/pixelfx](https://github.com/patch-gg/pixelfx) | 8,807 | +138 | JavaScript | MIT | 2026-11-13 | 244 pixel art effects, every one a small piece of code. Plus a Claude Code skill to make your own. |
| [rddmwmddr/android-ad-cleaner](https://github.com/rddmwmddr/android-ad-cleaner) | 8,802 | +99 | Python | MIT | 2026-11-21 | 关掉国产安卓手机系统里的广告、热搜、资讯推荐和营销推送。不 root，可还原，支持 AI 智能体一键执行。 |
| [unclebob/ub-mode](https://github.com/unclebob/ub-mode) | 8,380 | +71 | - | MIT | 2026-11-02 | - |
| [erkamyaman/rust-anything](https://github.com/erkamyaman/rust-anything) | 8,212 | +649 | Rust | MIT | 2026-11-23 | Rewrite your whole app in Rust, one piece at a time, checked against the original's recorded behavior at every step. CL… |
| [valentderah/totk-pc-recomp](https://github.com/valentderah/totk-pc-recomp) | 8,073 | +130 | C | MIT | 2026-11-23 | Static recompilation of The Legend of Zelda: Tears of the Kingdom to native Windows and Linux x86-64, with a Vulkan ren… |
| [Lee-xeo/Claude-Cage](https://github.com/Lee-xeo/Claude-Cage) | 7,870 | +416 | Go | MIT | 2026-11-23 | Cage：为 Claude 特化的轻量化虚拟机，彻底杜绝网络泄露。多平台适配，支持多账号管理、远程部署、移动端操控。 |
| [mdiri-ai/SoduWork](https://github.com/mdiri-ai/SoduWork) | 6,858 | +333 | JavaScript | MIT | 2026-11-23 | The AI-native engine for teams and their agents. Multi-harness, multi-agent, self-hosted. |

### 近期活跃项目

查询规则：`pushed:>=2026-11-16 stars:>=1000 fork:false archived:false`

| 项目 | Stars | 增量 | 语言 | 许可证 | 最近推送 | 简介 |
|---|---:|---:|---|---|---|---|
| [public-apis/public-apis](https://github.com/public-apis/public-apis) | 500,917 | +227 | Python | MIT | 2026-11-22 | A collective list of free APIs |
| [morluto/rea](https://github.com/morluto/rea) | 474,579 | +1483 | TypeScript | MIT | 2026-11-23 | Reverse engineer anything with agents, from app behavior down to native binaries. |
| [freeCodeCamp/freeCodeCamp](https://github.com/freeCodeCamp/freeCodeCamp) | 459,512 | +51 | TypeScript | BSD-3-Clause | 2026-11-23 | freeCodeCamp.org's open-source codebase and curriculum. Learn math, programming, and computer science for free. |
| [EbookFoundation/free-programming-books](https://github.com/EbookFoundation/free-programming-books) | 402,098 | +49 | Python | CC-BY-4.0 | 2026-11-21 | :books: Freely available programming books |
| [openclaw/openclaw](https://github.com/openclaw/openclaw) | 395,070 | +61 | TypeScript | MIT | 2026-11-23 | The AI that really does things. Any OS. Any Platform. The lobster way. 🦞 |
| [mattpocock/skills](https://github.com/mattpocock/skills) | 330,787 | +870 | Shell | MIT | 2026-11-19 | Skills for Real Engineers. Straight from my .agents directory. |
| [affaan-m/ECC](https://github.com/affaan-m/ECC) | 309,174 | +667 | JavaScript | MIT | 2026-11-23 | The agent harness performance optimization system. Skills, instincts, memory, security, and research-first development… |
| [practical-tutorials/project-based-learning](https://github.com/practical-tutorials/project-based-learning) | 290,306 | +81 | Python | MIT | 2026-11-23 | Curated list of project-based tutorials |
| [deepseek-ai/deepseek-harness](https://github.com/deepseek-ai/deepseek-harness) | 285,760 | +542 | TypeScript | MIT | 2026-11-22 | DeepSeek Harness: Everything is a Plugin. |
| [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | 265,515 | +262 | Python | MIT | 2026-11-23 | The agent that grows with you |
| [react/react](https://github.com/react/react) | 252,940 | +83 | JavaScript | MIT | 2026-11-23 | The library for web and native user interfaces. |
| [anomalyco/opencode](https://github.com/anomalyco/opencode) | 228,682 | +218 | TypeScript | MIT | 2026-11-23 | The open source coding agent. |
| [yt-dlp/yt-dlp](https://github.com/yt-dlp/yt-dlp) | 210,075 | +331 | Python | Unlicense | 2026-11-22 | A feature-rich command-line audio/video downloader |
| [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) | 207,299 | +894 | TypeScript | AGPL-3.0 | 2026-11-23 | Knowledge infrastructure to make your agents smarter. Search, scrape and access 550+ data providers through one API. |
| [tensorflow/tensorflow](https://github.com/tensorflow/tensorflow) | 201,785 | +81 | C++ | Apache-2.0 | 2026-11-23 | An Open Source Machine Learning Framework for Everyone |
| [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) | 197,083 | +575 | JavaScript | MIT | 2026-11-22 | Makes your AI agent think like the laziest senior dev in the room. The best code is the code you never wrote. |
| [microsoft/vscode](https://github.com/microsoft/vscode) | 195,792 | +77 | TypeScript | MIT | 2026-11-23 | Visual Studio Code |
| [avelino/awesome-go](https://github.com/avelino/awesome-go) | 195,484 | +205 | Go | MIT | 2026-11-22 | A curated list of awesome Go frameworks, libraries and software |
| [ultraworkers/claw-code](https://github.com/ultraworkers/claw-code) | 194,732 | 基线 | Rust | MIT | 2026-11-23 | An agent-managed museum exhibit, built in Rust with Gajae-Code / LazyCodex — developed and maintained with no human int… |
| [ohmyzsh/ohmyzsh](https://github.com/ohmyzsh/ohmyzsh) | 190,862 | +93 | Shell | MIT | 2026-11-22 | 🙃   A delightful community-driven (with 2,500+ contributors) framework for managing your zsh configuration. Includes 30… |

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

