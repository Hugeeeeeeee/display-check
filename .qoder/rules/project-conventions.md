---
trigger: always_on
description: 显示器自检项目的交付规则：构建产物同步、文案国际化、隐私红线、渲染安全、Git 与部署约定
---

# 项目规则 · 显示器自检（Display Check）

纯静态单页应用：`index.html` + `styles.css` + `app.js` + `build.py`，无框架、无依赖、无网络请求。文档双语：`README.md`（中文）与 `README.en.md`（English），内容需一一对应。

## 1. 构建产物必须同步（最容易忘）

改动 `index.html` / `styles.css` / `app.js` / `build.py`（含其中的 `_headers` 模板）之后，**必须立即执行**：

```bash
python3 build.py
```

它会重新生成单文件版 `monitor-check.html` 与站点目录 `site/`（`index.html`、`404.html`、`_headers`、`robots.txt`、`LICENSE`）。
为了让 Cloudflare Pages 不需要在云端跑 Python，**产物是连同源码一起提交的**，所以 `.gitignore` 刻意不忽略 `site/` 与 `monitor-check.html`。

交付前自检：`monitor-check.html`、`site/index.html`、`site/404.html` 三者**逐字节相同**（`md5 -r` 对比）；`site/` 文件清单与 `build.py` 的写出列表一致，两份 README 里对 `site/` 的描述也跟着对齐。

## 2. 文案一律走语言字典（i18n）

- 所有面向用户的文字都必须进 `app.js` 里的 `ZH` / `EN` 字典，通过 `t(key)` 渲染；**不允许在 HTML 或 JS 中写死文案**。两份字典键数必须相等（当前各 252 条）。
- 新增/修改界面文案时，`ZH` 与 `EN` **必须同时补齐、键完全对齐**，`{占位符}` 名称也要一致；缺失键会回退中文并显示 `???`。
- 新增第三种语言：只需复制一份字典并在 `STRINGS` 登记，**不得修改渲染逻辑**（`buildLangSeg()`、`nextLang()`、缺项回退都从 `Object.keys(STRINGS)` 自动派生）；另需在 `detectLang()` 补一条浏览器语言映射。
- DOM 钩子三种：`data-i18n`（textContent）、`data-i18n-html`（含 `<kbd>`/`<span>` 的片段）、`data-i18n-attr`（`"attr:key,attr:key"`）。
- 带 `{占位符}` 的键（如 `verdict.remaining`、`verdict.notStartedSub`、`lang.use`、`sub.speedFps`）**不能**直接挂 `data-i18n`，必须由 JS 调 `t(key, params)` 渲染。
- 静态 HTML 里的中文只作为首屏兜底：`#startLabel`、`#statHz`、`#verdictTitle` / `#verdictSub`、`#langSeg` 的 `aria-label` 等真实值都由 JS 写入；想给这些节点补 `data-i18n` 先确认键不含占位符。
- 缺键时 `t()` 返回 `???`，并**按首次出现的键名**打印 `[i18n] untranslated key: <key>`；验收方式是中英各扫一遍界面看有没有 `???`。
- 语言判定顺序：`localStorage` 手动选择值 → `navigator.language` 以 `zh` 开头用 `zh-CN` → 其余 `en`；切换时同步更新 `document.documentElement.lang`、`<title>` 与 `meta` / OG / Twitter 文案，且当前已打开的界面（测试中 / 报告页 / 小抄）就地更新，不要求返回首页。
- 测试画面本身（色块、棋盘格、CJK 与拉丁样张文字、图案）不随语言变化，只翻译说明文字——样张文字本身就是锐度测试的内容。
- 术语用显示器领域地道英文：dead pixels、banding、backlight bleed、uniformity、ghosting / motion clarity、refresh rate、viewing angle、gamma、grayscale levels、dither。
- 切语言时的红线：不得丢进度、不得重置计时或重测、不得播放多余音效；`localStorage` 不可用（`file://`）时静默兜底。

## 3. 隐私红线（出现即算事故）

- 任何文件、注释、meta、README、导出内容中**禁止**出现真实姓名、真实邮箱、本机绝对路径、磁盘卷名。
- 作者名义统一匿名写法 `The Display Check Authors` + GitHub noreply 邮箱，协议 MIT（`LICENSE` 为唯一事实来源）。
- 提交记录同样受此约束：作者 / 提交者用 GitHub noreply 地址（`用户名@users.noreply.github.com`）。
- 外链只用普通 `<a target="_blank" rel="noopener noreferrer">`；**禁止** `fetch`、XHR、WebSocket、统计脚本、外部字体、CDN、远程图片，以保持 `_headers` 中 `connect-src 'none'` 始终成立。README 顶部的 shields.io 徽章属于文档，允许存在，但文档里要写明应用本身与部署站点不请求任何外部资源。
- 屏幕参数、标记结果、备注只写 `localStorage`（三个键：进度 `displaycheck.progress.v1`、语言 `displaycheck.lang.v1`、Star 说明条已读 `displaycheck.starHinted.v1`）；分享只走本地能力（复制摘要、打印 / 存 PDF、导出 / 导入 JSON）。
- 交付前对源码与产物做一次隐私字符串扫描，确认无个人路径与邮箱；**任何 token / 密码 / API Key 都不得写入仓库、README、导出内容，也不得长期留在磁盘**：需要时只作为一次性环境变量传递，任务结束删除临时文件，并提醒使用者吊销该凭据。

