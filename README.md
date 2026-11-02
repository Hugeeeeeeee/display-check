# 显示器自检 · Display Check

**中文** | [English → README.en.md](README.en.md)

[![License: MIT](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![Offline](https://img.shields.io/badge/100%25-offline-blue)](#隐私与安全)
[![Star on GitHub](https://img.shields.io/badge/Star%20on%20GitHub-display--check-f5a623)](https://github.com/Hugeeeeeeee/display-check)

新显示器到手、二手屏想验货、售后要证据 —— 打开一个网页，10 项全屏测试走完，得到一份能打印、能复制、能导出的检测报告。

- **完全本地**：没有后端、没有统计、没有外部字体与 CDN，浏览器不发出任何对外请求（`connect-src 'none'`）。
- **10 项全屏测试**：坏点、色阶、灰阶、均匀性、漏光、锐度、拖影、刷新率、可视角度、伽马。
- **一份报告**：结论 + 逐项结果 + 备注 + 屏幕信息，支持打印 / 保存 PDF、复制文字摘要、导出备份 JSON。
- **中英双语界面**：按浏览器语言自动选择，`L` 键随时切换。
- **进度只存在本机**：关掉页面再打开，接着测。

> ⭐ **[给这个项目点个 Star](https://github.com/Hugeeeeeeee/display-check)** —— 项目完全匿名、不收一分钱、没有广告，Star 是它唯一能拿到的回报：让更多人（尤其是刚拿到新显示器不知道怎么验的人）能找到它。已经用过的话，[点一下就好](https://github.com/Hugeeeeeeee/display-check)，谢谢。

在线试用：<https://displaycheck.pages.dev> ｜ 仓库：<https://github.com/Hugeeeeeeee/display-check>

## 打开

三种方式任选，都不需要安装、不需要联网：

| 方式 | 适合 |
| --- | --- |
| 双击 `monitor-check.html` | 单文件离线版，发给别人、拷到 U 盘或另一台电脑 |
| 浏览器打开 `index.html` | 本地开发版，依赖同目录的 `styles.css` 与 `app.js` |
| <https://displaycheck.pages.dev> | 直接在线用，内容和单文件版逐字节一致 |

建议用 Chrome / Edge / Safari 的较新版本。进入测试后会自动尝试全屏，但浏览器只允许“真实点击”触发全屏：从首页点卡片、按 `F` 都没问题；直接粘贴带 `#测试名` 的链接进入时不会自动全屏，按 `F` 手动切换即可。

## 10 项测试

按首页卡片顺序，也可以按 `1`–`9`、`0` 直接跳到对应一项。

| # | 测试 | 看什么 |
| --- | --- | --- |
| 1 | 坏点与纯色 | 9 种纯色全屏（白 / 黑 / 红 / 绿 / 蓝 / 青 / 品红 / 黄 / 灰），黑色找亮点、白色找暗点 |
| 2 | 色阶与渐变 | 渐变是否平滑、有没有断层；可切 6 个通道（灰阶 / 暗部 / 亮部 / R / G / B），可开「抖动」排除浏览器插值造成的假断层 |
| 3 | 灰阶细节 | 黑阶 0–10、白阶 245–255 能不能分辨出层次 |
| 4 | 亮度均匀性 | 7 种全屏底色下四角与中心是否偏色、有没有暗角；`G` 叠网格便于定位 |
| 5 | 漏光与黑位 | 关灯看纯黑，边缘有没有光晕、黑位有没有泛白 |
| 6 | 锐度与像素 | 1:1 棋盘格有没有摩尔纹，细线是否连续，小字号文字有没有发虚或彩边 |
| 7 | 响应与拖影 | 高速运动条纹的边缘有没有拖尾、白边或黑边（过冲），速度可调 80–1600 px/s |
| 8 | 刷新与帧同步 | `requestAnimationFrame` 实测帧率，看是否接近标称 Hz、竖条移动是否匀速；同时统计掉帧 |
| 9 | 可视角度 | 四色块 + 中心点，侧视时颜色与亮度不应明显发白或偏色 |
| 10 | 伽马校准 | 棋盘格与纯灰对比，滑块调到左右亮度一致时读数即当前 γ（桌面屏通常在 2.2 附近） |

## 测试内控件

每一项都在底部 HUD 里给了对应控件，`空格` 触发当前测试的主操作：

| 测试 | 控件 | `空格` 的作用 |
| --- | --- | --- |
| 坏点与纯色 | 9 个色块，点击直接切换 | 下一个颜色 |
| 色阶与渐变 | 通道下拉菜单 + 「抖动」开关 | 下一个通道 |
| 灰阶细节 | —（静态图，专注观察） | — |
| 亮度均匀性 | 7 个底色块 + 网格开关（`G`） | 下一个底色 |
| 漏光与黑位 | —（纯黑，建议关灯） | — |
| 锐度与像素 | 黑 / 白背景切换 | 换背景 |
| 响应与拖影 | 速度滑块 80–1600 px/s + 暂停 / 继续 | 暂停 / 继续 |
| 刷新与帧同步 | 暂停 / 继续（顶部实时显示实测 Hz 与掉帧） | 暂停 / 继续 |
| 可视角度 | —（正面看完再侧视） | — |
| 伽马校准 | 纯灰滑块 120–240 + 一键重置 | 重置为 186 |

每一项都能按 `M`（或点底部笔形图标）写 **备注**，例如「右下角漏光」「中央有亮斑」。备注会显示在首页卡片和报告里，并随文字摘要、备份 JSON 一起导出，只保存在你的浏览器。

## 快捷键

| 按键 | 作用 |
| --- | --- |
| `←` `→` | 上一个 / 下一个测试 |
| `空格` | 当前测试的主操作（换颜色、换通道、暂停等）；焦点在 HUD 控件上时让给控件本身 |
| `P` / `X` | 标记正常 / 异常 |
| `M` | 给当前项写备注 |
| `G` | 均匀性测试显示网格 |
| `F` | 全屏 / 退出全屏 |
| `R` | 打开 / 关闭检测报告 |
| `T` / `?` / `F1` | 打开判定小抄与快捷键面板 |
| `L` | 切换界面语言 / switch language |
| `1`–`9` `0` | 在首页直接打开第 1–9 项与第 10 项 |
| `Esc` | 退出全屏；不在全屏时返回首页 / 关闭报告 / 关闭小抄 |

按住 `Ctrl` / `Cmd` / `Alt` 的组合键不会触发这里的快捷键；焦点落在 HUD 控件（色块、下拉菜单、滑块、按钮）上时，`空格` 交给控件本身而不是当前测试的主操作。备注用浏览器原生输入框填写，因此窗口里没有任何可输入文本的表单元素。

触屏：测试中 **左右滑动** 切换上/下一项，**双击屏幕** 标记为正常。

## 使用流程

1. 点首页 **开始完整检测** —— 从第一个未测项开始，并开启连续模式。
2. 每项看完按 `P`（正常）或 `X`（异常），连续模式自动进入下一项。
3. 第 10 项标记完自动生成 **检测报告**：结论、逐项结果、备注、屏幕信息（分辨率 / 实测刷新率 / 像素比 / 色域与 HDR 能力）。
4. 报告上可以：
   - **打印 / 保存 PDF**：走浏览器打印，排版专为 A4 调整过，页脚带上项目地址；
   - **复制文字摘要**：纯文本，直接粘进聊天记录或售后工单；
   - **备份进度 / 恢复进度**：导出、导入 JSON，换电脑或换设备接着测；
   - **重新检测**：清空本轮结果。
5. 单独点首页卡片看某一项时不会自动跳到下一项；随时按 `R` 或点右上角图标看报告。

## 判定小抄

不确定结果怎么读时按 `T`（或 `?`），应用内就有完整判读标准；以下是同一份内容：

- **坏点**：纯色下出现常亮白点、彩点或不亮的黑点即为坏点 / 亮点。
- **色阶**：渐变出现明显竖条纹说明色深或伽马处理不佳；开启 **抖动** 后仍然断层才可疑（抖动用于排除浏览器插值造成的假性断层）。
- **灰阶**：黑阶能分辨到 2–3 级、白阶 245–255 有层次即可。
- **均匀性**：四角与中心不应有明显暗角或偏色；轻微差异属正常。
- **漏光**：IPS 轻微角落漏光正常，大面积光晕或泛白可考虑退换。
- **锐度**：1:1 棋盘格不应出现摩尔纹；文字不应发虚或出现明显彩边。
- **拖影**：运动条纹边缘不应有长拖尾、白边或黑边（过冲）。
- **刷新**：实测 Hz 应接近标称值，竖条移动应匀速无跳格。
- **视角**：侧视时颜色不应明显泛白、偏色或丢失细节。
- **伽马**：滑块在 186 附近两侧亮度一致，说明 γ 接近 2.2。

## 测试建议

1. 使用显示器原生分辨率，系统缩放设为 100%（高 DPI 屏可按系统推荐值，但缩放会破坏 1:1 像素测试）。
2. 关闭夜间模式、护眼模式、HDR 以及厂商的色彩增强 / 锐化后再测。
3. 坏点、漏光、灰阶建议在暗室进行，并让屏幕预热 20–30 分钟。
4. 响应与刷新测试尽量在独立全屏窗口里做，浏览器后台标签页会限制动画帧率。

## 语言

- **界面语言**只有两个：简体中文（`zh-CN`）与 English（`en`），全部文案各自 252 条，逐键对齐，没有占位缺项。
- 优先读上次手动选择的值（`localStorage` 的 `displaycheck.lang.v1`），没选过时按浏览器语言判断：`zh*` 用简体中文，其余用 English。
- 切换入口：首页右上角「中 / EN」分段控件、测试中与报告页右上角的语言按钮、键盘 `L`（多语言时循环切换）。切换后当前测试、报告、小抄、摘要立即更新，不用返回首页。
- 报告文字摘要、备份 JSON、打印页脚、`<title>`、`meta description`、Open Graph / Twitter 卡片文案都跟随当前语言；测试画面本身（色块、棋盘格、汉字与拉丁样张）不随语言变化 —— 样张文字本身就是锐度测试内容。
- **加第三种语言**：在 `app.js` 里复制一份 `ZH` 字典改文案、按语言代码命名，然后在 `STRINGS` 里登记一行；分段控件、`L` 键循环、缺项回退全部自动生效。另外在 `detectLang()` 里补一句浏览器语言到该代码的映射。字典缺项会回退到中文并在界面显示 `???`、在 Console 打印该键名，不会出现空白或裸露键名 —— 因此新增语言后可以用“全界面扫一遍有没有 `???`”来做验收。

## 目录结构

```
index.html                 开发版页面（引用下面两个文件）
styles.css                 全部样式，含打印样式
app.js                     全部逻辑与中英文案
build.py                   打包：生成单文件版与 site/
monitor-check.html         产物：单文件离线版（内联样式与脚本）
site/                      产物：可直接部署的静态站点
  index.html 404.html      页面（404.html 内容与 index.html 相同，任何路径都能打开工具）
  _headers                 安全响应头与缓存策略
  robots.txt  LICENSE
.qoder/rules/              项目自有的开发与交付约定
```

## 构建

```bash
python3 build.py
```

只有标准库，无需安装任何依赖。产物：

- `monitor-check.html` —— 单文件离线版，`styles.css` 与 `app.js` 内联进去；
- `site/` —— 部署目录，`index.html` 与 `404.html` 内容等同单文件版。

改完 `index.html` / `styles.css` / `app.js`，或 `build.py` 里的 `_headers` 模板之后，**必须**再执行一次 `python3 build.py`，否则线上产物与源码不同步。三个 HTML 产物应当逐字节一致，可以用 `md5 -r monitor-check.html site/index.html site/404.html` 自检。

本机没有 Node 也可以验证 `app.js` 语法（macOS 自带的 JXA，注意这里没有 `require`）：

```bash
osascript -l JavaScript -e "ObjC.import('Foundation'); var s=$.NSString.stringWithContentsOfFileEncodingError('app.js',$.NSUTF8StringEncoding,null).js; new Function(s); 'syntax ok'"
```

## 部署到 Cloudflare Pages

线上站点 <https://displaycheck.pages.dev> 用 **Direct Upload** 部署，产物就是仓库里的 `site/`，云端不执行任何构建。更新两种方式任选：

1. **Direct Upload**：本地先 `python3 build.py`，再把 `site/` 拖进 Pages 项目的上传区，或用 wrangler 一条命令：

   ```bash
   npx wrangler pages deploy site --project-name displaycheck
   ```

2. **连接 Git 自动部署**：在 Cloudflare Pages 选择 *Connect to Git* 并选中本仓库，**Framework preset: None**、**Build command 留空**、**Output directory** 填 `site`、production branch 填 `main`。`site/` 已提交在仓库里，云端无需构建；之后每次 `git push` 自动重新部署，几分钟生效。

pages.dev 的项目名 **全局唯一**：`display-check`、`monitor-check`、`screen-check` 已被他人占用，本项目用的是 `displaycheck`。自行部署时若提示名称已存在，换名后记得同步改本文件顶部、这里以及 [README.en.md](README.en.md) 里的链接。

`site/_headers` 已经配好安全响应头与 HTML 不缓存，不需要在平台上额外设置。

## 隐私与安全

页面不发任何请求，这一点由代码和响应头双重保证：

- 无后端、无统计、无广告、无外部字体与 CDN；`Content-Security-Policy: connect-src 'none'` 在响应头层面封死对外连接，`base-uri 'none'`、`form-action 'none'` 断掉跳转与提交。
- 不采集也不上传屏幕参数、标记结果与备注。它们只存在浏览器 `localStorage` 的三个键里（进度 `displaycheck.progress.v1`、语言 `displaycheck.lang.v1`、Star 提示的已读标记 `displaycheck.starHinted.v1`），清空浏览器数据即彻底删除。
- 分享结果全靠本地产物：复制文字摘要、打印 / 保存 PDF、导出备份 JSON，内容完全由你决定。
- 响应头关闭摄像头 / 麦克风 / 定位 / 支付 / USB / 各类传感器权限，发送 `Referrer-Policy: no-referrer`，并用 `frame-ancestors 'none'` + `X-Frame-Options: DENY` 禁止被他人页面嵌入。
- 备注等内容在写入 DOM 前一律做 HTML 转义，导入他人发来的备份 JSON 时只接受已知测试编号、强制字符串类型并截断到 300 字 —— 粘贴一段坏 JSON 不会执行任何脚本，也不会污染界面。
- 对外链接只有一个 GitHub 仓库地址，且只出现在普通 `<a target="_blank" rel="noopener noreferrer">` 里。
- 顶部徽章只在 GitHub 上阅读 README 时加载，应用本身与部署站点不请求任何外部资源。
- 项目以匿名作者名义发布（见 `LICENSE`），提交记录使用 GitHub 的 noreply 邮箱。

*Privacy in short: no backend, no analytics, no ads, no external fonts or CDNs; `connect-src 'none'` blocks outbound requests at the header level. Screen specs, marks and notes never leave your browser — they live in `localStorage` only, and sharing happens through local artefacts (copied summary, printed PDF, exported JSON).*

## 常见问题

- **打开就是英文？** 浏览器语言不是 `zh*` 时会自动选 English，点右上角「中」或按 `L` 切换，选择会记住。
- **进测试没有全屏？** 浏览器只允许真实用户手势触发全屏，按 `F` 手动切换；某些浏览器在“返回上一级”后的手势判定较严，多点一次即可。
- **刷新率测出来偏低 / 跳动？** `requestAnimationFrame` 反映的是浏览器实际呈现帧率，会被标签页节流、系统省电、可变刷新率影响。请在全屏、前台、关闭其他重负载页面后再测。
- **灰阶/渐变看到断层，是不是屏坏了？** 先开「抖动」再看：抖动后仍存在的断层才可疑，消失的大概率是浏览器插值或位深处理造成的假象。
- **换电脑了，结果还在吗？** 不在。用报告页的 **备份进度** 导出 JSON，到新设备 **恢复进度** 导入即可。
- **备注丢了？** 备注和结果一起存在本机 `localStorage`；清理浏览器数据、或使用无痕窗口都会清空，重要结果请及时打印或导出 JSON。

## 反馈与贡献

- 用起来有问题、想加一项测试（比如均匀性的分区采样、更多色温场）：直接开 [Issue](https://github.com/Hugeeeeeeee/display-check/issues)，附上浏览器版本、分辨率与缩放。
- 改代码请遵循：不引入任何外部依赖与请求；文案一律进 `ZH` / `EN` 字典（不要在渲染逻辑里硬编码中文）；改完执行 `python3 build.py` 并确认三个 HTML 产物一致。
- 提 PR 前请说明改动动机，界面类改动请同时给出中英文文案。

## Star

再次说明这个项目想要什么：**一个 Star**。

- 仓库：<https://github.com/Hugeeeeeeee/display-check>（在线试用：<https://displaycheck.pages.dev>）
- 觉得有用，[点个 Star](https://github.com/Hugeeeeeeee/display-check)；也想让别人看到的话，转发给正在验新显示器的朋友。

应用内的 Star 引导刻意做得很克制：只有完整测完 10 项并第一次打开报告时才出现一次说明条，关闭或看过之后记录在 `localStorage`（`displaycheck.starHinted.v1`），不再重复打扰；报告页脚与文字摘要里各有一行项目地址。它只是一个普通跳转链接，没有任何统计脚本或外部请求。

仓库地址只写在 **一处** —— `app.js` 顶部的 `REPO` 常量（改完必须重新执行 `python3 build.py`，否则 `monitor-check.html` 与 `site/` 里的地址不会更新）：

```js
const REPO = 'Hugeeeeeeee/display-check';   // 不要加 https://
```

它会同时驱动首页的 GitHub 入口、报告页顶部的一次性说明条、报告底部页脚、文字摘要与备份 JSON 里的项目地址。保持占位符 `YOUR_GITHUB_USERNAME` 不动时，这些入口会自动隐藏，不会出现指向不存在页面的链接。

## 许可

MIT，可自由使用、修改与分发，详见 [LICENSE](LICENSE)（线上 <https://displaycheck.pages.dev/LICENSE> 也可查看）。

---

如果这个项目帮你验出了坏点、或者帮你省下一次退换，[点个 Star](https://github.com/Hugeeeeeeee/display-check) 就是最好的反馈。English readers: see [README.en.md](README.en.md).
