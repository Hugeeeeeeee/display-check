---
trigger: always_on
description: 显示器自检项目的交付规则：构建产物同步、文案国际化、隐私红线、Git 约定
---

# 项目规则 · 显示器自检（Display Check）

纯静态单页应用：`index.html` + `styles.css` + `app.js` + `build.py`，无框架、无依赖、无网络请求。

## 1. 构建产物必须同步（最容易忘）

改动 `index.html` / `styles.css` / `app.js` / `build.py`（含其中的 `_headers` 模板）之后，**必须立即执行**：

```bash
python3 build.py
```

它会重新生成单文件版 `monitor-check.html` 与站点目录 `site/`（`index.html`、`404.html`、`_headers`、`robots.txt`、`LICENSE`）。
为了让 Cloudflare Pages 不需要在云端跑 Python，**产物是连同源码一起提交的**，所以 `.gitignore` 刻意不忽略 `site/` 与 `monitor-check.html`。

交付前自检：产物内容与源码逐字节一致；`site/` 文件数量与 `build.py` 的写出清单一致（README 的 `site/` 说明也要跟着对齐）。

## 2. 文案一律走语言字典（i18n）

- 所有面向用户的文字都必须进 `app.js` 里的 `ZH` / `EN` 字典，通过 `t(key)` 渲染；**不允许在 HTML 或 JS 中写死文案**。
- 新增/修改界面文案时，`ZH` 与 `EN` **必须同时补齐、键完全对齐**；缺失键会回退中文并显示 `???`。
- 新增第三种语言：只需复制一份字典并在 `STRINGS` 登记，**不得修改渲染逻辑**。
- DOM 钩子三种：`data-i18n`（textContent）、`data-i18n-html`（含 `<kbd>`/`<span>` 的片段）、`data-i18n-attr`（`"attr:key,attr:key"`）。静态 HTML 里的中文只作为首屏兜底，真实值由 JS 按当前语言写入。
- 语言判定顺序：`localStorage` 手动选择值 → `navigator.language` 以 `zh` 开头用 `zh-CN` → 其余 `en`；切换时同步更新 `document.documentElement.lang`，且当前已打开的界面（测试中/报告页/小抄）就地更新，不要求返回首页。
- 测试画面本身（色块、棋盘格、CJK 样张文字、图案）不随语言变化，只翻译说明文字。
- 术语用显示器领域地道英文：dead pixels、banding、backlight bleed、uniformity、ghosting / motion clarity、refresh rate、viewing angle、gamma、grayscale levels、dither。
- 切语言时的红线：不得丢进度、不得重置计时或重测、不得播放多余音效；`localStorage` 不可用（`file://`）时静默兜底。

## 3. 隐私红线（出现即算事故）

- 任何文件、注释、meta、README、导出内容中**禁止**出现真实姓名、真实邮箱、本机绝对路径、磁盘卷名。
- 作者名义统一匿名写法 `The Display Check Authors` + GitHub noreply 邮箱，协议 MIT（`LICENSE` 为唯一事实来源）。
- 提交记录同样受此约束：作者/提交者用 GitHub noreply 地址（`用户名@users.noreply.github.com`）。
- 外链只用普通 `<a target="_blank" rel="noopener noreferrer">`；**禁止** `fetch`、XHR、WebSocket、统计脚本、外部字体、CDN、远程图片，以保持 `_headers` 中 `connect-src 'none'` 始终成立。
- 屏幕参数、标记结果、备注只写 `localStorage`；分享只走本地能力（复制摘要、打印/存 PDF、导出/导入 JSON，以及受控剪贴板权限流程）。
- 交付前对源码与产物做一次隐私字符串扫描，确认无个人路径与邮箱。

## 4. GitHub Star 引导：只改一处

- 仓库地址的唯一来源是 `app.js` 顶部的 `const REPO = '用户名/仓库名'`（不带 `https://`）；`GITHUB_URL` 与 `REPO_READY` 由它派生，首页 Star 入口、报告一次性说明条、打印页脚、文字摘要与备份 JSON 全部引用它。
- `REPO` 仍是占位符 `YOUR_GITHUB_USERNAME` 时，上述入口必须自动隐藏且不留 `localStorage` 痕迹——不允许出现指向不存在页面的链接。
- 说明条只在完成一整轮并首次打开报告时出现一次，可关闭，记录在 `localStorage`；不用弹窗、不施压。
- 改了 `REPO` 必须回到规则第 1 条重跑 `build.py`。
- README 顶部徽章行与 Star 章节都直接指向 `GITHUB_URL` 对应的真实仓库地址；`REPO` 改动时两处一并同步。

## 5. Git 与部署约定

- **不代为执行** `git init` / `commit` / `push` / 远程设置变更，也不改 git 配置；先说明准备执行的命令与内容，得到明确确认后再做。
- 不使用 `push --force`、`branch --force` 等破坏性操作；需要重建历史时改用新建分支。
- 部署：线上站点用 Cloudflare Pages **Direct Upload**（产物 = 仓库里的 `site/`，云端不跑构建）；若要自动部署则改为 GitHub → Pages *Connect to Git* → Framework preset **None**、Build command **留空**、Output directory **`site`**、production branch 与实际分支一致。
- 线上域名 `displaycheck.pages.dev`（Pages 项目名全局唯一，`display-check`、`monitor-check`、`screen-check` 已被他人占用）；README 顶部「打开」小节、「Star」小节与「部署到 Cloudflare Pages」小节的链接都与该域名一致，域名变更时三处一起改。

## 6. 交付前自检清单

1. `osascript -l JavaScript -e "new Function(<app.js 源码>)"` 语法通过（本机无 node）。
2. `python3 build.py` 已执行，产物与源码一致。
3. 中英文各走一遍：首页、10 项测试、HUD、报告、文字摘要、备份 JSON、小抄、打印视图无 `???`、无裸露键名、无空白位。
4. Console 无 error/warning，尤其不得出现 `[i18n] untranslated keys`。
5. 窄屏（约 390px）无横向溢出；`@media print` 下只出报告内容，`.star-bar` 隐藏、`.report-promo` 保留。
6. 语言手动切换后刷新保持；测试中/报告页就地切换不退出流程。
7. 占位符模式下所有 Star 入口隐藏；产物与源码隐私扫描干净。