## 4. 渲染与浏览器 API 安全

- 任何用户可控文本（备注，以及别人发来的备份 JSON）拼进 `innerHTML` 前必须经过 `esc()` 转义；能用 `textContent` 就不要拼 HTML。
- 导入外部 JSON 必须**白名单校验**：只接受已知测试 id、强制 `typeof === 'string'`、`trim()` 后截断到 300 字，非法项直接丢弃；不得把外部对象整体合并进状态。
- 有用户手势限制的 API（`requestFullscreen`、剪贴板、下载）必须先判定再调用：无手势时静默跳过，避免在 Console 留下浏览器拒绝报错（例如直接打开 `#pixels` 分享链接进入测试）。
- 备注使用浏览器原生 `window.prompt` 填写，因此页面内没有可输入文本的表单元素；新增控件时不要破坏这个前提（否则 `P` / `X` 等快捷键会干扰输入）。

## 5. GitHub Star 引导：只改一处，且只说一次

- 仓库地址的唯一来源是 `app.js` 顶部的 `const REPO = '用户名/仓库名'`（不带 `https://`）；`GITHUB_URL` 与 `REPO_READY` 由它派生，首页 Star 入口、报告一次性说明条、打印页脚、文字摘要与备份 JSON 全部引用它。
- `REPO` 仍是占位符 `YOUR_GITHUB_USERNAME` 时，上述入口必须自动隐藏且不留 `localStorage` 痕迹——不允许出现指向不存在页面的链接。
- 说明条只在完成一整轮并首次打开报告时出现一次，可关闭，记录在 `localStorage`；**不用弹窗、不施压、不在测试进行中打断**。
- 改了 `REPO` 必须回到规则第 1 条重跑 `build.py`。
- 文档侧的 Star 引导共四处 ×2 份文件：`README.md` 与 `README.en.md` 各自的顶部徽章行、置顶引导块、`## Star` / `## Star` 小节、结尾一句；改仓库地址或措辞时两份一起改，语气保持“感谢式”而不是“索取式”。

## 6. Git 与部署约定

- **不代为执行** `git init` / `commit` / `push` / 远程设置变更，也不改 git 配置；先说明准备执行的命令与内容，得到明确确认后再做。
- 不使用 `push --force`、`branch --force` 等破坏性操作；需要重建历史时改用新建分支。
- 部署：线上站点用 Cloudflare Pages **Direct Upload**（产物 = 仓库里的 `site/`，云端不跑构建）；若要自动部署则改为 GitHub → Pages *Connect to Git* → Framework preset **None**、Build command **留空**、Output directory **`site`**、production branch 与实际分支一致。
- 用 API 做 Direct Upload 的顺序是固定的：`GET .../pages/projects/{name}/upload-token` 取 JWT → `POST /pages/assets/check-missing` → `POST /pages/assets/upload`（base64 键值）→ **`POST /pages/assets/upsert-hashes`（漏掉这一步就会“部署成功但是空站”）** → `POST .../deployments`。其中 `manifest` 字段是扁平映射 `{"路径": "文件md5"}`（不是 `{"file": …}` 也不是 `{"checksum": …}`），`_headers` 作为独立的 multipart 文件字段随同一请求提交。
- 线上域名 `displaycheck.pages.dev`（Pages 项目名全局唯一，`display-check`、`monitor-check`、`screen-check` 已被他人占用）。需要同步该域名的位置：`README.md` 与 `README.en.md` 各自的置顶链接行、`## 打开` / `## Open it` 表格、部署小节、`## Star` 小节、`## 许可` / `## License` 小节，共五处 ×2 份文件。

## 7. 交付前自检清单

1. 语法通过（本机无 node，用自带 JXA；注意 JXA 里没有 `require`）：

   ```bash
   osascript -l JavaScript -e "ObjC.import('Foundation'); var s=$.NSString.stringWithContentsOfFileEncodingError('app.js',$.NSUTF8StringEncoding,null).js; new Function(s); 'syntax ok'"
   ```
2. `python3 build.py` 已执行，三个 HTML 产物彼此逐字节相同。
3. 中英文各走一遍：首页、10 项测试、HUD、报告、文字摘要、备份 JSON、小抄、打印视图无 `???`、无裸露键名、无空白位。
4. Console 无 error / warning，尤其不得出现 `[i18n] untranslated key:`，也不得出现全屏被浏览器拒绝的报错。
5. 窄屏（约 390px）无横向溢出、HUD 不溢出；`@media print` 下只出报告内容，`.star-bar` 隐藏、`.report-promo` 保留。
6. 语言手动切换后刷新保持；测试中 / 报告页就地切换不退出流程、不丢进度。
7. 占位符模式下所有 Star 入口隐藏；源码与产物隐私扫描干净（无凭据、无本机路径、无真实姓名邮箱）。
8. 两份 README 的测试清单、控件表、快捷键表、部署方式与隐私条目互相对应，且与代码实况一致（新增测试或快捷键时两处同时改）。
